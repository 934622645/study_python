# -*- coding: utf-8 -*
def square_root_bi(x, precision):
    """
    :param x: 数字
    :param precision: 精度
    :return: 根号数值
    :rtype: float
    """
    # pre conditions
    assert x > 0
    assert precision > 0.0

    # initialization
    low = 0
    high = x
    middle = (low + high) / 2.0
    count = 0
    while abs(high - low) > precision and count < 100:
        if middle ** 2 < x:
            low = middle
        else:
            high = middle
        middle = (low + high) / 2.0
        count += 1

    # rear conditions
    assert count < 100
    return middle


if __name__ == '__main__':
    print(square_root_bi(2888999, 0.00001))
