import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("好数对的数目", """
给你一个整数数组 nums。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
返回好数对的数目。


示例 1：
输入：
6
1 2 3 1 1 3
输出：
4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始


示例 2：
输入：
4
1 1 1 1
输出：
6
解释：数组中的每组数字都是好数对


示例 3：
输入：
3
1 2 3
输出：0



提示：
1 <= nums.length <= 100
1 <= nums[i] <= 100
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int numIdenticalPairs(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[i] == nums[j]) {
                    ++ans;
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int len = in.nextInt();
        int[] num = new int[len];
        for (int j = 0; j < len; ++j){
                num[j]= in.nextInt();
        }
        System.out.println(numIdenticalPairs(num));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 100)
    print(n, file=f)
    print(" ".join([str(random.randint(1, 100)) for _ in range(100)]), file=f)

