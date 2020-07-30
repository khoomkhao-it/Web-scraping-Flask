import Digital #Beautifulsoup
import Covid
import Oil
import json, time
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/')
def Main():
   return render_template('Main.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      select =  request.form.getlist('button')#ดึงการเลือกของหน้า Main มาว่าเลือกอะไร
      #print(result)
      
      if select == ['Investing']:
         return render_template ("Investing.html")

      elif select == ['Covid']:
         Disease = {'ผู้ป่วยสะสม': Covid.stack(),
         'ผู้ป่วยรายใหม่': Covid.new(),
         'ผู้ป่วยรุนแรง': Covid.heavy(),
         'เสียชีวิต': Covid.dead()}
         #java = {Covid.stack(),Covid.new(),Covid.heavy(),Covid.dead()}
         dataDisease = json.dumps(Disease, ensure_ascii=False)
         print(Disease)
         return render_template("Covid.html",result = Disease,dataDisease = dataDisease)

      elif select == ['Oil']:
         shell ={'ฟิวเซฟ แก๊สโซฮอล์91': Oil.gas91(),
         'ฟิวเซฟ ดีเซล': Oil.FDiesel(),
         'อี20 แก๊สโซฮอล์': Oil.gasE20(),
         'ดีเซลB20': Oil.DieselB20(),
         'ฟิวเซฟ ดีเซลB10': Oil.DieselB10(),
         'วี-เพาเวอร์ แก๊สโซฮอล์95': Oil.gas95(),
         'วี-เพาเวอร์ ดีเซล': Oil.VDiesel(),}
         dataOil = json.dumps(shell, ensure_ascii=False)
         
         return render_template("Oil.html",result = shell,dataOil = dataOil)

      elif select == ['Credit']:
         return render_template("Credit.html",result = "")

      else :return render_template("Main.html")
#สำหรับการส่งค่าไปแสดงเป็น real time

def get_digital():
    '''this could be any function that blocks until data is ready'''
    Digital.soupD = Digital.setgetD()

    digital = '<table>'
    digital += '<tr>' + '<th>' + 'ชื่อ' + '</th>'
    digital += '<th>' + 'ชื่อย่อ' + '</th>' 
    digital += '<th>' + 'ราคา(USD)' + '</th>' + '</tr>'
    #digital += '<th>' + 'ราคา(THB)' + '</th>' 

    #Bitcoin
    digital += '<tr>' + '<td width="200px">' + 'Bitcoin ' + '</td>' 
    digital += '<td>' + 'BTC' + '</td>'
    digital += '<td style="text-align:right">' + Digital.BTC() + '</td>'

    #Ether
    digital += '<tr>' + '<td>' + 'Ethereum ' + '</td>'
    digital += '<td>' + 'ETH' + '</td>'
    digital += '<td style="text-align:right">' + Digital.ETH() + '</td>' + '</tr>'

    #Tether
    digital += '<tr>' + '<td>' + 'Tether ' + '</td>'
    digital += '<td>' + 'USDT' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.USDT() + '</td>' + '</tr>'

    #Ripple
    digital += '<tr>' + '<td>' + 'Ripple ' + '</td>'
    digital += '<td>' + 'XRP' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.XRP() + '</td>' + '</tr>'

    #Bitcoin cash
    digital += '<tr>' + '<td>' + 'Bitcoin Cash ' + '</td>'
    digital += '<td>' + 'BCH' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.BCH() + '</td>' + '</tr>'

    #Bitcoin sv
    digital += '<tr>' + '<td>' + 'Bitcoin SV ' + '</td>'
    digital += '<td>' + 'BSV' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.BSV() + '</td>' + '</tr>'

    #Litecoin
    digital += '<tr>' + '<td>' + 'Litecoin ' + '</td>'
    digital += '<td>' + 'LTC' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.LTC() + '</td>' + '</tr>'

    #Binance Coin
    digital += '<tr>' + '<td>' + 'Binance Coin ' + '</td>'
    digital += '<td>' + 'BNB' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.BNB() + '</td>' + '</tr>'

    #EOS
    digital += '<tr>' + '<td>' + 'EOS ' + '</td>'
    digital += '<td>' + 'EOS' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.EOS() + '</td>' + '</tr>'

    #Tezos
    digital += '<tr>' + '<td>' + 'Tezos ' + '</td>'
    digital += '<td>' + 'XTZ' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.XTZ() + '</td>' + '</tr>'

    #Cardano
    digital += '<tr>' + '<td>' + 'Cardano ' + '</td>'
    digital += '<td>' + 'ADA' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.ADA() + '</td>' + '</tr>'

    #Chainlink
    digital += '<tr>' + '<td>' + 'Chainlink ' + '</td>'
    digital += '<td>' + 'LINK' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.LINK() + '</td>' + '</tr>'

    #Stellar
    digital += '<tr>' + '<td>' + 'Stellar ' + '</td>'
    digital += '<td>' + 'XLM' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.XLM() + '</td>' + '</tr>'

    #Crypto.com Coin
    digital += '<tr>' + '<td>' + 'Crypto.com Coin ' + '</td>'
    digital += '<td>' + 'CRO' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.CRO() + '</td>' + '</tr>'

    #UNUS SED LEO
    digital += '<tr>' + '<td>' + 'UNUS SED LEO ' + '</td>'
    digital += '<td>' + 'LEO' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.LEO() + '</td>' + '</tr>'

    #Monero
    digital += '<tr>' + '<td>' + 'Monero ' + '</td>'
    digital += '<td>' + 'XMR' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.XMR() + '</td>' + '</tr>'

    #TRON
    digital += '<tr>' + '<td>' + 'TRON ' + '</td>'
    digital += '<td>' + 'TRX' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.TRX() + '</td>' + '</tr>'

    #Huobi Token
    digital += '<tr>' + '<td>' + 'Huobi Token ' + '</td>'
    digital += '<td>' + 'HT' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.HT() + '</td>' + '</tr>'

    #Ethereum Classic
    digital += '<tr>' + '<td>' + 'Ethereum Classic ' + '</td>'
    digital += '<td>' + 'ETC' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.ETC() + '</td>' + '</tr>'

    #USD Coin
    digital += '<tr>' + '<td>' + 'USD Coin ' + '</td>'
    digital += '<td>' + 'USDC' + '</td>' 
    digital += '<td style="text-align:right">' + Digital.USDC() + '</td>' + '</tr>'


    digital += '</table>'
    print('แสดงผลแล้วจ้า real-time แล้วจ้า')
    return digital

@app.route('/streamdigital')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_digital())
    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == '__main__':
   app.run(debug = True)