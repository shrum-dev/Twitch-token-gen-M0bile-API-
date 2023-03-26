import requests
import random
import time
import string
import threading
import asyncio
import json
import sys
import re, os
from colorama import Fore, init

init()

xdecrequ = 0

os.system("cls & title GEN MADE BY SHRUM#1111")

class colors:
 
 
        reset = '\033[0m'
        bold = '\033[01m'
        disable = '\033[02m'
        underline = '\033[04m'
        reverse = '\033[07m'
        strikethrough = '\033[09m'
        invisible = '\033[08m'
 
        class fg:
                black = '\033[30m'
                red = '\033[31m'
                green = '\033[32m'
                orange = '\033[33m'
                blue = '\033[34m'
                purple = '\033[35m'
                cyan = '\033[36m'
                lightgrey = '\033[37m'
                darkgrey = '\033[90m'
                lightred = '\033[91m'
                lightgreen = '\033[92m'
                yellow = '\033[93m'
                lightblue = '\033[94m'
                pink = '\033[95m'
                lightcyan = '\033[96m'

def run():
    while True:
      try:
           xdevid = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
           for i in range(10):
                generate(xdevid)
      except Exception as e:
          None

with open('config.json') as r:
    config = json.load(r)


def addbio(token, userid):
    try:
        r = open('bio.txt', 'r').read().splitlines()
        bio = random.choice(r)
        headers = {
                'Accept': 'application/vnd.twitchtv.v3+json',
                'Accept-Language': 'en-us',
                'api-consumer-type': 'mobile; Android/1404000',
                'authorization': f'OAuth {token}',
                'client-id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
                'client-session-id': '7f4b1045-f52b-49da-bcef-a81394610476',
                'connection': 'Keep-Alive',
                'content-type': 'application/json',
                'host': 'gql.twitch.tv',
                'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000',
                'x-apollo-operation-id': '14396482e090e2bfc15a168f4853df5ccfefaa5b51278545d2a1a81ec9795aae',
                'x-apollo-operation-name': 'UpdateUserDescriptionMutation',
                'x-app-version': '14.4.0',
                'x-device-id': 'e5c5e81ebfca405784e1da77aacca842'
        }

        data =   {
            "operationName": "UpdateUserDescriptionMutation",
            "variables": {
            "userID": userid,
            "newDescription": bio
            },
            "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "14396482e090e2bfc15a168f4853df5ccfefaa5b51278545d2a1a81ec9795aae"
            }
            }
        }

        requests.post('https://gql.twitch.tv/gql', headers=headers,  json=data)
        return userid
    except Exception as e:
         None

def newmail():
    nammeme = ''.join(random.choices(string.ascii_lowercase+string.digits,k=8))
    cookies = {
        '_ga': 'GA1.2.1504564596.1671993819',
        '__gads': 'ID=40884ef522879ad1-222b4f9d05d90017:T=1671945218:RT=1671945218:S=ALNI_MazDJQ5YWgRY_qHDWNaXT3iTZL1Lg',
        '_gid': 'GA1.2.1344899792.1673781678',
        '_gat': '1',
        '__gpi': 'UID=00000b96d4a98623:T=1671945218:RT=1673781677:S=ALNI_Mb-ieF9Qfb3QKIfRYRrLKIx9SZ00g',
    }

    headers = {
        'authority': 'api.internal.temp-mail.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'application-name': 'web',
        'application-version': '2.2.29',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.2.1504564596.1671993819; __gads=ID=40884ef522879ad1-222b4f9d05d90017:T=1671945218:RT=1671945218:S=ALNI_MazDJQ5YWgRY_qHDWNaXT3iTZL1Lg; _gid=GA1.2.1344899792.1673781678; _gat=1; __gpi=UID=00000b96d4a98623:T=1671945218:RT=1673781677:S=ALNI_Mb-ieF9Qfb3QKIfRYRrLKIx9SZ00g',
        'origin': 'https://temp-mail.io',
        'referer': 'https://temp-mail.io/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    json_data = {
        'domain': 'bloheyz.com',
        'name': nammeme,
    }

    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', cookies=cookies, headers=headers, json=json_data).json()
    email = response["email"]
    return email

def check(email1, token, code):
    global pending
    try:
    
        cookies = {
            '_ga': 'GA1.2.1504564596.1671993819',
            '__gads': 'ID=40884ef522879ad1-222b4f9d05d90017:T=1671945218:RT=1671945218:S=ALNI_MazDJQ5YWgRY_qHDWNaXT3iTZL1Lg',
            '_gid': 'GA1.2.1344899792.1673781678',
            '_gat': '1',
            '__gpi': 'UID=00000b96d4a98623:T=1671945218:RT=1673781677:S=ALNI_Mb-ieF9Qfb3QKIfRYRrLKIx9SZ00g',
        }

        headers = {
            'authority': 'api.internal.temp-mail.io',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'application-name': 'web',
            'application-version': '2.2.29',
            # 'cookie': '_ga=GA1.2.1504564596.1671993819; __gads=ID=40884ef522879ad1-222b4f9d05d90017:T=1671945218:RT=1671945218:S=ALNI_MazDJQ5YWgRY_qHDWNaXT3iTZL1Lg; _gid=GA1.2.1344899792.1673781678; _gat=1; __gpi=UID=00000b96d4a98623:T=1671945218:RT=1673781677:S=ALNI_Mb-ieF9Qfb3QKIfRYRrLKIx9SZ00g',
            'origin': 'https://temp-mail.io',
            'referer': 'https://temp-mail.io/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        response = requests.get(
            f'https://api.internal.temp-mail.io/api/v3/email/{email1}/messages',
            cookies=cookies,
            headers=headers,
        )
        code = response.text.split("subject")[1].split("Your Twitch Verification Code")[0].strip('":" –')[0:6]

        return code
    except Exception as e:
        None
def emailvalid(email, token, code):
    try:
        time.sleep(5)
        recode = check(email, token, code)
        headers = {
            'Accept': 'application/vnd.twitchtv.v3+json',
            'Accept-Language': 'en-us',
            'api-consumer-type': 'mobile; Android/1404000',
            'authorization': f'OAuth {token}',
            'client-id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
            'client-session-id': '7f4b1045-f52b-49da-bcef-a81394610476',
            'connection': 'Keep-Alive',
            'content-type': 'application/json',
            'host': 'gql.twitch.tv',

            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000',
            'x-apollo-operation-id': '72babafce68ab9862b6e4067385397b5d70caf4c2b45566970f57e5184411649',
            'x-apollo-operation-name': 'ValidateVerificationCode',
            'x-app-version': '14.4.0',
            'x-device-id': '1f7f9ff52df04002adfb0ee89dc97f11'
        }

        data =  {
            "operationName": "ValidateVerificationCode",
            "variables": {
            "input": {
                "address": email,
                "code": recode,
                "key": code
            }
            },
            "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "72babafce68ab9862b6e4067385397b5d70caf4c2b45566970f57e5184411649"
            }
            }
        }
        r = requests.post("https://gql.twitch.tv/gql", json=data, headers=headers)
        solv = colors.fg.darkgrey + email + colors.fg.lightgrey
        print(f"{Fore.BLUE}[-] Email added{Fore.RESET}", solv)
        addbio(token, code)
        return solv
    except Exception as e:
        None

def generate(xdevid):
      global xdecrequ
    
      try:
            hf = open("users.txt", "r").read().splitlines()
            hif = random.choice(hf)
            username = hif + ''.join(random.choices(string.ascii_lowercase+string.digits,k=5))
            p1 = open('proxy.txt', 'r').read().splitlines()
            li1o = random.choice(p1)
            proxies = {"http": "http://" + li1o, "https": "http://" + li1o}
            password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
            eemail = newmail()

            headers = {
                "Content-Type": "text/json"
            }

            data = {
                    "clientKey": config["captcha_key"],
                    "task": {
                    "type": "AntiKasadaTask",
                    "pageURL": "https://gql.twitch.tv",
                    "proxy": li1o,
                    "cd": True,
                    "onlyCD": False,
                    "userAgent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000"
                    }
            }

            response = requests.post('https://api.capsolver.com/kasada/invoke', json=data, headers=headers, proxies=proxies)
            current_useragent = response.json()["solution"]["user-agent"]
            current_kpsdkcd = response.json()["solution"]["x-kpsdk-cd"]
            current_kpsdkct = response.json()["solution"]["x-kpsdk-ct"]

            headers = {
                "accept": "application/vnd.twitchtv.v3+json",
                "accept-encoding": "gzip",
                "accept-language": "en-us",
                "api-consumer-type": "mobile; Android/1407000",
                "client-id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "connection": "Keep-Alive",
                "content-length": "0",
                "host": "passport.twitch.tv",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000",
                "x-app-version": "14.4.0",
                "x-device-id": xdevid,
                "x-kpsdk-cd": current_kpsdkcd,
                "x-kpsdk-ct": current_kpsdkct,
            }
            r = requests.post('https://passport.twitch.tv/integrity',headers=headers, proxies=proxies)
            pg = r.json()["token"]
            solv = colors.fg.darkgrey + pg + colors.fg.lightgrey
            print(f'{Fore.CYAN}[+] Integrity{Fore.RESET}', solv)

            headers = {
                "accept": "application/vnd.twitchtv.v3+json",
                "accept-language": "en-us",
                "api-consumer-type": "mobile; Android/1407000",
                "client-id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "connection": "Keep-Alive",
                "content-length": "738",
                "content-type": "application/json; charset=UTF-8",
                "host": "passport.twitch.tv",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000",
                "x-app-version": "14.4.0",
                "x-device-id": xdevid
            }

            dathh = {
              "birthday": {"day": 20,"month": 12,"year": 2001},
              "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
              "email": eemail,
              "include_verification_code": True,
              "integrity_token": pg,
              "password": password,
              "username": username
            }

            re = requests.post('https://passport.twitch.tv/protected_register',headers=headers, json=dathh, proxies=proxies)
            token = re.json()["access_token"]
            usercode = re.json()["userID"]
            f1 = open("tokens.txt", "a")
            f1.write(f"{token}\n")
            solv1 = colors.fg.darkgrey + token + colors.fg.lightgrey
            print(f'{Fore.GREEN}[!] GENED{Fore.RESET}', solv1)

            xdecrequ += 1
            emailvalid(eemail, token, usercode)
      except Exception as e:
            None

thread = config["threads"]
for i in range(int(thread)):
    threading.Thread(target=run).start()

  