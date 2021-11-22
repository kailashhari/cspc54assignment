console.log('feedback.js');

chrome.storage.sync.get(['url'], (res) => {
    document.getElementById('url').value = res.url;
})

document.getElementById('feedback-form').addEventListener('submit', function(e) {
    e.preventDefault();

    chrome.storage.sync.get([
        'url',
        'favicon',
        'requestURL',
        'AnchorURL',
        'LinksInScript',
        'ServerFormHandler',
        'InfoEmail',
        'StatusBarCust',
        'DisableRightClick',
        'UsingPopupWindow',
        'IframeRedirection'
    ], (res) => {
        var data = {
            url: document.getElementById('url').value,
            phishing: document.getElementById('phishing').value,
            favicon: res.favicon,
            requestURL: res.requestURL,
            AnchorURL: res.AnchorURL,
            LinksInScript: res.LinksInScript,
            ServerFormHandler: res.ServerFormHandler,
            InfoEmail: res.InfoEmail,
            StatusBarCust: res.StatusBarCust,
            DisableRightClick: res.DisableRightClick,
            UsingPopupWindow: res.UsingPopupWindow,
            IframeRedirection: res.IframeRedirection
        };
        console.log(data);
        $.get(
            'http://localhost:5000/feedback',
            data,
            function(res) {
                console.log(res);
                if (res == "!") {
                    alert('Thank you for your feedback!');
                    window.close();
                }
            }
        )
    });


});