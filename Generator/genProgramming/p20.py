import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("统计位数为偶数的数字", """
给你一个整数数组nums，请你返回其中位数为偶数的数字的个数。


示例 1：
输入：5 
     12 345 2 6 7896
输出：2
解释：
12 是 2 位数字（位数为偶数）
345 是 3 位数字（位数为奇数）
2 是 1 位数字（位数为奇数）
6 是 1 位数字 位数为奇数）
7896 是 4 位数字（位数为偶数）
因此只有 12 和 7896 是位数为偶数的数字


示例 2：
输入：4
     555 901 482 1771
输出：1 
解释： 
只有 1771 是位数为偶数的数字。


示例 3：
输入：3
     235  32 546
输出：1 
解释： 
只有 32 是位数为偶数的数字。


提示：
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int findNumbers(int[] nums) {
        int res=0;
        int tmp=1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<10){
                continue;
            }
            if(nums[i]>10){
                while(nums[i]/10 > 0){
                    tmp++;
                    nums[i]=nums[i]/10;
                }
                if(tmp % 2 ==0){
                    res++;
                }
            }
            tmp=1;
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int  n = in.nextInt();
        int num[] = new int[n];
        for (int j = 0; j < n; ++j){
            num[j] = in.nextInt();
        }
        System.out.println(findNumbers(num));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(0, 500)
    print(n, file=f)
    print(" ".join([str(random.randint(1, 100000)) for _ in range(n)]), file=f)

