#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
from selenium import webdriver
import time
import random
import datetime
import os



class GetLinks:
    # def __init__(self, text):
    #     self.text = text
    count=0

    def spit_link(entry_link, i):
        pre_link = entry_link.split('-1', 1)[0]
        link = pre_link + f'-{i}.html'
        return link


    def meitu_link(entry_link, i):
        pre_link = entry_link.split('.html', 1)[0]
        link = pre_link + f'_{i}.html'
        return link




    def get_links(self,text,canvas, entry_link, window):
        options = webdriver.ChromeOptions()
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        wd = webdriver.Chrome(r'D:\Python37-32\Scripts\chromedriver.exe', options=options)
        wd.implicitly_wait(3)
        wd.get(entry_link)
        if entry_link.find('xinwenba') != -1:
            pagedata = wd.find_element_by_css_selector('.paging li a').get_attribute('outerHTML')
            page_count = pagedata.split('共', 1)[1]
            page_count = page_count.split('页', 1)[0]
            print(f'一共有{page_count}页')
            for i in range(int(page_count)):
                # 进度条
                fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
                x = 465 / int(page_count)  # 465是矩形填充满的次数
                n = x * (i + 1)
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0.02)  # 控制进度条流动的速度
                # 获取链接
                link = GetLinks.spit_link(entry_link, i + 1)
                print(f'page {i + 1} link:{link}')
                wd.get(link)
                sleeptime = random.randint(2, 4)
                time.sleep(sleeptime)
                elements = wd.find_elements_by_css_selector('.picture p>img')
                for element in elements:
                    data = element.get_attribute('outerHTML')
                    pre_link = data.split('src="', 1)[1]
                    link = pre_link.split('" alt', 1)[0]
                    print(link)
                    text.insert('end', link + '\n')
        elif entry_link.find('meitulu.com') != -1:
            pagedata=wd.find_element_by_css_selector('a[href*="item"]:nth-last-child(2)').get_attribute('outerHTML')
            page_count = pagedata.split('_', 1)[1]
            page_count = page_count.split('.html', 1)[0]
            print(f'一共有{page_count}页')
            ##  第一页获得
            wd.get(entry_link)
            sleeptime = random.randint(2, 4)
            time.sleep(sleeptime)
            elements = wd.find_elements_by_css_selector('.content>center img')
            for element in elements:
                data = element.get_attribute('outerHTML')
                pre_link = data.split('src="', 1)[1]
                link = pre_link.split('" alt', 1)[0]
                print(link)
                text.insert('end', link + '\n')

            ##后面几页获得
            for i in range(1,int(page_count)):
                # 进度条
                fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
                x = 465 / int(page_count)  # 465是矩形填充满的次数
                n = x * (i + 1)
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0.02)  # 控制进度条流动的速度

                # 获取链接
                link = GetLinks.meitu_link(entry_link, i + 1)
                print(f'page {i + 1} link:{link}')
                wd.get(link)
                sleeptime = random.randint(2, 4)
                time.sleep(sleeptime)
                elements = wd.find_elements_by_css_selector('.content>center img')
                for element in elements:
                    data = element.get_attribute('outerHTML')
                    pre_link = data.split('src="', 1)[1]
                    link = pre_link.split('" alt', 1)[0]
                    print(link)
                    text.insert('end', link + '\n')
        wd.close()

# getlink=GetLinks()
# getlink.get_links('https://www.xinwenba.net/plus/view-573875-1.html')