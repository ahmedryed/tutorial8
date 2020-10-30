import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MinWebTest(unittest.TestCase):
    # execute the test <x = 0, y = 0, z = 0, submitButton = click> and check the output message is correct
    def test0(self):
        driver = webdriver.Firefox(executable_path=r"/Users/ryedahmed1/Downloads/geckodriver.exe")
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"min.html")
        
        #Testing 0, 0, 1 -> Output: 0
        elem = driver.find_element_by_id("x")
        elem.send_keys(0) # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys(0) # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys(1) # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(0, 0, 1) = 0", output)

        driver.close()


    def test1(self):
        driver = webdriver.Firefox(executable_path=r"/Users/ryedahmed1/Downloads/geckodriver.exe")
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"min.html")

        #Testing -1, 1, 1 -> Output: 0 (from before)
        driver.find_element_by_id("x").clear()
        driver.find_element_by_id("y").clear()
        driver.find_element_by_id("z").clear()
        elem = driver.find_element_by_id("x")
        elem.send_keys(-1) # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys(1) # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys(1) # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        #elem.click() # don't click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(0, 0, 1) = 0", output)

        driver.close()


    def test2(self):
        driver = webdriver.Firefox(executable_path=r"/Users/ryedahmed1/Downloads/geckodriver.exe")
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"min.html")
        
        #Testing 1, 1, -1 -> Output: -1
        driver.find_element_by_id("x").clear()
        driver.find_element_by_id("y").clear()
        driver.find_element_by_id("z").clear()
        elem = driver.find_element_by_id("x")
        elem.send_keys(1) # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys(1) # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys(-1) # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(1, 1, -1) = -1", output)

        driver.close()


    def test3(self):
        driver = webdriver.Firefox(executable_path=r"/Users/ryedahmed1/Downloads/geckodriver.exe")
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"min.html")

        #Testing 1, 0, -1 -> Output: -1 (didn't click)
        driver.find_element_by_id("x").clear()
        driver.find_element_by_id("y").clear()
        driver.find_element_by_id("z").clear()
        elem = driver.find_element_by_id("x")
        elem.send_keys(1) # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys(0) # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys(-1) # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        #elem.click() #don't click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(1, 1, -1) = -1", output)

        driver.close()
    
    
    def test4(self):
        driver = webdriver.Firefox(executable_path=r"/Users/ryedahmed1/Downloads/geckodriver.exe")
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"min.html")
        #Testing 0, -1, -1 -> Output: -1
        driver.find_element_by_id("x").clear()
        driver.find_element_by_id("y").clear()
        driver.find_element_by_id("z").clear()
        elem = driver.find_element_by_id("x")
        elem.send_keys(0) # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys(-1) # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys(-1) # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(0, -1, -1) = -1", output)


        driver.close() # close the browser window



if __name__ == '__main__':test
    unittest.main()
