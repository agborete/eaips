from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Assuming you've set up your WebDriver instance (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Navigate to a web page
driver.get("https://www.example.com")

# Find an input element (e.g., a search box)
search_box = driver.find_element_by_name("q")

# Type something into the search box and press Enter
search_box.send_keys("example example-4")
search_box.send_keys(Keys.RETURN)  # Equivalent to pressing Enter key

# Close the browser
driver.quit()
