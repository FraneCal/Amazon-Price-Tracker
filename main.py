from bs4 import BeautifulSoup
import requests
import smtplib

# Example product
url = "https://www.amazon.com/dp/B09W28YNHJ/ref=syn_sd_onsite_desktop_0?ie=UTF8&pd_rd_plhdr=t&th=1"

header = {
    # You can find the the header info on this site: https://myhttpheader.com/
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

amazon_page = response.text

soup = BeautifulSoup(amazon_page, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText().split('$')[1]

# Example price
if float(price) < 59.99:
    my_email = 'YOUR GMAIL GOES HERE'
    password = 'YOUR SMTP GMAIL PASSWORD GOES HERE'
    # You can find the password following this site: https://hotter.io/docs/email-accounts/app-password-gmail/

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='OTHER PERSONS EMAIL',
                                msg='Subject: The price is below 60$. Go buy it now.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
