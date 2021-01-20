import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
url="https://www.timeanddate.com/weather/united-arab-emirates/dubai"
r=requests.get(url)
n = ToastNotifier() 
soup=BeautifulSoup(r.text,'html5lib')
# print(soup.prettify())
web=soup.find('div',class_="bk-focus__qlook")
for i in web.find("div",class_="h2"):
    n.show_toast("Notification Weather", i, duration = 10, icon_path =r"weather.ico") 
