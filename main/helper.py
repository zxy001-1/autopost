# coding=utf-8
import time

import requests

hapi = "https://api.weishao.com.cn"
api = 'lightapp.weishao.com.cn'
dat = "schoolcode=chzu&username=203135&password=203135&verifyValue=&verifyKey=203135_chzu&ssokey="
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
url = 'https://lightapp.weishao.com.cn/check/reportstatistics'
try:
    # 多次重定向后登录
    url2 = requests.get(url, allow_redirects=False).headers['Location']
    res = requests.get(url2, allow_redirects=False).headers
    cook = res['set-cookie']
    url3 = hapi + res['Location']
    head = {
        'Host': api,
        'cache-control': 'max-age=0',
        'Content-Length': '92',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        "Cookie": cook
    }
    url4 = hapi + requests.post(url3, data=dat, headers=head, allow_redirects=False).headers['Location']

    head2 = {
        'Host': api,
        'cache-control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        "Cookie": cook
    }
    url5 = requests.get(url4, headers=head2, allow_redirects=False).headers['Location']
    cook = "Hm_lvt_2897656ea377e58fb1af08554ed019b4=1611801447,1611805930,1611815687,1611818213;" + \
           requests.get(url5, headers=head2, allow_redirects=False).headers['set-cookie'].split("; ")[0]
except Exception:
    print("登录错误")


def off(lists, id):
    reporturl = "https://lightapp.weishao.com.cn/api/reportstatistics/reportstatistics/getStatistical"
    data2 = {"type": "org", "identity": "", "para": {"organization_id": id, "organization_path_str": "3313,3314,3320"},
             "date": time.strftime("%Y-%m-%d"), "activityid": "5599", "flag": 0, "domain": "chzu", "stucode": "203135"}
    head3 = {
        'Host': api,
        "Content-Length": str(len(str(data2))),  # 传入数据长度
        'cache-control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'Content-Type': 'application/json',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        "Cookie": cook
    }
    x = 0
    res = requests.post(reporturl, json=data2, headers=head3).json().get("data").get("users")
    for i in range(len(res)):
        if res[i].get("is_report") == 0:
            info = {
                "stucode": res[i].get("user_id"),
                "password": res[i].get("user_id"),
                "notice": "false",
            }
            x = x + 1
            lists.append(info)
    return x


# 抓包获取的
# 网工201:3313
# 网工202:3314
# 智能20 :3320
classes = ["3313", "3314"]  # ,"3320"]
# 未打卡的人的学号列表
lists = []
# 每个班未打卡的人数
num = []
for i in range(2):
    num.append(str(off(lists, classes[i])))
print("共有" + str(len(lists)) + "人未打卡\n网工201 共" + num[0] + "人\n网工202 共" + num[1] + "人\n")  # 智能20  共" + num[2] + "人\n")
'''
if len(lists) == 0:
    print("所有人打卡完成")
    sys.exit()

for i in range(0, len(lists)):
    print("开始为 " + lists[i].get("stucode") + " 打卡")
    try:
        cook = sign.login(lists[i], UA)
        main.run(lists[i], UA, cook)
    except ConnectionError:
        print("---为 " + lists[i].get("stucode") + " 打卡失败")
print("\n所有人打卡完成")
'''
