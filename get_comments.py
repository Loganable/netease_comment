# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:55:09 2020

@author: Logan
"""


import requests
import json
import time

def get_comments(url):
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
               'referer': "https://music.163.com/song?id=1338149101"}
    params = "XWS5IH+Y7yb5q8fF2mZMOLaBmJkC3TnkAFz8vb1wAlUcAeZLxjxPEgKLVvfBehj5H9PYXtAg6Rrwr7k2jx3V0n1XdDN1jsz0Cw+zBzVrEAT662Y6v+168jYw4IKHfOAmD1dgwO5cTZ9pFLE9DLkx9G9t4nouI6m70YsgGJz84Kf/ge/vBsSL8uXXeUVqvoed"
    encSecKey = "6b9cf1d37573522eff172f003f985b3a481fd16d43fd43897e76e7922681e1070c63a371eae06cf9f806e350c00803195849972ad3baa5428355bde76b8a867ef3f809bae00a4cd9ae942eff714a07b9ebcb8675fd1233fc10ce0689cc1e652daecdb70acebefa7cd2cace77e8d64ebdd5321e121c3502aacfcd8de9d6b965c5"
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(url.split('=')[1])
    
    res = requests.post(target_url, headers=headers, data={"params": params, "encSecKey": encSecKey})
    
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(each['time']/1000))
            file.write(each['user']['nickname'] + ' : ' + comment_time + '\n\n')
            file.write("点赞数：" + str(each['likedCount']) + '\n\n')
            file.write(each['content'] + '\n')
            file.write("--------------------------------\n")

def main():
    url = input("")
    get_comments(url)

if __name__ == "__main__":
    main()