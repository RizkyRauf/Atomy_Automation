import time
import logging
import random
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from config import chrome_driver_path

class Register:
    def __init__(self):
        self.driver_path = chrome_driver_path.CHROME_DRIVER_PATH

    def register(self, driver, Id_Atomy, Nama, Email, Telpon, Alamat, Password, Pas_Tamu, Tanggal_Lahir, Nik_KTP):
        try:
            if driver:
                self.navigate_to_register_page(driver)
                self.agree_to_term(driver)
                self.fill_registration_form(driver, Nama, Telpon, Alamat, Password, Pas_Tamu, Tanggal_Lahir, Nik_KTP)
                self.fill_search_location(driver)
                self.fill_email_end(driver, Email)
                self.check_sponsor_ID(driver, Id_Atomy)
                id_member_text = self.end(driver)

                data_to_save = {
                    'Nama AT': Nama,
                    'Email AT': Email,
                    'Telpon AT': Telpon,
                    'Alamat AT' : Alamat,
                    'PW ATOMY': Password,
                    'PW TAMU': Pas_Tamu,
                    'PW META': 'larasati22',
                    'Tanggal Lahir': Tanggal_Lahir,
                    'ID ATOMY': id_member_text,
                    'NIK KTP': str(Nik_KTP)
                }

                # Print the data for debugging
                print("Data to save:", data_to_save)

                self.save_to_file(data_to_save)
                self.logout(driver)
                return driver
            else:
                print("Driver Tidak ditemukan")
                return driver

        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan elemen")
            return None
        except Exception as e:
            logging.error(f"Error: {str(e)}")

    def navigate_to_register_page(self, driver):
        try:
            registration_url = 'https://www.atomy.com/id/Home/Account/MemberJoin_Step1'
            driver.get(registration_url)
            time.sleep(5)

            daftar_xpath = '//*[@id="container"]/div/div/div[1]/a'
            daftar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, daftar_xpath)))
            daftar.click()
            print("Berhasil dan melanjutkan agree to terms")

        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan elemen")
            return None
        except Exception as e:
            logging.error(f"error {(str(e))}")

    def agree_to_term(self, driver):
        try:
            # Klik checkbox untuk menyetujui
            checkbox_path = '//*[@id="agreeAllTop"]'
            checkbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, checkbox_path)))
            checkbox.click()

            #scroll
            for _ in range(5):
                driver.execute_script("window.scrollTo(0, 500)")
                time.sleep(3)

            konfirmasi_path = '//*[@id="bNext"]'
            konfirmasi_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, konfirmasi_path)))
            konfirmasi_button.click()
            print(" Berhasil dan melanjutkan fill registration form...")
            time.sleep(5)

        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan element...")
            return None
        except Exception as e:
            logging.error(f"error {(str(e))}")

    def fill_registration_form(self, driver, Nama, Telpon, Alamat, Password, Pas_Tamu, Tanggal_Lahir, Nik_KTP):
        self.fill_field(driver, '//*[@id="txtFirstName"]', Nama)
        self.fill_field(driver, '//*[@id="txtSocialNo"]', Nik_KTP)
        self.fill_field(driver, '//*[@id="txtBirthDay"]', Tanggal_Lahir, Keys.ENTER)
        self.fill_field(driver, '//*[@id="txtPwd"]', Password)
        self.fill_field(driver, '//*[@id="txtPwd2"]', Password)
        self.fill_field(driver, '//*[@id="txtGpwd"]', Pas_Tamu)
        self.fill_field(driver, '//*[@id="txtHandPhone"]', Telpon)
        self.fill_field(driver, '//*[@id="txtAddr2"]', Alamat)

    def fill_field(self, driver, xpath, value, *args):
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(value, *args)
        time.sleep(2)

    def fill_search_location(self, driver):
        cari_awal_xpath = '//*[@id="btnSearchZipcode"]'
        cari_awal = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, cari_awal_xpath)))
        cari_awal.click()
        time.sleep(2)
        
        try:
            provinsi_dropdown = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selState'))))
            provinsi_options = provinsi_dropdown.options
            random_provinsi_index = random.randint(1, len(provinsi_options) - 1)
            provinsi_dropdown.select_by_index(random_provinsi_index)
            time.sleep(3)

            kabupaten = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selCity'))))
            kabupaten_options = kabupaten.options
            random_kabupaten_index = random.randint(1, len(kabupaten_options) -1)
            kabupaten.select_by_index(random_kabupaten_index)
            time.sleep(2)

            kecamatan = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selMeon'))))
            kecamatan_options = kecamatan.options
            random_kecamatan_index = random.randint(1, len(kecamatan_options) -1)
            kecamatan.select_by_index(random_kecamatan_index)
            time.sleep(2)

            search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'btnSearch')))
            search.click()
            time.sleep(2)

            index_acak = random.randint(1, 5)
            pilih_xpath = f"//tbody[@id='tbdZipCodeList']/tr[{index_acak}]/td[6]"
            pilih = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, pilih_xpath)))
            pilih.click()
            time.sleep(2)
        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan element...")
            return None
        except Exception as e:
            logging.error(f"error {(str(e))}")
        
    def fill_email_end(self, driver, Email):
        try:
            email_xpath = '//*[@id="txtEmail1"]'
            email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, email_xpath)))
            email.send_keys(Email)
            time.sleep(3)

            gmail_path = '//*[@id="selEmail2"]/option[2]'
            gmail = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, gmail_path)))
            gmail.click()
            time.sleep(3)

            konfirmasi_xpath = '//*[@id="container"]/p[3]/a[1]'
            konfirmasi_button2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, konfirmasi_xpath)))
            konfirmasi_button2.click()
            print("Berhasil mengisi form")
            time.sleep(3)
        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan element...")
            return None
        except Exception as e:
            logging.error(f"error {(str(e))}")
        
    def check_sponsor_ID(self, driver, Id_Atomy):
        try:
            ID_sponsor = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'txtChuchonNo')))
            ID_sponsor.send_keys(Id_Atomy)
            time.sleep(2)

            search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'bChuchon')))
            search.click()
            time.sleep(2)

            huwon_cust1_xpath = '//*[@id="huwon_cust1"]'
            huwon_cust2_xpath = '//*[@id="huwon_cust2"]'

            huwon_cust1 = driver.find_element(By.XPATH, huwon_cust1_xpath)
            huwon_cust2 = driver.find_element(By.XPATH, huwon_cust2_xpath)

            if huwon_cust1.get_attribute('value') or huwon_cust2.get_attribute('value'):
                print(f'Tidak dilanjutkan karena huwon1 memliki value = {huwon_cust1}')
                print(f"Tidak dilanjutkan karena huwon2 memliki value = {huwon_cust2}")

            else:
                print("Dilanjutkan untuk memproses data selanjutnya")
                konfirmasi_xpath = '//*[@id="bOk"]'
                konfirmasi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, konfirmasi_xpath)))
                konfirmasi.click()
                time.sleep(2)

            end_konfirmasi_xpath = '//*[@id="container"]/p[3]/a[1]'
            end_konfirmasi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, end_konfirmasi_xpath)))
            end_konfirmasi.click()
            time.sleep(3)

        except TimeoutException:
            logging.error("Timeout: Tidak dapat menemukan element...")
            return None
        except Exception as e:
            logging.error(f"error {(str(e))}")

    
    def end(self, driver):
        try:
            for _ in range(6):
                driver.execute_script("window.scrollTo(0, 500)")
                time.sleep(3)

            konfrim_akhir_xpath = '//*[@id="container"]/p[3]/a[1]'
            konfrim_akhir = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, konfrim_akhir_xpath)))
            konfrim_akhir.click()
            time.sleep(3)

            nama_xpath = "//h3[@class='tb2Title']/span[@class='mcolor']"
            id_xpath = "//h3[@class='tb2Title']/span[@class='fs14 gray ml20']/em[1]"
            sandi_xpath = "//h3[@class='tb2Title']/span[@class='fs14 gray ml20']/em[2]"

            nama_element = driver.find_element(By.XPATH, nama_xpath)
            id_element = driver.find_element(By.XPATH, id_xpath)
            sandi_element = driver.find_element(By.XPATH, sandi_xpath)

            nama_txt = nama_element.text
            id_txt = id_element.text
            sandi_txt = sandi_element.text

            print(f"Berhasil mendaftarkan \nNama = {nama_txt}\nID = {id_txt}\nSandi = {sandi_txt}")
            return id_txt
        except Exception as e:
            print(f"Terjadi kesalahan saat mencari elemen: {str(e)}")
            return None


    def save_to_file(self, data):
        try:
            login_data = pd.read_excel('data/login_data.xlsx')
        except FileNotFoundError:
            login_data = pd.DataFrame()

        new_data = pd.DataFrame(data, index=[0]) 
        login_data = pd.concat([login_data, new_data], ignore_index=True) 
        login_data.to_excel('data/login_data.xlsx', index=False) 
        print("Data telah diperbarui")
        return login_data

    
    def logout(self, driver):
        try:
            logout = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="logoutForm"]/ul/li[2]/a'))
            )
            logout.click()
            time.sleep(3)
        except Exception as e:
            logging.error(f"Error during logout: {str(e)}")