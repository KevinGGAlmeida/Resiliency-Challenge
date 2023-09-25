from selenium import webdriver
from functions import *

class Resiliency:

    def __init__(self,site):
        self.site = site
        self.driver = webdriver.Chrome()

    def Launch(self):
        self.driver.get(self.site)

    def DownloadFile(self):
        self.file = SpreedSheet(self.driver)
    
    def FillingOutForm(self):
        for lines in self.file.index:
            print(lines)
            for Index in range(1,9):
                try:
                    Insert(self.driver,Index,self.file[GetName(self.driver,Index)][lines])
            
                except:
                    SelectState(self.driver,self.file['State'][lines])

            Disclosure(self.driver,self.file["Non-Disclosure On File"][lines])
            ActiveDiscount(self.driver,self.file["Offers Discounts"][lines])
            Add(self.driver)
        Submit(self.driver)
        sleep(3)
        self.driver.save_screenshot("Finished.png")

Run = Resiliency('https://developer.automationanywhere.com/challenges/resiliency-challenge.html?_gl=1*l9o0nu*_ga*MTk5MzUyNjk4Ny4xNjk1NjczOTQw*_ga_DG1BTLENXK*MTY5NTY3MzkzOS4xLjAuMTY5NTY3Mzk0Mi41Ny4wLjA.&_ga=2.14435703.1942585217.1695673943-1993526987.1695673940')
Run.Launch()
Run.DownloadFile()
Run.FillingOutForm()