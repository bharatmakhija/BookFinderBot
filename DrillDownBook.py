import StringConstants
import ElementConstants
def reviewBook(bookname,url):
    print(StringConstants.informationLoadingMessage + bookname + StringConstants.havingUrlMsg + url)
    import requests
    from bs4 import BeautifulSoup
    try:
        r = requests.get(url, timeout = ElementConstants.drilldownTimeOutCount)
    except requests.exceptions.Timeout:
        print(StringConstants.timeoutError)
    except requests.exceptions.TooManyRedirects:
        print(StringConstants.badUrlError)
    except requests.exceptions.RequestException as e:
        print(StringConstants.unexpectedError)
        print(e)
        exit(1)
    soup = BeautifulSoup(r.content,ElementConstants.beautifulSoupMethodName)
    try:
        for d in soup.find_all(ElementConstants.divComponent, {ElementConstants.classComponent: ElementConstants.drilldownElementToRead}):
                k = d.find_all(ElementConstants.spanComponent)
                try:
                    print(k[1].text)
                except:
                    print(StringConstants.noInformationFoundError)
    except:
        print(StringConstants.noInformationFoundError)
