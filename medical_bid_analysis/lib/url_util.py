#!/usr/bin/env python
#coding:gbk
# url_util.py

import sys
import string
import re

# for url
strict_wise_url_keys = ['3g', 'mobile', 'siteapp', 'wap', 'page.baidu.com', 'http://m.', '4g', '5g', 'mobi.']
loose_wise_url_keys = strict_wise_url_keys[:]
loose_wise_url_keys.extend(['taobao', 'tmall'])

# for string
src = string.punctuation + ' '
delEStr = string.maketrans(src, " " * len(src))


def regularize_str(SrcStr):
    '''
        规范化一个str, 多次调用等价于一次调用
    '''
    SrcStr = SrcStr.replace('\0', '')
    SrcStr = SrcStr.replace('\t', ' ')
    SrcStr = SrcStr.replace('\n', ' ')
    SrcStr = SrcStr.replace('\r', ' ')
    SrcStr = SrcStr.replace('\1', ' ')
    SrcStr = SrcStr.replace('\2', ' ')
    # SrcStr = SrcStr.translate(delEStr).strip().replace(" ", ",")

    # 如果有3个空格及以上空格，只保留２个
    while '   ' in SrcStr:
        SrcStr = re.sub(r'   +', '  ', SrcStr).strip()

    return SrcStr.strip()

def is_valid_url(url):
    '''
        判断url是否为有效的url
    '''
    if url == None: 
        return False
    if url.find('.') < 0:
        return False
    if url.find('\t') >= 0:
        return False
    return True


def is_wise_url(url, strict=True):
    '''
       检查一个url是否是wise url, 当strict 是False时，将taobao, tmall视为wise url, 因为他们在无线访问时会自动跳转
    '''
    contain_wise_key = False

    wise_url_keys = strict_wise_url_keys
    if not strict:
        wise_url_keys = loose_wise_url_keys

    for wise_key in wise_url_keys:
        if url.find(wise_key) >= 0:
            contain_wise_key = True
            break

    return contain_wise_key

def remove_sharp(url):
    '''
        去除 url中#以后的部分
    '''
    sharp_index = url.find('#')    
    if sharp_index > 0:
        return url[0:sharp_index]
    else:
        return url 

def regularize_url(url, remove_slash=False):
    '''
        将一个url规范化
        1. 去除#以后的部分
        2. 如果不以"http://"开头，添加"http://"
        3. 如果remove_slash 等于 True且url以".com/"或".cn/"结尾，去除末尾的"/"
    '''
    if url == None:
        raise Exception('invalid url: None')
    elif url.find('.') < 0:
        raise Exception('invalid url: %s' % (url))
    
    regularized_url = remove_sharp(url)
    if not regularized_url.startswith('http'):
        regularized_url = 'http://' + regularized_url

    if remove_slash and (regularized_url.endswith('.cn/') or regularized_url.endswith('.com/')):
        regularized_url = regularized_url[:-1]
    
    # pc的奇葩url中有'\0'
    regularized_url = regularized_url.replace('\0', '')
    regularized_url = regularized_url.replace('\t', '')
    regularized_url = regularized_url.replace('\r', '')
    regularized_url = regularized_url.replace('\n', '')
    regularized_url = regularized_url.replace('\1', '')
    regularized_url = regularized_url.replace('\2', '')

    return regularized_url.strip()
