import requests
from  bs4 import BeautifulSoup
URL = 'https://www.flipkart.com/philips-air-led-desk-light-table-lamp/p/itm2d75394816799?pid=TLPEG647YKEUTZFW&lid=LSTTLPEG647YKEUTZFWRVREY8&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=c8343545-0a14-4648-83cc-533e7b28c191.TLPEG647YKEUTZFW.SEARCH&ppt=sp&ppn=sp&ssid=dj5ws99ugg0000001594040583233&qH=b5b340b3da6a2e83'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("div", {"class" :"_1vC4OE _3qQ9m1"})
p_name=soup.findAll("span", {"class" : "_35KyD6"})
print (p_name, results)
