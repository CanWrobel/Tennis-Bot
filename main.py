import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Initialize the WebDriver with headless options
driver = webdriver.Chrome(options=chrome_options)

# URL der zu überprüfenden Seite
url = "https://zeh2.zeh.hu-berlin.de/sportarten/aktueller_zeitraum/_Tennis_-_Sporthalle.html"
driver.get(url)

print(driver.page_source)



# # Überprüfen, ob der gewünschte Text auf der Seite erscheint
# if "desired string or keyword" in driver.page_source:
#     print("Der Kurs ist frei!")
# else:
#     print("Der Kurs ist noch nicht frei.")

# WebDriver schließen
driver.quit()