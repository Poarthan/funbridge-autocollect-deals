from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def collect_deals(user_name, user_password):
    driver = webdriver.Chrome()

    driver.get("https://play.funbridge.com/home")

    title = driver.title
    print(title)
    if title == "Funbridge":
        driver.implicitly_wait(5)
    
        username_box = driver.find_element(by=By.NAME, value="login")
        password_box = driver.find_element(by=By.NAME, value="password")
        
        username_box.send_keys(user_name)
        password_box.send_keys(user_password)
        submit_button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        submit_button.click()
        
        driver.implicitly_wait(5)
    
        gift_button = driver.find_element(by=By.XPATH, value="//button[@aria-label='Claim my gift']")
        gift_button.click()

        driver.implicitly_wait(5)
        
        try:
            claim = driver.find_element(by=By.XPATH, value="//span[.='Claim']")
            claim.click()
            print("Claimed")

            driver.implicitly_wait(5)
            try:
                claim = driver.find_element(by=By.XPATH, value="//span[.='Claim']")
                claim.click()
                print("claimed")
            except:
                print("Already claimed")
        except:
            print("Already claimed")
        driver.implicitly_wait(5)

        #find_out_more_button = driver.find_element(by=By.XPATH, value="//span[.='Find out more']")

        #find_out_more_button.click()

        driver.quit()

        return True
    elif title == "Funbridge - Home":
        print("Already logged in", user_name, "HELLA SUS")

        driver.quit()

        return False

    driver.quit()

    

    # text_box.send_keys("Selenium") 
    #gift_button = driver.find_element(by=By.CSS_SELECTOR, value=".main-header-button-red")
    #submit_button.click()


   # message = driver.find_element(by=By.ID, value="message")
   # value = message.text
   # assert value == "Received!"

    driver.quit()
#collect_deals()

result=collect_deals("your_username_or_email", "your_password")
if not result:
    time.sleep(5)
    collect_deals("your_username_or_email", "your_password")
time.sleep(5)
exit()
