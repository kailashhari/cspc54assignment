chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
    let url = tabs[0].url;
    console.log(url);
});

var Feedback = {
    id: "Feedback",
    title: "Send Feedback",
    contexts: ["all"],
};

chrome.contextMenus.create(Feedback);

chrome.contextMenus.onClicked.addListener(function(clickData) {

    if (clickData.menuItemId == "Feedback") {
        chrome.storage.sync.set({
            url: clickData.pageUrl,
        });
        window.open(
            "Feedback.html",
            "extension_popup",
            "width=500,height=500,status=no,scrollbars=yes,resizable=no"
        );
    }
});