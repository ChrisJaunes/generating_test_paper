import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("将数字用字符代替", """
给你一个下标从 0开始的字符串 s，它的偶数下标处为小写英文字母，奇数下标处为数字。
定义一个函数shift(c, x)，其中c是一个字符且x是一个数字，函数返回字母表中c后面第 x个字符。
比方说，shift('a', 5) = 'f'和shift('x', 0) = 'x'。
对于每个 奇数下标i，你需要将数字s[i] 用shift(s[i-1], s[i])替换。
请你替换所有数字以后，将字符串 s返回。题目 保证shift(s[i-1], s[i])不会超过 'z'。


示例 1：
输入：a1c1e1
输出：abcdef
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'


示例 2：
输入：a1b2c3d4e
输出：abbdcfdhe
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'


提示：
1 <= s.length <= 100
s只包含小写英文字母和数字。
对所有 奇数 下标处的i，满足shift(s[i-1], s[i]) <= 'z'。

    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public String replaceDigits(String s) {
        char[] a=s.toCharArray();
        char temp='a';
        for(int i=0;i<a.length;i++){
            if(a[i] <48 || a[i] >57 ){
                temp=a[i];
            }else{
                a[i] = (char)(temp + Integer.parseInt(a[i]+""));
            }
        }
        return String.valueOf(a);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        System.out.println(replaceDigits(s));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 100)
    mix_string = []
    for i in range(n):
        if i % 2:
            mix_string.append(random.sample('0123456789', 1)[0])
        else:
            mix_string.append(random.choice(string.ascii_lowercase))
    print("".join(temp for temp in mix_string), file=f)

