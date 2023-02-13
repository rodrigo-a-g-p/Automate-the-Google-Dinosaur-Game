from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Start the game
dinosaur_game_url = 'https://elgoog.im/t-rex/'
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(dinosaur_game_url)
time.sleep(3)

page_body = driver.find_element(By.TAG_NAME, 'body')
page_body.send_keys(Keys.ARROW_UP)
time.sleep(3)


def run(input_speed_value):
    # # Alternatively, this function can be deployed
    # game_over_js_function = 'Runner.instance_.gameOver=()=>{}'
    speed_js_function = f'Runner.instance_.setSpeed({input_speed_value})'
    driver.execute_script(speed_js_function, page_body)


def init_game():
    speed_value = 100000
    while True:
        run(speed_value)
        speed_value += 10000
        time.sleep(1)


init_game()
