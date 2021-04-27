from Generator import *
from data_cleaning import *


def test_generator():
    generator(r"..\DataBase\problem_set_std1.CSV")


def test_data_cleaning():
    data_cleaning(r"..\DataBase\problem_set_java.xls")


if __name__ == '__main__':
    # test_generator()
    test_data_cleaning()

