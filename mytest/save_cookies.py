"""
@author     :jph
@phone      :18038327071
@date       :2022/7/17 10:47
@Project    :mytest
@FileName   :save_cookies.py
@SoftWare   :PyCharm
@Description:使用selenium登录京东并保存cookies信息
登录地址：https://passport.jd.com/new/login.aspx
"""
import json
import time

from mytest.utils import create_chrome_driver

# 获取浏览器驱动
driver = create_chrome_driver()
url = 'https://passport.jd.com/new/login.aspx'
driver.get(url=url)
time.sleep(30)  # 休眠30s供我们手动登陆操作
driver.refresh()
with open('jd.json', 'w') as file:
    cookies = driver.get_cookies()  # cookies是一个列表，其中的元素是字典
    json.dump(cookies, file)
    print(f'cookies保存完毕，请到{file.name}文件中查看')
