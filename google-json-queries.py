#!./env/bin/python3

import time
import json
import sys
from selenium import webdriver

def get_google_results(search, page=0):
    output = []
    driver = webdriver.Firefox()
    driver.get('http://www.google.com/')
    search_box = driver.find_element_by_id("lst-ib")
    search_box.send_keys(search)
    button = driver.find_element_by_name("btnG")
    button.click()
    time.sleep(1)
    start = page * 10
    driver.get(driver.current_url+"&start=%i" %start)
    time.sleep(1)
    results = driver.find_elements_by_class_name("g")
    for result in results:
        dump = result.text.split("\n")
        output.append(dump)
    return json.dumps(output, ensure_ascii=False).encode('utf-8').decode('utf-8')

if __name__ == "__main__":
    get_google_results("github lupin012345", 1)
