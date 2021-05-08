import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("检查两个字符串数组是否相等", """
给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；
否则，返回 false 。
数组表示的字符串是由数组中的所有元素 按顺序 连接形成的字符串。


示例 1：
输入：2 2
     ab  c
     a  bc
输出：true
解释：
word1 表示的字符串为 "ab" + "c" -> "abc"
word2 表示的字符串为 "a" + "bc" -> "abc"
两个字符串相同，返回 true


示例 2：
输入：2 2
     a  cb  
     ab  c
输出：false


示例 3：
输入： 3 1
    abc  d  defg
    abcddefg
输出：true


提示：
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] 和 word2[i] 由小写字母组成
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuffer  s1 = new StringBuffer();
        StringBuffer s2 =new StringBuffer();
        for(int i=0;i<word1.length;i++){
            s1.append(word1[i]);
        }
        for(int i=0;i<word2.length;i++){
            s2.append(word2[i]);
        }
        if(new String(s1).equals(new String(s2))){
            return true;
        }
        return false;

    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int size1 = in.nextInt();
        int size2 = in.nextInt();
        String[] word1 = new String[size1];
        String[] word2 = new String[size2];
        for (int j = 0; j < size1; ++j) {
            word1[j] = in.next();
        }
        for (int k = 0; k < size2; ++k){
            word2[k] = in.next();
        }
        System.out.println(arrayStringsAreEqual(word1, word2));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(0, 103)
    m = random.randint(0, 103)
    print(n, file=f)
    print(m, file=f)
    for i in range(n):
        print("".join([random.choice(string.ascii_lowercase) for _ in range(103)]), file=f)
    for i in range(m):
        print("".join([random.choice(string.ascii_lowercase) for _ in range(103)]), file=f)


