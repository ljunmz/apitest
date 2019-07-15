from redminelib import Redmine
from utils.requestUitls import doRequestCookie


def getRedmineCookie():
    method = "GET"
    url = "http://red.shiguangxu.com/redmine/login"
    jsons = {}
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    datas = {}
    r = doRequestCookie(method, url, datas, jsons, header)

    # json_str = json.loads(r)
    return r


def redmin():
    redmine = Redmine('http://red.shiguangxu.com/redmine/', key='339e1f86-828b-4e9c-9e0f-6534c9f7320b')
    project = redmine.get('5985')
    print(project)


print(redmin())
