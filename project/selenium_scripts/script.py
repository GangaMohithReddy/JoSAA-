from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Ensure the path is correctly formatted with forward slashes
PATH = "C:/Users/91630/OneDrive - Indian Institute of Technology Guwahati/Desktop/chromedriver.exe"

# Initialize the ChromeDriver service
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get("https://techwithtim.net")
print(driver.title)
# Add a delay to keep the browser open for a while (e.g., 10 seconds)
time.sleep(10)

# Close the browser
driver.quit()
