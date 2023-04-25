import requests
from bs4 import BeautifulSoup
URL = "https://www.cet.ac.in/head-of-departments/"

req = requests.get(URL)
source_code = req.content

soup = BeautifulSoup(source_code,'lxml')
table = soup.find('table')
rows = table.find_all('tr')
rows = rows[1:]
for i in rows:
    columns = i.find_all('td')
    hodname = columns[0]
    department = columns[1]
    phone = columns[2]
    print(hodname.text,department.text,phone.text)