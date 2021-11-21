def main(url):
    if url.rfind('//') > 7:
        return -1
    else:
        return 1


print(main('http://www.google.com'))
print(main('http://www.google.com/https//'))
