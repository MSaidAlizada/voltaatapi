from bs4 import BeautifulSoup
from flask import Flask
import requests
app = Flask(__name__) 

# url of the website
doc = "https://www.voltaat.com/products/"

# getting response object
#res = requests.get(doc)

#soup = BeautifulSoup(res.content, "html.parser")
#print()

@app.route("/voltaat/<name>")
def productBarcode(name):
    url = doc + name
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return (soup.find("span", itemprop="Barcode").text[-4:])
