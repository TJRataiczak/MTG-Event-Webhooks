from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sqlite3


conn = sqlite3.connect("discordbot.db")
c = conn.cursor()

driver = webdriver.Firefox()
driver.get("https://locator.wizards.com/store/12723")

myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dayOfWeek.text-center")))

eventnames = driver.find_elements_by_class_name("event-name")
companioncodes = driver.find_elements_by_class_name("row.no-gutters.pt-1.event-info")
daysofweek = driver.find_elements_by_class_name("dayOfWeek.text-center")
months = driver.find_elements_by_class_name("month.text-center")
daysofmonth = driver.find_elements_by_class_name("dayOfMonth.text-center")

for i in range(len(eventnames)):
    print(eventnames[i].text.lower())
    finaleventdate = f"{daysofweek[i].text}, {months[i].text} {daysofmonth[i].text}"
    print(finaleventdate)
    if "modern" in eventnames[i].text.lower():
        c.execute(f"INSERT INTO events VALUES ('863187370119659560', '{eventnames[i].text}', '{finaleventdate}', 'Modern')")
    elif "standard" in eventnames[i].text.lower():
        c.execute(f"INSERT INTO events VALUES ('863187370119659560', '{eventnames[i].text}', '{finaleventdate}', 'Standard')")
    elif "pioneer" in eventnames[i].text.lower():
        c.execute(f"INSERT INTO events VALUES ('863187370119659560', '{eventnames[i].text}', '{finaleventdate}', 'Pioneer')")
    elif "legacy" in eventnames[i].text.lower():
        c.execute(f"INSERT INTO events VALUES ('863187370119659560', '{eventnames[i].text}', '{finaleventdate}', 'Legacy')")
    else:
        c.execute(f"INSERT INTO events VALUES ('863187370119659560', '{eventnames[i].text}', '{finaleventdate}') SELECT serverID, eventname, eventdate")

conn.commit()
conn.close()
driver.close()