from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

def month_to_num(long_month):
    return {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }[long_month]

current_date = datetime.datetime.now()

conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
c = conn.cursor()

c.execute("SELECT storeid, wizardsid FROM stores")

stores = c.fetchall()

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

for store in stores:

    c.execute(f"DELETE FROM events WHERE storeid='{store[0]}'")

    driver.get(store[1])

    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dayOfWeek.text-center")))

    event_names = driver.find_elements(By.CSS_SELECTOR, "span.event-name")
    months = driver.find_elements(By.CSS_SELECTOR, "div.month.text-center")
    days_of_the_month = driver.find_elements(By.CSS_SELECTOR, "div.dayOfMonth.text-center")
    descriptions = driver.find_elements(By.CSS_SELECTOR, "div[itemprop='location performer'] > div:nth-child(1)")


    for i in range(len(event_names)):
        year = current_date.year
        if month_to_num(months[i].text) < month_to_num(months[0].text):
            year += 1
        c.execute(f"INSERT INTO events VALUES ('{store[0]}', '{event_names[i].text}', '{year}-{month_to_num(months[i].text)}-{days_of_the_month[i].text}', '{descriptions[i].text}')")
    driver.close()
    print(f"Stored all events for: {store[0]}")

conn.commit()
conn.close()