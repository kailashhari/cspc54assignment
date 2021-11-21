def main(url):
    dName = url.split('/')[2]
    cnt = dName.count('.')
    if cnt > 2:
        return -1
    elif cnt == 2:
        return 0
    else:
        return 1

print("MULTISUBDOMAINS")
print(main("https://www.google.com"))
print(main("https://www.google.com.tw"))
print(main("https://www.google.co.jp"))