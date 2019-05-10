from selenium import webdriver
import threading

from webdriver_manager.chrome import ChromeDriverManager

last_seen = "Offline"


def check_for_online():
    global last_seen
    threading.Timer(1.0, check_for_online).start()
    try:
        is_online = driver.find_element_by_class_name('O90ur')
        if is_online.text != last_seen:
            last_seen = is_online.text
            print(is_online.text)
    except:
        print("---------------------")
        last_seen = "Offline"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

i = input("Press any key to Continue")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format("My No"))
user.click()

check_for_online()
