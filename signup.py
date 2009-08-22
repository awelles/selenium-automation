from selenium import selenium
import unittest, time, re

class signup(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://qa.jobplanr.com/")
        self.selenium.start()
    
    def test_signup(self):
        sel = self.selenium
        sel.open("/login?next=/main_app")
        sel.type("id_username", "user409")
        sel.type("id_location", "Boston MA")
        sel.type("id_terms", "term1, term2")
        sel.type("//form[@id='signup-form']/p[4]/input", "email90@server.com")
        sel.type("id_password1", "password")
        sel.type("id_password2", "password")
        sel.click("//input[@value='Sign Up']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
