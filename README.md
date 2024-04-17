# Unflagging and image support on 100 stars!

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

So if you want a good hCaptcha solver I will recommend you to use [fCaptcha](https://t.me/hCapSolution) which uses a hsw reverse and is unflagged for discord.

## proof

hsw decrypted:

```json
{
    "proof_spec": {
        "difficulty": 2,
        "fingerprint_type": 0,
        "_type": "w",
        "data": "YxjYjxrrqypUPc91QRVyQB4RqN74TdHTTHCm9KBeOvrI\/CQoSq9hzdIAP\/uL4XYxOW27yPu9PaTrN6OTAoPe+i\/98G50DRHA9WVBxftfNSVOvMfr7C+AL\/RLdyy+d1c0Yrx6sfAMjX2d3hlDYGmj3CInJGxGfg8O2wnkCJpv6IsamC2AEP9Mvz9KuXWTAcBCF6N3kQ18kEaxncon7oz1Y2lwI450fsFL\/tvisOT7HW2ePkSEHoivo+JA5dfZbWoo",
        "_location": "https:\/\/newassets.hcaptcha.com\/c\/282d0ff",
        "timeout_value": 1000
    },
    "rand": [
        0.7013999307074494,
        0.9185949647799134
    ],
    "components": {
        "navigator": {
            "user_agent": "Mozilla\/5.0 (Windows NT 10.0; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) discord\/1.0.9041 Chrome\/120.0.6099.291 Electron\/28.2.10 Safari\/537.36",
            "language": "sv",
            "languages": [
                "sv",
                "sv-SE"
            ],
            "platform": "Win32",
            "max_touch_points": 10,
            "webdriver": false,
            "notification_query_permission": null,
            "plugins_undefined": false
        },
        "screen": {
            "color_depth": 24,
            "pixel_depth": 24,
            "width": 1366,
            "height": 768,
            "avail_width": 1366,
            "avail_height": 728
        },
        "device_pixel_ratio": 1,
        "has_session_storage": true,
        "has_local_storage": true,
        "has_indexed_db": true,
        "web_gl_hash": "-1",
        "canvas_hash": "12416080031521948649",
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
        "parent_win_hash": "15877724132084714748",
        "webrtc_hash": "-1",
        "performance_hash": "4140103483592612201",
        "unique_keys": "__localeData__,__REACT_DEVTOOLS_SHOW_INLINE_WARNINGS_AND_ERRORS__,PermissionStore,ReadStateStore,useEffect,SnowflakeUtils,DiscordNative,canonicalizeReplace,SearchableSelect,findByCode,ScrollerThin,MaskedLink,MessageStore,zustandPersist,useToken,Button,ModalImageClasses,SelectedGuildStore,TextArea,regeneratorRuntime,UserProfileStore,__isReactDndBackendSetUp,0,__BILLING_STANDALONE__,findExportedComponent,shortcutList,InviteActions,useCallback,webpackChunkdiscord_app,platform,wpex,React,UserSettingsActionCreators,Paginator,__SECRET_EMOTION__,ComponentTypes,Dialog,GuildMemberStore,__SENTRY__,reload,IconUtils,lodash,__REACT_DEVTOOLS_APPEND_COMPONENT_STACK__,fakeRender,Parser,UserProfileActions,findByProps,hcaptcha,SettingsRouter,Card,__REACT_DEVTOOLS_HIDE_CONSOLE_LOGS_IN_STRICT_MODE__,__SENTRY_IPC__,useRef,hcaptchaOnLoad,MessageActions,moment,zustandCreate,Vencord,Flex,PluginsApi,wp,RelationshipStore,restart,wpsearch,Switch,OAuth2AuthorizeModal,Slider,WindowStore,UserUtils,useMemo,ButtonWrapperClasses,__timingFunction,wpexs,findComponentByCode,UploadHandler,SelectedChannelStore,ContextMenuApi,useReducer,TextAndImagesSettingsStores,findAll,canonicalizeReplacement,findStore,Api,DiscordErrors,GuildChannelStore,ReactDOM,RestAPI,Tooltip,Flux,findAllByProps,VencordNative,plugins,clearImmediate,Alerts,Select,Clickable,VencordStyles,__OVERLAY__,showToast,__REACT_DEVTOOLS_BROWSER_THEME__,DraftStore,Timestamp,findAllComponentsByCode,grecaptcha,Popout,Avatar,findAllByCode,GuildStore,ButtonLooks,FluxDispatcher,GLOBAL_ENV,canonicalizeMatch,setImmediate,useStateFromStores,Settings,1,Toasts,EmojiStore,IntlPolyfill,NavigationRouter,useState,ComponentDispatch,PresenceStore,Forms,wpc,TabBar,UserStore,hljs,DraftType,ApplicationAssetUtils,createDiscordStream,TextInput,MenuTypes,Menu,_ws,UtilTypes,popupBridge,PermissionsBits,i18n,FocusLock,StatusSettingsStores,ChannelStore,__REACT_DEVTOOLS_COMPONENT_FILTERS__,__DISCORD_WINDOW_ID,__REACT_DEVTOOLS_BREAK_ON_CONSOLE_ERRORS__,PrivateChannelsStore,wreq",
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
            2252840959,
            "16290568259171983358"
        ],
        [
            2840639612,
            "[1,4,5,7,9,10,12,20,21,24,25,29,31]"
        ],
        [
            1108939890,
            "[\"Europe\/Stockholm\",-60,-60,-3203646808000,\"centraleuropeisk normaltid\",\"sv\"]"
        ],
        [
            104149656,
            "[1,2,3,4,17]"
        ],
        [
            4173238370,
            "[[\"navigation:newassets.hcaptcha.com\",40.59999996423721,95.39999997615814],[\"script:newassets.hcaptcha.com\",43.5,205.59999999403954],[\"xmlhttprequest:api.hcaptcha.com\",0,77.09999996423721]]"
        ],
        [
            2545605315,
            "[[\"lWITJmrHdsFna=giTZLnaxLCmYUiTZhM\",\"5\",\"13\",\"QWMZKZPVLRBRY\"],[\"MXkcMYuYym9VnfbzQYucMYusam9VnfbDMYusu2VmCWd2MRFtMWItJoAzaWADMWQju3EtKWItJuVmBjVNdWZgMYucsVFFMYuiVHdmC5HsRPAjMlGiVHdmC5nkMlAjMl4uQullu==QuzEV\",\"d\",\"7\",\"XNSTGPYCWUBCH\"]]"
        ],
        [
            2228825458,
            "1713343091784.1"
        ],
        [
            2444509564,
            "[\"Windows\",\"10.0.0\",null,\"64\",\"x86\",\"120.0.6099.291\"]"
        ],
        [
            2416260428,
            "4932383211497360507"
        ],
        [
            850956849,
            "4226317358175830201"
        ],
        [
            1325100515,
            "true"
        ],
        [
            3197530747,
            "[1366,768,1366,728,24,24,false,10,1,1366,728,true,true,true,false]"
        ],
        [
            4165641576,
            "[32767,32767,16384,8,8,16]"
        ],
        [
            3570513324,
            "4631229088072584217"
        ],
        [
            2005859105,
            "[2147483647,2147483647,4294967294]"
        ],
        [
            4250147733,
            "15307345790125003576"
        ],
        [
            2509526170,
            "[2147483647,2147483647,2147483647,2147483647]"
        ],
        [
            91877612,
            "[[[\"https:\/\/newassets.hcaptcha.com\/captcha\/v1\/b1c589a\/hcaptcha.js\",0,5]],[[\"*\",84,9]]]"
        ],
        [
            728511561,
            "12593688630062279982"
        ],
        [
            522949833,
            "[\"AjN3IDm=cjN4qzm4\",\"8\",\"9\",\"SYMQMKXQUEQLV\"]"
        ],
        [
            2062697704,
            "[[277114314453,277114314460,277114314451,357114314456,277114314452,554228628898,57114314443,717114314371391,554228628897,277114314456,1108457257862,277114314450,554228628919,277114314460,277114314451],false]"
        ],
        [
            611315898,
            "3313549113868922289"
        ],
        [
            1019203231,
            "[[],35,34,null,false,false,true,37,true,true,true,true,true,[\"Raven\",\"_sharedLibs\",\"hsw\",\"__wdata\"],[[\"getElementsByClassName\",[]],[\"getElementById\",[]],[\"querySelector\",[]],[\"querySelectorAll\",[]]],[],true]"
        ],
        [
            1438349120,
            "6174559167396075939"
        ],
        [
            2974784595,
            "[0,18407,18407]"
        ],
        [
            3095117296,
            "[\"5.0 (Windows NT 10.0; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) discord\/1.0.9041 Chrome\/120.0.6099.291 Electron\/28.2.10 Safari\/537.36\",\"Mozilla\/5.0 (Windows NT 10.0; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) discord\/1.0.9041 Chrome\/120.0.6099.291 Electron\/28.2.10 Safari\/537.36\",8,4,\"sv\",[\"sv\",\"sv-SE\"],\"Win32\",null,[\"Not_A Brand 8\",\"Chromium 120\"],false,\"Windows\",2,5,true,false,100,false,false,false,\"[object Keyboard]\",false,false]"
        ],
        [
            3227950072,
            "[24,24,65536,212992,200704]"
        ],
        [
            2963547975,
            "[16,1024,4096,7,12,120,[23,127,127]]"
        ],
        [
            1177832592,
            "[76843806720,76843806720,null,null,1098907648,true,true,true,null]"
        ],
        [
            2158825350,
            "[1,1024,1,1,4]"
        ],
        [
            188652528,
            "[16,4096,30,16,16384,120,12,120,[23,127,127]]"
        ],
        [
            262879291,
            "16153807394097295248"
        ],
        [
            3025237892,
            "17002384262467705698"
        ],
        [
            1538111826,
            "2337666753322697468"
        ],
        [
            2455893439,
            "\"Europe\/Stockholm\""
        ],
        [
            2970644973,
            "[\"mDQJ3B2NhDMJwE2DhBGJTJaF\",\"7\",\"e\",\"XECWHDBSUQEBL\"]"
        ],
        [
            2620085432,
            "[4,120,4]"
        ],
        [
            3197521464,
            "11038406483972230190"
        ],
        [
            2150450975,
            "140443318783123448"
        ],
        [
            2772590518,
            "[\"Google Inc. (Intel)\",\"ANGLE (Intel, Intel(R) UHD Graphics (0x00004E71) Direct3D11 vs_5_0 ps_5_0, D3D11)\"]"
        ],
        [
            1826871708,
            "[[254,[254,254,254,255,254,254,254,255,254,254,254,255,254,254,254,255]],[[11,0,1,105.015625,13,5,105.6171875],[[12,0,-1,113.125,17,4,113],[11,0,0,111,12,4,111],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[11,0,1,105.015625,13,5,105.6171875],[12,0,0,109.640625,14,3,110.1953125]]],[0,2,4,5,6,8,9,12,13,15,17,18,19,21,22,23,28,29,30,31,33,34,35,37,39,42,47,48,49,66,67,69,71,72,75,76,77,78,79,81,82],[0,0,0,0,14,3,0]]"
        ],
        [
            1007274290,
            "9345374751420407194"
        ],
        [
            3487278513,
            "1117"
        ],
        [
            3467501445,
            "57"
        ],
        [
            4272905495,
            "143.69999998807907"
        ],
        [
            1668959119,
            "627"
        ],
        [
            639595872,
            "1801.199999988079"
        ],
        [
            930901639,
            "144.10000002384186"
        ],
        [
            1268522788,
            "[16384,32,16384,2048,2,2048]"
        ],
        [
            3235903591,
            "[[true,\"sv-SE\",true,\"Microsoft Bengt - Swedish\",\"Microsoft Bengt - Swedish\"]]"
        ],
        [
            28433086,
            "40.59999996423721"
        ],
        [
            1246555942,
            "[10]"
        ],
        [
            1579262840,
            "[-6.172840118408203,-20.710678100585938,120.71067810058594,-20.710678100585938,141.42135620117188,120.71067810058594,-20.710678100585938,141.42135620117188,-20.710678100585938,-20.710678100585938,0,0,300,150,false]"
        ]
    ],
    "suspicious_events": [],
    "messages": null,
    "stack_data": null,
    "stamp": "1:2:2024-04-17:YxjYjxrrqypUPc91QRVyQB4RqN74TdHTTHCm9KBeOvrI\/CQoSq9hzdIAP\/uL4XYxOW27yPu9PaTrN6OTAoPe+i\/98G50DRHA9WVBxftfNSVOvMfr7C+AL\/RLdyy+d1c0Yrx6sfAMjX2d3hlDYGmj3CInJGxGfg8O2wnkCJpv6IsamC2AEP9Mvz9KuXWTAcBCF6N3kQ18kEaxncon7oz1Y2lwI450fsFL\/tvisOT7HW2ePkSEHoivo+JA5dfZbWoo::rwbWaioj:1d",
    "href": "https:\/\/discord.com\/register?redirect_to=%2Fchannels%2F%40me",
    "ardata": null,
    "errs": {
        "list": []
    },
    "perf": [
        [
            1,
            16
        ],
        [
            2,
            151
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
* 
