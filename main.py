from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

url = ("https://www.linkedin.com/jobs/search/?currentJobId=3675473329&f_AL=true&"
       "geoId=103644278&keywords=marketing&location=United%20States&refresh=true")

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Sign in").click()

username = driver.find_element(By.NAME, "session_key")
username.send_keys("jalalwaleed18@gmail.com")

password = driver.find_element(By.NAME, "session_password")
password.send_keys("Ha$n1998")

driver.find_element(By.CLASS_NAME, "login__form_action_container").click()

time.sleep(15)

all_jobs = driver.find_elements(By.XPATH, "//div[@data-view-name='job-card']")

for job in all_jobs:
    time.sleep(2)
    print("called")
    job.click()
    time.sleep(2)

    try:
        driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()
        time.sleep(2)

        phone = driver.find_element(By.XPATH, "//input[@class=' artdeco-text-input--input']")
        phone.clear()
        phone.send_keys("777142703")

        scroll_amount = 500  # Adjust the value as needed
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(2)
        submit = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit.get_attribute("aria-label") == "Continue to next step":
            close = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-modal__dismiss svg')
            close.click()
            time.sleep(3)
            print("moha")
            discard = driver.find_element(By.XPATH, "//span[text()='Discard']")
            time.sleep(2)

            discard.click()
            time.sleep(2)
            continue
        else:
            submit.click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#artdeco-modal-outlet button").click()

    except NoSuchElementException:
        print('not found')
        continue
time.sleep(5)

driver.quit()
