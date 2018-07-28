import requests
import re
import time
import PPC_keywords
import json

# Через амс апи амазона узнает поисковый объем для ключевой фразы
# Нужна свежая амс кука для запуска

def generate_params(keywords):
    params = ""
    for kw in keywords:
        p = "keywords={}&matchTypes=PHRASE&".format(kw)
        params = params+p
    return params

def get_volume(keywords):



    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,lt;q=0.8,ru;q=0.7,fr;q=0.6',
    'Referer': 'https://ams.amazon.com/campaigns/sponsored-search/new',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_mkto_trk=id:810-GRW-452&token:_mch-amazon.com-1484061060381-88259; aws-target-static-id=1485524802296-762573; ubid-tacbus=132-9844918-8928223; aws-session-id=142-0843907-1990040; aws-session-id-time=2123236246l; s_ev22=%5B%5B%27Deliver%2520by%2520%27%2C%271492601338858%27%5D%5D; aws-business-metrics-last-visit=1492709164976; aws-ubid-main=132-7039748-6402408; aws-session-token="u584qOrM2MXDFuFigZpoJqNoKZMy0m1gQ0j3ZBC1YsnYs9Wt88/bstSvlKYU9Xbrlok9js4eWAEyBFF0jVMZcA9lK1aDVoAx1fJg4zMRQx/AErvIZ0/A3qCIZV1REEqhFpHq6lojBkHMQY6Vrbq1rOkhoujaNah6UiqF6pUC/l2Xt1qyE88IfFMRz0JGDbHNz/j2m0U+BpJaNzRMSIJ6mkF4+ELDlMHKeClcXOqTVPw="; aws-x-main=kc7yw5HyskaRxugEEOJkXbr8I6H1EN9aPPxDckKvxlBVXBUGBRyYJ5y3uz0XKqNp; aws-at-main=Atza|IwEBIBfMZmgFSOc3dq2xzeXdJX1C1gdJqp_wK9wBaaY0Ma4vlOY46DolOonQFWLEGlYoF3pupKnaYRAWCyPp0F36UcFWNeJ3MwuebvfWReDbsQhvzQQHLQStDBhuOw3uF5Yo850UwwFVzM1B677A6rst_InOifD2cebtQ5rBlSfKg4LGCVd46qlLOKB9YxKkGX97zpgky4Fb_bdrEa79C0DUX-RR5pKf0rzcT4yvtpG8BsNxDJxrbAoj0cD_FcOIb3Pj1ujSqlPXBLePaIFYjgkKhRq4L41dxt1PtIXQNkpIaNw7aif7vwHcav_KEFObjKkXGY9GFJbzlE1pgL2cWaxvBbgHt30XsQ2Ac_REK1NVDEMyGq7djBDmHIzbmfAI-Yjvb3ohgAYrb12ELZ9pvSsHTt3cxio5IMVY-hxGMLTrX8mSD0X9eMUp-WIqW3aUN1dijHw; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A353138835046%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22Dzmitry%22%2C%22keybase%22%3A%22GLExhrU9Rr9rimIUbcW27Mfgp1s%2FPXzn8tHU8xAYB1k%5Cu003d%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D; __utmv=194891197.kc7yw5HyskaRxugEEOJkXbr8I6H1EN9aPPxDckKvxlBVXBUGBRyYJ5y3uz0XKqNp; __utma=194891197.1713669663.1489746890.1494862703.1494862722.29; regStatus=registered; session-id-time-jp=2082787201l; ubid-acbjp=358-5809614-8417007; sid="h/gwCbZpHKdXyvaAVvYBxg==|nY7or5K2JnLbDwAZbVVtiTE2/M1875jrfHBmYc106Sg="; lc-main=en_US; x-wl-uid=1koH5Za1e5oDko/Xpoor7aZ7+PYXnvCtTsPPnrAPgVgwUuVgI0s4Quc/8FsAJEiWDPeQC+3pDJ7C7LNQnUrzsIOWhwE4Dw849PSwVXtlRYpFr1gZBxaqTSjbP5g3xXfqpR+8kawa695c=; session-id-time-eu=2152526189l; ubid-acbuk=259-5260486-4787724; x-acbuk="40FF?2FzTyEC2?E8dmwwwpn9JxzwVL?nVdpgFPaV8LyO6Q9CMNZjWdFxsPjdm1Je"; s_vn=1559726217475%26vn%3D1; s_pers=%20s_vnum%3D1913118759093%2526vn%253D49%7C1913118759093%3B%20s_fid%3D50773B5755B50E31-17FDC45A77BFF7FA%7C1687351148384%3B%20s_dl%3D1%7C1529586548385%3B%20gpv_page%3DUS%253AAS%253AFBA-pricing%7C1529586548389%3B%20s_ev15%3D%255B%255B%2527ASUSCOLDirect%2527%252C%25271528722803013%2527%255D%252C%255B%2527NSGoogle%2527%252C%25271529584748393%2527%255D%255D%7C1687351148393%3B; s_fid=5104CD606F5162CE-1C443397E53F1747; lwa-context=7978394df66aa7df45fe803d57d61ce8; _rails-root_session=ZjBGSVpmVzMwblMydW1QdVcxY3YrSlRiVWlaeDhjcWE5NVNkODNmQ2pXVnVlNkNFZzdxMXZySlZzcElkeGRXQUxmVllVeXQ5ZnJUMVhvY0YrWko2bjdwYUUxMU1hdXppS2k1NW9YaTBpNGlpWmxpMW1MZ0hHeTRDTHZvKytCSUYzcnQ0ZjFBcEhJTU5zcVFIcTRzWm5NcnVjSHlZQy91ZWZka1gvNU42QjVEWHZoQ0YvWDJLQ3ZDUE0wZFpsVHk1LS1zR1JmSmVkWTlNQlNhSUdnUldXdFJ3PT0%3D--655a2d7262f9313ec2d30a5896b40e8d43d71e5e; skin=noskin; s_vnum=1925372470275%26vn%3D31; s_sq=%5B%5BB%5D%5D; s_nr=1531818569395-Repeat; s_dslv=1531818569397; s_ppv=85; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B; JSESSIONID=9E57607058E780CB9A714DF357D4B81F; session-id=146-3140671-5234701; ubid-main=135-1583131-5873258; csm-hit=GZYJ0EZW69T83WTZVWF4+s-GZYJ0EZW69T83WTZVWF4|1532210365848; session-id-time=2162930371l; session-token="Le8ZIOVaNcOpzjADqzZp4gDoS48o8b7lzkGZZ7GGejqs7wPxLwKyNTPFqVTIfp1yTJZ5raJ3mSn2MgS8fMa5vVNpe6ZRZoB7QsE057wgXXeIiMpjm56ZR0KZKz+4MR/SJQSPICDkWk91kgMP9SyP07BwQArbFTSUz+1o/kjbcmO2AKz0eyPGRLsGEjRmMHNygFyfbpDO5zZdvZVv1h97h/b/DLH5nwGpLUE0fWJqM34="; x-main="bgjUfrqSsulXY6AlV0TQhcB@DuVisLxCDiwT7PDAR52HfSNKwZ2vG@XSLelASJWx"; at-main=Atza|IwEBIFO-75GsB30mArzx-ytowCDjPAJGCc7Vi9HJI5pCb82MqXZ1xf72IoIQ7bhfteXrFSEuaxVmftZ9yIRx_QP3eTXeOpZ38dkADA6vSNpKTv3pk5y3KFIItKMTu6L8mbAkPqSoYFv8g5Y9303IWRE72co4eZWe6xruT7nt9nYjGE1sp7G3oBdcPGrxb0ugvzkJkhwnduErDld6HeXmCg7H4dDTylTllY-C17oew70dIku5WTQgj_cThNrccce0xtD3doKh2tJcq-qr9U8jBgfsMmT0d-bRC9BMVfnV2rWU2XWdGlGqrVNyfbDYuiAoJxcwb0-rofyJu-tCXkcWJOWYpCDCDuTRm6TbuIj09STmd8RZE1ajFqHn_uweZ8RQJ29B-TOfJx0pJDll6lkJRWcuWiBYAxnyxB2V9jyAqKejMVOOtQ; sess-at-main="6MyjzRJm87gBRfK6Sb++8cFOk4gNkQpE6tAl7dXyp5M="; sst-main=Sst1|PQE-DSTj5KQTnDOv2DdL6a30C8L1mL5b5ueWOiVmfYumaRVEu-qkqHa7qWI-2BI0NwZXk7MoPh9s5ljq9Ek1Nuf-bGJEzGstwdeDQvGXrOmCxkEXgiLbZ74jGvBm7cCfcs-2WxMNE_xLFjsxJKrqrY8GLJGs6LWIx1bAJH8fQO7zuAUICvdhyyGjO8gEKGLFmFnmi-oW2xIFjNd1KoWGL8_CAbNZUCD9iP-Pa8RYIBT8SqiOPvMwlrM4mqTrk93oO8lVVLJFi8AK47uO3bOQushIiTKs9sImC334uu2gLuWwB0qmaq7OfMcdOA6BWVamg899kuqrZF6w-70FoGdLUaeF-w'

    }

    params = generate_params(keywords)
    data = params+"entityId=ENTITYG3UOKJWY87EC&startDateUTC=Thu%2C+19+Jul+2018+22%3A08%3A57+GMT&landingPageUrl=https%3A%2F%2Fams.amazon.com%2Fhsa-ad-landing-page%2Fpreview%3Fasins%3DB0725QS78J%2CB07BL325JJ%2CB01MSYOAPH&cacheWarmup=false"
    url = "https://ams.amazon.com/api/keyword-power"
    r = requests.post(url, data, headers = headers, verify=False)
    return r.text

kw = PPC_keywords.generate()
#print(kw)
print(len(kw))

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

kw_chunks = chunks(kw, 500)
print(len(kw)/500)
final = []
for kw in kw_chunks:
    volumes = json.loads(get_volume(kw))
    #print(volumes)
    powers = volumes['keywordPowers']
    #print(powers)
    output = [[x['keyword'], x['power']] for x in powers if x['power'] != 'l']
    final.extend(output)
print(final)