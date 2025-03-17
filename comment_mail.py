import requests
import re
from bs4 import BeautifulSoup, Comment

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

patron_mail = "[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com"

comments = [com for com in soup.find_all(string=lambda text: isinstance(text, Comment))]
mail = re.findall(patron_mail, soup.get_text())
print(comments)
print(mail)
