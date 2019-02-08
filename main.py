import requests
from lxml import html
import urllib.request
import os
import getpass


def login(email, password):
    payload = {
        "email": email,
        "password": password
    }
    session_requests = requests.session()
    login_url = 'https://mybrandnewlogo.com/login'
    result = session_requests.post(
        login_url,
        data=payload,
        headers=dict(referer=login_url)
    )
    if (result.content == b'{"message":"you\'re now logged in","redirect":"/logos"}'):
        return session_requests
    else:
        return 'Failed'


def scrape_all_logos(session_requests):
    url = 'https://mybrandnewlogo.com/logos/1'
    result = session_requests.get(
        url,
        headers=dict(referer=url)
    )
    tree = html.fromstring(result.content)
    img_src = tree.xpath(
        "//div[@class='b-logo-thumbnail']/a/@href")
    for i in range(len(img_src)):
        img_src[i] = 'https://mybrandnewlogo.com' + img_src[i]
    return img_src


def scrape_specific_img(url, session_requests, filename, filepath):
    result = session_requests.get(
        url,
        headers=dict(referer=url)
    )
    tree = html.fromstring(result.content)
    img_src = tree.xpath(
        "//div[@class='b-logo-thumbnail__wrap--white']/img/@src")[0]

    urllib.request.urlretrieve(
        img_src, filepath + '\\' + filename + '.png')
