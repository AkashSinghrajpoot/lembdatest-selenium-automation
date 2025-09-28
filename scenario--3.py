from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------
# LambdaTest Configuration
# -------------------------------
options = ChromeOptions()
options.browser_version = "dev"  # or set a specific version
options.platform_name = "Windows 10"

lt_options = {
    "username": "akashwill8055",       # Replace with your LambdaTest username
    "accessKey": "LT_MMIYRK49tJxySbkrR0pp7Lrd0sjoQLaZR4ZwJkmaEdYNgJp",    # Replace with your LambdaTest access key
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

# -------------------------------
# STEP 1: Open Input Form Demo
# -------------------------------
driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")

# -------------------------------
# STEP 2: Submit without filling form
# -------------------------------
submit_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "//form[@id='seleniumform']//button[contains(text(),'Submit')]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@id='seleniumform']//button[contains(text(),'Submit')]"))).click()
except:
    driver.execute_script("arguments[0].click();", submit_button)

# -------------------------------
# STEP 3: Validation Message
# -------------------------------
name_field = driver.find_element(By.NAME, "name")
validation_msg = name_field.get_attribute("validationMessage")
print("Validation message:", validation_msg)
assert "fill out this field" in validation_msg

# -------------------------------
# STEP 4: Fill form fields
# -------------------------------
driver.find_element(By.ID, "name").send_keys("akash_singh")
driver.find_element(By.ID, "inputEmail4").send_keys("johndoe@example.com")
driver.find_element(By.ID, "inputPassword4").send_keys("Test@123")
driver.find_element(By.ID, "company").send_keys("lambdatest")
driver.find_element(By.ID, "websitename").send_keys("https://www.lambdatest.com")
driver.find_element(By.ID, "inputCity").send_keys("New York")
driver.find_element(By.ID, "inputAddress1").send_keys("123 AI Street")
driver.find_element(By.ID, "inputAddress2").send_keys("Suite 101")
driver.find_element(By.ID, "inputState").send_keys("New York")
driver.find_element(By.ID, "inputZip").send_keys("10001")

# -------------------------------
# STEP 5: Select Country
# -------------------------------
country_dropdown = Select(driver.find_element(By.NAME, "country"))
country_dropdown.select_by_visible_text("United States")

# -------------------------------
# STEP 6: Submit the form
# -------------------------------
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@id='seleniumform']//button[contains(text(),'Submit')]"))).click()
except:
    driver.execute_script("arguments[0].click();", submit_button)

# -------------------------------
# STEP 7: Success message
# -------------------------------
success_message = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Thanks for contacting us')]"))
).text
print("Success message:", success_message)
assert "Thanks for contacting us, we will get back to you shortly." in success_message

# -------------------------------
# Close browser
# -------------------------------
driver.quit()
