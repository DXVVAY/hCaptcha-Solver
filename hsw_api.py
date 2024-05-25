from playwright.sync_api import sync_playwright
from core.logger import log as logger
from flask import Flask, request
from tls_client import Session
from queue import Queue, Empty
from re import findall
import threading
import requests
import logging
import asyncio
import time
import jwt

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)
session = Session(client_identifier='chrome_118', random_tls_extension_order=True)
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
session.headers = {
    "host": 'hcaptcha.com',
    "connection": 'keep-alive',
    "accept": 'application/json',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    "sec-ch-ua": '"Chromium";v="118", "Not A(Brand";v="24", "Google Chrome";v="118"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": '"Windows"',
    "origin": 'https://newassets.hcaptcha.com',
    "referer": 'https://newassets.hcaptcha.com/',
    "sec-fetch-site": 'same-site',
    "sec-fetch-mode": 'cors',
    "sec-fetch-dest": 'empty',
    "accept-encoding": 'gzip, deflate, br',
    "accept-language": 'en-US,en-SE;q=0.9,sv-SE;q=0.6'
}

class inst:
    instance = None

class HSW:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.queue = Queue()
        self.playwright_thread = threading.Thread(target=self.task)
        self.playwright_thread.start()

    def inject_hsw(self) -> str:
        js = session.get('https://hcaptcha.com/1/api.js?render=explicit&onload=hcaptchaOnLoad').text
        version = findall(r'v1\/([A-Za-z0-9]+)\/static', js)[1]
        req_token = session.post('https://api.hcaptcha.com/checksiteconfig', params={
            'v': version,
            'host': 'discord.com',
            'sitekey': '4c672d35-0701-42b2-88c3-78380b0db560',
            'sc': '1',
            'swa': '1',
            'spst': '1',
        }).json()["c"]["req"]

        url = jwt.decode(req_token, options={"verify_signature": False})['l']
        version = url.split("/c/")[1]
        logger.info(f"Pulled hsw.js -> {version}")
        hsw_js = requests.get(f"{url}/hsw.js").text
        self.page.add_script_tag(content="Object.defineProperty(navigator, \"webdriver\", {\"get\": () => false})")
        self.page.add_script_tag(content=hsw_js)

    def process_queue(self):
        while True:
            try:
                req, callback = self.queue.get(timeout=1)
                with self.lock:
                    hsw = self.page.evaluate(f"hsw('{req}')")
                    callback(hsw)
            except Empty:
                continue

    def run(self):
        inst.instance = self
        self.page.goto("https://discord.com/")
        self.page.wait_for_load_state('domcontentloaded')
        self.inject_hsw()

    def task(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
        self.page.route("https://discord.com/", lambda r: r.fulfill(status=200, content_type="text/html",))
        self.run()
        self.process_queue()

    @app.route('/hsw', methods=["POST"])
    def get_hsw():
        s = time.time()
        req = request.get_json()["req"]
        result = Queue()

        def handle(hsw):
            result.put(hsw)

        inst.instance.queue.put((req, handle))

        hsw = result.get()
        logger.info(f"Successfully Got HSW {hsw[:80]} / Length: {len(hsw)} / Time: {str(time.time() - s)[:5]}", "Success")
        return hsw

threading.Thread(target=lambda: app.run(host='0.0.0.0', port="5000", debug=False, use_reloader=False)).start()
HSW()