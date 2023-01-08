import json
import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

def generate_transcript(video_id):
    try:
        # Must be a single transcript.
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        script = ""

        for text in transcript:
            t = text["text"]
            if t != '[Music]':
                script += t + " "

        return script, len(script.split())
    except:
        # Return empty values if there is an error generating the transcript
        return "", 0

video_ids = [
"kd_CEW4WksY",
"n2j4r5G-OYk",
"vz0vt0_hdv4&t=3191s",
"gRxpcmMA548&t=2460s",
"Dwi6UbdpZyk",
"voWKlhA7jV4&t=5s",
"oJENpymNn7c",
"UUZE7eK2dho&t=2084s",
"4O6mwAz8Ufc",
"RZdj-lZuC00&t=3089s",
"YoOzKC0Vsho",
"NLLCEyJAiqw",
"qJp8fL_nkpU&t=1329s",
"tUSN8stwHqc&t=2425s",
"fr3fxNtQnzE",
"S_nJ-8U_gQk&t=3757s",
"elOPBBli2Ec",
"c7nWti4MiHQ",
"OnVf_FgNZPs",
"-45GSsgN2HE&t=627s",
"qfLvglVuIBM",
"3QVlWl-N3O8&t=2938s",
"UZMfLhkazRI",
"KzKBtvZI40E",
"dBeosjr7PyY",
"-diEHAq4nGU",
"KrNw2X-pS3g",
"9WBWk5iU_9s",
"EohLtQNgsT0&t=209s",
"7x5M4lxK-dw&t=3490s",
"kwrw2ECniE4",
"iJWvPUoAkpo",
"hbIgmVWZTgM&t=1126s",
"DbA8sUHkNqg&t=3917s",
"28QJ4y-QSrU",
"EpKgigxEoho",
"jOHw_cLY7Kk&t=5s",
"HnW-xEgCego",
"Ym_56wTU8yA",
"j3BxaWxm0ok&t=29s",
"4oSLJyUt2ps&t=246s",
"KfSSplX2Lpk",
"ER7bO2hFndE&t=269s",
"viL8ykYJqKo&t=29s",
"290S2wVSgGc",
"xGilIA5MIuA&t=2826s",
"hbUZcRWaBHA&t=934s",
"OKI1X1qFgwg&t=3869s",
"aRHLhDkkGY4&t=4122s",
"FSC2IJnfEbk",
"PQFuKZBZJYo",
"dSAJPNCZLp8&t=310s",
"7YJ1SMw4mJs&t=49s",
"PB3D4KqURqQ",
"jMgBdn4Sad8",
"dL60Qvntw58&t=11s",
"uNGiJt90ac4&t=2415s",
"F3eTnrWOAwY",
"azWH1ft8Nhs&t=140s",
"ztYYrq8OLNo&t=216s",
"D2oYyNtfUm8&t=659s",
"k85jaTO2nqU&t=2803s",
"kp0Nun9LvNA",
"FXPtBtQA434",
"sN3igKSSETs",
"wPBI_s4ySh4&t=1956s",
"kaFSsAhxbCI",
"gnghxXfwOmc&t=31s",
"n33ppZ2APJc",
"fDK4OBsytdw&t=12s",
"lYDg5C_ughw&t=169s",
"_WrZzdJUJeM",
"q09rCxEBApU&t=15s",
"YAtQSKJ2HCA",
"V0ej29G7ZGg",
"GfASdLlDYQM&t=468s",
"91yxQC1Fitw",
"jblB9otywQQ&t=230s",
"9yjQGdw_QhY",
"PAYDjZABHrA&t=31s",
"dmvacTYd_YQ",
"rw6cJ3vKck4",
"PHYMQINvvmE&t=13s",
"bu3v7lE9gYI",
"7J4pKCumZps",
"Poc5H6aVTlw&t=31s",
"_FczUETbksU",
"jVwcH8c3boA",
"chgsVkO7Cqg",
"tWtWR97j6K0",
"pBSJa3iOxJQ",
"nC_cyhSkx4M",
"T3_XtJS2290&t=290s",
"-FI2qJe_E2E",
"ktghagq5_Mc",
"KVFetFmiFuw",
"Jb0u5C2CUN8&t=165s",
"IC6yEVlqqyc",
"qMMJ7RMVr5Y&t=8s",
"F5PpCnv6ogE",
"q9Eho1eAigg",
"gkrUXS8pRT0",
"aevGG8hcTig",
"BMCu3apx9Ns",
"sKfv4DossBc",
"Yt77QTrWk5g",
"ADrtzt146Gs&t=985s",
"0VL0jfmJGrg",
"zWIxnWhDFWg",
"Qt_XUKV16Fg",
"eybXYSzWteE",
"gsRkOnJHVeQ",
"gesHCZsWw00&t=1s",
"GsOVqTxZxyo",
"aUrhq5SmxiQ&t=747s",
"HuytSzVYEpA&t=1788s",
"LzUMOVNGkwo",
"MZq7cXm0-SM",
"e9-z05ijZ7U",
"BUmPWQuGNvs",
"lhWNCv9NhFg",
"5xhugkEbdec",
"ENSSoreFwBw",
"-Trp3mjjzf4",
"te3oca0fWEc",
"lJeCt8pyFVQ",
"_4BX4s4EeU8",
"ih9N4xFbNF4",
"hJ5bRxeYVGo",
"CCthihcnsBE",
"92FUVls_HgI",
"OKB_Fqj6u4I",
"ZXZbtgxUERY",
"ppy5aKQuEVY",
"vSp97E9yi5I",
"IOXkz1A5Kls&t=96s",
"2G12i-vdyk8&t=387s",
"KNz8jWQl5eU",
"sP547pZnCAs",
"i4SxdRElLwY",
"57qIflVpcv0",
"0LcpH_BKAqc",
"F2tljx5A98Q&t=1698s",
"kxJp8nsqaAs",
"0MaFPFjGWt0",
"ZOOpUQVvy5Y",
"QOYzIQ1ku7w",
"H1FYJlaxlOg",
"dFdG-6q3bGE",
"GZBky3e31YQ",
"GaVIZNI6U9M",
"S-rMXKMwa3Y",
"TTyLa4NsOKI",
"XGGF-Pf0Bg4",
"9uRFMpV4KzI",
"0Dggcf6AME0",
"4KfuQwB5rIs&t=2s",
"8m69oef7UJ8&t=1389s",
"Uxk4UvjnIq4",
"OU7w9HBzj8g",
"g2O3YIFyCok",
"5otJ_h1mjR4&t=175s",
"OrnqTgUGP_U",
"_yQwIe_06j4",
"NK1QIrMpcIs",
"x0Kgw38gXPg&t=21s",
"DKi6LiaTmuA",
"zZ7WN61cKJ8",
"dRgqUMTZX-s",
"bPumPdKbYBk",
"uGjNzErxg0E",
"igVcGYbNWVE",
"biuC4bUMvV0",
"ho22vkGFljg&t=12s",
"U_t4gI5Gib4&t=2066s",
"OQYjgieN_g8",
"_gD0hKNpuS4",
"8ndkqTY8foI",
"kzfSlCo2cGk&t=4172s",
"M1xTZ25yTKg",
"doHudrBHjHs",
"NoyFOeucPd4",
"9R18gs-5a4w",
"DqjMHErY10s",
"eh4j4yr27ZE",
"fGMc7DYhT7o",
"6p3K9bUS7cU&t=570s",
"0UGMRoB99Bk",
"puaj2oVgpck",
"1rInfEZjfGQ",
"_0kzqt3VZPU",
"X64vs8N5ctE",
"jCOSoVC0eZk&t=1s",
"UZQqidPMu6k",
"gchz3sdFdyk",
"dRF9rTqmJO8",
"FIL_9kCcTQc",
"9NRMaZ_nGw0",
"mnm_4WrWIIk",
"4qQG8qRltG4&t=1528s",
"p2MOAwF8f0Q&t=238s",
"EAaSnVwC9AM",
"8-WZKJ4rCfU",
"FLixboxUejQ",
"jUNIB_DDEMs",
"fOW2ZkYKOu4",
"8yWIOKW6YOw",
"QuOe6EPrxTw",
"YC-IhUl7fyY",
"4bjxFnAIAiI",
"z5oNMipn3Bk",
"49vWG8COZr4",
"bXIt9_rzs3I",
"NL8k40c6Lsc",
"kzcsq4xBtQ8",
"KprMrUregQQ&t=929s",
"fFiPVGN3J2M",
"3UD9poByGJk",
"lUoVcP5aEWw",
"FiQ2_vnVXRM",
"8wy2gOm1OJQ",
"VYH5AdhJt54",
"mBbDdxVlr70",
"Z4oW5ODW3r4",
"aUdu4lL4PUw",
"Drvb2sl460Y",
"YCq6RjGi-qA",
"YkLNy4vpPCI",
"f0lmY-wX_RE",
"qsITQ7pCZ2w&t=21s",
"Zohr8ukayAM",
"bgnesKjVcQs",
"3YwLBiTSmzA",
"mtfzljmVcSk&t=732s",
"Ez8pWWjiG-k",
"2vQYfMt1ooo",
"18CPOAc9eQw",
"40cZdzYHd2I",
"sdKxzWniujU",
"TEL81g7P1Ns",
"SfgJXVhINQA",
"H_eg74TWbFE",
"4uw6Zpq1U1A",
"fCPkg_QH_KA&t=9s",
"HCK3KrnQ15A",
"ReMOG_XwVBo",
"tjSmLYm9lY8",
"qupxnhvh7Jo",
"MOsie3uPTIU",
"O-10iau1bbA",
"38g3A1N5Wa0",
"o3ycgHnXmEI",
"pPROtfn1gAI",
"CSrBq2IXtKI",
"9SAAu6mAMAg",
"RCHqXIRv-qc",
"kRV1oHH26W8&t=2s",
"ZfTn0hFtVBw",
"5WOzdCZRDnU&t=2s",
"EMlrLQ967Tc",
"iIfRdjqYTH8",
"v5MPmpkwSQw",
"QDRDhNCV8W8",
"x8QQplxF6vs",
"ZdzDf9HFvFw&t=1522s",
"dCRalT0sAwo",
"gwHPaoCTW2E",
"sKlMnCtxuxM&t=1961s",
"SxHA9uyGIKk",
"3NfcPxFct-s&t=546s",
"GvuZrrsCoYs",
"WKut1IpyM8w",
"q7xqQpNQpTs",
"kKozccr60XM",
"MBIgYNAI9Fk",
"mcvhGmq1kGo&t=561s",
"Tkw-wWA0sjk",
"lfd6M9y9_TI",
"DUfUQFskyLg&t=519s",
"CarCWCl1JFk",
"hQTZDC47MN8",
"thN8VLUMOHY&t=3039s",
"A58P2xKrlTs",
"73EV8SHiR8Q",
"LpYqpMuP2nI",
"TrgpXyh5MXg",
"bDOXYn15qx4",
"bN0eTaT-vfk",
"qZCT-6pRYjw",
"VBuGaVAJFEQ",
"h7SN5bHDTBI",
"C5XdrLi7OmI",
"liRUa-Q5hF8",
"MEC-6QR5uy4",
"bv4b3XpiA5s",
"DI1ATngEPc4",
"9qQBjZakm4M",
"QZKmoL3j3tE",
"tUVFhRTOQdA",
"BpvfwVglvkY",
"zJEhG7fJaTw",
"dMIlcsvNYVg",
"wRyImMK0tyo",
"IdMN1VhfxME",
"BXgWF0Ke8PA",
"mGH8D90PA-c",
"OialI0ZNU3g&t=1s",
"QU24ix6GNiA",
"t8eNuRVFHeA&t=580s",
"BIqSQIMflTY",
"YedLNDjLL38",
"UJIuvQZGVSA&t=3s",
"g8TwxyhkTIQ",
"MFmBrMK-dOw",
"OjQ5qiErVVI",
"XZzJoSWug5g",
"ShgOGhEpBQY",
"_-v1U9DU5tM",
"5AnbL1lzpV0",
"LC6GkPQ3LRA",
"wpS1rXpn_UM",
"mhABUJ1Ya8o",
"ZERX2aJZqB8",
"SsweMF0Ws9E",
"WY-CBjrrOIY",
"GGAhx4GEf3I",
"0RKJSP68WSw",
"bGKJ-lvbB5A",
"zIMnrECZ7VI",
"N4X4yRFV59c",
"yl4UH66i0kw",
"YumEIQcI0KU",
"zbd6bz42oec",
"pDDmPi1lqNQ",
"b9aF2hhyjc0",
"ro0Blj7DVKA",
"-vOkFpZn6Eo",
"k9ewzaclfNY",
"5Xi2P3VGZ6c",
"2OPVp5KxwC0",
"bHIaUdwscyU",
"68SJ-5cEvyU",
"rH7E2d98NMo",
"IMcoGe5wYL8",
"vWLB3IrRUzk",
"gSxCZApJxjA",
"fHYAAV5EgRU",
"kEN5pcKbr9Q",
"gEaLP2RXSUc",
"h0ZZr61DJk4",
"NDN3gOTGGZo",
"jr07F1koMu0",
"1tnEi7wtxa0",
"iB3kIRL5Q4M",
"kfgBpNJe6Yc",
"fS3RSY00Lgg",
"vy5myYA97XE",
"wMah4vJAjnw",
"do1kfrgL6lM",
"l__LOdOqUQQ",
"sHKEAk6pxgo",
"RUhIxtOjJbo",
"0zZXUKe6MHY",
"mSbehsL1tCc",
"p3pSVrM0f_Y",
"yjjP6BTFDG8",
"_Osk_b0i5Pc",
"XH0by7sSoSc",
"ObpBZTWo4XE",
"5vscGRRdLro",
"cMLHkC2nMsw",
"iz6Um1Im3N0",
"1aqEDa-QtHo",
"eiFvlD9uIco",
"t7iVJBxlm-A",
"FrtvfC8oUKQ",
"EnwnkgLAx8o",
"GkNJbj5qbXM",
"bfa-S1D7dT8",
"rOmEYhbgjls",
"sBMmYOZn6a0",
"4wEa7qVhHOo",
"-RNTTFumXiE",
"YeExf0tqYSk",
"YyAV6eKv-D4",
"xM4WBW3jz_c",
"3KJZEzpgwdo",
"5wq4WgjafJ0",
"wNcuFdO_-qc",
"ySw_-ExrvGM",
"7s-yfHou_DA",
"YSf_OeszKfE",
"LOrGDNjrbs8",
"FvuNJCqoEvY",
"s8sg-xz9oi4",
"Gz4qL5w_inU",
"wNlpZAbjYmI",
"bpshHntGcjo",
"wuB79LddVgo",
"NtRCqi_NOQw",
"EnTXS6AwaDk",
"WExtmMPbl-8",
"j41Nu06zCSc",
"7UmZdKYYRAQ",
"PtZkAZlYKLA",
"FOdkglCm_oM",
"VZC9dLbZyhI",
"WnDdy2cj-4s",
"dCXAoi_1nbE",
"aeYLWJMAi4Q",
"Xqy6zKzN1io",
"EA9OjezToF0",
"97ffBAWuFmo",
"H0y00vcCK4s",
"zfszuDsekkU",
"3BE79HLoqJ0",
"qr6Xa9QyEbI",
"N-DhGGhrLMc",
"LDNs-nN5FB4",
"JWX7A9I5Tz8",
"RG4snbbtchg",
"oVQcDjA48-U",
"LO8pzYdJRqE",
"JDkADw8J9O8",
"NHJqVnq6GVk",
"F8Pwk6lCkZo&t=447s",
"s2ytPBksorQ",
"Yqoe3NGeeek",
"YH_4Ht_P0vk",
"yQpYUbwVY1A",
"AlCXaKB5BFc",
"UjIRjMWP1Fo",
"k6Rqn7Urjjw",
"J6LToevaHxg",
"lCXL4fw29YM",
"XKOMck-3L50",
"j6-B_87dMCI",
"FNzBxhgoJz4",
"v4oGGRpGcV8",
"EKu3l4ipPZc",
"sI0vhP-d2hE",
"CpbpUS5AJQE",
"pGXUuCuxdag",
"ev_RrMm57vc",
"J6VJv0BMUoE&t=1s",
"QTufgV6Ggws",
"BZ5ghqvmQOY",
"PQnA3gLzah0",
"wyoU8jU7J6I",
"un-bCjl-Y7s",
"fMEsNtmFIrc",
"znBKLlEalJ4",
"ELu2qxK_YEQ",
"3byyUYwo428",
"I322mVxBzc8",
"eqKuya1Bj3U",
"ynhneDSFWus",
"hQrDGedyZPM",
"7oJ51_cqhLs",
"TrjhpQNROuI",
"yKEV3rpU-U4",
"UCunNlIoIL4",
"mwNgcRVVOu0",
"R9pGJcXi6ZE",
"QzRtOZZfazM",
"c_ywLK2kSSE",
"9s8rpqWLmHI",
"AZxcrYBkaQ0",
"1K8N3U3bumk",
"qi6gGCZ8XpY",
"z6SY9jxATkA",
"iUgBqCrfDhE",
"XqrTQXekcrU",
"QGeK5DUYG9g",
"OVU3bP8jIuA",
"UWP_JcKCCQQ",
"YLJPR-Mnc3w",
"nP7OJcJqPjk",
"SzkQA-3EaY0",
"AhXScMtGUX0",
"oAUMACG0TEs",
"WwJWNEzW0_c",
"I3OkQk9F53s",
"G8lV-_l-GU4",
"9GGgrqqstzg",
"8gxDlB5l87M",
"H-PH7bLYsRA",
"hIW1HEOOMGs",
"ifiCROOSUzw",
"-WOxvaX8vNY",
"tl-9Fo1EeNo",
"BVWaTljNJZA",
"J6kABUHgGS4",
"-Fv4kdLwBq4",
"xLw7cDwaeQ8",
"As6rQ5Mp4As",
"zDdXksMI0BY",
"3k2XjeWXs3s",
"f1CFGwbaH5U",
"hQCcyt2cNIs",
"9yeVAOzeozM",
"dhNzpc3Yi1E",
"QWtI4WQrfC8",
"S9xHm4EwTZ0",
"wtHfe6IAQe4",
"64cxUewdOPc&t=1227s",
"HHQzjMNJ0_M",
"emC8YdGjWsI",
"x_TCKrTjf0Y",
"Shd76iXQc4w",
"hiVe845c2x8",
"eUcNaixCUe4",
"cr9n5BJe3ZY",
"-VcvCK1RZ2M",
"vGE64Ze-Oz0",
"qm8hnrxfDng",
"zNMzTu4X84k",
"q4UXcCt361I",
"ggJ1hYG6A3Y",
"AkLcvXZ3WJA",
"yHRLGLIiZuU",
"1SI2_dX0fTQ",
"r8WO7DSsidM",
"D0-mzhPOLi0",
"pE0CEIo0Img",
"Q-e6KKYK8ps",
"HqWd5hAbdoA",
"-RrX8YSAnLI",
"AzmXIKRBioI",
"05gUSVlrM9g",
"hrPaAhHE9aY",
"cSwzEyI7Qa4",
"R08alyj7GSY",
"Xm8RPBDZaC8",
"JK27WEm-CM8",
"y01gpxEBUV4",
"m91IBzCXdCY",
"PNetlwixYfk",
"uU6wxTEt_k4",
"IRhgSUnxYAQ",
"P_KaFd2Pe1o",
"4WbzQtZAWI8",
"R0GBo8IAu4M",
"PIl_crTtI90",
"CfGM6QSqAgY",
"8pelYuK37_8",
"y7RcwQ4ni1o",
"OTkn7KsPM3g",
"OEW5qEbqkgE",
"GFegGWLtkUs",
"rNoKqg3PVYU",
"lpqmvE3CS9I",
"gc6Tu26GmK0",
"BsLf5hE2yS8",
"21DP3LcHYfs",
"8Nws1AUnyc4",
"EFdtgZkDUYc",
"fAcOPiiPBRQ",
"zIMitbVSd6o",
"O-mz4V3pLww",
"84mF7j2Rt7U",
"Fk7gOFkxtts",
"mMm-9YHFbRk",
"RGO39CfohcE",
"yKkA3Ey4-Tk",
"rznOVt1a1q8",
"pzsF6jIx6L4",
"LWLqmGs8BeQ",
"F_ogZe4TXyw",
"_Oa9SovGJv8",
"Sgma3o8fiE0",
"kXiV6PpGo6M",
"W79f_y2EbYk",
"ACQvfvV1eZE",
"TryxiGL9G_w",
"0vmhGTnF62c",
"nW0In97nEzc",
"B0FtXYMPSMU",
"abWzRUhfTsc",
"Dmh_OUoVUwo",
"3HW9m8_bwdM",
"M-HosXpa6uM",
"EakDp68sgvM",
"6MPCa8Zk2bw",
"UrwopH6kJ9s",
"NBqvoQGL2Oc",
"21EzvrvHCiA",
"7MroHEqbV30",
"hCItqpcUPTQ",
"loCxuCpqWQ0",
"bKyTtyIFSuQ",
"7WJ1UANm9lY",
"qQYVyEmX-hA",
"P7WekOoeSHE",
"cjVDXapThxQ",
"OIqI0oyAKHQ",
"I0X_hqXBarI",
"Y62yLLK2Ays",
"ARaYnMIaABs",
"t5PbcLXu_LI",
"be5vl40gj3s",
"vL5qPsFSk_g",
"AU96VMkUibE",
"2n-m4Bx93Wc",
"1D8ShMg3cC8",
"_6OicRMxK90",
"aSpULJ2Tv6k",
"5XTSl6by_iw",
"cZ-yqMfpElg",
"akddVCeFkb0",
"o1-S8eCUFLE",
"Hb55XOJsiaw",
"j6rQV0G9V3E",
"zl2US-eNJPE",
"RwcCerkPPUI",
"IEk8Vuu9tr8",
"wFSUe-EtU00",
"ob_eGsfDhD4",
"NJvFH42xBUs",
"iiELOqU8XYs",
"OC4_PWLJgrc",
"LjstUQ1L7PI",
"QXJA2E8UQ60",
"k99wq3TRxp8",
"WxewIXvHO4s",
"yeiYJ57DrH4",
"s1xbSvdeilc",
"pb1R7aI3GLo",
"7pT51EZNcso",
"bTtq-M9iDHI",
"hUwNgxwN_pE",
"8gtkn9CFWjs",
"EhC5wfbusVk",
"vs7twa66cwA",
"DWOcGBHsPO8",
"h3EAxeNIaeU",
"oBRTbrcFk1g",
"oe7IsuL6-Vg",
"B0l911VC3-M",
"a7dr0tqrBP0",
"Tav7GUlCVE4",
"HnhhH19dQhg",
"QD5DEykQJXU",
"LARMc3Q7jQQ",
"CJl00Y0zB18",
"d7bbGUSP1vU",
"0Bsy0f9RPHY",
"HHcruYaa1xQ",
"TO4RJc28vLI",
"ptib14aEmPc",
"227qQbsqNh4",
"gfaS8MR-tk0",
"w-E1f_zTR8A",
"ZCVgBxtO2RA",
"5ISEJJpayjs",
"AyWNZM2r04s",
"Q9wKtRHbgGQ",
"skCWCR51QV0"
]

# Initialize an empty list to store the transcript data
transcript_data = []

counter = 1

# Loop through the list of video IDs
for video_id in video_ids:
    # Print the current video ID to the console, along with the counter value
    print("Processing video ID {}: {}".format(counter, video_id))

    # Generate the transcript for the current video
    transcript, no_of_words = generate_transcript(video_id)

    # Append the transcript data to the list
    transcript_data.append({
        'video_id': video_id,
        'transcript': transcript,
        'word_count': no_of_words
    })

    # Increment the counter
    counter += 1

# Write the list to the JSON file
with open('JSON Outputs/alltranscripts.json', 'w', encoding='utf-8') as json_file:
    json.dump(transcript_data, json_file, ensure_ascii=False)