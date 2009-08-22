from selenium import selenium
import unittest, time, re

class add_1st_opportunity(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_add_1st_opportunity(self):
        sel = self.selenium
        sel.open("/main_app")
        sel.click("link=Add Opportunities")
        sel.wait_for_page_to_load("30000")
        sel.type("id_name", "Opportunity 1")
        sel.type("id_amount", "$400")
        sel.select("id_rate", "label=Annual")
        sel.type("id_web", "www.opportunity1.com")
        sel.click("id_cover")
        sel.select("id_application", "label=Mail")
        sel.type("id_instruction", "instructins")
        sel.type("id_description", "decription")
        sel.select("id_type", "label=Full time")
        sel.click("//input[@value='submit']")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
