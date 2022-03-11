# -*- coding: utf-8 -*-
from antlinker import antlinker
from server import *


def safe_report():
    test = antlinker('17615515967', '')  # 登录
    try:
        test.refresh_token()  # 利用access.token，refresh.token直接登录
    except:
        test.get_token()  # 重新登录

    if test.get_user_info():
        server(test.upload_temperature(), test.safe_report())  # 微信推送
    else:
        server("登录失败", "用户信息获取失败")
        print("用户信息获取失败")


if __name__ == "__main__":
    safe_report()
