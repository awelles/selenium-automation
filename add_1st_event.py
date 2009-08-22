from selenium import selenium
import unittest, time, re

class add_1st_event(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_add_1st_event(self):
        sel = self.selenium
        sel.open("/tasks/")
        sel.click("link=Add Events")
        sel.wait_for_page_to_load("30000")
        sel.type("id_name", "Event 1")
        sel.type("id_location", "Event location")
        sel.type("id_description", "event description")
        sel.click("//input[@value='submit']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
