# -*- coding: utf-8 -*-
# @Time : 2020/9/2 13:35
# @Author : KevinHoo
# @Site : 
# @File : URLdecoder.py.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com


decode_dict = {
    ' ': '%20',
    '"': '%22',
    '#': '%23',
    '%': '%25',
    '&': '%26',
    '(': '%28',
    ')': '%29',
    '+': '%2B',
    ',': '%2C',
    '/': '%2F',
    ':': '%3A',
    ';': '%3B',
    '<': '%3C',
    '=': '%3D',
    '>': '%3E',
    '?': '%3F',
    '@': '%40',
    '\\': '%5C',
    '|': '%7C',
}


# 百分号解码
def seperatorOff(a):
    print('converting url...')
    for key in decode_dict:
        a = a.replace(decode_dict[key], key)
    return a


def splice(list, index, num):
    for i in range(num):
        list[index + i] = ''
    while '' in list:
        list.remove('')

    return list


class Fv:
    def i7(a:list, b):
        c = a[0]
        a[0] = a[b % len(a)]
        a[b % len(a)] = c

    def D3(a:list, b):
        splice(a, 0, b)

    def Hm(a:list, num:int):
        a.reverse()

def Gv(s):
    a = []
    for item in s:
        a.append(item)
    Fv.Hm(a, 30)
    Fv.i7(a, 69)
    Fv.Hm(a, 3)
    Fv.i7(a, 20)
    Fv.Hm(a, 52)
    Fv.i7(a, 32)
    Fv.D3(a, 3)
    return ''.join(a)


def decode(s):
    return Gv(s)


if __name__ == '__main__':
    sigcipher = ""
    sigcipher = seperatorOff(sigcipher)
    s = ""
    s = decode(s)