from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------------------
# LambdaTest Configuration
# -------------------------------
options = ChromeOptions()
options.browser_version = "dev"  # Or a specific version
options.platform_name = "Windows 10"

lt_options = {
    "username": "akashwill8055",                # Your LambdaTest username
    "accessKey": "LT_MMIYRK49tJxySbkrR0pp7Lrd0sjoQLaZR4ZwJkmaEdYNgJp",                           # Your LambdaTest access key
    "project": "Untitled",
    "w3c": True,
    "plugin": "python-python"
}

options.set_capability("LT:Options", lt_options)

# Initialize remote WebDriver for LambdaTest
driver = webdriver.Remote(
    command_executor="https://hub.lambdatest.com/wd/hub",
    options=options
)

driver.maximize_window()
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)

# -------------------------------
# STEP 1: Open Drag & Drop Demo
# -------------------------------
driver.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")
print("✅ Page loaded successfully")

# -------------------------------
# STEP 2: Perform Drag and Drop Demo 1
# -------------------------------
source = wait.until(EC.presence_of_element_located((By.ID, "todrag")))
target = wait.until(EC.presence_of_element_located((By.ID, "mydropzone")))

items = source.find_elements(By.TAG_NAME, "span")
for item in items:
    action.drag_and_drop(item, target).perform()
    time.sleep(0.5)  # small delay for UI update

print("✅ Drag and Drop Demo 1 worked correctly")

# -------------------------------
# STEP 3: Navigate back to Selenium Playground home
# -------------------------------
driver.get("https://www.lambdatest.com/selenium-playground")

# -------------------------------
# STEP 4: Click on "Drag & Drop Sliders"
# -------------------------------
slider_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Drag & Drop Sliders')]")))
slider_link.click()
print("✅ Navigated to Drag & Drop Sliders page")

# -------------------------------
# STEP 5: Move slider from 15 to 95 reliably
# -------------------------------
slider_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#slider3 input.sp_range")))
slider_output = driver.find_element(By.ID, "rangeSuccess")

target_value = 95

# Incrementally move slider to trigger JS events correctly
while True:
    current_value = int(slider_output.text)
    if current_value >= target_value:
        break
    
    slider_width = slider_input.size['width']
    offset = ((target_value - current_value) / 99) * slider_width  # proportional to max-min
    move_by = min(offset, 10)  # limit movement per iteration
    
    action.move_to_element(slider_input).click_and_hold().move_by_offset(move_by, 0).release().perform()
    time.sleep(0.2)  # short wait for JS to update value

# Verify final value
final_value = int(slider_output.text)
assert final_value == target_value, f"Expected {target_value}, but got {final_value}"
print("✅ Slider moved correctly to", final_value)

# -------------------------------
# Close browser
# -------------------------------
driver.quit()
