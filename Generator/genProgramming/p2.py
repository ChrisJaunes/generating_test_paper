import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("一维数组的动态和", """
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。


示例 1：
输入：
4
1 2 3 4
输出：
1 3 6 10
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。


示例 2：
输入：
5
1 1 1 1 1
输出：
1 2 3 4 5
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。


示例 3：
输入：
5
3 1 2 10 1
输出：
3 4 6 16 17


提示：
1 <= nums.length <= 1000
-10^6<= nums[i] <=10^6
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
     static public int[] runningSum(int[] nums) {
        int[] a=new int[nums.length];
        int sum=0;
        for(int i=0;i<nums.length;i++){
            sum=sum+nums[i];
            a[i] = sum;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int length = in.nextInt();
        int temp[] = new int[length];
        for (int i = 0; i < length; ++i){
            temp[i] = in.nextInt();
        }
        int answer[] = runningSum(temp);
        int n = 0;
        while (n < length){
            System.out.print(answer[n]);
            System.out.print(" ");
            ++n;
        }
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 1000)
    print(n, file=f)
    s = " ".join([str(random.randint(1, n - 1)) for _ in range(1, n)])
    print(s, file=f)
