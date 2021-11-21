def main(URL):
    dName = URL.split('/')[2]
    if '-' in dName:
        return -1
    else:
        return 1


print(main('https://www.google.com/'))
print(main('https://www.google.com/search?q=python-3'))
print(main('https://www.goo-gle.com/search?q=python-3'))
