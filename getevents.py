from calendar import month
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import sqlite3


def month_to_num(long_month):
    return {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }[long_month]

current_date = datetime.datetime.now()

conn = sqlite3.connect("apexgamingesports.db")
c = conn.cursor()

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="C:\Program Files\geckodriver.exe")

driver.get("https://locator.wizards.com/store/12723")

myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dayOfWeek.text-center")))

event_names = driver.find_elements(By.CSS_SELECTOR, "span.event-name")
event_times = driver.find_elements(By.CSS_SELECTOR, "div.event-time")
event_descriptions = driver.find_elements(By.CSS_SELECTOR, "div[itemprop='location performer'] > div:nth-child(2)")
event_months = driver.find_elements(By.CSS_SELECTOR, "div.month.text-center")
event_days = driver.find_elements(By.CSS_SELECTOR, "div.dayOfMonth.text-center")

c.execute(f"DELETE FROM events")

for event_name, event_time, event_description, event_month, event_day in zip(event_names, event_times, event_descriptions, event_months, event_days):
    year = current_date.year
    if month_to_num(event_month.text) < month_to_num(event_month.text):
        year += 1
    c.execute(f"INSERT INTO events VALUES ('{event_name.text}', '{year}-{month_to_num(event_month.text)}-{event_day.text}', '{event_description.text}', '{event_time.text}')")

driver.close()
conn.commit()
conn.close()