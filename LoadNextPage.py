import StringConstants
def getUrl(pagenum,booktitle):
    url = StringConstants.goodReadSearchString + str(pagenum) + "&q=" + booktitle + "&tab=books"
    return str(url)
