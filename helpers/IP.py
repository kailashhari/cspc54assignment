import re


def main(url):
    pat = re.compile(
        "^http[s]?:\/\/((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]).*")
    if re.fullmatch(pat, url):
        return -1
    else:
        return 1


print(main("http://192.168.1.1/asdawe/adsdw"))
print(main("http://1baidu.com1/asdawe/adsdw"))
