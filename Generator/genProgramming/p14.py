import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("整数的各位积和之差", """
给你一个整数n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。


示例 1：
输入：234
输出：15 
解释：
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15


示例 2：
输入：4421
输出：21
解释： 
各位数之积 = 4 * 4 * 2 * 1 = 32 
各位数之和 = 4 + 4 + 2 + 1 = 11 
结果 = 32 - 11 = 21


提示：
1 <= n <= 10^5
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int subtractProductAndSum(int n) {
        int tmp=0;
        int tmp2=1;
        while(n>0){
            tmp2 =tmp2 *(n%10);
            tmp +=n%10;
            n=n/10;
        }
        return tmp2 - tmp;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(subtractProductAndSum(n));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 100000)
    print(n, file=f)