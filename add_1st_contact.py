from selenium import selenium
import unittest, time, re

class add_1st_contact(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_add_1st_contact(self):
        sel = self.selenium
        sel.open("/main_app")
        sel.click("link=Add Contact")
        sel.wait_for_page_to_load("30000")
        sel.select("id_salutation", "label=Mr.")
        sel.type("id_first_name", "Guy")
        sel.type("id_last_name", "Johnson")
        sel.type("id_job_title", "CEO")
        sel.type("id_description", "The best guy I've ever met.")
        sel.type("id_phone", "617-000-0000")
        sel.type("id_email", "guy@johnson.com")
        sel.type("id_street", "123 Main Street")
        sel.type("id_city", "Boston")
        sel.type("id_state", "MA")
        sel.type("id_zip_code", "01243")
        sel.type("id_country", "USA")
        sel.type("id_im", "johnnyboy147")
        sel.click("//input[@value='submit']")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
