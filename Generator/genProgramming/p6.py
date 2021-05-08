import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("数组元素积的符号", """
已知函数signFunc(x) 将会根据 x 的正负返回特定值：
如果 x 是正数，返回 1 。
如果 x 是负数，返回 -1 。
如果 x 是等于 0 ，返回 0 。
给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。
返回 signFunc(product) 。


示例 1：
输入：7
     -1 -2 -3 -4 3 2 1
输出：1
解释：数组中所有值的乘积是 144 ，且 signFunc(144) = 1


示例 2：
输入：5
     1 5 0 2 -3
输出：0
解释：数组中所有值的乘积是 0 ，且 signFunc(0) = 0


示例 3：
输入：5
     -1 1 -1 1 -1
输出：-1
解释：数组中所有值的乘积是 -1 ，且 signFunc(-1) = -1


提示：
1 <= nums.length <= 1000
-100 <= nums[i] <= 100
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int arraySign(int[] nums) {
        int temp=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<0){
                temp++;
            }
            if(nums[i]>0){
                continue;
            }
            if(nums[i]==0){
                return 0;
            }
        }
        if(temp%2==0){
            return 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner i  new Scanner(System.in);
        int le  in.nextInt();
        int[] num = new int[len];
        for (int j = 0; j < len; ++j){
                num[j]= in.nextInt();
        }
        System.out.println(arraySign(num));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 1000)
    print(n, file=f)
    print(" ".join([str(random.randint(-100, 100)) for _ in range(1, n + 1)]), file=f)
