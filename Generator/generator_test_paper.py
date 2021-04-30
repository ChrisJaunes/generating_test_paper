import pandas as pd


def generator_single_test(pset_path: str, ptest_config: dict, seed: int = 10, num: int = 0) -> None:
    # 从execl中获取 试题集合
    pset = pd.read_excel(pset_path, sheet_name=0)
    assert isinstance(pset, pd.DataFrame)
    # print(pset, pset.head())
    # pset_used = pset[pset["使用次数"] == 0]

    # ptest 使用 试题集合 和 试卷配置 产生试卷
    ptest = pd.DataFrame()
    # ferr 报告缺失的试题
    ferr = open(f"__cache__/test_paper{num}.err", "w")

    # 遍历试卷配置
    for _, v in ptest_config.items():
        print(f"{_}: {v}")
        assert isinstance(v, dict)

        # 通过 清洗以后的知识点 和 使用次数 对其进行筛选， 筛选以后的试题为可以抽取的试题
        assert isinstance(v["清洗以后的知识点"], list)
        pset_filter = pset["清洗以后的知识点"] == v["清洗以后的知识点"][0]
        for i in v["清洗以后的知识点"]:
            pset_filter = pset_filter | (pset["清洗以后的知识点"] == i)
        pset_filter = pset_filter & (pset["使用次数"] == 0)
        # print(pset[pset_filter])
        # print(len(pset[pset_filter]))

        # 选取抽题策略
        policy = v["抽题策略"]
        assert isinstance(policy, dict)

        # 根据策略进行抽题
        for pk, pv in v["抽题策略"].items():
            view = pset[pset_filter & (pset["题型"] == pk)]
            # print(view)
            # print(view.sample(n=pv))
            assert isinstance(view, pd.DataFrame)
            if pv > len(view):
                print(f"[Error]| {_} | {pv} | {pv - len(view)}", file=ferr)
                pv = len(view)
            view = view.sample(n=pv, random_state=seed)
            assert isinstance(view, pd.DataFrame)
            # print(view)
            # print([i[0] for i in view.iterrows()])
            ptest = pd.concat([ptest, view[["题型", "题型序号", "难度", "对应的知识点", "清洗以后的知识点", "题干", "选择", "答案"]]])
            pset.loc[[i[0] for i in view.iterrows()], "使用次数"] += 1

    # 保存试卷
    ptest.to_excel(r"__cache__\test_paper{0}.xlsx".format(num), encoding="utf8")
    pset[1:].to_excel(r"__cache__\problem_set.xlsx", encoding="utf8")
