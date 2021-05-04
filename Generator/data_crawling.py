# -*- coding: utf-8 -*

"""
目标，爬取全部的题目以及答案
1. 利用cookie访问网页，记录全部的题目id并记录在内存中 需要把标签的属性记下来
2. 依次访问这些题目的网页，爬取问题选项和答案
3. 存储在__cache__里
"""

import requests
from lxml import etree
import re
import pandas as pd
from collections import namedtuple


def Crawler(context):
    cookie = context.cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': cookie
    }

    def getSession(url: str):
        session = requests.Session()
        return session.get(url, headers=headers)

    return getSession


def getCrawler():
    CrawlerContext = namedtuple('CrawlerContext', ['cookie'])
    crawlerContext = CrawlerContext("")
    crawler = Crawler(crawlerContext)
    return crawler


def getPageLinks(url: str, crawler, linkNum: int = 30):
    # 爬取 url
    response = crawler(url)
    # print(response.text)
    # 对html页面进行解析
    selector = etree.HTML(response.text)
    # 将题目链接追加到pageLinks
    pageLinks = []
    for i in range(linkNum):
        aPageId = selector.xpath(f'/html/body/div[1]/div[2]/div[2]/div[1]/ul/li[{i + 1}]/a/@href')
        pageLinks.append('https://www.nowcoder.com'+"".join(aPageId))
    return pageLinks


def access(pageLinks: list, crawler, choiceNum: int = 7,
           tMajor: str = "None", tSource: str = "牛客", tHard: int = 3, tType: int = "None"):
    # 遍历并且爬取试题
    rowLists = []
    for url in pageLinks:
        # 爬取 url
        response = crawler(url)
        selector = etree.HTML(response.text)
        # 把题目后没用的文字用“ ”代替
        question = re.sub("_计算机专业技能-网络基础专项练习_牛客网|<span>|</span>|\n", '', selector.xpath('/html/head/title/text()')[0])
        # 输出问题
        # print('\n', question)
        # 全部选项
        all_choice = []
        for i in range(1, choiceNum):
            content = selector.xpath(f'/html/body/div[1]/div[2]/div[2]/div[3]/div[{i}]//text()')
            if content and len(content) < 7:
                all_choice.append(f"{chr(ord('A') + (i - 1))} : {content[1]}")
        # 筛掉判断题
        if len(all_choice) < 4:
            print("\n".join(all_choice))
            continue
        # 正确选项，text（）里有正确选项
        rightAns: list = re.findall("[ABCDEF]", selector.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/h1/text()')[0])
        # 输出正确选项
        # print(rightAns)
        rowLists.append([tMajor, tSource,
                         '多选题' if len(rightAns) > 1 else '单选题', tHard, tType,
                         question, '\n'.join(all_choice), ' '.join(rightAns)])
    # 构造 DataFrame 存储数据
    paper_supplement = pd.DataFrame(rowLists, columns=('专业', '来源', '题型', '难度', '对应的知识点', '题干', '选择', '答案'))
    return paper_supplement


def save(paper_supplement: pd.DataFrame):
    # 一次卷子只有3道多选，所以得多次
    # old_paper = pd.read_excel(r"supplement\DB-primary.xlsx")
    # pd.concat([old_paper, paper_supplement], ignore_index=True).to_excel(r"supplement\DB-primary.xlsx", encoding="utf8")
    # 空目录时使用
    paper_supplement.to_excel(r"__cache__\DB-primary.xlsx", encoding="utf8")


def getSingleTestPaper(url, crawler):
    print(url, crawler)
    urls = getPageLinks(url, crawler)
    paper_supplement = access(urls, crawler)
    print(paper_supplement)
    save(paper_supplement)

