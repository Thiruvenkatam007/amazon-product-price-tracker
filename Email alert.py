# ===============================================Importing desired functions==========================================================
import requests
from bs4 import BeautifulSoup
import smtplib
import csv
import datetime
import os
import time

url = "https://www.amazon.in/Samsung-Galaxy-Cloud-Lavender-Storage/dp/B08V9VMRQF?ref_=Oct_DLandingS_D_d2acc06b_62"

# ====================Here we are using smtp package to send email to the users======================================================
# ======================Please note google disabled smtp package function to enable it you need to change some settings=============
# https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
# ======================Please see this link================================================================================


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("email", "password")

    subject = "Hey! The prices are affordable"
    body = f"Go and order now at {url}"
    msg = f"Subject:{subject}\n\n\n\n{body}"

    server.sendmail("from_address",
                    "to_address", msg)
    print("email sent")
    server.quit()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36'}


def check_price_and_log():
    page = requests.get(url, headers=headers)

    bs = BeautifulSoup(page.content, 'html.parser')

    bs.prettify().encode("utf-8")

    product_title = bs.find(id="productTitle").get_text()
    print(product_title.strip())

    product_price = bs.find(
        "span", attrs={'class': 'a-price-whole'}).get_text().strip()

    product_price = product_price.replace(",", "")
    price_float = float(product_price[:len(product_price)-1])
    print(price_float)

    file_exists = True

    if not os.path.exists("./price.csv"):
        file_exists = False
    # ========================================Creating CSV file for the price logs=================================================
    with open("price.csv", "a") as file:
        writer = csv.writer(file, lineterminator="\n")
        fields = ["Timestamp", "price"]

        if not file_exists:
            writer.writerow(fields)

        timestamp = f"{datetime.datetime.date(datetime.datetime.now())},{datetime.datetime.time(datetime.datetime.now())}"
        writer.writerow([timestamp, price_float])
        print("wrote csv data")

    return price_float


while True:
    price = check_price_and_log()
    # ===========================================CHnage this below value to set the value you want to be notified================
    if (price <= 60000):
        send_email()
    time.sleep(43200)
