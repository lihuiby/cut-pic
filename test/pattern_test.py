import re

def test01(str):
    trackPattern = re.compile(
        ".*(class=\"text-primary kz_anim\")( href=\")(/\w+\.html)(\" target).*")
    trackMatch = trackPattern.match(str)
    print(trackMatch.group())
    print(trackMatch.group(1))
    print(trackMatch.group(2))
    print(trackMatch.group(3))
    return None
abc = "',{'企业名称':'湖南鼎一致远科技发展有限公司'});\" class=\"text-primary kz_anim\" href=\"/snapshoot_5f3d5d3031cb5c60b1fb4b77b83550ba.html\" target=\"_blank\">"
test01(abc)