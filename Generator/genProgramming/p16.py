import random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("所有奇数长度子数组的和", """
给你一个正整数数组arr，请你计算所有可能的奇数长度子数组的和。
子数组 定义为原数组中的一个连续子序列。
请你返回 arr中 所有奇数长度子数组的和 。


示例 1：
输入：5
     1 4 2 5 3
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


示例 2：
输入：2
    1 2
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为3 。


示例 3：
输入3
    10 11 12
输出：66


提示：
1 <= arr.length <= 100
1 <= arr[i] <= 1000
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int sumOddLengthSubarrays(int[] arr) {
        int len = arr.length, res = 0;
        for(int i = 0; i < len; i ++){
            int LeftOdd = (i+1)/2, LeftEven = i/2+1;
            int RightOdd = (len-i)/2, RightEven = (len-1-i)/2+1;
            res += arr[i]*(LeftOdd*RightOdd + LeftEven*RightEven);
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int  n = in.nextInt();
        int[] arr = new int[n];
        for (int j = 0; j < n; ++j){
            arr[j] = in.nextInt();
        }
        System.out.println(sumOddLengthSubarrays(arr));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 100)
    print(n, file=f)
    print(" ".join([str(random.randint(1, 1000)) for _ in range(n)]), file=f)