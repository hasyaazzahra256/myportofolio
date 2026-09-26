import os
import sys
import django
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

USER_PASSWORD = os.getenv("E2E_USER_PASSWORD")
ADMIN_PASSWORD = os.getenv("E2E_ADMIN_PASSWORD")

if not USER_PASSWORD or not ADMIN_PASSWORD:
    sys.exit("E2E_USER_PASSWORD dan E2E_ADMIN_PASSWORD belum diisi di berkas .env.")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portofolio.settings")
django.setup()

from django.contrib.auth.models import User

def setup_users():
    user, _ = User.objects.get_or_create(username="burhan_test")
    user.set_password(USER_PASSWORD)
    user.is_superuser = False
    user.is_staff = False
    user.save()

    admin, _ = User.objects.get_or_create(username="admin_test")
    admin.set_password(ADMIN_PASSWORD)
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()

def main():
    setup_users()

    options = webdriver.ChromeOptions()
    if "--headless" in sys.argv:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    base_url = "http://127.0.0.1:8000"

    try:
        # 1. Cek CSRF Token dan Cookie
        try:
            driver.get(f"{base_url}/login/")
        except Exception:
            print(f"Server belum berjalan di {base_url}. Jalankan 'python manage.py runserver' terlebih dahulu.")
            return

        csrf = wait.until(
            EC.presence_of_element_located((By.NAME, "csrfmiddlewaretoken"))
        )
        assert csrf.get_attribute("value")
        assert driver.get_cookie("csrftoken")
        print("[PASS] CSRF token dan cookie terverifikasi")

        # 2. Cek Login User Biasa dan Cookie Sesi
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("burhan_test")
        driver.find_element(By.NAME, "password").send_keys(USER_PASSWORD)
        
        login_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))
        )
        login_btn.click()

        wait.until(EC.url_to_be(f"{base_url}/"))
        assert driver.get_cookie("sessionid")
        assert driver.get_cookie("last_login")
        print("[PASS] Login user biasa dan cookie sesi berhasil")

        # 3. Cek Pembatasan Akses User Biasa (Otorisasi 403)
        driver.get(f"{base_url}/projects/add/")
        assert "403" in driver.title or "Forbidden" in driver.page_source or "Permission Denied" in driver.page_source
        print("[PASS] Otorisasi user biasa dibatasi (403)")

        # 4. Cek Akses Superuser ke Form Proyek
        driver.get(f"{base_url}/logout/")
        
        driver.get(f"{base_url}/login/")
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("admin_test")
        driver.find_element(By.NAME, "password").send_keys(ADMIN_PASSWORD)
        
        admin_login_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))
        )
        admin_login_btn.click()

        wait.until(EC.url_to_be(f"{base_url}/"))

        driver.get(f"{base_url}/projects/add/")
        wait.until(EC.presence_of_element_located((By.NAME, "csrfmiddlewaretoken")))
        print("[PASS] Akses superuser ke form proyek berhasil")

        # 5. Cek Logout dan Penghapusan Cookie
        driver.get(f"{base_url}/logout/")

        cookie_last_login = driver.get_cookie("last_login")
        assert cookie_last_login is None or cookie_last_login["value"] == ""
        print("[PASS] Logout dan pembersihan cookie berhasil")

        print("\nSemua pengujian E2E berhasil!")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()