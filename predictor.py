from api import request

from helpers import IP
from helpers import LONG
from helpers import TINY
from helpers import AT
from helpers import REDIRECT
from helpers import HIPHEN
from helpers import MULTISUBDOMAINS
from helpers import HTTPSDOMAIN
from helpers import PORT


def predictor(
    url, 
    favicon, 
    requestURL,
    AnchorURL,
    LinksInScript,
    ServerFormHandler,
    InfoEmail,
    StatusBarCust,
    DisableRightClick,
    UsingPopupWindow,
    IframeRedirection ):
    result = request.main(url)
    print("Requrl: ", requestURL)
    returnable = [
        IP.main(url),
        LONG.main(url),
        TINY.main(url),
        AT.main(url),
        REDIRECT.main(url),
        HIPHEN.main(url),
        MULTISUBDOMAINS.main(url),
        result["https_invalid"],
        result["domain_reg_length"],
        favicon,
        PORT.main(url),
        HTTPSDOMAIN.main(url),
        requestURL,
        AnchorURL,
        LinksInScript,
        ServerFormHandler,
        InfoEmail,
        result["abnormal_url"],
        result["redirects"],
        StatusBarCust,
        DisableRightClick,
        UsingPopupWindow,
        IframeRedirection,
        result["domain_age"],
        result['dns_record'],
        result["web_traffic"],
        result["page_rank"],
        result["google_index"],
        result["link_point"],
        result["statistics"],
    ]
    print( returnable)
    result_r = []
    for r in returnable:
        if r == None:
            r = 0
        else:
            r = int(r)
        # print(i,r)
        result_r.append(r)
    return result_r