'''A TextBasedBrowser where you enter a website and receive all the text in
that website'''

import os
import sys
import requests
from colorama import init, Fore
from bs4 import BeautifulSoup
from collections import deque

saved_webpage = ['bloomberg.com', 'nytimes.com']
stack = deque()

# check for valid Url
def valid_url():
    url = input()
    if '.' in url and url != 'blooomberg.com':
        webpage_save(url)
        # show = input()
        # webpage_show(show)
    elif url == 'exit':
        exit()
    elif url == 'back':
        print(stack.popleft())
    else:
        print('Error: Invalid Url')
        valid_url()

# Creation of Directory where all the pages are stored
def cmd_work():
    dir_name = sys.argv[1]
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

# Saving the page
def webpage_save(url):
    if '.com' in url:
        saved_pagename = url.rstrip('.com')
    elif '.org' in url:
        saved_pagename = url.rstrip('.org')
    with open(os.path.join(sys.argv[1], saved_pagename + '.txt'), 'w+', encoding='UTF-8') as file:
        url = 'https://' + url
        response = requests.get(url)
        file.write(response.text)
        parsing(url, saved_pagename, response)

# Retrieving the page that is being stored
def webpage_show(url):
    if url == 'exit':
        exit()
    with open(os.path.join(sys.argv[1], url + '.txt'), 'r', encoding='UTF-8') as file:
        if url == 'bloomberg':
            print(file.read())
        elif url == 'nytimes':
            print(file.read())
        else:
            print(file.read())

# Parser used to pull out Text from the page
def parsing(url, saved_pagename, response):
    with open(os.path.join(sys.argv[1], saved_pagename + '.txt'), 'w+', encoding='UTF-8') as file:
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p','ul','ol','li','a']
        value = []
        for j in tags:
            match = soup.findAll(j)
            for i in match:
                if j == 'a':
                    init()
                    value.append(Fore.BLUE + i.text.strip('\n'))
                else:
                    value.append(i.text.strip('\n'))
        for i in value:
            file.write(i.strip() + '\n')
    webpage_show(saved_pagename)

def main():
    cmd_work()
    while True:
        valid_url()


main()
