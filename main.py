import os
import time
import config
import numpy as np
import spintax
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from random import randint, randrange, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM
from lxml.html import fromstring
import requests
from itertools import cycle
import json
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words


def login(email, password, proxy=None):

    options = uc.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    if proxy is not None:
        options.add_argument('--proxy-server=%s' % proxy)

    driver = uc.Chrome(options=options, executable_path=CM().install(),use_subprocess=True)
    driver.get('https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0')

    wait=WebDriverWait(driver, 50);
    email_field=wait.until(EC.visibility_of_element_located((By.ID,'identifierId')))
    for char in email:
        email_field.send_keys(char)

    wait.until(EC.visibility_of_element_located((By.ID,"identifierNext"))).click()
    time.sleep(3)
    password_field=wait.until(EC.visibility_of_element_located((By.NAME,'Passwd')))
    for char in password:
        password_field.send_keys(char)
    wait.until(EC.visibility_of_element_located((By.ID,"passwordNext"))).click()
    
    time.sleep(3)#if accounts ask otp means change sleep into 15 seconds  
    
    with open("urls.txt") as f:
         for url in f:
             driver.get(url) 
             
    time.sleep(7)
    
    driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

    time.sleep(2) 

    driver.execute_script("window.scrollTo(0, 600);")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()

    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
     
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
    
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

    driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

    driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

    time.sleep(3)

    send_comment_button = driver.find_element_by_id("submit-button").click()
      
    time.sleep(4)

    driver.close()#after one acc auto login and hits 30 cmts it again choose another accs and do same process


def main(email,password):
    driver = login(email, password)
    wait = WebDriverWait(driver, 50);
    keywords = [];
    
        
       

if __name__ == '__main__':
    with open('email.txt', 'r', encoding="utf8") as f:
        keywords = [line.strip() for line in f]
        for user in keywords:
            email_pass = user.split(",")
            main(email_pass[0],email_pass[1])

