def main(url):
    domain = url.split('/')[2]
    # check if domain contains port
    if ':' in domain:
        port = domain.split(':')[1]
        if port in ['80', '443']:
            return 1
        else:
            return -1
    else:
        return 1

print(main('http://www.google.com'))
print(main('http://www.google.com:80'))
print(main('http://www.google.com:800/'))
