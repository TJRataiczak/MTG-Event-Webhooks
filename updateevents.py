from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sqlite3


conn = sqlite3.connect("discordbot.db")
c = conn.cursor()

c.execute("SELECT serverID, storeID FROM servers")

results = c.fetchall()

for result in results:
    c.execute(f"DELETE FROM events WHERE serverID = '{result[0]}'")
    print(results)
    driver = webdriver.Firefox()
    driver.get(f"https://locator.wizards.com/store/{result[1]}")

    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dayOfWeek.text-center")))

    eventnames = driver.find_elements_by_class_name("event-name")
    months = driver.find_elements_by_class_name("month.text-center")
    daysofmonth = driver.find_elements_by_class_name("dayOfMonth.text-center")

    for i in range(len(eventnames)):
        print(eventnames[i].text)
        finaleventdate = f"{months[i].text} {daysofmonth[i].text}"
        print(finaleventdate)
        if "modern" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Modern')")
        elif "standard" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Standard')")
        elif "pioneer" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Pioneer')")
        elif "legacy" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Legacy')")
        elif "sealed" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Sealed')")
        elif "draft" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Draft')")
        elif "prerelease" in eventnames[i].text.lower():
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}', 'Prerelease')")
        else:
            c.execute(f"INSERT INTO events VALUES ('{result[0]}', '{eventnames[i].text}', '{finaleventdate}') SELECT serverID, eventname, eventdate")
    driver.close()

conn.commit()
conn.close()