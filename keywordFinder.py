import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import argparse

# Set up argparse, a command-line parsing module
parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of the file with the urls")       # add_argument() specify which command-line options the program is willing to accept
parser.add_argument("chars", help="number of chars to be displayed", type=int)      
parser.add_argument("keyword", help="keyword to be looked for")           
args = parser.parse_args()                  # parse_args() returns some data from the options specified
fileWithURL = args.file

# Get the urls from the text file
with open (fileWithURL, "r") as f:
    urls = f.readlines()
f.close()

# Create output file and empty it
o = open ("output.txt", "w")
o.close()

# These should be taken from Command Line
keyword = args.keyword
charsExpected = args.chars

# Setup all data about each url
def setupURL():

    print(url)
    # Download page's content in html
    uClient = uReq(url)
    pageHTML = uClient.read()
    uClient.close()

    # html parsing
    pageSoup = soup(pageHTML, "html.parser")

    # Get all text on page
    pageText = pageSoup.get_text()
    return pageText

# Function that gets the final strings
def getString(pageText):
    
    index = 0
    finalString = ""
    keywordLength = len(keyword)
    foundPrinted = False

    # Find all instances of the keyword
    while index < len(pageText):
        index = pageText.find(keyword, index)

        if index == -1:                         # it will always give -1 at the end, after it found all the keywords
            if finalString == "":                   # If it gives -1 but hasn't found any keywords, it means there are none
                print("NOT FOUNT")
                o = open ("output.txt", "a")
                o.write(url)
                o.write("\n")
                o.write("NOT FOUND")
                o.write("\n")
            break

        charsBeforeAndAfter = charsExpected / 2             # half of the chars go before keyword, half after
        startStringIndex = int(index - charsBeforeAndAfter)  # Index of char half of charsExpected length before keyword
        endStringIndex = int(index + keywordLength + charsBeforeAndAfter)   # Index of char half of charsExpected length after keyword

        finalString = pageText[startStringIndex : endStringIndex]    # Final string containing keyword and the necessary chars
        if foundPrinted == False:
            print("FOUND")
            foundPrinted = True
            o = open ("output.txt", "a")
            o.write(url)
            o.write("\n")
            o.write("FOUND")
            o.write("\n")    
        
        o.write(finalString)
        o.write("\n")

        index += 1

    o.close()


for url in urls:
    url = url.rstrip('\n')                  # Take care of the extra \n char at the end of URL
    pageText = setupURL()
    getString(pageText)  


