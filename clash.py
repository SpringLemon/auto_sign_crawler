from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def clash():
    try:
        driver = get_web_driver()
        driver.get("https://ikuuu.me/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-lg btn-block login']").click()
        time.sleep(1)
        element = driver.find_element_by_xpath("//*[@class='btn btn-icon icon-left btn-primary' or @class='btn btn-icon disabled icon-left btn-primary']")
        
        if "disabled" not in element.get_attribute("class"):
            # 如果不包含 "disabled" 类，则触发点击操作
            element.click()
        else:
            # 如果包含 "disabled" 类，则只打印日志
            print("Element is disabled, skipping click.明日再来")
        
        # driver.find_element_by_xpath("//*[@class='btn btn-icon icon-left btn-primary']").click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    clash()
