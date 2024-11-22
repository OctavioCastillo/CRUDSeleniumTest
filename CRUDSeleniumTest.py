import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CRUD_TEST(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://mern-crud-mpfr.onrender.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def create(self, nombre:str, email:str, años:str, test_type):
        self.new_record = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/button')))
        self.new_record.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/form/div[1]/div/input'))).send_keys(nombre)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "age").send_keys(años)

        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/div[3]/div[2]/div').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/form/div[3]/div[2]/div/div[2]/div[1]'))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/form/button'))).click()

        if test_type=="create":
            try:
                output = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/form/div[4]/div/p'))).text
                print(f"message:{output}")
                return(output)
            except Exception as e:
                output = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/form/div[5]/div/p'))).text
                print(f"message:{output}")
                return(output)
        else:
            self.driver.refresh()

    # def test_create_new_record(self):
    #     output = self.create("luis1", "luis1@gmail.com", "25", "create")
    #     self.assertEqual(output, "Successfully added!")

    # def test_create_new_record_existing_email(self):
    #     output = self.create("luis1", "luis1@gmail.com", "25", "create")
    #     self.assertEqual(output, "That email is already taken.")

    # def test_modify_age(self):
    #     self.modify_record = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/button[1]')))
    #     self.modify_record.click()
    #     age = self.driver.find_element(By.NAME, "age")
    #     time.sleep(5)
    #     age.clear()
    #     age.send_keys("50")
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/form/button'))).click()
    #     output = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/form/div[4]/div/p'))).text
    #     print(output)
    #     self.assertEqual(output, "Successfully updated!")

    # def test_delete_record(self):
    #     deleted_record = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/button[2]')))
    #     deleted_record.click()
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/button[1]'))).click()

    # def test_find_one(self):
    #     self.create("octavio", "octavio@gmail.com", "23", "pass")
    #     self.create("diego", "diego@gmail.com", "23", "pass")
    #     self.create("juan", "juan@gmail.com", "23", "pass")
    #     name = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[1]'))).text
    #     print(name)
    #     self.assertEqual("Diego", name)

    def test_find_all(self):
        self.create("eduardo", "eduardo@gmail.com", "25", "pass")
        name1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[1]/td[1]').text
        name2 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[1]').text
        name3 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[3]/td[1]').text
        name4 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[4]/td[1]').text

        email1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[1]/td[2]').text
        email2 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[2]').text
        email3 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').text
        email4 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/table/tbody/tr[4]/td[2]').text

        # hacer 8 asserts para cada uno 
        

    # def tearDown(self):
    #     self.driver.refresh()
    #     self.driver.quit()

unittest.main()


