import re


def solution():
    # pattern = re.compile(r'(?P<years>\d+).(?P<month>\d+).(?P<day>\d+)[.]?(?=.docx$)')
    pattern = re.compile(r"""
     (?P<years>\d+)         # 匹配年份
     .                      # 间隔
     (?P<month>\d+)         # 匹配月份
     .                      # 间隔
     (?P<day>\d+)           # 匹配天数   
     .*[.](?=xlsx$)[^.]*$   # 文件末尾
    """, re.VERBOSE)
    test = '2021-11-20.xlsx'
    m = pattern.match(test)
    if m is not None:
        print(m.groupdict())
    else:
        print('is None')


if __name__ == '__main__':
    solution()
