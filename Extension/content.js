// Listen for 
console.log('content.js');
// // chrome.runtime.onMessage.addListener(function(msg, sender, sendResponse) {
// //     console.log(msg);
// //     if (msg.text === 'clicked_browser_action') {
// //         // Call the specified callback, passing
// //         // the web-page's DOM content as argument
// //         sendResponse(document.body.outerHTML);
// //         return true;
// //     }
// // });

// chrome.runtime.onMessage.addListener(
//     function(request, sender, sendResponse) {
//         console.log(sender.tab ?
//             "from a content script:" + sender.tab.url :
//             "from the extension");
//         if (request.greeting === "hello")
//             sendResponse({ farewell: "goodbye" });
//     }
// );

function isFaviconDomainUnidentical() {
    var reg = /[a-zA-Z]\//;
    var url = window.location.href;
    if (document.querySelectorAll("link[rel*='shortcut icon']").length > 0) {
        var faviconurl = document.querySelectorAll("link[rel*='shortcut icon']")[0].href;
        if ((url.substring(0, url.search(reg) + 1)) == (faviconurl.substring(0, faviconurl.search(reg) + 1))) {
            console.log("NP");
            return -1;
        } else {
            console.log("P");
            return 1;
        }
    } else {
        console.log("NP");
        return -1;
    }
}

function isImgFromDifferentDomain() {
    var totalCount = document.querySelectorAll("img").length
    var identicalCount = getIdenticalDomainCount("img");
    if (((totalCount - identicalCount) / totalCount) < 0.22) {
        console.log("NP");
        return -1;
    } else if ((((totalCount - identicalCount) / totalCount) >= 0.22) && (((totalCount - identicalCount) / totalCount) <= 0.61)) {
        console.log("Maybe");
        return 0;
    } else {
        console.log("P");
        return 1;
    }
}

function isAnchorFromDifferentDomain() {
    var totalCount = document.querySelectorAll("a").length
    var identicalCount = getIdenticalDomainCount("a");
    if (((totalCount - identicalCount) / totalCount) < 0.31) {
        console.log("NP");
        return -1;
    } else if ((((totalCount - identicalCount) / totalCount) >= 0.31) && (((totalCount - identicalCount) / totalCount) <= 0.67)) {
        console.log("Maybe");
        return 0;
    } else {
        console.log("P");
        return 1;
    }
}

function isScLnkFromDifferentDomain() {
    var totalCount = document.querySelectorAll("script").length + document.querySelectorAll("link").length
    var identicalCount = getIdenticalDomainCount("script") + getIdenticalDomainCount("link");
    if (((totalCount - identicalCount) / totalCount) < 0.17) {
        console.log("NP");
        return -1;
    } else if ((((totalCount - identicalCount) / totalCount) >= 0.17) && (((totalCount - identicalCount) / totalCount) <= 0.81)) {
        console.log("Maybe");
        return 0;
    } else {
        console.log("P");
        return 1;
    }
}

function isFormActionInvalid() {
    var totalCount = document.querySelectorAll("form").length
    var identicalCount = getIdenticalDomainCount("form");
    if (document.querySelectorAll('form[action]').length <= 0) {
        console.log("NP");
        return -1;
    } else if (identicalCount != totalCount) {
        console.log("Maybe");
        return 0;
    } else if (document.querySelectorAll('form[action*=""]').length > 0) {
        console.log("P");
        return 1;
    } else {
        console.log("NP");
        return -1;
    }
}

function isMailToAvailable() {
    if (document.querySelectorAll('a[href^=mailto]').length <= 0) {
        console.log("NP");
        return -1;
    } else {
        console.log("P");
        return 1;
    }
}

function isStatusBarTampered() {
    if ((document.querySelectorAll("a[onmouseover*='window.status']").length <= 0) || (document.querySelectorAll("a[onclick*='location.href']").length <= 0)) {
        console.log("NP");
        return -1;
    } else {
        console.log("P");
        return 1;
    }
}

function isIframePresent() {
    if (document.querySelectorAll('iframe').length <= 0) {
        console.log("NP");
        return -1;
    } else {
        console.log("P");
        return 1;
    }
}

function isPopupPresent() {
    if (document.querySelectorAll('.popup').length <= 0) {
        console.log("NP");
        return -1;
    } else {
        console.log("P");
        return 1;
    }
}

function isRightClickAvailable() {
    if (document.querySelectorAll('a[oncontextmenu]').length <= 0) {
        console.log("NP");
        return -1;
    } else {
        console.log("P");
        return 1;
    }
}

function getIdenticalDomainCount(tag) {
    var i;
    var identicalCount = 0;
    var reg = /[a-zA-Z]\//;
    var url = window.location.href;
    var mainDomain = url.substring(0, url.search(reg) + 1);
    var nodeList = document.querySelectorAll(tag);
    if (tag == "img" || tag == "script") {
        nodeList.forEach(function(element, index) {
            i = nodeList[index].src
            if (mainDomain == (i.substring(0, i.search(reg) + 1))) {
                identicalCount++;
            }
        });
    } else if (tag == "form") {
        nodeList.forEach(function(element, index) {
            i = nodeList[index].action
            if (mainDomain == (i.substring(0, i.search(reg) + 1))) {
                identicalCount++;
            }
        });
    } else if (tag == "a") {
        nodeList.forEach(function(element, index) {
            i = nodeList[index].href
            if ((mainDomain == (i.substring(0, i.search(reg) + 1))) && ((i.substring(0, i.search(reg) + 1)) != null) && ((i.substring(0, i.search(reg) + 1)) != "")) {
                identicalCount++;
            }
        });
    } else {
        nodeList.forEach(function(element, index) {
            i = nodeList[index].href
            if (mainDomain == (i.substring(0, i.search(reg) + 1))) {
                identicalCount++;
            }
        });
    }
    return identicalCount;
}


var url = document.URL;
console.log(url);

chrome.storage.sync.set({
    url: url,
    favicon: isFaviconDomainUnidentical(),
    requestURL: isImgFromDifferentDomain(),
    AnchorURL: isAnchorFromDifferentDomain(),
    LinksInScript: isScLnkFromDifferentDomain(),
    ServerFormHandler: isFormActionInvalid(),
    InfoEmail: isMailToAvailable(),
    StatusBarCust: isStatusBarTampered(),
    DisableRightClick: isRightClickAvailable(),
    UsingPopupWindow: isPopupPresent(),
    IframeRedirection: isIframePresent()
});



$.get(
    "http://localhost:5000/predict", {
        url: url,
        favicon: isFaviconDomainUnidentical(),
        requestURL: isImgFromDifferentDomain(),
        AnchorURL: isAnchorFromDifferentDomain(),
        LinksInScript: isScLnkFromDifferentDomain(),
        ServerFormHandler: isFormActionInvalid(),
        InfoEmail: isMailToAvailable(),
        StatusBarCust: isStatusBarTampered(),
        DisableRightClick: isRightClickAvailable(),
        UsingPopupWindow: isPopupPresent(),
        IframeRedirection: isIframePresent()
    }
).done(function(data) {
    if (data == 0) {
        alert("This website is not safe to visit");
    } else {
        alert("This website is safe to visit");
    }
});