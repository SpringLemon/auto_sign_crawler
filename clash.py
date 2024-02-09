import sys
from util import *
import time
from datetime import datetime, timezone
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # 添加 TimeoutException 导入

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def clash():
    driver = None
    try:
        #打印时间
        current_time = datetime.now()
        print("Current time:", current_time)
        print("Time zone:", current_time.astimezone().tzinfo)
        
        driver = get_web_driver()
        driver.get("https://ikuuu.me/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-lg btn-block login']").click()
        time.sleep(10)
        clickable_elements = driver.find_elements(By.XPATH, "//*[@class='btn btn-icon icon-left btn-primary']")
        try:
            disabled_element = driver.find_element(By.XPATH, "//*[@class='btn btn-icon disabled icon-left btn-primary']")
            print("已经签到过了，无需再次签到。")
        except NoSuchElementException:
            print("可以点击，尝试点击")
            driver.execute_script("arguments[0].click();", clickable_elements[0])
            #clickable_element.click()
            # 等待一段时间，确保点击操作完成
            time.sleep(5)
            print("点击成功")
    except TimeoutException as e:
        print(f"等待超时，无法找到可点击元素。 {str(e)}")
    except Exception as e:
        print(f"出现额外的异常，An error occurred: {str(e)}")
        raise
    finally:
        if driver:
            driver.quit()

if __name__ == '__main__':
    clash()
