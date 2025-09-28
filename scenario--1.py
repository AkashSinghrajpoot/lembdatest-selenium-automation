from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 🔑 Replace with your LambdaTest credentials
LT_USERNAME = "akashwill8055"
LT_ACCESS_KEY = "LT_MMIYRK49tJxySbkrR0pp7Lrd0sjoQLaZR4ZwJkmaEdYNgJp"

# ---------------------------
# Capabilities Setup
# ---------------------------
options = webdriver.ChromeOptions()
options.browser_version = "dev"
options.platform_name = "Windows 10"

lt_options = {}
lt_options["username"] = LT_USERNAME
lt_options["accessKey"] = LT_ACCESS_KEY
lt_options["project"] = "LambdaTest Selenium Playground"
lt_options["w3c"] = True
lt_options["plugin"] = "python-pytest"

options.set_capability("LT:Options", lt_options)

# ---------------------------
# Remote WebDriver (LambdaTest Hub)
# ---------------------------
driver = webdriver.Remote(
    command_executor=f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub",
    options=options
)

try:
    # ---------------------------
    # Open Simple Form Demo Page
    # ---------------------------
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert "simple-form-demo" in driver.current_url

    # ---------------------------
    # Single Input Message
    # ---------------------------
    message = "Welcome to LambdaTest"
    message_box = driver.find_element(By.ID, "user-message")
    message_box.clear()
    message_box.send_keys(message)
    driver.find_element(By.ID, "showInput").click()
    time.sleep(1)
    displayed_message = driver.find_element(By.ID, "message").text
    assert displayed_message == message
    print("✅ Single Input Message Test Passed")

    # ---------------------------
    # Two Input Fields
    # ---------------------------
    num1 = "5"
    num2 = "10"
    expected_sum = str(int(num1) + int(num2))

    input_a = driver.find_element(By.ID, "sum1")
    input_b = driver.find_element(By.ID, "sum2")
    input_a.clear()
    input_b.clear()
    input_a.send_keys(num1)
    input_b.send_keys(num2)

    # Click "Get Total" button
    driver.find_element(By.XPATH, "//button[text()='Get Sum']").click()
    time.sleep(1)

    sum_displayed = driver.find_element(By.ID, "addmessage").text
    assert sum_displayed == expected_sum, f"Expected '{expected_sum}', but got '{sum_displayed}'"
    print("✅ Two Input Fields Sum Test Passed")

finally:
    driver.quit()
