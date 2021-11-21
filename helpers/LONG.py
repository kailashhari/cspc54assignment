def main(URL):
    if len(URL) < 54:
        return 1
    elif len(URL) <= 75:
        return 0
    else:
        return -1


print(main("http://www.google.com"))
print(main("http://www.google.com/search?q=python"))
print(main("http://www.google.com/search?q=python&q=python"))
print(main("http://www.google.com/search?q=python&q=python&q=python"))
print(main("http://www.google.com/search?q=python&q=python&q=python&q=python"))
print(main("http://www.google.com/search?q=python&q=python&q=python&q=python&q=python"))
print(main("http://www.google.com/search?q=python&q=python&q=python&q=python&q=python&q=python"))
print(main("http://www.google.com/search?q=python&q=python&q=python&q=python&q=python&q=python&q=python"))
