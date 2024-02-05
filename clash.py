from util import *
import time
from datetime import datetime, timezone
from selenium.common.exceptions import NoSuchElementException

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def clash():
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
        time.sleep(1)
        clickable_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-icon icon-left btn-primary']"))
        )
        try:
            disabled_element = driver.find_element(By.XPATH, "//*[@class='btn btn-icon disabled icon-left btn-primary']")
            print("已经签到过了，无需再次签到。")
        except NoSuchElementException:
            print("可以点击，尝试点击")
            driver.execute_script("arguments[0].click();", clickable_element)
            #clickable_element.click()
            # 等待一段时间，确保点击操作完成
            time.sleep(2)
            print("点击成功")
        # driver.find_element_by_xpath("//*[@class='btn btn-icon icon-left btn-primary']").click()
    except Exception as e:
        print(f"出现额外的异常，An error occurred: {str(e)}")
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    clash()
