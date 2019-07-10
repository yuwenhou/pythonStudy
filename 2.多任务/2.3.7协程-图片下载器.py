import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(file_name,img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(file_name, 'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", "https://rpic.douyucdn.cn/asrpic/190704/7177978_1444.png"),
        gevent.spawn(downloader, "2.jpg", "https://rpic.douyucdn.cn/asrpic/190704/3764147_1442.png"),
    ])



if __name__ == '__main__':
    main()