#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 10:44:34 2025

@author: romitbenkar
"""
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import re

# # Path to your chromedriver
# chrome_driver_path = "/Users/romitbenkar/bin/chromedriver"  # <- Change this
# service = Service(executable_path=chrome_driver_path)

# options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')
# options.add_argument("--window-size=1920,1080")

# driver = webdriver.Chrome(service=service, options=options)

# # Open the webpage
# url = "https://www.henryharvin.com/schedule/power-bi-certification-training-course"
# driver.get(url)

# # Wait for JavaScript to load the content (increase if needed)
# time.sleep(5)

# # Get the entire HTML after JS has rendered
# page_source = driver.page_source

# # Search for "price_inr":"<amount>"
# match = re.search(r'"price_inr"\s*:\s*"(\d+)"', page_source)

# if match:
#     price_inr = match.group(1)
#     print(f"Price in INR: ₹{price_inr}")
# else:
#     print("Price not found.")

# driver.quit()
#%%
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# import re

# # 🔧 Set the correct path to your chromedriver
# chrome_driver_path = "/Users/romitbenkar/bin/chromedriver"  # ✅ Full absolute path
# service = Service(executable_path=chrome_driver_path)

# options = webdriver.ChromeOptions()

# options.add_argument('--disable-gpu')
# options.add_argument('--window-size=1920,1080')

# driver = webdriver.Chrome(service=service, options=options)

# # 🎯 Target URL
# url = "https://www.henryharvin.com/schedule/power-bi-certification-training-course"
# driver.get(url)

# # Wait for content to load
# time.sleep(5)

# # Get full HTML after JS loads
# html = driver.page_source

# # Extract price_inr and course_name using regex
# price_match = re.search(r'"batch_price"\s*:\s*"(\d+)"', html)
# course_match = re.search(r'"course_name"\s*:\s*"([^"]+)"', html)

# # Display results
# if course_match and price_match:
#     course_name = course_match.group(1)
#     price_inr = price_match.group(1)
#     print(f"Course Name: {course_name}")
#     print(f"Price (INR): ₹{price_inr}")
# else:
#     print("❌ Could not find course_name or price_inr")

# driver.quit()

#%%
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# import re
# import pandas as pd

# # Set your chromedriver path
# chrome_driver_path = "/Users/romitbenkar/bin/chromedriver"
# service = Service(executable_path=chrome_driver_path)

# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')  # Optional: no browser window
# options.add_argument('--disable-gpu')
# options.add_argument('--window-size=1920,1080')

# driver = webdriver.Chrome(service=service, options=options)

# # ✅ List of course URLs to scrape
# urls = [
# "https://www.henryharvin.com/schedule/10-days-korean-language-course",
# "https://www.henryharvin.com/schedule/7-qc-tools-training",
# ]

# # Store data
# data = []

# for url in urls:
#     driver.get(url)
#     time.sleep(5)  # Allow time for JS to load

#     html = driver.page_source

#     # Extract price and course name
#     price_match = re.search(r'"batch_price"\s*:\s*"(\d+)"', html)
#     course_match = re.search(r'"course_name"\s*:\s*"([^"]+)"', html)

#     if course_match and price_match:
#         course_name = course_match.group(1)
#         price_inr = price_match.group(1)
#     else:
#         course_name = "Not Found"
#         price_inr = "Not Found"

#     data.append({
#         "course_name": course_name,
#         "price_inr": price_inr,
#         "url": url
#     })

# driver.quit()

# # Convert to DataFrame and save to Excel
# df = pd.DataFrame(data)
# df.to_excel("/Users/romitbenkar/Downloads/henryharvin_courses.xlsx", index=False)

# print("✅ Data saved to henryharvin_courses.xlsx")
#%%
import undetected_chromedriver as uc
import time
import re
import pandas as pd
import random

# Setup undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)

urls = [

"https://www.henryharvin.com/schedule/basic-certification-in-hr-generalist-by-iit-guwahati"

# Add more URLs here
]

data = []

for url in urls:
    driver.get(url)
    time.sleep(random.uniform(6, 10))  # Add variability to act human

    html = driver.page_source

    price_match = re.search(r'"batch_price"\s*:\s*"(\d+)"', html)
    course_match = re.search(r'"course_name"\s*:\s*"([^"]+)"', html)

    if course_match and price_match:
        course_name = course_match.group(1)
        price_inr = price_match.group(1)
    else:
        course_name = "Not Found"
        price_inr = "Not Found"

    data.append({
        "course_name": course_name,
        "price_inr": price_inr,
        "url": url
    })

driver.quit()

df = pd.DataFrame(data)
df.to_excel(r"C:\Users\taslim.siddiqui\Downloads\Scraped_Prices_2.xlsx", index=False)

print("✅ Data saved to henryharvin_courses.xlsx")

