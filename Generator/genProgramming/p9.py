import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("猜数字", """
小A 和 小B 在玩猜数字。
小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。
他们一共进行三次这个游戏，请返回 小A 猜对了几次？

输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。


示例 1：
输入:1 2 3 
     1 2 3
输出：3
解释：小A 每次都猜对了。


示例 2：
输入：2 2 3 
     3 2 1
输出：1
解释：小A 只猜对了第二次。


示例 3：
输入：2 2 3 
     3 1 2
输出：0
解释：小A一次也没有猜对


限制：
guess 的长度 = 3
answer 的长度 = 3
guess 的元素取值为 {1, 2, 3} 之一。
answer 的元素取值为 {1, 2, 3} 之一。
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int game(int[] guess, int[] answer) {
        int tmp =0;
        for(int i = 0;i < guess.length;i++){
            if(guess[i] == answer[i]){
                tmp++;
            }
        }
        return tmp;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] gue = new int[3];
        int[] ans = new int[3];
        for (int j = 0; j < 3; ++j){
            gue[j] = in.nextInt();
        }
        for (int k = 0; k < 3; ++k){
            ans[k] = in.nextInt();
        }
        System.out.println(game(gue, ans));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    print(" ".join([str(random.randint(1, 3)) for _ in range(1, 4)]), file=f)
    print(" ".join([str(random.randint(1, 3)) for _ in range(1, 4)]), file=f)
