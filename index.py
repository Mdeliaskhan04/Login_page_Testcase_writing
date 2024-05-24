from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize window on start-up

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Navigate to Facebook
driver.get("https://www.facebook.com/")

# Print driver information
print("Driver title:", driver.title)
print("Driver name:", driver.name)
print("Driver URL:", driver.current_url)

# Quit the driver
driver.quit()
# This line prints the current URL of the driver

