import urllib.request
import re

qccHost = "https://www.qcc.com"
qccComponyUrl = "https://www.qcc.com/firm_5f3d5d3031cb5c60b1fb4b77b83550ba.html"
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.5.2.18321'
}

headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'https://www.qcc.com/'
           }

requestQ = urllib.request.Request(url=qccComponyUrl, headers=headers)
response = urllib.request.urlopen(requestQ)
result = response.read().decode('utf-8')
split = result.split("查看工商官网快照")
if len(split) == 3 and result.find("text-primary kz_anim"):
    str = split[1]
    print(str)
    trackPattern = re.compile(
        ".*(class=\"text-primary kz_anim\")( href=\")(/\w+\.html)(\" target).*")
    trackMatch = trackPattern.match(str)
    downUrl = qccHost + trackMatch.group(3)
    print(downUrl)
else:
    print("%s \r\n查询异常" %result)



