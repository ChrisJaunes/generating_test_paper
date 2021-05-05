import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("左旋转字符串", """
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


示例 1：
输入: 
abcdefg 2
输出:
cdefgab


示例 2：
输入: 
lrloseumgh 6
输出: 
umghlrlose


限制：
1 <= k < s.length <= 10000
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
class Solution {
    static public String reverseLeftWords(String s, int n) {
        return s.substring(n, s.length()) + s.substring(0, n);
    }
    static public void main(String[] argv) throws IOException{
        Scanner cin = new Scanner(System.in);
        String s = cin.next();
        int n = Integer.valueOf(cin.next());
        System.out.print(reverseLeftWords(s, n));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(5, 10000)
    print("".join([random.choice(string.ascii_letters) for _ in range(n)]), file=f)
    print(random.randint(1, n - 1), file=f)