from bs4 import BeautifulSoup
import requests
import os
import json
import sqlite3

conn = sqlite3.connect("bmtc.db")
c = conn.cursor()


print("enter the type of bus")
bustype=input()
if (bustype=='A/C-Service'):
    url1="https://www.mybmtc.com/ac-service?fareid=acs&qt-home_quick_tab_bottom=2"
elif (bustype=='General Service'):
    url1="https://www.mybmtc.com/general-service?fareid=gns&qt-home_quick_tab_bottom=2"
else:
    print("Please Type valid bus service")
    os._exit(1)

data = []
req1=requests.get(url1)
data1 =req1.text
soup=BeautifulSoup(data1,"html.parser")
rows = soup.find_all('tr')
for row in rows:
   
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print(data)

#data1={["Fare Stage Number", "Adults", "Children", "Senior Citizens"],data}

with open('data1.json', 'w') as outfile:
    json.dump(data, outfile)

c.execute('CREATE TABLE IF NOT EXISTS fares(Fare Stage Number TEXT, Adults TEXT, Children TEXT, Senior Citizens TEXT)')


c.executemany("INSERT INTO fares (bus_id, route_id, timings, bus_Stop) values (? , ? , ? , ?)",
        (bus, route, time, stop) 
    )
conn.commit()
c.execute("SELECT * FROM fares")

data = c.fetchall()
   
for row in data:
    print(row)
c.close()
conn.close()

