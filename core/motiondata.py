from scipy import interpolate
import numpy as np
import string
import random
import math
import time

# not fully my code
# but heavily modified and updated by dexv

class util:
    @staticmethod
    def randint(a: int, b: int) -> int:
        return random.randint(min(a, b), max(a, b))

    @staticmethod
    def get_ms() -> int:
        return int(time.time() * 1000)

    @staticmethod
    def get_mm(start: tuple, goal: tuple, screen_size: tuple, max_points: int, random_amount: int, polling_rate: int) -> list:
        cp = util.randint(3, 5)
        x, y = np.linspace(start[0], goal[0], num=cp, dtype='int'), np.linspace(start[1], goal[1], num=cp, dtype='int')
        r = [util.randint(-random_amount, random_amount) for _ in range(cp)]
        x += np.clip(r, 0, screen_size[0])
        y += np.clip(r, 0, screen_size[1])
        tck, _ = interpolate.splprep((x, y), k=3 if cp > 3 else cp - 1)
        u = np.linspace(0, 1, num=min(2 + int(math.sqrt((goal[0] - start[0]) ** 2 + (goal[1] - start[1]) ** 2) / polling_rate), max_points))
        points = interpolate.splev(u, tck)
        return [[int(x), int(y), util.get_ms()] for x, y in zip(*(i.astype(int) for i in points)) if time.sleep(1 / util.randint(80, 240)) is None]

    @staticmethod
    def periods(timestamps: list) -> float:
        periods = [timestamps[i + 1] - timestamps[i] for i in range(len(timestamps) - 1)]
        return sum(periods) / len(periods) if periods else 0

    @staticmethod
    def distance(a: tuple, b: tuple) -> float:
        return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    @staticmethod
    def get_random_point(bbox: tuple) -> tuple:
        return util.randint(bbox[0][0], bbox[1][0]), util.randint(bbox[0][1], bbox[1][1])

    @staticmethod
    def get_center(bbox: tuple) -> tuple:
        x1, y1 = bbox[0]
        x2, y2 = bbox[1]

        return int(x1 + (x2 - x1) / 2), int(y1 + (y2 - y1) / 2)

class rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_dimensions(self) -> tuple:
        return self.width, self.height

    def get_box(self, rel_x: int, rel_y: int) -> tuple:
        return (rel_x, rel_y), (rel_x + self.width, rel_y + self.height)

    def get_corners(self, rel_x: int = 0, rel_y: int = 0) -> list:
        return [(rel_x, rel_y), (rel_x + self.width, rel_y), (rel_x, rel_y + self.height), (rel_x + self.width, rel_y + self.height)]

class widget_check:
    def __init__(self, rel_position: tuple) -> None:
        self.widget = rectangle(300, 75)
        self.check_box = rectangle(28, 28)
        self.rel_position = rel_position

    def get_check(self) -> tuple:
        return self.check_box.get_box(16 + self.rel_position[0], 23 + self.rel_position[1])

    def get_closest(self, position: tuple) -> tuple:
        corners = self.widget.get_corners(self.rel_position[0], self.rel_position[1])
        sorted_corners = sorted(corners, key=lambda c: util.distance(position, c))
        return sorted_corners[0], sorted_corners[1]

class text_challenge:
    def __init__(self, box_centre: tuple, screen_size: tuple) -> None:
        x = min(max(box_centre[0] + 25, 0), screen_size[0] / 2 - 185)
        y = min(max(box_centre[1] - 150, 10), screen_size[1] - 310)
    
        self.widget_position = (x, y)
        self.widget = rectangle(370, 300)
        self.text_box = rectangle(314, 40)
        self.button = rectangle(80, 35)

    def get_text_box(self) -> tuple:
        return self.text_box.get_box(28, 165)

    def get_button_box(self) -> tuple:
        return self.button.get_box(280, 255)

    def get_closest(self, position: tuple) -> tuple:
        corners = self.widget.get_corners(self.widget_position[0], self.widget_position[1])
        sorted_corners = sorted(corners, key=lambda c: util.distance(position, c))
        return sorted_corners[0], sorted_corners[1]

COMMON_SCREEN_SIZES = [
    (1024, 768),
    (1280, 720),
    (1280, 800),
    (1280, 960),
    (1280, 1024),
    (1366, 768),
    (1440, 900),
    (1600, 900),
    (1600, 1200),
    (1680, 1050),
    (1920, 1080),
    (1920, 1200),
    (2048, 1152),
    (2560, 1440),
    (2560, 1600)
]

COMMON_CORE_COUNTS = [
    2,
    4,
    6,
    8,
    12,
    16,
    32
]

class get_cap:
    global COMMON_SCREEN_SIZES, COMMON_CORE_COUNTS
    def __init__(self, user_agent: str, href: str) -> None:
        self.user_agent = user_agent
        screen_size = random.choice(COMMON_SCREEN_SIZES)
        self.screen_size = screen_size
        widget_id = '0' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        random_point = util.get_random_point(((0, 0), (screen_size[0] - 150, screen_size[1] - 38)))
        self.widget = widget_check(random_point)
        self.position = util.get_random_point(((0, 0), screen_size))
        data = {
            'st': util.get_ms(),
            'mm': [],
            'mm-mp': 0,
            'md': [],
            'md-mp': 0,
            'mu': [],
            'mu-mp': 0,
            'v': 1,
            'topLevel': self.top_level(),
            'session': [],
            'widgetList': [widget_id],
            'widgetId': widget_id,
            'href': href,
            'prev': {
                'escaped': False,
                'passed': False,
                'expiredChallenge': False,
                'expiredResponse': False
            }
        }

        goal = util.get_random_point(self.widget.get_check())
        self.mouse_movement = util.get_mm(self.position, goal, self.screen_size, 20, 3, 10)
        data['mm'] = [[x - random_point[0], y - random_point[1], t] for x, y, t in self.mouse_movement]
        data['mm-mp'] = util.periods([x[-1] for x in self.mouse_movement])
        data['md'].append(data['mm'][-1][:-1] + [util.get_ms()])
        time.sleep(1 / util.randint(3, 7))
        data['mu'].append(data['mm'][-1][:-1] + [util.get_ms()])
        self.data = data

    def top_level(self) -> dict:
        data = {
            'inv': False,
            'st': util.get_ms(),
            'sc': {
                'availWidth': self.screen_size[0],
                'availHeight': self.screen_size[1],
                'width': self.screen_size[0],
                'height': self.screen_size[1],
                'colorDepth': 24,
                'pixelDepth': 24,
                'top': 0,
                'left': 0,
                'availTop': 0,
                'availLeft': 0,
                'mozOrientation': 'landscape-primary',
                'onmozorientationchange': None
            },
            'nv': {
                'permissions': {},
                'pdfViewerEnabled': True,
                'doNotTrack': 'unspecified',
                'maxTouchPoints': 0,
                'mediaCapabilities': {},
                'vendor': '',
                'vendorSub': '',
                'cookieEnabled': True,
                'mediaDevices': {},
                'serviceWorker': {},
                'credentials': {},
                'clipboard': {},
                'mediaSession': {},
                'webdriver': False,
                'hardwareConcurrency': random.choice(COMMON_CORE_COUNTS),
                'geolocation': {},
                'userAgent': self.user_agent,
                'language': 'nl-NL',
                'languages': ['nl-NL', 'nl'],
                'locks': {},
                'onLine': True,
                'storage': {},
                'plugins': [
                    'internal-pdf-viewer',
                    'internal-pdf-viewer',
                    'internal-pdf-viewer',
                    'internal-pdf-viewer',
                    'internal-pdf-viewer'
                ]
            },
            'dr': '',
            'exec': False,
            'wn': [[self.screen_size[0], self.screen_size[1], 1, util.get_ms()]],
            'wn-mp': 0,
            'xy': [[0, 0, 1, util.get_ms()]],
            'xy-mp': 0,
            'mm': [],
            'mm-mp': 0
        }

        goal = util.get_random_point(self.widget.get_closest(self.position))
        mouse_movement = util.get_mm(self.position, goal, self.screen_size, 75, 3, 15)
        self.position = goal
        data['mm'] = mouse_movement
        data['mm-mp'] = util.periods([x[-1] for x in mouse_movement])

        return data

class check_cap:
    global COMMON_SCREEN_SIZES, COMMON_CORE_COUNTS
    def __init__(self, old_motion_data: dict) -> None:
        self.position = []
        self.old_motion_data = old_motion_data
        self.screen_size = old_motion_data.screen_size
        self.widget = text_challenge(util.get_center(old_motion_data.widget.get_check()), self.screen_size)
    
        data = {
            'st': util.get_ms(),
            'dct': util.get_ms(),
            'mm': [],
            'mm-mp': 0,
            'md': [],
            'md-mp': 0,
            'mu': [],
            'mu-mp': 0,
            'v': 1,
            'topLevel': self.top_level()
        }
    
        rel_position = (self.position[0] - self.widget.widget_position[0], self.position[1] - self.widget.widget_position[1])
    
        for _ in range(3):
            for box in [self.widget.get_text_box(), self.widget.get_button_box()]:
                goal = util.get_random_point(box)
                data['mm'] += util.get_mm(rel_position, goal, self.screen_size, 15 if box == self.widget.get_text_box() else 30, 3, 17)
                rel_position = goal
                data['md'].append(list(goal) + [util.get_ms()])
                time.sleep(1 / util.randint(4 if box == self.widget.get_text_box() else 7, 9))
                data['mu'].append(list(goal) + [util.get_ms()])
                time.sleep(10 / util.randint(8, 15))
    
        self.data = data

    def top_level(self) -> dict:
        data = self.old_motion_data.data['topLevel']
        data['mm'] += self.old_motion_data.mouse_movement
        position = tuple(data['mm'][-1][:-1])
        data['mm'] += util.get_mm(position, util.get_random_point(self.widget.get_closest(position)), self.screen_size, 60, 3, 16)
        data['mm-mp'] = util.periods([x[-1] for x in data['mm']])
        self.position = tuple(data['mm'][-1][:-1])
        return data

class motion_data:
    def __init__(self, user_agent: str, url: str) -> None:
        self.user_agent = user_agent
        self.url = url
        self.get_captcha_motion_data = get_cap(self.user_agent, self.url)

    def get_captcha(self) -> dict:
        return self.get_captcha_motion_data.data

    def check_captcha(self) -> dict:
        return check_cap(self.get_captcha_motion_data).data