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
    crawlerContext = CrawlerContext("__snaker__id=DM49Ws5dMIa9oTv2; NOWCODERUID=D60CE7A7B12E831C306597DA09A1DACF; NOWCODERCLINETID=6276CD1A9ED3213DD255EC0C82369756; from=nowcoderexam; gr_user_id=fd117638-ee50-4b67-beed-e62a682a778d; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=4660088; grwng_uid=4bf44f29-75f4-4a00-a071-507b012831c5; _9755xjdesxxd_=32; c196c3667d214851b11233f5c17f99d5_gr_session_id=3a641f72-9e84-435b-a10b-def13eced625; t=519BBC8F0B0CF8FD3B7BC0A88C19CB82; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=3a641f72-9e84-435b-a10b-def13eced625; c196c3667d214851b11233f5c17f99d5_gr_session_id_3a641f72-9e84-435b-a10b-def13eced625=true; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1619952208,1619952245,1620146404,1620147649; qc_qid_set_next_pre=358074_97545_369502_162236_1085940_590667_358785_358787_1056742_1555123_591386_1636096_1636008_1636012_1636011_335753_1531372_800819_1664956_1664960; gdxidpyhxdE=CpnoKeT7p0ZH%5C3eEfBsIoihZJ%2FOgBC%2BJ8N78CivuC9kohhU64YntbuAITilIK4%2Bj04NsP1OcC7ABAmgL6w601jK%5Cyw5bvS2J6W%2FLb7ji7U234H0z%5C9mEgRTIfPkLt%2B9dB9gBX4NwAgm%5Cpvj%2FKPbzNt7CbnijLq1%2Bn%2B2v86tI0m%2B16VIB%3A1620148799258; c196c3667d214851b11233f5c17f99d5_gr_cs1=4660088; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1620149383; SERVERID=01ca37401d33369101f3ce5bd23561b1|1620150384|1620146549")
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


def getSingleTestPaper(url, crawler):
    print(url, crawler)
    urls = getPageLinks(url, crawler)
    paper_supplement = access(urls, crawler)
    print(paper_supplement)
    # 保存文件， 第一次使用请建立problem_set_index.txt文件
    f = open(r"__cache__\problem_set_index.txt", "r+")
    index = int(f.read()) + 1
    paper_supplement.to_excel(rf"__cache__\problem_set{index}.xlsx", encoding="utf8")
    f.seek(0)
    f.write(str(index))
    f.close()


if __name__ == "__main__" :
    getSingleTestPaper("https://www.nowcoder.com/test/question/done?tid=44123030&qid=166241", getCrawler())