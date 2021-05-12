from string import Template

import requests


class Solution:
    URL = Template('https://search.jd.com/Search?keyword=${commodity}'
                   '&qrst=1&wq=${commodity}&stock=1&page=${page}&s=${amount}&click=0')

    def __init__(self, commodity):
        self.commodity = commodity
        self.page = 1
        self.amount = 1
        self.url = ''
        self.update_url()

    def update_url(self):
        self.url = Solution.URL.safe_substitute(
            commodity=self.commodity,
            page=self.page,
            amount=self.amount
        )

    def get_next_url(self):
        self.page += 2
        if self.amount == 1:
            self.amount = 56
        else:
            self.amount += 60
        self.update_url()


def get_html_txt(url_in):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        r = requests.get(url_in, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


def parser_page(info_list, content):
    pass


def show_info(info_list):
    pass


if __name__ == '__main__':
    demo = Solution('书包')
    info = []
    for i in range(0, 10):
        text = get_html_txt(demo.url)
        demo.get_next_url()
        if text is not None:
            parser_page(info, text)
        show_info(info)
