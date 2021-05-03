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

def pageid(url, cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': cookie
    }

    session = requests.Session()

    response = session.get(url, headers=headers)

    # print(response.text)

    selector = etree.HTML(response.text)

    pagelinks = []

    for i in range(30):
        apageid = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/ul/li['+str(i+1)+']/a/@href')

        pagelinks.append('https://www.nowcoder.com'+"".join(apageid))

        # print(pagelinks)

    return pagelinks

def access(urls, cookie):

    paper_supplement = pd.DataFrame(columns=('专业', '来源', '题型', '难度', '对应的知识点', '题干', '选择', '答案', '题型序号', '使用次数', '清洗以后的知识点'))
    k = 0

    for url in urls:

        # print('\n'+url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Cookie': cookie
        }

        session = requests.Session()

        response = session.get(url, headers=headers)


        selector = etree.HTML(response.text)

        # 把题目后没用的文字用“ ”代替
        question = re.sub("_计算机专业技能-网络基础专项练习_牛客网|<span>|</span>|\n", '', selector.xpath('/html/head/title/text()')[0])

        # 正确选项，text（）里有正确选项
        # rightans是个[]，
        rightans = re.findall("[ABCDEF]", selector.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/h1/text()')[0])

        # 输出问题
        # print('\n', question)

        # 输出正确选项
        # print(rightans)

        # 1，7 由于个别题目有F选项，所有有7
        # 输出选项
        all_choice = []
        for i in range(1, 7):
            content = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div['+str(i)+']//text()')
            if len(content)<7 and content:
                answer = chr(ord('A')+(i-1))+':'+content[1]
                all_choice.append(answer)
                # print(answer)
        #筛掉判断题
        if len(all_choice) < 4:
            print(all_choice)
            continue

        temp = str
        if len(rightans) > 1:
            temp = '多选题'
        else:
            temp = '单选题'

        rowlist = ['网络原理', '牛客', temp, 1, '网络原理', question, ' '.join(all_choice), ' '.join(rightans), 0, 0, '网络原理']

        paper_supplement.loc[k] = rowlist
        k = k + 1
        print(k)
    # 一次卷子只有3道多选，所以得多次
    old_paper = pd.read_excel(r"supplement\DB-primary.xlsx")
    pd.concat([old_paper, paper_supplement], ignore_index=True).to_excel(r"supplement\DB-primary.xlsx", encoding="utf8")

    # 空目录时使用
    # paper_supplement.to_excel(r"supplement\DB-primary.xlsx", encoding="utf8")

if __name__ == '__main__':

    cookie = 'NOWCODERUID=9D5272097A6902751E68E5DDEB75BBB3; NOWCODERCLINETID=99291351A68365C472F54536F0F6E0BA; gr_user_id=ca9dd8e3-1a9a-4b19-aa11-ea339d65094d; gdxidpyhxdE=8UA0rleLjG9xpGLHISQapde5GAXgY9%2FHcslU37HYxNl%2FvNCYNtCW%2BVlR4a%2FQ%2FpJCUtzSqsq%2BhuQ8s6907%2BZ%5C%2FkiDcoUZxicI21ch2KBLIvONE%2FcjS1IOPBMpGxLx91CxD2QVooEEJsQ1ct%2BlBZBO18gedL55lLGjnRAdTHZnwWf1sX4H%3A1619953386954; _9755xjdesxxd_=32; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=485880017; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=6525e1ac-2801-466b-8bcf-9e0fcd05cae4; c196c3667d214851b11233f5c17f99d5_gr_session_id=6525e1ac-2801-466b-8bcf-9e0fcd05cae4; c196c3667d214851b11233f5c17f99d5_gr_session_id_6525e1ac-2801-466b-8bcf-9e0fcd05cae4=true; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1619954577,1619955311,1619959786,1619967050; callBack=https%3A%2F%2Fwww.nowcoder.com%2FintelligentTest; t=7398ECF4A2A8FB963B2E3C3D938182CA; c196c3667d214851b11233f5c17f99d5_gr_cs1=485880017; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1619967912; SERVERID=76c38881415ad3405ef5a3db2e9b59bb|1619967917|1619967898'

    # 试题答案解析网页
    urls = pageid('https://www.nowcoder.com/test/question/done?tid=44104458&qid=58190', cookie)
    # print(urls)
    access(urls, cookie)
