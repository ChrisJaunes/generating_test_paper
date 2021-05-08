import random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("把数字变成0的操作次数", """
给你一个非负整数num，请你返回将它变成 0 所需要的步数。 
如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。


示例 1：
输入：14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。


示例 2：
输入：8
输出：4
解释：
步骤 1） 8 是偶数，除以 2 得到 4 。
步骤 2） 4 是偶数，除以 2 得到 2 。
步骤 3） 2 是偶数，除以 2 得到 1 。
步骤 4） 1 是奇数，减 1 得到 0 。


示例 3：
输入：123
输出：12


提示：
0 <= num <= 10^6
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int numberOfSteps (int num) {
        int tmp =0;
        while(num>0){
            if(num % 2 ==0){
                num=num/2;
                tmp++;
            }else{
                num =num-1;
                tmp++;
            }
        }
        return tmp;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int  n = in.nextInt();
        System.out.println(numberOfSteps(n));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(0, 1000000)
    print(n, file=f)
