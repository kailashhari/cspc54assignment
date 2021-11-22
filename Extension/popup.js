document.getElementById('warning').style.display = 'none';
document.getElementById('success').style.display = 'none';
document.getElementById('danger').style.display = 'none';





document.getElementById('button').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { greeting: "hello" }, function(response) {
            console.log(response.farewell);
        });
    });
});