import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("拿硬币", """
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。
我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。


示例 1：
输入：3
     4 2 1
输出：4
解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。



示例 2：
输入：3
     2 3 10
输出：8


示例 3：
输入：4
     7 5 3 1
输出：10



限制：
1 <= n <= 4
1 <= coins[i] <= 10
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int minCount(int[] coins) {
        int count = 0;
        for(int coin: coins){
            //右移一位相当于除以2，和1按位与相当于除2取余
            count += (coin >> 1) + (coin & 1);
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n =  in.nextInt();
        int[] coins = new int[n];
        for (int j = 0; j < n; ++j){
            coins[j] = in.nextInt();
        }
        System.out.println(minCount(coins));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 4)
    print(n, file=f)
    print(" ".join([str(random.randint(1, 10)) for _ in range(n)]), file=f)