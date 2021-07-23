import os
import urllib.parse
import webbrowser

code = """
var regexp = new RegExp(/playerCaptionsTracklistRenderer.*?(youtube.com\/api\/timedtext.*?)"/);
var match = regexp.exec(document.body.innerHTML);
if (!match) {
  alert ("No captions found");
  return;
}
var url = regexp.exec(document.body.innerHTML)[1];
var new_window = open("http://Imatrei.github.io/ko-en-card-generator/caption.py?url=" + encodeURIComponent(url));
"""

code = code.replace("$url", encodedURL)
code = urllib.parse.quote(code)

html = """
<a href="javascript:(function(){ $code })()">YouTube Transcription</a>
"""

html = html.replace("$code", code)

path = os.path.abspath('index.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)
