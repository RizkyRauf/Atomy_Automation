import time
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config import chrome_driver_path

class Login:
    def __init__(self):
        self.driver_path = chrome_driver_path.CHROME_DRIVER_PATH

    def login(self, Id_Atomy, Password_Atomy):
        try:
            # Inisialisasi Service object
            service = Service(self.driver_path)

            # Inisialisasi Options object
            options = Options()
            # options.add_argument("user-data-dir=C:/Users/rauf/AppData/Local/Google/Chrome/User Data")

            driver = webdriver.Chrome(service=service, options=options)
            
            login_url = "https://www.atomy.com/id/Home/Account/Login"
            driver.maximize_window()
            driver.get(login_url)
            time.sleep(4)

            # Masukkan ID ATOMY
            id_path = '//*[@id="userId"]'
            id_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, id_path)))
            id_field.send_keys(Id_Atomy)

            # Masukkan Password
            password_path = '//*[@id="userPw"]'
            password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, password_path)))
            password_field.send_keys(Password_Atomy)

            # Klik Login
            login_button_path = '//*[@id="frm"]/div/div/div[1]/p[1]'
            login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, login_button_path)))
            login_button.click()

            time.sleep(4)

            return driver
        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan elemen")
            return None
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return None
