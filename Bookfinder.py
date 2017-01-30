#MY FIRST PYTHON SCRIPT
#importing Libraries
import requests
import os
from DrillDownBook import reviewBook
from LoadNextPage import getUrl

os.system('cls')
from bs4 import BeautifulSoup
book_name = []
book_url = []
print("hi, this is my first python script, this is all about you giving booktitle name and extracting every information related to it on your screen")
Book_title = input('Enter Book title: ')

#print(soup.prettify())
counter = 1
flag = 1
pageno = 0
while(flag):
    #url = 'https://www.goodreads.com/search?q='+Book_title
    pageno += 1
    url = getUrl(pageno,Book_title)
    try:
        r = requests.get(url, timeout = 6)
    except requests.exceptions.Timeout:
        print("TimeOut error")
    except requests.exceptions.TooManyRedirects:
        print("Url is bad: TooManyRedirects")
    except requests.exceptions.RequestException as e:
        print("Some Unexpected error has occured::")
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
    flag = int(input('keep loading 1/0 :'))

num = int(1)
while(num):
    x = int(input('enter books serial number which you want to review: '))
    bookurl ="https://www.goodreads.com"+ book_url[x-1]  #must give a check here weather book url is correct or not.
    Ddb = reviewBook(book_name[x-1],bookurl)
    num = int(input('enter 1 to continue , 0 to end: '))
end = input('enter key to exit: ')
