from mytest.utils import create_chrome_driver, add_cookies

browser_driver = create_chrome_driver()
browser_driver.get('https://www.jd.com/')
add_cookies(browser_driver, 'jd.json')  # 添加用户信息cookies,模拟登录
