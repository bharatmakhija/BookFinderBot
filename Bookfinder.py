#MY FIRST PYTHON SCRIPT
#importing Libraries
import requests
import os
from DrillDownBook import reviewBook
from LoadNextPage import getUrl
import StringConstants
os.system('cls')
from bs4 import BeautifulSoup
book_name = []
book_url = []
print(StringConstants.welcomeMsg);
Book_title = input(StringConstants.enterBookTitleMsg)

counter = 1
flag = 1
pageno = 0
while(flag):
    pageno += 1
    url = getUrl(pageno,Book_title)
    try:
        r = requests.get(url, timeout = 6)
    except requests.exceptions.Timeout:
        print(StringConstants.timeoutError)
    except requests.exceptions.TooManyRedirects:
        print(StringConstants.badUrlError)
    except requests.exceptions.RequestException as e:
        print(StringConstants.unexpectedError)
        print(e)
        break

    soup = BeautifulSoup(r.content,"lxml")
    for tr in soup.find_all('tr'):       #FYI, [2:] slice here is to skip two header rows.
        y = tr.find_all("span", {"itemprop": "name"})
        try:
           print( "%(first)d " %{"first":counter} +". " + y[0].text + "  by: " + y[1].text + " " + y[2].text)
           counter = counter + 1
           book_name.append(y[0].text)
        except:
           try:
                print("%(first)d " %{"first":counter} + ". " +y[0].text + " by: " + y[1].text)
                counter = counter + 1
                book_name.append(y[0].text)
           except:
               pass
        a = tr.find_all('a', href=True)
        book_url.append(a[1]['href'])
    flag = int(input(StringConstants.loadingMsg))

num = int(1)
while(num):
    x = int(input(StringConstants.enterSerialNoMsg))
    bookurl =StringConstants.goodReadsString + book_url[x-1]
    Ddb = reviewBook(book_name[x-1],bookurl)
    num = int(input(StringConstants.continueString))
end = input(StringConstants.exitString)
