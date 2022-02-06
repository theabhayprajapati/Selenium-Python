import os
from selenium import webdriver

os.environ['PATH'] += r'C:\seleniumdriver\chromedriver_win32'
driver = webdriver.Chrome()

