from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import math
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

LETTERBOXD_USERNAME = os.getenv('LETTERBOXD_USERNAME')
LETTERBOXD_PWD = os.getenv('LETTERBOXD_PWD')

options = Options()
options.add_argument("--headless=new")
chrome = webdriver.Chrome(options)

def get_lettrboxd_lists(user_id):

    # Go to https://letterboxd.com``
    chrome.get('https://www.letterboxd.com')

    # Accept Cookies
    cookie_consent_button = chrome.find_element(By.XPATH, '//*[@id="html"]/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    cookie_consent_button.click()

    # Log In
    login_button = chrome.find_element(By.XPATH, '//*[@id="header"]/section/div[1]/div/nav/ul/li[1]/a/span[2]')
    login_button.click()

    time.sleep(1)

    username_field = chrome.find_element(By.XPATH, '//*[@id="username"]')
    username_field.send_keys(LETTERBOXD_USERNAME)

    time.sleep(2)

    pwd_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    pwd_field.send_keys(LETTERBOXD_PWD)

    login_button_click = chrome.find_element(By.XPATH, '//*[@id="signin"]/fieldset/div/div[4]/div[1]/input')
    login_button_click.click()

    time.sleep(3)

    # Go to my watchlist
    chrome.get('https://www.letterboxd.com/omerseydoux/watchlist/')

    time.sleep(2)

    watchlist_count = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/section/header/h1/span[2]'))
        )

    watchlist_count = str(watchlist_count.text).removesuffix('FILMS')
    watchlist_count = int(watchlist_count)

    time.sleep(3)

    i = 0
    my_watchlist = []

    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    movie_elements = chrome.find_elements(By.CLASS_NAME, "frame-title")

    for movie in movie_elements:
            i+=1
            if movie.get_attribute("innerText") == '':
                my_watchlist.append(movie.text)
            else:
                movie.get_attribute("innerText")
                my_watchlist.append(movie.get_attribute("innerText"))

    user_watchlist = []

    url = f'https://letterboxd.com/{user_id}/watchlist/'
    chrome.get(url)

    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    movie_elements = chrome.find_elements(By.CLASS_NAME, "frame-title")

    watchlist_count = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-nav"]/h1/span[2]'))
        )

    watchlist_count = str(watchlist_count.text).removesuffix('FILMS')
    watchlist_count = int(watchlist_count)

    i = 0
    page = 1

    total_pages = math.ceil(watchlist_count / 28)
    while page <= total_pages:
        url = f'https://letterboxd.com/{user_id}/watchlist/page/{page}/'
        chrome.get(url)
        time.sleep(1)  # Consider using explicit waits instead of sleep
        movie_elements = chrome.find_elements(By.CLASS_NAME, "frame-title")
        
        for movie in movie_elements:
            movie_title = movie.text or movie.get_attribute("innerText")
            if movie_title:
                user_watchlist.append(movie_title)
                movie_title
        
        page += 1 

    return my_watchlist, user_watchlist
