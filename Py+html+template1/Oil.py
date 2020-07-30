import requests
from bs4 import BeautifulSoup

url = "https://www.shell.co.th/th_th/motorists/shell-fuels/fuel-price/app-fuel-prices.html" # url ของเว็บที่ต้องการดูข้อมูล
data = requests.get(url) #นำตัวแปรที่เก็บเว๊ปมาใส่ ทำการอ่านหน้าเว็ป
soup = BeautifulSoup(data.text,'html.parser') #ดึงข้อมูล www แต่ไม่มีการจัดหน้า

if( int(data.status_code) == 200):
    def gasE20():
        gasE20 = soup.find("td", {"data-h-title": "บาท/ลิตร"}).text
        return (gasE20)

    def gas91():
        gas91 = soup.find("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).text
        return (gas91)

    def FDiesel():
        FDiesel = soup.find("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).text
        return (FDiesel)

    def DieselB20():
        DieselB20 = soup.find("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).text
        return (DieselB20)

    def DieselB10():
        DieselB10 = soup.find("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).text
        return (DieselB10)

    def gas95():
        gas95 = soup.find("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).text
        return (gas95)

    def VDiesel():
        VDiesel = soup.find("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).find_next("td",{"data-h-title":"บาท/ลิตร"}).text
        return (VDiesel)