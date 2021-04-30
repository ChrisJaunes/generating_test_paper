import pandas as pd


def data_cleaning(path, attr_mapping = {}, data_ignore = {}) -> None:
    a = pd.read_excel(path, sheet_name=0)
    b = pd.read_excel(path, sheet_name=1)
    c = pd.read_excel(path, sheet_name=2)
    d = pd.read_excel(path, sheet_name=3)
    e = pd.read_excel(path, sheet_name=4)
    # print(a, type(a))
    print(d, type(d))

    # 便于查找题目在原始文件中的序号
    a["题型序号"] = range(4, len(a)+4)
    b["题型序号"] = range(3, len(b)+3)
    c["题型序号"] = range(3, len(c)+3)
    d["题型序号"] = range(3, len(d)+3)
    e["题型序号"] = range(3, len(e)+3)

    # 由于编程题的特殊型，编程题不考虑知识点类型
    e["对应的知识点"] = "编程题"

    # 表连接
    pset = pd.concat([a, b, c, d, e])

    # 由于存在重复的题目，因此对于完全相同的题目进行去重处理，相同题目和选项只保留一个
    pset.drop_duplicates(subset=[r"题干", r"选择"], keep='first', inplace=True)

    # 增加列表示该试题是否被使用的次数
    pset["使用次数"] = 0

    # 由于有些极其类似的题目，但是些许差异无法被drop_duplicates去重， 使用data_ignore文件
    # Todo

    # 打印pset的属性
    print(pset.shape)
    print("=================================================================================================")
    print(set(list(pset[r"对应的知识点"])))

    # 由于各个来源的知识点不同，对其进行标准化处理
    pset[r"清洗以后的知识点"] = pset[r"对应的知识点"].map(attr_mapping)

    pset.to_excel(r"__cache__\problem_set.xlsx", encoding="utf8")

