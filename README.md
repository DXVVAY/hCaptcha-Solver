<br/>
<p align="center">
  <a href="https://github.com/DXVVAY">
    <img src="https://github.com/DXVVAY/hCaptcha-Text-Solver/assets/89728480/ca479b71-e143-4894-890f-10aec6e63e61" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">fCaptcha Text Challenge Solver</h3>

  <p align="center">
    <a href="https://discord.gg/fCaptcha">Discord</a>
    .
    <a href="https://t.me/hCapSolution">Telegram</a>
  </p>
</p>

<p align="center">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/DXVVAY/hCaptcha-Text-Solver/total">
  <img alt="Contributors" src="https://img.shields.io/github/contributors/DXVVAY/hCaptcha-Text-Solver?color=dark-green">
  <img alt="Forks" src="https://img.shields.io/github/forks/DXVVAY/hCaptcha-Text-Solver?style=social">
  <img alt="Stargazers" src="https://img.shields.io/github/stars/DXVVAY/hCaptcha-Text-Solver?style=social">
  <img alt="Issues" src="https://img.shields.io/github/issues/DXVVAY/hCaptcha-Text-Solver">
  <img alt="License" src="https://img.shields.io/github/license/DXVVAY/hCaptcha-Text-Solver">
</p>

<p align="center">
  <a href="https://discord.gg/xvirus">
    <img alt="Discord" src="https://img.shields.io/discord/1193273961476280451?label=&logo=discord&logoColor=ffffff&color=C50F1f&labelColor=C50F1f">
  </a>
  <a href="https://www.codefactor.io/repository/github/DXVVAY/hCaptcha-Text-Solver">
    <img src="https://www.codefactor.io/repository/github/DXVVAY/hCaptcha-Text-Solver/badge" alt="CodeFactor" />
  </a>
    <img alt="lines" src="https://sloc.xyz/github/DXVVAY/hCaptcha-Text-Solver">
</p>

## About The Project

<p align="center">
  <img alt="preview" src="https://github.com/DXVVAY/DXVVAY/assets/89728480/cca39ba5-8b4b-44ac-bab9-687ca62fa3fa">
</p>

This is a AI based (gpt4free) hcaptcha text challenge solver that utilizes the playwright module to generate the hsw N data.

Even tho this solves any text challenge without any problem it may be very flagged for some websites like discord.

So if you want a solver that is unflagged for discord register etc (image solver) reach me on [telegram](https://t.me/dexv0)

## Getting Started

All you need for this is proxies since hCaptcha also ratelimits!!!!!!!!!!!!

### Installation

- Requires: `Python 3.10+`
- clone the repository: `git clone --recursive https://github.com/DXVVAY/hCaptcha-Text-Solver.git`
- Install the requirements: `pip install -r requirements.txt`
- Edit `main.py` to add your proxies
- Start: `python3 main.py`

---

## Usage

Run `hsw_api.py` before running anything, and then add the usage that is shown in `main.py` to any one your projects the require hCaptcha solving.

Please be aware that this only works on sites that support hCaptcha text challenge.

## Disclaimer

|This project was made for Educational purposes|
|-------------------------------------------------|
This project was created only for good purposes and personal use.
By using this, you agree that you hold responsibility and accountability of any consequences caused by your actions.

## License

Distributed under the GPL-3.0 License. See [LICENSE](https://github.com/DXVVAY/hCaptcha-Text-Solver/blob/main/LICENSE) for more information.

# Main Solver

This solver is flagged for obv reasons (playwright hsw) + Text Challenge. 

So if you want a good hCaptcha solver I will recommend you to use [fCaptcha Telegram](https://t.me/hCapSolution) / [fCaptcha Discord](https://disocrd.gg/fcaptcha) which uses a hsw reverse and is unflagged for discord.

## proof

event hashes "dehashed" (reversed):
![Code_mvv17K9lT3vxc](https://github.com/DXVVAY/hCaptcha-Solver/assets/89728480/d120781e-4307-41f3-a85c-d1cc33c54ba4)

hsw decrypted (AES-256-GCM):

```json
{
    "proof_spec": {
        "difficulty": 2,
        "fingerprint_type": 0,
        "_type": "w",
        "data": "GpvDi79R76nvqyruGCGhKcyWjEA6oWW39NRkHmh6Q1w6SdN7zpxodnkQvFB7gRlEIYgXU26QBD4NWdXuhE4H4aZDHxbb2ec6prRT3eWl1+WxD+Dk4iC2BxvbTQOoZm54lCcysscXl4vCfyNbDc6E0QR4KVwrz6mbfsoqdHt+OCOqD4zfN+hhJd8dKGrsk/wZ5vM24tMf+1cMZG5h16otSTdoodS5qilGjL2eP2VaqQdAB+Lecsk=Lq2GtjwAB3NTvtZN",
        "_location": "https://newassets.hcaptcha.com/c/de80b1b",
        "timeout_value": 1000.0
    },
    "rand": [
        0.37582791536757076,
        0.5740331697743386
    ],
    "components": {
        "navigator": {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9146 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36",
            "language": "en-US",
            "languages": [
                "en-US"
            ],
            "platform": "Win32",
            "max_touch_points": 0,
            "webdriver": false,
            "notification_query_permission": null,
            "plugins_undefined": false
        },
        "screen": {
            "color_depth": 24,
            "pixel_depth": 24,
            "width": 1668,
            "height": 862,
            "avail_width": 1668,
            "avail_height": 822
        },
        "device_pixel_ratio": 1.0,
        "has_session_storage": true,
        "has_local_storage": true,
        "has_indexed_db": true,
        "web_gl_hash": "-1",
        "canvas_hash": "3290922276056775431",
        "has_touch": false,
        "notification_api_permission": "Granted",
        "chrome": false,
        "to_string_length": 33,
        "err_firefox": null,
        "r_bot_score": 0,
        "r_bot_score_suspicious_keys": [],
        "r_bot_score_2": 0,
        "audio_hash": "-1",
        "extensions": [
            false
        ],
        "parent_win_hash": "14533946090530726899",
        "webrtc_hash": "-1",
        "performance_hash": "11097854906383886648",
        "unique_keys": "__localeData__,__REACT_DEVTOOLS_SHOW_INLINE_WARNINGS_AND_ERRORS__,DiscordNative,regeneratorRuntime,2,__isReactDndBackendSetUp,0,__BILLING_STANDALONE__,webpackChunkdiscord_app,platform,__SECRET_EMOTION__,__SENTRY__,__REACT_DEVTOOLS_APPEND_COMPONENT_STACK__,hcaptcha,__REACT_DEVTOOLS_HIDE_CONSOLE_LOGS_IN_STRICT_MODE__,__SENTRY_IPC__,hcaptchaOnLoad,Vencord,__timingFunction,DiscordErrors,VencordNative,clearImmediate,VencordStyles,__OVERLAY__,__REACT_DEVTOOLS_BROWSER_THEME__,grecaptcha,GLOBAL_ENV,setImmediate,1,IntlPolyfill,createDiscordStream,_ws,popupBridge,__REACT_DEVTOOLS_COMPONENT_FILTERS__,__DISCORD_WINDOW_ID,__REACT_DEVTOOLS_BREAK_ON_CONSOLE_ERRORS__",
        "inv_unique_keys": "__wdata,sessionStorage,localStorage,hsw,_sharedLibs",
        "common_keys_hash": 276567530,
        "common_keys_tail": "chrome,caches,cookieStore,ondevicemotion,ondeviceorientation,ondeviceorientationabsolute,launchQueue,documentPictureInPicture,onbeforematch,getScreenDetails,openDatabase,queryLocalFonts,showDirectoryPicker,showOpenFilePicker,showSaveFilePicker,originAgentCluster,credentialless,speechSynthesis,oncontentvisibilityautostatechange,onscrollend,webkitRequestFileSystem,webkitResolveLocalFileSystemURL,Raven",
        "features": {
            "performance_entries": true,
            "web_audio": true,
            "web_rtc": true,
            "canvas_2d": true,
            "fetch": true
        }
    },
    "events": [
        [
            382530556,
            "[\"m2ydNxQtmWEdm2cZ\",\"17\",\"b\",\"TGVMODKMWLYZB\"]"
        ],
        [
            2444897354,
            "\"America/Los_Angeles\""
        ],
        [
            254857823,
            "[60,72,65536,245760,245760]"
        ],
        [
            938239901,
            "[[],35,34,null,false,false,true,37,true,true,true,true,true,[\"Raven\",\"_sharedLibs\",\"hsw\",\"__wdata\"],[[\"getElementsByClassName\",[]],[\"getElementById\",[]],[\"querySelector\",[]],[\"querySelectorAll\",[]]],[],true]"
        ],
        [
            1303365628,
            "1117"
        ],
        [
            227790277,
            "[16,4096,31,32,16384,124,14,128,[23,127,127]]"
        ],
        [
            553070510,
            "[8192,8192,8192,8,8,4]"
        ],
        [
            2489756571,
            "1.9000000953674316"
        ],
        [
            1893274106,
            "13051680398954254262"
        ],
        [
            67516181,
            "[2,3,4]"
        ],
        [
            3124014409,
            "[4,128,4]"
        ],
        [
            1938239965,
            "9345374751420407194"
        ],
        [
            1003038916,
            "627"
        ],
        [
            1481601550,
            "15307345790125003576"
        ],
        [
            200401693,
            "4226317358175830201"
        ],
        [
            3838545372,
            "57"
        ],
        [
            1287155446,
            "45.34999990463257"
        ],
        [
            1827241937,
            "[32,4096,16384,7,14,128,[23,127,127]]"
        ],
        [
            1303333220,
            "[[\"lcMYucTxZmLwITjkjNCQ9GaOOKCYp2bO\",\"3\",\"9\",\"ENFOYJJQCUOKF\"],[\"kMLAJML8kQvp1UYz2dqNnzpAJMLC0a3RHaHz3BYNnzwItjoADBwADMwEfMsNvKpMkMLAJMLgYRpbnBZz2ypAJMLI1CqdXCZbJMLgYRrdHdodkdVj3CmbJMLEJlZ4cMwItjKLme59mywItjoU1yJvneZN\",\"e\",\"8a\",\"TTJFVBYSLBZCZ\"]]"
        ],
        [
            3869232296,
            "[1]"
        ],
        [
            2132158760,
            "[[[\"https://newassets.hcaptcha.com/captcha/v1/18fa736/hcaptcha.js\",0,5]],[[\"*\",84,9]]]"
        ],
        [
            3569888996,
            "[141010673664,141010673664,null,null,4294705152,true,true,true,null]"
        ],
        [
            925727266,
            "4932383211497360507"
        ],
        [
            1739511171,
            "[[true,\"en-US\",true,\"Microsoft David - English (United States)\",\"Microsoft David - English (United States)\"],[false,\"en-US\",true,\"Microsoft Mark - English (United States)\",\"Microsoft Mark - English (United States)\"],[false,\"en-US\",true,\"Microsoft Zira - English (United States)\",\"Microsoft Zira - English (United States)\"]]"
        ],
        [
            1340581728,
            "469.2000002861023"
        ],
        [
            3837888977,
            "[2147483647,2147483647,2147483647,2147483647]"
        ],
        [
            3339831915,
            "[\"America/Los_Angeles\",480,480,-3203492822000,\"Pacific Standard Time\",\"en-US\"]"
        ],
        [
            2882164405,
            "[8192,64,16384,2048,15,2048]"
        ],
        [
            1031696114,
            "[1,1023,1,1,4]"
        ],
        [
            312358085,
            "[2147483647,2147483647,4294967294]"
        ],
        [
            527778036,
            "1825316679185413516"
        ],
        [
            1248513529,
            "1556.7000002861023"
        ],
        [
            4066678044,
            "16290568259171983358"
        ],
        [
            2758849376,
            "17002384262467705698"
        ],
        [
            2826985353,
            "[\"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9146 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36\",\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9146 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36\",8,6,\"en-US\",[\"en-US\"],\"Win32\",null,[\"Not_A Brand 8\",\"Chromium 120\"],false,\"Windows\",2,5,true,false,0,false,false,false,\"[object Keyboard]\",false,false]" 
        ],
        [
            1295957164,
            "[-6.172840118408203,-20.710678100585938,120.71067810058594,-20.710678100585938,141.42135620117188,120.71067810058594,-20.710678100585938,141.42135620117188,-20.710678100585938,-20.710678100585938,0,0,300,150,false]"
        ],
        [
            1607176087,
            "16153807394097295248"
        ],
        [
            1204159645,
            "[[145,[145,145,145,255,145,145,145,255,145,145,145,255,145,145,145,255]],[[11,0,1,105.015625,13,5,105.6171875],[[12,0,-1,113.125,17,4,113],[11,0,0,111,12,4,111],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[12,0,0,109.640625,14,3,110.1953125]]],[0,2,4,5,6,8,9,12,13,15,17,18,19,21,22,23,28,29,30,31,33,34,35,37,39,42,47,48,49,66,67,69,71,72,75,76,77,78,79,81,82],[0,0,0,0,14,3,0]]"
        ],
        [
            962453388,
            "[1,4,5,7,9,12,20,21,23,25,30,31]"
        ],
        [
            1004633796,
            "[\"Google Inc. (Google)\",\"ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver)\"]"
        ],
        [
            1791986573,
            "2337666753322697468"
        ],
        [
            3978583396,
            "9854590905640690920"
        ],
        [
            978353121,
            "false"
        ],
        [
            1514173249,
            "4631229088072584217"
        ],
        [
            2092456731,
            "[\"Windows\",\"12.0.0\",null,\"64\",\"x86\",\"120.0.6099.291\"]"
        ],
        [
            1022788021,
            "1716626686408.1"
        ],
        [
            304009087,
            "[0,10480,10480]"
        ],
        [
            3142658631,
            "11038406483972230190"
        ],
        [
            2809130260,
            "[\"zKMlq0zr91uml3dKd3ATv2dQfWdZ\",\"12\",\"9\",\"ZEVJQKFOAYEQU\"]"
        ],
        [
            3225703681,
            "1032251938945356892"
        ],
        [
            22109551,
            "[[277114314453,277114314460,277114314451,357114314456,277114314452,554228628898,57114314443,717114314371391,554228628897,277114314456,1108457257862,277114314450,554228628919,277114314460,277114314451],false]"
        ],
        [
            506452458,
            "[[\"navigation:newassets.hcaptcha.com\",1.9000000953674316,63.90000009536743],[\"script:newassets.hcaptcha.com\",10.90000033378601,40.84999990463257],[\"xmlhttprequest:api2.hcaptcha.com\",0,48]]"
        ],
        [
            803029788,
            "[1668,862,1668,822,24,24,false,0,1,1668,822,true,true,true,false]"
        ]
    ],
    "suspicious_events": [],
    "messages": null,
    "stack_data": null,
    "stamp": "1:2:2024-05-25:GpvDi79R76nvqyruGCGhKcyWjEA6oWW39NRkHmh6Q1w6SdN7zpxodnkQvFB7gRlEIYgXU26QBD4NWdXuhE4H4aZDHxbb2ec6prRT3eWl1+WxD+Dk4iC2BxvbTQOoZm54lCcysscXl4vCfyNbDc6E0QR4KVwrz6mbfsoqdHt+OCOqD4zfN+hhJd8dKGrsk/wZ5vM24tMf+1cMZG5h16otSTdoodS5qilGjL2eP2VaqQdAB+Lecsk=Lq2GtjwAB3NTvtZN::Lvw814VB:4",
    "href": "https://discord.com/register",
    "ardata": null,
    "errs": {
        "list": []
    },
    "perf": [
        [
            1,
            7.0
        ],
        [
            2,
            473.0
        ],
        [
            3,
            0.0
        ]
    ]
}
```

# Credits

* **DEXV** - *Shit head (retarded)* - [DEXV](https://dexv.lol) - Main Author
* **Dort** - *Cool Guy* - [Dort](https://t.me/motionData) - Thaught Me ALOT
* **Body** - *Sexy Frenchie* - [Body](https://t.me/bodyalhoha) - Helped Me With Some Stuff
