# main.py
import time
import pandas as pd
from modules.login import Login
from modules.register import Register

def main():
    login_data = pd.read_excel('data/login_data.xlsx')
    registration_data = pd.read_excel('data/registration_data.xlsx')

    l = 0  # Indeks data login saat ini
    max_login_data_index = len(login_data) - 1
    

    while l <= max_login_data_index:
        Id_Atomy = str(login_data['ID ATOMY'][l])
        Password_Atomy = str(login_data['PW ATOMY'][l])
        print(f"Id_Atomy: {Id_Atomy}, Password_Atomy: {Password_Atomy}")

        login_instance = Login()
        driver = login_instance.login(Id_Atomy, Password_Atomy)

        if driver:
            print(f"Login Berhasil dengan ID Atomy {Id_Atomy}")

            for j, row_reg in registration_data.iterrows():
                Nama = row_reg['Nama Atomy']
                Email = row_reg['Email Atomy']
                Telpon = str(row_reg['Telpon Atomy'])
                Alamat = row_reg['Alamat Atomy']
                Password = row_reg['PW ATOMY']
                Pas_Meta = row_reg['PW TAMU']
                Tanggal_Lahir = row_reg['TANGGAL LAHIR']
                Nik_KTP = str(row_reg['NIK Atomy'])

                register_instance = Register()
                data_register = register_instance.register(
                    driver, Id_Atomy, Nama, Email, Telpon, Alamat, Password, Pas_Meta, Tanggal_Lahir, Nik_KTP
                    )
                
                if data_register:
                    print(f"Berhasil Mendaftarkan {j+1} {Nama}")
                    driver.quit()
                    time.sleep(2)

                    # Setelah selesai dengan pendaftaran, periksa apakah ada data login baru
                    updated_login_data = pd.read_excel('data/login_data.xlsx')
                    if len(updated_login_data) > max_login_data_index:
                        max_login_data_index = len(updated_login_data) - 1

                    print("Melakukan login dengan akun yang baru...")
                    l += 1

                    # Login dengan akun baru
                    Id_Atomy = str(updated_login_data['ID ATOMY'][l])
                    Password_Atomy = str(updated_login_data['PW ATOMY'][l])
                    driver = login_instance.login(Id_Atomy, Password_Atomy)


                else:
                    print(f"Data {j+1} Gadget")
                    driver.quit()
                    time.sleep(2)

        else:
            print(f"Login Gagal dengan ID Atomy {Id_Atomy}")

if __name__ == "__main__":
    main()
