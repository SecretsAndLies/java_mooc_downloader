import pdfkit
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getListOfURLS(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    c = "PagesInThisSection__StyledLink-sc-6agvdl-2 gWgsIe"
    urls = []

    for link in soup.find_all(class_=c):
        shortLink = link.get('href')
        longLink = f"https://java-programming.mooc.fi{shortLink}"
        urls.append(longLink)
    return urls


def convertURLToPDF(url, out):
    pdf = pdfkit.from_url(url, out)


def getListOfParts():
    listOfPartURLS = []
    baseURL = "https://java-programming.mooc.fi/part-"
    for i in range(1, 15):
        listOfPartURLS.append(f"{baseURL}{i}")
    return listOfPartURLS


def main():
    parts = getListOfParts()
    for partNum, part in enumerate(parts):
        urls = getListOfURLS(part)
        for urlNum, url in enumerate(urls):
            output = f"{partNum+1}-{urlNum+1}.pdf"
            print(output)
            convertURLToPDF(url, output)


main()
