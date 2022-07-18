"""
@author     :jph
@phone      :18038327071
@date       :2022/7/17 10:46
@Project    :mytest
@FileName   :utils.py
@SoftWare   :PyCharm
@Description:获取浏览器驱动，设置网站cookies
"""
import json

from selenium import webdriver


def create_chrome_driver(*, headless=False):  # 默认浏览器是有头的
    """创建浏览器驱动"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    if headless:
        options.add_argument('--headless')
    # selenium反反爬设置
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 获得浏览器驱动
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {"source": """
            Object.defineProperty(navigator, "webdriver", { get: () => undefined })        
        """}
    )  # 把webdriver从True改为undefined，声明我不是selenium程序

    return browser


def add_cookies(browser, cookie_file):
    """解析保存cookies信息的文件，并给browser添加cookies信息"""
    with open(cookie_file, 'r') as file:
        cookie_list = json.load(file)  # 读取文件中的cookies  字典组成的list类型
        for cookie_dict in cookie_list:  # 添加登录后的cookies信息，这个cookies信息保存在文件file中
            browser.add_cookie(cookie_dict)
