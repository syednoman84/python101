import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Website URL
url = "https://www.educative.io/courses/grokking-coding-interview/solution-sort-colors"

# Send a request and parse HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Create a folder to save images
os.makedirs("images", exist_ok=True)

# Find and download all image URLs
for img_tag in soup.find_all("img"):
    img_url = img_tag.get("src")
    if img_url:
        img_url = urljoin(url, img_url)  # Handle relative URLs
        img_name = os.path.join("images", img_url.split("/")[-1])

        # Download and save image
        img_data = requests.get(img_url).content
        with open(img_name, "wb") as f:
            f.write(img_data)
        print(f"Downloaded: {img_name}")
