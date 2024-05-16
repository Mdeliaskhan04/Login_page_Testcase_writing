from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.facebook.com/")

print("Driver title:", driver.title)
print("Driver name:", driver.name)
print("Driver URL:", driver.current_url)  # This line prints the current URL of the driver

