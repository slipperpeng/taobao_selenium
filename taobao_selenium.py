from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 


driver = webdriver.Firefox(executable_path=r"H:\python学习笔记\A-python之网络爬虫\selenium的运用\geckodriver.exe") 
wait = WebDriverWait(driver,10)
driver.get('https://login.taobao.com/member/login.jhtml')


# 点击密码登录
choose_mm = wait.until(
	EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static'))
)
choose_mm.click()

# 将浏览器识别Selenium的webdriver属性进行更改,改为false即可绕开验证码的检测
script1 = 'Object.defineProperties(navigator,{"webdriver":{get:() => false}});'
driver.execute_script(script1)	


# 输入用户名
username = wait.until(
	EC.presence_of_element_located((By.CSS_SELECTOR,'#TPL_username_1'))
)
username.send_keys("你的用户名")

# 输入密码 
password = wait.until(
	EC.presence_of_element_located((By.CSS_SELECTOR,'#TPL_password_1'))
)
password.send_keys("你的密码")


# 实现登录
login = wait.until(
	EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_SubmitStatic'))
)
login.click()

















