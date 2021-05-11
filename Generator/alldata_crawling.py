import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #鼠标事件
import re
import random
import pandas as pd

driver = webdriver.Edge()

"""
        一星：5
        二星：25
        三星：55
        四星：85
        五星：115
"""

"""
    数据库：23
    操作系统：25
    网络基础：40
"""

def ini_web():
    driver.get('https://www.nowcoder.com/login')
    # driver.set_window_size(1500, 1000)

    # 输入用户名
    time.sleep(1)
    name_text = driver.find_element_by_id("jsEmailIpt")
    # print(name_text)
    name_text.send_keys("18576270124")

    # 输入密码
    time.sleep(2)
    key_text = driver.find_element_by_id("jsPasswordIpt")
    # print(key_text)
    key_text.send_keys("12345689")

    # 登录！
    login_b = driver.find_element_by_id("jsLoginBtn")
    login_b.click()

def get_paper(hard: int = 25, konwledge: int = 40):
    # 延时等待网页加载
    time.sleep(1)
    problem_database = driver.find_element_by_link_text("题库")
    problem_database.click()

    # 专项练习
    time.sleep(1)
    special_practise_button = driver.find_element_by_link_text("知识点专项练习")
    special_practise_button.click()

    # 选择知识点
    """
        诶，不会定位，只能通过数第几个checkbox。。
        数据库：23
        操作系统：25
        网络基础：40
    """
    time.sleep(1)
    check_box = driver.find_elements_by_class_name("checkbox")[konwledge]
    check_box.click()

    # 题目难度选择
    """
        (⊙﹏⊙)，滑动选择的星星不知道怎么更改，只能通过鼠标悬停来选择难度。。。
        一星：5
        二星：25
        三星：55
        四星：85
        五星：115
    """
    level_choice = driver.find_element_by_xpath("//span[@title='请点击选择分数']")
    ActionChains(driver).move_to_element_with_offset(level_choice, hard, 0).perform()

    # 题目数量选择
    """
        again，只能通过数第几个radio。。
        30题：7
        20题：6
        10题：5
    """
    time.sleep(1)
    number_choice = driver.find_elements_by_class_name("radio")[7]
    number_choice.click()

    # 点击练习模式
    time.sleep(1)
    practise_pattern = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
    practise_pattern.click()

    # 提前交卷
    time.sleep(1)
    pre_submit = driver.find_element_by_xpath("//input[@value='提前交卷']")
    pre_submit.click()

    # 确认：立即交卷
    time.sleep(1)
    now_submit = driver.find_element_by_xpath("//a[@class='btn btn-primary confirm-btn']")
    now_submit.click()

    # 查看答案解析
    time.sleep(1)
    look_details = driver.find_element_by_xpath("//a[@class='btn btn-primary btn-lg nc-req-auth']")
    look_details.click()

def get_single_data(qMajor: str = "网络原理-初级", qSource: str = "牛客", qHard:int = 1, qKnowledge: str = "网络原理-初级", rest: str = "网络基础专项练习"):
    rowList = []
    # 问题：
    Question = driver.find_element_by_xpath("/html/head/title")
    question = re.sub(f"_计算机专业技能-{rest}_牛客网|<span>|</span>|\n", '', Question.get_attribute('textContent'))
    # print(question)

    # 答案：
    time.sleep(1)
    Answer = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/h1')
    answer = "".join(re.findall("[ABCDEF]", Answer.get_attribute('textContent')))
    # print(answer)

    # 选项：
    choice_A = 'A:' + driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[1]').get_attribute(
        'textContent')[1:].strip()
    choice_B = 'B:' + driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]').get_attribute(
        'textContent')[1:].strip()
    choice_C = 'C:' + driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[3]').get_attribute(
        'textContent')[1:].strip()
    choice_D = 'D:' + driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[4]').get_attribute(
        'textContent')[1:].strip()

    # # print(type(choice_A))
    # if choice_A.find("\n") == -1:
    #     print(choice_A)
    # if choice_B.find("\n") == -1:
    #     print(choice_B)
    # 筛掉判断题:
    if choice_C.find("\n") != -1:
        return
    if choice_D.find("\n") != -1:
        return

    # 筛掉“王道论坛”图片题
    if question.find("王道论坛") != -1:
        return

    # 筛掉五（或以上）选题:
    if answer.find('E' or 'F' or 'G') != -1:
        return

    # 随机单选改填空:
    if random.sample([0, 1], 1)[0] and len(answer) == 1:
        content = str
        if answer == 'A':
            content = choice_A[2:]
        if answer == 'B':
            content = choice_B[2:]
        if answer == 'C':
            content = choice_C[2:]
        if answer == 'D':
            content = choice_D[2:]
        rowList = [qMajor, qSource,
                   '填空题', qHard, qKnowledge, question, '',
                   ('正确答案:' + content)
                   ]
        # 筛掉(D:A和B )的题目,可能错杀。。
        if content.find('A' or 'B' or 'D' or 'C') != -1:
            return
        return rowList

    rowList = [qMajor, qSource,
               '多选题' if len(answer) > 1 else '单选题', qHard, qKnowledge, question,
               (choice_A + '\n' + choice_B + '\n' + choice_C + '\n' + choice_D), ('正确答案:' + answer)
               ]
    return rowList

def get_data(qMajor: str = "网络原理-初级", qSource: str = "牛客", qHard:int = 1, qKnowledge: str = "网络原理-初级", rest: str = "网络基础专项练习"):
    rowLists = []
    for n in range(1, 31):
        temp_button = driver.find_element_by_link_text(str(n))
        time.sleep(1)
        temp_button.click()
        time.sleep(1)
        temp: list = get_single_data(qMajor, qSource, qHard, qKnowledge, rest)
        if temp != None:
            # print("===\n")
            rowLists.append(temp)

    # 构造 DataFrame 存储数据
    print(rowLists)
    time.sleep(1)
    paper_supplement = pd.DataFrame(rowLists, columns=('专业', '来源', '题型', '难度', '对应的知识点', '题干', '选择', '答案'))
    # return paper_supplement

    # 保存文件， 第一次使用请建立problem_set_index.txt文件
    f = open(r".\__cache__\problem_set_index.txt", "r+")
    index = int(f.read()) + 1
    paper_supplement.to_excel(rf".\__cache__\problem_set{index}.xlsx", encoding="utf8")
    f.seek(0)
    f.write(str(index))
    f.close()

def generate_data():
    ini_web()
    # # 网络原理-初级 10套
    # for a in range(10):
    #     get_paper()
    #     get_data()
    # # 网络原理-中级 10套
    # for b in range(10):
    #     get_paper(55)
    #     get_data("网络原理-中级", "牛客", 2, "网络原理-中级")
    # 数据库-初级 10套
    # for c in range(9):
    #     get_paper(25, 23)
    #     get_data("数据库-初级", "牛客", 1, "数据库-初级", "数据库专项练习")
    # # 数据库-中级 10套
    # for c in range(4):
    #     get_paper(55, 23)
    #     get_data("数据库-中级", "牛客", 2, "数据库-中级", "数据库专项练习")
    # # 操作系统-初级 10套
    # for c in range(10):
    #     get_paper(25, 25)
    #     get_data("操作系统-初级", "牛客", 1, "操作系统-初级", "操作系统专项练习")
    # 操作系统-中级 10套
    # for c in range(2):
    #     get_paper(55, 25)
    #     get_data("操作系统-中级", "牛客", 2, "操作系统-中级", "操作系统专项练习")

    # 数据库-初级 10套
    for c in range(10):
        get_paper(25, 23)
        get_data("数据库-初级", "牛客", 1, "数据库-初级", "数据库专项练习")

if __name__ =='__main__':
    print("start")
    generate_data()




