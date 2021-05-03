import pandas as pd
import data_cleaning


def generator(path: str):
    """
    作为试题应该提供的属性：类型、知识点、难度、能力范畴
    考虑试卷质量的指标：
        试题类型分布符合试卷题型分布要求
        试题知识点符合试卷知识点要求
        试题知识点分布符合试卷要求
        试题难度符合试卷要求
    其中：
        对于试题集，筛选符合试卷知识点要求是比较容易的
    :param path:
    :return:
    """
    c = pd.read_csv(path, encoding="utf8")
    # print(type(c))    dataframe
    print(c[c[r"初级"] == "Yes"][{r"知识点", r"能力范畴"}])
