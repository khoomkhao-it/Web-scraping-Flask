import requests
import time
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
urlD = 'https://th.investing.com/crypto/currencies'
response = requests.get(urlD, headers=headers).text
soupD = BeautifulSoup(response, 'html.parser')

def setgetD():
    response = requests.get(urlD, headers=headers).text
    soupD = BeautifulSoup(response, 'html.parser')
    return(soupD)
#------------------------------------Digital-----------------------------------------------------------------
def BTC():    
    BTC = soupD.find("a", {"href": "/crypto/currency-pairs?c1=189&c2=12"}).text
    return(BTC)

def ETH():
    ETH = soupD.find("a", {"href": "/crypto/currency-pairs?c1=195&c2=12"}).text
    return(ETH)

def USDT():
    USDT = soupD.find("a", {"href": "/crypto/currency-pairs?c1=205&c2=12"}).text
    return(USDT)

def XRP():
    XRP = soupD.find("a", {"href": "/crypto/currency-pairs?c1=197&c2=12"}).text
    return(XRP)

def BCH():
    BCH = soupD.find("a", {"href": "/crypto/currency-pairs?c1=215&c2=12"}).text
    return(BCH)

def BSV():
    BSV = soupD.find("a", {"href": "/crypto/currency-pairs?c1=1867&c2=12"}).text
    return(BSV)

def LTC():
    LTC = soupD.find("a", {"href": "/crypto/currency-pairs?c1=191&c2=12"}).text
    return(LTC)

def BNB():
    BNB = soupD.find("a", {"href": "/crypto/currency-pairs?c1=233&c2=12"}).text
    return(BNB)

def EOS():
    EOS = soupD.find("a", {"href":"/crypto/currency-pairs?c1=204&c2=12"}).text
    return(EOS)

def XTZ():
    XTZ = soupD.find("a", {"href": "/crypto/currency-pairs?c1=1289&c2=12"}).text
    return(XTZ)

def ADA():
    ADA = soupD.find("a", {"href": "/crypto/currency-pairs?c1=302&c2=12"}).text
    return(ADA)

def LINK():
    LINK = soupD.find("a", {"href": "/crypto/currency-pairs?c1=332&c2=12"}).text
    return(LINK)

def XLM():
    XLM = soupD.find("a", {"href": "/crypto/currency-pairs?c1=229&c2=12"}).text
    return(XLM)

def CRO():
    CRO = soupD.find("a", {"href": "/crypto/currency-pairs?c1=1889&c2=12"}).text
    return(CRO)

def LEO():
    LEO = soupD.find("a", {"href": "/crypto/currency-pairs?c1=1929&c2=12"}).text
    return(LEO)

def XMR():
    XMR = soupD.find("a", {"href": "/crypto/currency-pairs?c1=202&c2=12"}).text
    return(XMR)

def TRX():
    TRX = soupD.find("a", {"href": "/crypto/currency-pairs?c1=295&c2=12"}).text
    return(TRX)

def HT():
    HT = soupD.find("a", {"href": "/crypto/currency-pairs?c1=1633&c2=12"}).text
    return(HT)

def ETC():
    ETC = soupD.find("a", {"href": "/crypto/currency-pairs?c1=200&c2=12"}).text
    return(ETC)

def USDC():
    USDC = soupD.find("a", {"href":"/crypto/currency-pairs?c1=1869&c2=12"}).text
    return(USDC)
