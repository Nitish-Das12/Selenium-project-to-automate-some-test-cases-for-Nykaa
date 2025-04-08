import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = uc.Chrome()
def face(driver):
    try:
        Makeup = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[1]"))
        )
        ActionChains(driver).move_to_element(Makeup).perform()
        time.sleep(2)
        face_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#my-menu > ul > li:nth-child(1) > ul > li > div > div:nth-child(1) > div > div > a'))
        )
        face_button.click()
        print("face section Successful.")

        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
def Night_cream(driver):
    try:
        skin = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[2]"))
        )
        ActionChains(driver).move_to_element(skin).perform()
        time.sleep(2)
        Night_cream_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#my-menu > ul > li:nth-child(2) > ul > li > div > div:nth-child(1) > div > ul:nth-child(2) > li:nth-child(2) > a'))
        )
        Night_cream_button.click()
        print("Night cream section Successful.")

        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
def Shampoo(driver):
    try:
        Hair = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[3]/a"))
        )
        ActionChains(driver).move_to_element(Hair).perform()
        time.sleep(2)  
        Shampoo_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#my-menu > ul > li:nth-child(3) > ul > li > div > div:nth-child(1) > div > ul > li:nth-child(1) > a'))
        )
        Shampoo_button.click()
        print("Shampoo section section Successful.")

        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")

def Brushes(driver):
    try:
        Appliences = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[4]/a"))
        )
        ActionChains(driver).move_to_element(Appliences).perform()
        time.sleep(2)  
        Brushes_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[4]/ul/li/div/div[1]/div/ul[1]/li[3]/a"))
        )
        Brushes_button.click()
        print("Brushes section Successful")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def Mens(driver):
    try:
        Mens_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[9]/a"))
        )
        Mens_section.click()
        print("Mens section Successful")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def Fragrance(driver):
    try:
        Fragrance_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[10]/a"))
        )
        Fragrance_section.click()
        print("Fragrence section Successful.")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def Natural(driver):
    try:
        Natural_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/div[2]/ul/li[6]/a"))
        )
        Natural_section.click()
        print("Natural section Successful")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def Decor(driver):
    try:
        fashion_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[1]/div/div[1]/ul[4]/li/a"))
        )
        ActionChains(driver).move_to_element(fashion_section).perform()
        time.sleep(2)  
        Decor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[1]/div/div[1]/ul[4]/li/ul/li/section/div/div/div/div[3]/div[2]/ul/li[2]/a"))
        )
        Decor_button.click()
        print("Decor section Successful")

        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
def Luxe(driver):
    try:
        Luxe_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[1]/div/div[1]/ul[3]/li/a"))
        )
        Luxe_section.click()
        print("Luxe section Successful")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def offers(driver):
    try:
        offers_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[3]"))
        )
        offers_section.click()
        print("offers section Successful")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def search_functionality(driver):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[1]/div/div[2]/div[1]/div/form/input"))
        )
        search_box.send_keys("lotion")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Products searched successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_download_app(driver):
    try:
        download_app_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[1]/div/div/div[2]/ul/li[1]/a/span[2]"))
        )
        time.sleep(2)
        download_app_button.click()
        print("Download App button clicked.")
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
def Store_and_events(driver):
    try:
        Store_and_events_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[1]/div/div/div[2]/ul/li[2]/a/span[2]"))
        )
        time.sleep(2)
        Store_and_events_button.click()
        time.sleep(2)
        print("Store and events Test Successful")
    except Exception as e:
        print(f"An error occurred: {e}")
def help(driver):
    try:
        help_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[1]/div/div/div[2]/ul/li[4]/a/span[1]"))
        )
        time.sleep(2)
        help_button.click()
        time.sleep(2)
        print("help Test Successful")
    except Exception as e:
        print(f"An error occurred: {e}")
def search_and_select(driver):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[1]/div/div[2]/div[1]/div/form/input"))
        )
        print("Search box found. Entering 'lotion' and submitting search.")
        search_box.send_keys("lotion")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Waiting for the lotion checkbox in the category section...")
        lotion_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#product-list-wrap > div:nth-child(3) > div > div.css-d2z3ro > a > div.css-1rd7vky > div.css-xrzmfa"))
        )
        lotion_checkbox.click()
        print("lotion checkbox clicked.")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")

def click_giftcard(driver):
    try:
        click_giftcard_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[1]/div/div/div[2]/ul/li[3]/a/span[2]"))
        )
        time.sleep(2)
        click_giftcard_button.click()
        time.sleep(2)
        print("Gift Card Clicked")
    except Exception as e:
        print(f"An error occurred: {e}")
def click_sign_in_button(driver):
    try:
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[2]/div[1]/div/button")
            )
        )
        sign_up_button.click()
        print("Sign Up button clicked.")
        log_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/button[1]")
            )
        )
        time.sleep(1)
        log_in_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")

def click_cart_button(driver):
    try:
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[2]/div[2]/button"))
        )
        cart_button.click()
        print("Cart button clicked.")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
def go_to_homepage(driver):
    driver.get("https://www.nykaa.com/")
    time.sleep(2)


def main():
    driver = uc.Chrome()
    try:
        driver.get("https://www.nykaa.com/")
        face(driver)
        go_to_homepage(driver)
        Night_cream(driver)
        go_to_homepage(driver)
        Shampoo(driver)
        go_to_homepage(driver)
        Brushes(driver)
        go_to_homepage(driver)
        Mens(driver)
        go_to_homepage(driver)
        Fragrance(driver)
        go_to_homepage(driver)
        Natural(driver)
        go_to_homepage(driver)
        Decor(driver)
        go_to_homepage(driver)
        Luxe(driver)
        go_to_homepage(driver)
        offers(driver)
        go_to_homepage(driver)
        search_functionality(driver)
        go_to_homepage(driver)
        select_download_app(driver)
        go_to_homepage(driver)
        Store_and_events(driver)
        go_to_homepage(driver)
        help(driver)
        go_to_homepage(driver)
        search_and_select(driver)
        go_to_homepage(driver)
        click_sign_in_button(driver)
        go_to_homepage(driver)
        click_cart_button(driver)
        go_to_homepage(driver)
        click_giftcard(driver)
        go_to_homepage(driver)
        


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if driver:
            driver.quit()
            print("Driver quit successfully.")


if __name__ == "__main__":
    main()
