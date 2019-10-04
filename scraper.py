#@author  Hussam Soufi: hussam1soufi@gmail.com

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.de/Optimum-Nutrition-Eiwei%C3%9Fpulver-Aminos%C3%A4uren-Chocolate/dp/B000GIQT2O/ref=sr_1_5?crid=294VJ56AA1GNW&keywords=protein+whey+5+kg&qid=1567338427&s=gateway&sprefix=protein+whey+5%2Caps%2C168&sr=8-5"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

def CheckPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:2])

    if(converted_price < 80):
        SendMail()

def SendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YourEmail@gmail.com', 'YourPassword')

    subject = 'price fell down!'
    body = 'Check this amazon URL https://www.amazon.de/Optimum-Nutrition-Eiwei%C3%9Fpulver-Aminos%C3%A4uren-Chocolate/dp/B000GIQT2O/ref=sr_1_5?crid=294VJ56AA1GNW&keywords=protein+whey+5+kg&qid=1567338427&s=gateway&sprefix=protein+whey+5%2Caps%2C168&sr=8-5'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'samtestsoufi@gmail.com',
        'hussam1soufi@gmail.com',
        msg
    )
    print('Hey Email has been sent!')

    server.quit()

while(True):
    CheckPrice()
    time.sleep(60 * 60)
