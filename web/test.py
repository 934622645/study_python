import requests
from bs4 import BeautifulSoup
import os


def get_image(url, dir):
    path = dir + '\\' + url.split('/')[-1]
    if not os.path.exists(dir):
        os.mkdir(dir)
    try:
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
            return 'is ok'
        else:
            return 'is exists'
    except:
        return '失败了'
    # url_global = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3020252718,2078753353&fm=11&gp=0.jpg'
    # dir_global = 'C:\\Users\\93462\\Desktop\\workSpace\\python\\study_python\\resource\\image'
    # print(get_image(url_global, dir_global))


def ip_address(ip):
    url = 'http://m.ip138.com/ip.sap?ip='
    try:
        r = requests.get(url + ip)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return 'ip failure'


def url_html_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'url html get fail'


def bs4_test():
    demo = url_html_text('https://python123.io/ws/demo.html')
    soup = BeautifulSoup(demo, 'html.parser')
    a = soup.a
    print(a.name)
    print(a.attrs)
    print(a.contents)
    soup.findAll()


def out_print():
    name = '好爸爸'
    id = 10
    sex = '性别'
    print('{0:-^10}{1:{3}^10}{2:{3}^6}'.format(id, name, sex, chr(12288)))


if __name__ == '__main__':
    url_global = 'https://mmbiz.qpic.cn/mmbiz_jpg/cDAL7lR5qvkfyRTYlehFBI4ONEM06t3GEG3GBUlTapBlEL4KQK1Kn4jH4QsDYTghAozMd9aMYPZia0eXGDz6CIw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1'
    dir_global = 'C:\\Users\\93462\\Desktop\\workSpace\\python\\study_python\\resource\\image'
    print(get_image(url_global, dir_global))
