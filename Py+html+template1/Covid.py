import requests
from bs4 import BeautifulSoup

url = "https://ddc.moph.go.th/viralpneumonia/index.php" # url ของเว็บที่ต้องการดูข้อมูล
data = requests.get(url)
soup = BeautifulSoup(data.text,'html.parser') #ดึงข้อมูล www แต่ไม่มีการจัดหน้า
if( int(data.status_code) == 200):
    def stack():   
        stack = soup.find("h4",{"class":"txt"}).text
        return(stack)

    def new():   
        new = soup.find("h4",{"class":"txt"}).find_next("h4",{"class":"txt"}).text
        return(new)

    def heavy():   
        heavy = soup.find("h4",{"class":"txt"}).find_next("h4",{"class":"txt"}).find_next("h4",{"class":"txt"}).text
        return(heavy)

    def dead():   
        dead = soup.find("h4",{"class":"txt"}).find_next("h4",{"class":"txt"}).find_next("h4",{"class":"txt"}).find_next("h4",{"class":"txt"}).text
        return(dead)
