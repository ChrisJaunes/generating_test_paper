import random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("有多少小于当前数字的数字", """
给你一个数组nums，对于其中每个元素nums[i]，
请你统计数组中比它小的所有数字的数目。
换而言之，对于每个nums[i]你必须计算出有效的j的数量，
其中 j 满足j != i 且 nums[j] < nums[i]。
以数组形式返回答案。


示例 1：
输入：5
    8 1 2 2 3
输出：4 0 1 1 3
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。


示例 2：
输入：4
    6 5 4 8
输出：2 1 0 3


示例 3：
输入：4
    7 7 7 7
输出：0 0 0 0


提示：
2 <= nums.length <= 500
0 <= nums[i] <= 100
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (nums[j] < nums[i]) {
                    cnt++;
                }
            }
            ret[i] = cnt;
        }
        return ret;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int  n = in.nextInt();
        int[] arr = new int[n];
        for (int j = 0; j < n; ++j){
            arr[j] = in.nextInt();
        }
        int ans[] = new int[n];
        ans = smallerNumbersThanCurrent(arr);
        for (int k = 0; k < n; ++k){
            System.out.print(ans[k]);
            System.out.print(" ");
        }
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(2, 500)
    print(n, file=f)
    print(" ".join([str(random.randint(0, 100)) for _ in range(n)]), file=f)