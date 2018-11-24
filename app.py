from flask import Flask
import requests
from module import OaDb, db
import time
import datetime
from requests.adapters import HTTPAdapter
import re

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def get_page(url):
    res = requests.get(url)
    page_bar = res.json().get("attributes").get("page_bar")
    l = re.split(r">|<\/a>", page_bar)
    print(l)
    return int(l[-6])


def get_data():
    url = "http://www.hebgt.gov.cn/cms/blztcxWebJson.do?jsMethod=getData&pageSize=100&pageIndex=%d"
    n = 0
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    p = get_page(url % 1)
    while True:
        n += 1
        if n > p:
            break
        try:
            res = s.get(url=url % n, headers=h, timeout=40)
            if len(res.json().get("attributes").get("data")) == 0:
                break
            for x in res.json().get("attributes").get("data"):
                all_data = OaDb(
                    position=x.get("position"),
                    createTime=datetime.datetime.fromtimestamp(x.get("createTime") / 1000),
                    comp=x.get("comp"),
                    itemname=x.get("itemName"),
                    dostat=x.get("doStat"),
                    cityname=x.get("cityName"),
                    casedate=datetime.datetime.fromtimestamp(x.get("caseDate") / 1000),
                    citycode=x.get("cityCode"),
                    workname=x.get("workName"),
                    showcode=x.get("showCode"),
                    domain=x.get("domain"),
                    commitman=x.get("commitMan"),
                    userphone=x.get("userPhone"),
                    itemdate=datetime.datetime.fromtimestamp(x.get("itemDate") / 1000),
                    itemcode=x.get("itemCode")
                )
                db.session.merge(all_data)
            db.session.commit()
        except Exception as e:
            s.close()
            print(e)
            print(n)


if __name__ == '__main__':
    app.run()
