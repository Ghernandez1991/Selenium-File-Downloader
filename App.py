# inmport dependencies
from splinter import Browser
from selenium import webdriver
import bs4 as BS
import time

# store executible path for chrome driver.
executable_path = {
    "executable_path": r"C:\Users\Gabriel Hernandez\Desktop\MAME_DOWNLOADER\chromedriver.exe"}
# create a browers object, we are not running headless because we want to see the files being downloaded.
browser = Browser("chrome", **executable_path, headless=False)

# create URL object
url = 'https://archive.org/download/mame_sl_0220/MAME%20SL%200.220%20%28Merged%29/'

# tell browser to visit the website
browser.visit(url)

# loop though all the links. We start at table row two, and go to table row 566.  THis was found using chrome developer tools, and looking for the xpath of each link inside the html table.
for row in range(2, 566):
    browser.find_by_xpath(
        f'//*[@id="maincontent"]/div/div/pre/table/tbody/tr{[row]}/td[1]/a[1]')[0].click()
    # LET THE USER KNOW THE FILE HAS BEEN CLICKED.
    print(f'link number{row} successfully clicked')
