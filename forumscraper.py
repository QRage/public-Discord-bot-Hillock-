import requests
from bs4 import BeautifulSoup
from shutil import copyfile
import asyncio

def scraper():
    url = "https://www.pathofexile.com/forum/view-thread/2551118/page/1"

    headers = {
        "Authorization" : "SAPISIDHASH 1623130218_185509d60d328a8b7be39f8419e3d33422df715c",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
        
    }

    req1 = requests.get(url, headers=headers)
    src1 = req1.text

    soup = BeautifulSoup(src1, "lxml")

    csstest = soup.select_one('.topBar a:nth-of-type(6)').get('href')

    global url2
    url2 = 'http://www.pathofexile.com'+csstest
    req2 = requests.get(url2, headers=headers)
    src2 = req2.text

    soup = BeautifulSoup(src2, "lxml")

    for x in range(10, 0, -1):
        if not soup.select_one("tr:nth-of-type({}) div.content".format(x)) == None:
            with open("msg.txt", "w") as newmsg:
                newmsg.write(soup.select_one("tr:nth-of-type({}) div.content".format(x)).text)
            with open("msg.txt", "r") as newmsg:
                with open("oldmsg.txt", "r") as oldmsg:
                    if newmsg.read() == oldmsg.read():
                        print("identy")
                        return False
                    print("not identy")
                    copyfile("msg.txt", "oldmsg.txt")
                    return True
        if x == 1:
            print("Cannot scan")
            return False



# if scraper() == False:
#     print("False check")
# if scraper() == True:
#     print("True check")