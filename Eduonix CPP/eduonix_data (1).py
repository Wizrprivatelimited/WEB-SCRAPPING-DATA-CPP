import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import math
import time

# API endpoint
url = "https://www.eduonix.com/Client_api/getEduonixCourseList"

# Basic Auth credentials
auth = HTTPBasicAuth("APIUSER-wizr", "APIPASSWD-wizr")

# Headers
headers = {
    "X-API-KEY": "db71f0e8c9a45d31b238ae7f4c906abdfe32107c",
    "X-CLIENT-NAME": "wizr"
}

# Limit per page
limit = 100  # You can change this to a larger value for fewer API calls

all_courses = []

# First call to get total count
params = {"pageno": 1, "limit": limit}
response = requests.get(url, headers=headers, params=params, auth=auth)

if response.status_code == 200:
    data = response.json()
    total_count = data.get("data", {}).get("total_count", 0)
    total_pages = math.ceil(total_count / limit)

    print(f"📊 Total Courses: {total_count}, Pages: {total_pages}")

    # Loop through all pages
    for page in range(1, total_pages + 1):
        print(f"📥 Downloading page {page}/{total_pages}...")
        params = {"pageno": page, "limit": limit}
        resp = requests.get(url, headers=headers, params=params, auth=auth)

        if resp.status_code == 200:
            page_data = resp.json()
            courses = page_data.get("data", {}).get("list", [])
            all_courses.extend(courses)
        else:
            print(f"⚠️ Failed to fetch page {page}: {resp.status_code}")

        time.sleep(0.5)  # Small delay to avoid API overload

    # Save to Excel
    if all_courses:
        df = pd.DataFrame(all_courses)
        df.to_excel("/Users/romitbenkar/Downloads/eduonix_all_courses.xlsx", index=False)
        print(f"✅ Download complete! Saved {len(all_courses)} courses to eduonix_all_courses.xlsx")
    else:
        print("⚠️ No course data found.")

else:
    print(f"❌ API call failed: {response.status_code}")
    print(response.text)
