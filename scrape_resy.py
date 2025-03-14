from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import ipdb
import re 
import time




def main():
    hit_list = 'https://resy.com/account/lists/68397658-3C85-11EE-B7A5-0AD4F74D5C39'

    browser = webdriver.Chrome()
    site = 'https://resy.com/cities/new-york-ny/venues/mokyo?date=2025-02-20&seats=2'
    reservation_data = scrape_page(site,browser)
    ipdb.set_trace()

def scrape_my_hit_list(url,browser):
    browser.get(url)
    html = browser.page_source


def scrape_page(url,browser):
    browser.get(url)
    html = browser.page_source
    try:
        time.sleep(10) #wait for load 
        soup = BeautifulSoup(html, "html.parser")
        print(soup)
        need_to_know_elem = browser.find_element(By.CLASS_NAME, "VenuePage__need-to-know")
        need_to_know_text = need_to_know_elem.text
        reservation_elem = re.search(r'^[^.]*\bReservations\b[^.]*\.', need_to_know_text, re.MULTILINE)
        reservation_data = reservation_elem.group(0)
    except:
        print("fail")
        reservation_data = None
    return reservation_data

    ipdb.set_trace()

    reservation_elem = re.search(r'^[^.]*\bReservations\b[^.]*\.', need_to_know_text, re.MULTILINE)
    #reservations_desc = 
    ipdb.set_trace()

    element = driver.find_element_by_class_name("VenuePage__need_to_know")
    soup = BeautifulSoup(html, "html.parser")
    element = browser.find_element(By.CLASS_NAME, "VenuePage__need-to-know")
    browser.close()
    return soup


def get_html(url):
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    browser.close()
    return html


if __name__ == "__main__":
    main()