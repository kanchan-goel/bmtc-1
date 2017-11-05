from bs4 import BeautifulSoup
import requests
import json
import sqlite3

conn = sqlite3.connect("bmtc.db")
c = conn.cursor()


bus=input()
route=input()

url1="https://www.mybmtc.com/route/busstops/"+bus+"/print/"+route
req1=requests.get(url1)
data1 =req1.text
soup=BeautifulSoup(data1,"html.parser")
stop=([i.text for i in soup.find_all('span',{'id':'busstop_name'})])

url2="https://www.mybmtc.com/route/schedule/"+bus
req2=requests.get(url2)
data2 =req2.text
soup=BeautifulSoup(data2,"html.parser")
time=[litag.text for ultag in soup.find_all('ul', {'class': 'routestime'}) for litag in ultag.find_all('li')]    

data={"bus_id":bus,
      "route_id":route,
      "timings":time,
      "bus_stop":stop
     }

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


c.execute('CREATE TABLE IF NOT EXISTS routes(bus_id TEXT, route_id TEXT, timings TEXT, bus_stop TEXT)')


c.executemany("INSERT INTO routes (bus_id, route_id, timings, bus_Stop) values (? , ? , ? , ?)",
        (bus, route, time, stop) 
    )
conn.commit()
c.execute("SELECT * FROM routes")

data = c.fetchall()
   
for row in data:
    print(row)
c.close()
conn.close()


