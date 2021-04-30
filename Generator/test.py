from Generator import *
from data_cleaning import *
from generator_test_paper import *
from format_test_paper import *
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def test_generator():
    generator(r"..\DataBase\problem_set_std1.CSV")


def test_data_cleaning():
    # f = open(r'__cache__\problems_set.yml', 'w', encoding='utf-8')
    # print(yaml.safe_dump(type_change, f, allow_unicode=True))
    f = open(r'..\DataBase\problems_set_attr_mapping.yml', 'r', encoding='utf-8')
    attr_mapping = yaml.safe_load(f)
    data_ignore = [65, 66]
    # print(attr_mapping, type(attr_mapping))
    data_cleaning(r"..\DataBase\problem_set_java.xls", attr_mapping)

    # print(pset)

    # for i in set(list(tab[r"对应的知识点"])):
    #     if i not in type_change:
    #         type_change[i] = ""
    # print(type(type_change))
    # for k, v in type_change.items():
    #     print(f' "{k}" : "{v}" , ')

    # for i in set(list(tab[r"清洗以后的大类知识点"])):
    #     for j in set(list(tab[tab[r"清洗以后的大类知识点"] == i][r"对应的知识点"])):
    #         print(f'| {j} | {len(tab[tab[r"对应的知识点"] == j])} | {dict(tab[tab[r"对应的知识点"] == j].groupby("题型").size())} | {dict(tab[tab[r"对应的知识点"] == j].groupby("难度").size())}')
    #     print(f'| {i} | {len(tab[tab[r"清洗以后的大类知识点"] == i])} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("题型").size())} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("难度").size())}')

    # i = "Java基础"
    # for j in set(list(tab[tab[r"清洗以后的大类知识点"] == i][r"对应的知识点"])):
    #     print(f'| {j} | {len(tab[tab[r"对应的知识点"] == j])} | {dict(tab[tab[r"对应的知识点"] == j].groupby("题型").size())} | {dict(tab[tab[r"对应的知识点"] == j].groupby("难度").size())}')
    # print(f'| {i} | {len(tab[tab[r"清洗以后的大类知识点"] == i])} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("题型").size())} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("难度").size())}')
    #

    # print(tab.groupby(["清洗以后的大类知识点", "对应的知识点", "题型"]).size())
    # print(tab.groupby(["清洗以后的大类知识点", "对应的知识点", "题型"]).get_group(("网络编程", "网络编程", "单选题")))

    # print(len(pset[pset[r"清洗以后的大类知识点"] == "网络编程"]))

    # for i in set(list(c[r"清洗以后的大类知识点"])):
    #     if isinstance(i, float): continue
    #     print((i, len(c[c[r"清洗以后的大类知识点"] == i])))
    #     c[c[r"清洗以后的大类知识点"] == i].to_csv(i + ".csv", encoding="utf8")
    # for i in set(list(c[r"对应的知识点"])):
    #     print("'{0}':'',".format(i))
    # print(pset[pset[r"对应的知识点"] == "事务管理方式"].values)


def test_generator_test_paper():
    f = open(r'..\DataBase\problems_set_request1.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 1)
    format_test_paper(1)

    f = open(r'..\DataBase\problems_set_request1.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 2)
    format_test_paper(2)

    f = open(r'..\DataBase\problems_set_request1.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 3)
    format_test_paper(3)

    f = open(r'..\DataBase\problems_set_request1.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 4)
    format_test_paper(4)

    f = open(r'..\DataBase\problems_set_request1.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 5)
    format_test_paper(5)

    f = open(r'..\DataBase\problems_set_request2.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 6)
    format_test_paper(6)

    f = open(r'..\DataBase\problems_set_request2.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 7)
    format_test_paper(7)

    f = open(r'..\DataBase\problems_set_request2.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 8)
    format_test_paper(8)

    f = open(r'..\DataBase\problems_set_request2.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 9)
    format_test_paper(9)

    f = open(r'..\DataBase\problems_set_request2.yml', 'r', encoding='utf-8')
    request = yaml.safe_load(f)
    generator_single_test(r"__cache__\problem_set.xlsx", request, 10, 10)
    format_test_paper(10)


if __name__ == '__main__':
    # test_generator()
    test_data_cleaning()
    # test_generator_test_paper()

