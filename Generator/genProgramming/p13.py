import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("判断句子是否为全字母句", """
全字母句 指包含英语字母表中每个字母至少一次的句子。
给你一个仅由小写英文字母组成的字符串 sentence ，
请你判断sentence 是否为全字母句 。
如果是，返回 true ；否则，返回 false 。


示例 1：
输入：thequickbrownfoxjumpsoverthelazydog
输出：true
解释：sentence 包含英语字母表中每个字母至少一次。


示例 2：
输入：leetcode
输出：false


提示：
1 <= sentence.length <= 1000
sentence 由小写英语字母组成

    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public boolean checkIfPangram(String sentence) {
        int res = 0;
        for ( char c : sentence.toCharArray()) {
            res |= 1 << (c - 'a');
            if ((res ^ 0x3ffffff) == 0) {
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String sentence = in.next();
        System.out.println(checkIfPangram(sentence));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 1000)
    print("".join([random.choice(string.ascii_lowercase) for _ in range(n)]), file=f)
