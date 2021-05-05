from sample import *
import p1
import p2
import p3
import p4
import p5


def generatorProblem(m, path: str, num: int = 10):
    # 生成测试数据文件夹
    path_test = os.path.join(path, "用例")
    os.makedirs(path_test, exist_ok=True)

    # 生成题目描述
    desc: ProgrammingProblemDesc = m.generatorProblemDesc()
    desc.printDesc(path)

    # 生成标程
    std: ProgrammingProblemSTD = m.generatorProblemSTD()
    std.printStd(path)

    # 生成测试输入文件
    for i in range(num):
        with open(os.path.join(path_test, f"in{i}.txt"), "w") as fp:
            m.generatorProblemTestSingle(fp, i)

    # 生成测试输出文件
    # java Solution < "用例/in1.txt" > "用例/out1.txt"
    pass


if __name__ == "__main__":
    generatorProblem(p3, "../__cache__/编程题/p3")
    for i in range(1, 6):
        eval(f'generatorProblem(p{i}, "../__cache__/编程题/p{i}")')
