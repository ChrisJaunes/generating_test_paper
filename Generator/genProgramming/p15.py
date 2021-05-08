import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("统计一致字符串的数目", """
给你一个由不同字符组成的字符串allowed和一个字符串数组words。
如果一个字符串的每一个字符都在 allowed中，就称这个字符串是 一致字符串 。
请你返回words数组中一致字符串 的数目。


示例 1:
ab 
5
ad bd aaab baa badab
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。


示例 2：
abc 
7
a b c ab ac bc abc
输出：7
解释：所有字符串都是一致的。


示例 3：
cad 
8
cc acd b ba bac bad ac d
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。


提示：
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
allowed中的字符 互不相同。
words[i] 和allowed只包含小写英文字母。
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> set = new HashSet<>();
        int num = 0;
        for (int i = 0;i < allowed.length();i++)
            set.add(allowed.charAt(i));
        for (int i = 0;i < words.length;i++){
            for (int j = 0;j < words[i].length();j++){
                if (!set.contains(words[i].charAt(j))) break;
                if (j == words[i].length()-1) num++;
            }
        }
        return num;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String all = in.next();
        int  n = in.nextInt();
        String[] word = new String[n];
        for (int j = 0; j < n; ++j){
            word[j] = in.next();
        }
        System.out.println(countConsistentStrings(all, word));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    print("".join([random.choice(string.ascii_lowercase) for _ in range(1, 26)]), file=f)
    n = random.randint(1, 104)
    print(n, file=f)
    for i in range(n):
        print("".join([random.choice(string.ascii_lowercase) for _ in range(1, 10)]), file=f)
