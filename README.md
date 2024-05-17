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

hsw decrypted (AES-256-GCM):

```json
{
  "proof_spec": {
    "difficulty": 2,
    "fingerprint_type": 0,
    "_type": "w",
    "data": "wlHjmTa2pb3FJJurmAcybqBflSCIcrI8q6/P4ASNHPa2AvANd4lazPQdBbcKuQYaaoZ+d4HTOAILOId1onHmylhOeM2V07O0lN2EjGCWnJNpdQom7bvVkk5FKTWs4epHJLeNwoIjP/Mm9YzNC9XgCdpr+4qoDU9y8U220G/IAGOcpTN0jKCq+M7EG/n3XjVRE62te0IAPrKJ6Mak3KtWeicXIUEmDt+OvqqXtCAdjO8iOkV3lDLSFiRgMKTgtA1N",
    "_location": "https://newassets.hcaptcha.com/c/f922a41",
    "timeout_value": 1000
  },
  "rand": [
    0.5497682371112909,
    0.9510314334183931
  ],
  "components": {
    "navigator": {
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.241 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36",
      "language": "en-US",
      "languages": [
        "en-US",
        "en-SE",
        "en-GB",
        "sv-SE"
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
      "width": 1920,
      "height": 1080,
      "avail_width": 1920,
      "avail_height": 1040
    },
    "device_pixel_ratio": 1,
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
    "parent_win_hash": "14672043374044359109",
    "webrtc_hash": "-1",
    "performance_hash": "4140103483592612201",
    "unique_keys": "regeneratorRuntime,_ws,1,GLOBAL_ENV,__BILLING_STANDALONE__,webpackChunkdiscord_app,__localeData__,createDiscordStream,popupBridge,hcaptcha,__SENTRY_IPC__,0,__OVERLAY__,DiscordErrors,clearImmediate,grecaptcha,DiscordSentry,__timingFunction,hcaptchaOnLoad,__isReactDndBackendSetUp,IntlPolyfill,__SENTRY__,__DISCORD_WINDOW_ID,setImmediate,__SECRET_EMOTION__,2,platform,DiscordNative",
    "inv_unique_keys": "localStorage,_sharedLibs,hsw,__wdata,sessionStorage",
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
      3957763561,
      "[\"Windows\",\"10.0.0\",null,\"64\",\"x86\",\"120.0.6099.291\"]"
    ],
    [
      3916977893,
      "[[\"NeydHCok1rU9EvmLcmyUcv55MlwitJSp\",\"b\",\"1a\",\"LRCTVMZNBIQGZ\"],[\"itBvEMyUitS1Kd5pgbwItjvnEUlBFswItjOU1qqTEUInKMLAJMLGUvonFtlnzsxEtkwItj3p3X18FMDjtjwItjJp3X18FMwItjlBXeSpWYzSUMxAJMLGcMLBDMwAtMnhJMpAJMLEJn1ADMyU\",\"7\",\"56\",\"CJSONRVQGTKLJ\"]]"
    ],
    [
      873741287,
      "[0,18407,18407]"
    ],
    [
      748900772,
      "11038406483972230190"
    ],
    [
      3498175614,
      "[\"o==wn4MDo2UDMzyD\",\"1a\",\"f\",\"KPPYCCNJKJION\"]"
    ],
    [
      143592240,
      "[[209,[209,209,209,255,209,209,209,255,209,209,209,255,209,209,209,255]],[[11,0,1,105.015625,13,5,105.6171875],[[12,0,-1,113.125,17,4,113],[11,0,0,111,12,4,111],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[12,0,0,109.640625,14,3,110.1953125]]],[0,2,4,5,6,8,9,12,13,15,17,18,19,21,22,23,28,29,30,31,33,34,35,37,39,42,47,48,49,66,67,69,71,72,75,76,77,78,79,81,82],[0,0,0,0,14,3,0]]"
    ],
    [
      3725196262,
      "[16,1024,4096,7,12,120,[23,127,127]]"
    ],
    [
      1877814445,
      "[1,2,3,4]"
    ],
    [
      2275435905,
      "4631229088072584217"
    ],
    [
      2691352878,
      "2404.399999976158"
    ],
    [
      2998564779,
      "[24,24,65536,212988,200704]"
    ],
    [
      2232178856,
      "[2147483647,2147483647,2147483647,2147483647]"
    ],
    [
      2854298529,
      "137.69999992847443"
    ],
    [
      137519462,
      "12073207331849695208"
    ],
    [
      1335970363,
      "4226317358175830201"
    ],
    [
      137955265,
      "\"Europe/Stockholm\""
    ],
    [
      669213918,
      "[\"Google Inc. (NVIDIA)\",\"ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 (0x00001F82) Direct3D11 vs_5_0 ps_5_0, D3D11)\"]"
    ],
    [
      3913991343,
      "115.20000004768372"
    ],
    [
      2571358880,
      "[\"Europe/Stockholm\",-60,-60,-3203646808000,\"Central European Standard Time\",\"en-US\"]"
    ],
    [
      4086018371,
      "[[true,\"en-US\",true,\"Microsoft David - English (United States)\",\"Microsoft David - English (United States)\"],[false,\"en-GB\",true,\"Microsoft Hazel - English (United Kingdom)\",\"Microsoft Hazel - English (United Kingdom)\"],[false,\"en-GB\",true,\"Microsoft Susan - English (United Kingdom)\",\"Microsoft Susan - English (United Kingdom)\"]]"
    ],
    [
      690142092,
      "[32767,32767,16384,8,8,8]"
    ],
    [
      3827436525,
      "15307345790125003576"
    ],
    [
      3311072794,
      "1117"
    ],
    [
      1613898511,
      "17002384262467705698"
    ],
    [
      3756317564,
      "2337666753322697468"
    ],
    [
      255383392,
      "[2147483647,2147483647,4294967294]"
    ],
    [
      872174808,
      "[\"5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.241 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36\",\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.241 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36\",8,4,\"en-US\",[\"en-US\",\"en-SE\",\"en-GB\",\"fa\",\"sv-SE\"],\"Win32\",null,[\"Not_A Brand 8\",\"Chromium 120\"],false,\"Windows\",2,5,true,false,50,false,false,false,\"[object Keyboard]\",false,false]"
    ],
    [
      338869435,
      "14882824317255702596"
    ],
    [
      2881608941,
      "57"
    ],
    [
      1587180961,
      "1715421331252.5"
    ],
    [
      334928754,
      "13177607191192652685"
    ],
    [
      531197711,
      "219.94999998807907"
    ],
    [
      2115854713,
      "[\"mdQj3b2NHdMjwE2dHbGjtjaF\",\"7\",\"e\",\"RVEVPWQJEKTRJ\"]"
    ],
    [
      2460707167,
      "[1,4,5,7,9,12,20,21,24,25,29,31]"
    ],
    [
      3719249172,
      "16290568259171983358"
    ],
    [
      1311261287,
      "[4,120,4]"
    ],
    [
      1587819988,
      "3313549113868922289"
    ],
    [
      2151859767,
      "[[],35,34,null,false,false,true,37,true,true,true,true,true,[\"Raven\",\"_sharedLibs\",\"__wdata\",\"hsw\"],[[\"getElementsByClassName\",[]],[\"getElementById\",[]],[\"querySelector\",[]],[\"querySelectorAll\",[]]],[],true]"
    ],
    [
      443486963,
      "4932383211497360507"
    ],
    [
      2371850788,
      "true"
    ],
    [
      1350382849,
      "[[277114314453,277114314460,277114314451,357114314456,277114314452,554228628898,57114314443,717114314371391,554228628897,277114314456,1108457257862,277114314450,554228628919,277114314460,277114314451],false]"
    ],
    [
      2622130410,
      "[16384,32,16384,2048,2,2048]"
    ],
    [
      2906236335,
      "[[[\"https://newassets.hcaptcha.com/captcha/v1/50fb34a/hcaptcha.js\",0,5]],[[\"*\",84,9]]]"
    ],
    [
      1405859696,
      "[16,4095,30,16,16380,120,12,120,[23,127,127]]"
    ],
    [
      3952131478,
      "[11]"
    ],
    [
      1421982308,
      "[7838650368,7838650368,null,null,1098907648,true,true,true,null]"
    ],
    [
      1068771096,
      "627"
    ],
    [
      3082579163,
      "16153807394097295248"
    ],
    [
      3070040703,
      "9345374751420407194"
    ],
    [
      1373138784,
      "[[\"navigation:newassets.hcaptcha.com\",173,190.39999997615814],[\"script:newassets.hcaptcha.com\",113.94999998807907,270.64999997615814],[\"xmlhttprequest:api.hcaptcha.com\",0,127.70000004768372]]"
    ],
    [
      414144794,
      "[-6.172840118408203,-20.710678100585938,120.71067810058594,-20.710678100585938,141.42135620117188,120.71067810058594,-20.710678100585938,141.42135620117188,-20.710678100585938,-20.710678100585938,0,0,300,150,false]"
    ],
    [
      3497821731,
      "[1,1024,1,1,4]"
    ],
    [
      694616987,
      "[1920,1080,1920,1040,24,24,false,0,1,1920,1040,true,true,true,false]"
    ]
  ],
  "suspicious_events": [],
  "messages": null,
  "stack_data": null,
  "stamp": "1:2:2024-05-11:wlHjmTa2pb3FJJurmAcybqBflSCIcrI8q6/P4ASNHPa2AvANd4lazPQdBbcKuQYaaoZ+d4HTOAILOId1onHmylhOeM2V07O0lN2EjGCWnJNpdQom7bvVkk5FKTWs4epHJLeNwoIjP/Mm9YzNC9XgCdpr+4qoDU9y8U220G/IAGOcpTN0jKCq+M7EG/n3XjVRE62te0IAPrKJ6Mak3KtWeicXIUEmDt+OvqqXtCAdjO8iOkV3lDLSFiRgMKTgtA1N::FtXtcppc:3a",
  "href": "https://canary.discord.com/register",
  "ardata": null,
  "errs": {
    "list": []
  },
  "perf": [
    [
      1,
      15
    ],
    [
      2,
      146
    ],
    [
      3,
      0
    ]
  ]
}
```

# Credits

* **DEXV** - *Shit head (retarded)* - [DEXV](https://dexv.lol) - Main Author
* **Dort** - *Cool Guy* - [Dort](https://t.me/motionData) - Thaught Me ALOT
* **Body** - *Sexy Frenchie* - [Body](https://t.me/bodyalhoha) - Helped Me With Some Stuff
