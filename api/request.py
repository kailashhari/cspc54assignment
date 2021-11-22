import requests
from datetime import datetime


def domain_registration_length(res):
    try:
        return 1 if datetime(res["WhoisRecord"]["expiresDate"]) - datetime(res["WhoisRecord"]["creationDate"]) > datetime.timedelta(days=365) else 0
    except:
        return 0

def domain_age(res):
    try:
        return 1 if res["WhoisRecord"]["estimatedDomainAge"] > 180*24 else 0
    except:
        return 0




def main(url):
    res = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_Bl5utm82hRNTXJQ01LVD1osWxRVXc&outputFormat=JSON&domainName="+url)
    
    res = res.json()
    # print(res)
    abnormal_url = 0
    domain = url.split("/")[2]

    if res:
        abnormal_url = 1
    else:
        abnormal_url = -1
    

    https_invalid = 0
    redirects = 0
    try:
        resp = requests.get(url)
        redirects = len(resp.history)
        redirects  = -1 if redirects > 4 else (0 if redirects > 1 else 1)
        https_invalid = 1
    except requests.exceptions.ConnectionError:
        https_invalid -1

    google_index = 0

    resp = requests.get("https://google.com/search?q=site%3"+domain)
    if "did not match" in resp.text:
        google_index = -1
    else:
        google_index = 1

    dns_record=0
    resp = requests.get("https://api.hackertarget.com/dnslookup/?q="+domain)
    dns_record = 1 if res else -1
    
    web_traffic = 0
    try:
        1 if res["WhoisRecord"]["registryData"]["webTraffic"] > 100000 else 0
    except:
        web_traffic = 0

    name_server = 0
    try:
        1 if res["WhoisRecord"]["registryData"]["nameServers"] else 0
    except:
        name_server = 0
        
    return {
        'domain_age': domain_age(res),
        'abnormal_url': abnormal_url,
        'https_invalid': https_invalid,
        'domain_reg_length': domain_registration_length(res),
        'dns_record': dns_record,
        'web_traffic': web_traffic,
        'page_rank': 1,
        'google_index': google_index,
        'link_point': 1,
        'statistics': name_server,
        'redirects': redirects
    }

print(type(datetime.now()))