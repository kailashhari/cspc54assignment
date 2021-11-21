def main(URL):
    if '@' in URL:
        return -1
    else:
        return 1


print(main('http://www.google.com'))
print(main('http://www.google.com@'))
