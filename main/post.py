# coding=utf-8
import requests
import getinfo


def run(UA, cook):
    # 读取个人提交信息
    info = getinfo.data(UA, cook)
    if info == 0:
        print("今日打卡已完成，自动打卡取消\n")
        return "已完成"
    # 提交今日打卡
    url = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    head = {
        'Host': 'yq.weishao.com.cn',
        'Connection': 'keep-alive',
        'User-Agent': UA,
        'Accept': '*/*',
        'Content-Length': str(len(str(info))),  # json转文字读取长度，再转为字符串
        'Content-Type': 'application/json',
        'Origin': 'https://yq.weishao.com.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    data = requests.post(url, json=info, headers=head).json()
    if data.get("errcode") == 0:
        print("打卡成功！")
        return "成功！"

    elif data.get("status") == 400:
        print("今日打卡已完成，自动打卡取消\n")
        return "已完成"

    else:
        print("---未知的errcode\n" + str(data) + "\n")
        return "未知结果"
