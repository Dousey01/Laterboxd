from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dotenv import find_dotenv, load_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv())
LETTERBOXD_USERNAME = os.getenv('LETTERBOXD_USERNAME')
LETTERBOXD_PWD = os.getenv('LETTERBOXD_PWD')

def setup_webdriver():
    """Initialize and return the Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)

def accept_cookies(chrome):
    """Accept cookies on the page."""
    try:
        cookie_consent_button = chrome.find_element(By.XPATH, '//*[@id="html"]/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
        cookie_consent_button.click()
    except:
        print("Cookie consent button not found or not clickable.")

def login(chrome, username, password):
    """Log in to the Letterboxd account."""
    chrome.get('https://www.letterboxd.com')
    accept_cookies(chrome)  # Assuming the cookie button appears on the homepage
    login_button = chrome.find_element(By.XPATH, '//*[@id="header"]/section/div[1]/div/nav/ul/li[1]/a/span[2]')
    login_button.click()
    time.sleep(1)
    
    username_field = chrome.find_element(By.XPATH, '//*[@id="username"]')
    username_field.send_keys(username)
    pwd_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    pwd_field.send_keys(password)
    
    login_button_click = chrome.find_element(By.XPATH, '//*[@id="signin"]/fieldset/div/div[4]/div[1]/input')
    login_button_click.click()
    time.sleep(3)  # Consider replacing this with an explicit wait

def get_user_watchlist(chrome, user_id):
    """Retrieve the watchlist for the specified user."""
    user_watchlist = []
    chrome.get(f'https://letterboxd.com/{user_id}/watchlist/')
    time.sleep(2)  # Again, consider using explicit waits here
    
    # Scroll and fetch movies
    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    movie_elements = chrome.find_elements(By.CLASS_NAME, "frame-title")
    for movie in movie_elements:
        movie_title = movie.text or movie.get_attribute("innerText")
        if movie_title:
            user_watchlist.append(movie_title)
    
    return user_watchlist
