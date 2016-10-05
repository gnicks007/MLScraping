# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:46:29 2016

find out info about a webpage: number of imported js, size, # of paragraphs etc 
use to analyze emails..can one get authenticated access to gmail inbox using API?

Analyze your inbox and writing style. can one access mood

@author: Litombe
"""


from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

def openHTML(url):
    response = urlopen(url)
    htmlRead = response.read()    
    
    return htmlRead
    
    
def main():
    data = openHTML('http://www.nba.com')
    print(data)
    
    """testString = "hello, World"
    
    result = re.match(r'hello', testString)
    print(result.group)
    
    if result:
        print("match found")      
    else:
        print("no match") """
    
    chowder = BeautifulSoup(data, 'html.parser')
    print(chowder.prettify())
    
    links = chowder.find_all('a')
    numLinks = len(links)    
    
    for link in links:
        print(link.get('href'))
    
    """print(chowder.get_text())"""
    
    tables = chowder.find_all('table')
    print(len(links))
    
    scripts = chowder.find_all('script')
    divs = chowder.find_all('div')
    
    print(len(scripts), len(divs))
    
main()

