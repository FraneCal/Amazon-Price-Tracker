# https://myhttpheader.com/

from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.com/dp/B09W28YNHJ/ref=syn_sd_onsite_desktop_0?ie=UTF8&pd_rd_plhdr=t&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

amazon_page = response.text

soup = BeautifulSoup(amazon_page, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText().split('$')[1]

if float(price) < 59.99:
    my_email = 'franecalusic94@gmail.com'
    password = 'xpfewbczcbmffepf'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='franecalusic@yahoo.com',
                                msg='Subject: The price is below 60$. Go buy it now.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
