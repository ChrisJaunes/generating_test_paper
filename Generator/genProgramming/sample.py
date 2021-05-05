import os
import subprocess


class ProgrammingProblemDesc(object):
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def printDesc(self, path):
        path = os.path.join(path, "题目描述.txt")
        with open(path, "w") as fp:
            print(self.title, file=fp)
            print(self.desc, file=fp)


class ProgrammingProblemSTD(object):
    def __init__(self, lang, text):
        self.lang: str = lang
        self.text = text

    def printStd(self, path):
        if self.lang.startswith("C++"):
            path = os.path.join(path, "Solution.cpp")
        elif self.lang.startswith("Java"):
            path = os.path.join(path, "Solution.java")

        with open(path, "w") as fp:
            print(self.text, file=fp)

        if self.lang.startswith("C++"):
            subprocess.call(f'g++ -g {path} -o {path.strip("cpp").__add__("exe")}', shell=True)
        elif self.lang.startswith("Java"):
            subprocess.call(f'javac {path}', shell=True)
