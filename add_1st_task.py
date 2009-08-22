from selenium import selenium
import unittest, time, re

class add_1st_task(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_add_1st_task(self):
        sel = self.selenium
        sel.open("/opportunities/")
        sel.click("link=Add Task")
        sel.wait_for_page_to_load("30000")
        sel.type("id_name", "task 1")
        sel.click("//input[@value='submit']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
