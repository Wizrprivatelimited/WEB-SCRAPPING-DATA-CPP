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
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)

urls = [
"https://www.henryharvin.com/schedule/r-programming-data-science-course#Certification",
"https://www.henryharvin.com/schedule/russian-language-course",
"https://www.henryharvin.com/schedule/sales-cloud-consultant",
"https://www.henryharvin.com/schedule/sales-executive-course",
"https://www.henryharvin.com/schedule/salesforce-marketing-cloud-email-specialist-certification",
"https://www.henryharvin.com/schedule/sanskrit-language-course",
"https://www.henryharvin.com/schedule/sap-fico-training",
"https://www.henryharvin.com/schedule/sap-mm-sd-integrated-mastery-training",
"https://www.henryharvin.com/schedule/sap-mm-training",
"https://www.henryharvin.com/schedule/sap-sd-training",
"https://www.henryharvin.com/schedule/saving-insurance-scheme-course",
"https://www.henryharvin.com/schedule/sbi-cbo-exam-prep-course",
"https://www.henryharvin.com/schedule/scrum-master-exam-preparation-course",
"https://www.henryharvin.com/schedule/scrum-owner-exam-preparation-course",
"https://www.henryharvin.com/schedule/scrum-study-agile-master-certified-course",
"https://www.henryharvin.com/schedule/service-desk-analyst-training",
"https://www.henryharvin.com/schedule/six-sigma-certification-with-marketing-analytics",
"https://www.henryharvin.com/schedule/six-sigma-champion-certified",
"https://www.henryharvin.com/schedule/six-sigma-green-belt-and-black-belt",
"https://www.henryharvin.com/schedule/six-sigma-green-belt-black-belt-agile-course",
"https://www.henryharvin.com/schedule/six-sigma-in-it",
"https://www.henryharvin.com/schedule/social-media-marketing-course",
"https://www.henryharvin.com/schedule/spanish-creative-writing-advance-level-course",
"https://www.henryharvin.com/schedule/spanish-creative-writing-beginner-level-course",
"https://www.henryharvin.com/schedule/spanish-fluency-conversation-course",
"https://www.henryharvin.com/schedule/spanish-language-course",
"https://www.henryharvin.com/schedule/spanish-language-course-for-kids",
"https://www.henryharvin.com/schedule/spc-training",
"https://www.henryharvin.com/schedule/ssc-chsl-preparation",
"https://www.henryharvin.com/schedule/startup-generalist-virtual-assistant-training-course",
"https://www.henryharvin.com/schedule/stock-market-course",
"https://www.henryharvin.com/schedule/strategy-consulting-course",
"https://www.henryharvin.com/schedule/supply-chain-management-course",
"https://www.henryharvin.com/schedule/system-administration-it-infrastructure-services",
"https://www.henryharvin.com/schedule/tableau-training",
"https://www.henryharvin.com/schedule/talk-to-me-in-korean-course",
"https://www.henryharvin.com/schedule/tally-prime-course",
"https://www.henryharvin.com/schedule/tamil-language-course",
"https://www.henryharvin.com/schedule/taxation-law-course",
"https://www.henryharvin.com/schedule/tax-litigation-and-advanced-corporate-taxation-course",
"https://www.henryharvin.com/schedule/tax-practitioner-course",
"https://www.henryharvin.com/schedule/tds-practitioner-course",
"https://www.henryharvin.com/schedule/technical-writing-course",
"https://www.henryharvin.com/schedule/technology-management-training-program-course",
"https://www.henryharvin.com/schedule/teen-mba-course",
"https://www.henryharvin.com/schedule/tefl-course",
"https://www.henryharvin.com/schedule/torfl-exam-preparation-course",
"https://www.henryharvin.com/schedule/total-productive-maintenance-tpm-for-production-and-quality-systems-course",
"https://www.henryharvin.com/schedule/tourism-and-hospitality-professional-course",
"https://www.henryharvin.com/schedule/trademark-law-course",
"https://www.henryharvin.com/schedule/trademark-licensing-prosecution-and-litigation-course",
"https://www.henryharvin.com/schedule/train-the-trainer-course",
"https://www.henryharvin.com/schedule/us-corporate-law-and-paralegal-studies-course",
"https://www.henryharvin.com/schedule/us-corporate-law-for-company-secretaries-and-chartered-accountants-course",
"https://www.henryharvin.com/schedule/us-intellectual-property-law-and-paralegal-studies-course",
"https://www.henryharvin.com/schedule/vmware-planning-management-operations-training",
"https://www.henryharvin.com/schedule/workday-finance-integration-service",
"https://www.henryharvin.com/schedule/workplace-in-diversity-course-seattle",
"https://www.henryharvin.com/schedule/young-learners-teacher-training",
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
df.to_excel("/Users/romitbenkar/Downloads/henryharvin_courses.xlsx", index=False)

print("✅ Data saved to henryharvin_courses.xlsx")

