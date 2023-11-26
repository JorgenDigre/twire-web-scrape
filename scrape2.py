from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Firefox driver using GeckoDriverManager
driver = webdriver.Firefox()

# URL of the webpage you want to scrape
url = "https://www.transfermarkt.com/mario-gotze/profil/spieler/74842"  # Replace with your desired URL

# Navigate to the webpage
driver.get(url)

# Find an element by its class name (change "your_class_name" to the desired class)
element = driver.find_element_by_class_name("data-header__shirt-number")

# Print the text of the found element
print(element.text)

# Close the browser
driver.quit()