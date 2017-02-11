#coding=utf-8

import requests
from pyquery import PyQuery
import shutil
import md5
from PIL import Image
import os


def get_pic_links(url='http://tieba.baidu.com/p/2166231880'):

  """
    得到一个页面中图片的链接
  """

  headers = {
      'Accept-Encoding': 'gzip, deflate, sdch',
      'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
  }
  img_link_list = []

  try:
    resp = requests.get(url=url, headers=headers, timeout=5)
    pq = PyQuery(resp.text)
    for pic in pq('img'):
      link = pic.attrib.get('src')
      img_link_list.append(link)
    return img_link_list
  except Exception as error:
    print error


def download_pic(url):

  """
    下载图片保存到本地
  """

  headers = {
      'Accept-Encoding': 'gzip, deflate, sdch',
      'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
  }

  pic_format = url.split('.')[-1]

  m = md5.new()
  m.update(url)
  file_name = ''.join([m.hexdigest(), '.', pic_format])

  try:
    response = requests.get(url=url, headers=headers, stream=True, timeout=5)
  except Exception as error:
    print error

  try:
    with open(file_name, 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
    print url, 'is ok... save as', file_name
  except Exception as error:
    print error

  # 根据图片尺寸判断是否是美女 删除其他图片
  try:
    img = Image.open(file_name)
    witdh, heigth = img.size
    if witdh < 500:
      print file_name, 'delete...'
      os.remove(file_name)
  except IOError as error:
    print "open {0} error {1}".format(file_name, error)


if __name__ == '__main__':
  links = get_pic_links()
  for link in links:
    download_pic(link)
