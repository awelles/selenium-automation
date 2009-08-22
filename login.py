from selenium import selenium
import unittest, time, re

class login(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_login(self):
        sel = self.selenium
        sel.open("/login?next=/main_app")
        sel.type("id_email", "john@welles.net")
        sel.type("id_password", "password")
        sel.click("//input[@value='Log in']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
