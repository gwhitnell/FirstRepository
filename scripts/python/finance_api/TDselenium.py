import time
import urllib
import requests
from splinter import Browser
from config import TDAmeritradeClientid, TDpassword, TDusername

# define the Chrome driver location
executable_path = {
    "executable_path": r"C:\Users\garet\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\chromedriver_win32\chromedriver"
}

# Create a new instance of the chrome broswer
browser = Browser("chrome", **executable_path, headless=False)

# define the components of the url
method = "GET"
url = "https://auth.tdameritrade.com/auth?"
client_code = TDAmeritradeClientid + "@AMER.OAUTHAP"
payload = {
    "response_type": "code",
    "redirect_uri": "http://localhost",
    "client_id": client_code,
}

# build the url

built_url = requests.Request(method, url, params=payload).prepare()
built_url = built_url.url

# go to our url
browser.visit(built_url)

# define elements to pass through
payload = {"username": TDusername, "password": TDpassword}

browser.find_by_id("username0").first.fill(payload["username"])
browser.find_by_id("password").first.fill(payload["password"])
browser.find_by_id("accept").first.click()
