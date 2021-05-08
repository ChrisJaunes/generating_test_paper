import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("重新排列数列", """
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。


示例 1：
输入：6
     2 5 1 3 4 7  
     3
输出：2 3 5 4 1 7 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]


示例 2：
输入：8
      1 2 3 4 4 3 2 1 
      4
输出： 1 4 2 3 3 2 4 1


示例 3：
输入：4
     1 1 2 2  
     2
输出：1 2 1 2


提示：
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int[] shuffle(int[] nums, int n) {
        int[] res = new int[nums.length];
        int index = 0;
        //按照题意分别添加元素
        for(int i = 0;i < nums.length/2;i++){
            res[index++] = nums[i];
            res[index++] = nums[i + n];
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner in =  new Scanner(System.in);
        int len = in.nextInt();
        int[] num = new int[len];
        for (int j = 0; j < len; ++j){
            num[j]= in.nextInt();
        }
        int n = in.nextInt();
        int[] answer = new int[len];
        answer = shuffle(num, n);
        for (int k = 0; k < len; ++k){
            System.out.print(answer[k]);
            System.out.print(" ");
        }
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(2, 500)
    if (n % 2):
        --n
    print(n, file=f)
    print(" ".join([str(random.randint(1, 1000)) for _ in range(1, n + 1)]), file=f)
    print(int(n/2), file=f)