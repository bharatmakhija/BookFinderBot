def getUrl(pagenum,booktitle):
    url = "https://www.goodreads.com/search?page="+ str(pagenum) + "&q=" + booktitle + "&tab=books"
    return str(url)
