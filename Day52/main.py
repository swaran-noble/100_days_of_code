import os
from bs4 import BeautifulSoup
import requests
import smtplib

# Practice
PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
# Live Site
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header={
    "Accept-Language":"en-GB,en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}
response = requests.get(PRACTICE_URL,headers=header)

soup = BeautifulSoup(response.content,"html.parser")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
#print(price)

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
#print(price_as_float)

# ========== Send an Email =========

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        result = connection.login(os.environ["MY_EMAIL"],os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRACTICE_URL}".encode("utf-8")
        )



