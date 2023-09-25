from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from pathlib import Path

from time import sleep
import os
from pathlib import Path
import pandas as pd


def ValidateDownload():
    for Try in range(0,50):
        for files in os.listdir(Path.home() / "Downloads"):
            if files.startswith("resiliency") and files.endswith(".csv"):
                file = pd.read_csv(Path.home() / f"Downloads/{files}",dtype="str")
                os.remove(Path.home() / f"Downloads/{files}")
                return file

            else:
                sleep(1)
                print("Waiting for the file")


        return "File not found"


def SpreedSheet(driver):
    try:
        driver.execute_script('document.querySelector(`[download="resiliency-challenge.csv"]`).click()')
        return ValidateDownload()
        

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
    

def GetName(driver,Index):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/form/div[2]/div/div/div[{Index}]')))
        return driver.find_element(By.XPATH,f'/html/body/div[2]/div/form/div[2]/div/div/div[{Index}]').text

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")


def Insert(driver,Index,Value):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/form/div[2]/div/div/div[{Index}]//input')))
        driver.find_element(By.XPATH,f'/html/body/div[2]/div/form/div[2]/div/div/div[{Index}]//input').send_keys(str(Value))

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")


def SelectState(driver,value):
    try:
        driver.execute_script(f'document.querySelector(`[value="{value}"]`).selected = true')

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")

def ActiveDiscount(driver,Value):
    try:
        if str(Value) == "YES":
            driver.execute_script('document.querySelector(`[value="1"]`).click()')
        else:
            driver.execute_script('document.querySelector(`[value="0"]`).click()')

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")

def Disclosure(driver,Value):
    try:

        if str(Value) == "YES":
            driver.find_element(By.ID,"nonDisclosure").click()

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
    

def Add(driver):
    driver.find_element(By.ID,"add_button").click()


def Submit(driver):
    driver.find_element(By.ID,"submit_button").click()

    