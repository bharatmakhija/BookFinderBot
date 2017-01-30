def reviewBook(bookname,url):
    print("PLease Wait! Loading Information on  "+ bookname + " haiving url: " + url)
    import requests
    from bs4 import BeautifulSoup
    try:
        r = requests.get(url, timeout = 6)
    except requests.exceptions.Timeout:
        print("TimeOut error")
    except requests.exceptions.TooManyRedirects:
        print("Url is bad: TooManyRedirects")
    except requests.exceptions.RequestException as e:
        print("Some Unexpected error has occured::")
        print(e)
        exit(1)
    soup = BeautifulSoup(r.content,"lxml")
    try:
        for d in soup.find_all('div', {"class": "readable stacked"}):
                k = d.find_all('span')
                try:
                    print(k[1].text)
                except:
                    print("No Information Found!")
    except:
        print("No Information found")
