import random
import string
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("宝石与石头", """
给定字符串J代表石头中宝石的类型，和字符串S代表你拥有的石头。S中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J中的字母不重复，J和S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。


示例 1:
输入: 
aA
aAAbbbb
输出: 
3


示例 2:
输入: 
z
ZZ
输出: 0


限制：
S和J最多含有50个字母。
J中的字符不重复。
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
import java.io.*;
import java.util.*;
public class Solution {
    static public int numJewelsInStones(String jewels, String stones) {
        int jewelsCount = 0;
        int jewelsLength = jewels.length(), stonesLength = stones.length();
        for (int i = 0; i < stonesLength; i++) {
            char stone = stones.charAt(i);
            for (int j = 0; j < jewelsLength; j++) {
                char jewel = jewels.charAt(j);
                if (stone == jewel) {
                    jewelsCount++;
                    break;
                }
            }
        }
        return jewelsCount;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String jew;
        String sto;
        jew = in.next();
        sto = in.next();
        System.out.println(numJewelsInStones(jew, sto));
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    jn = random.randint(1, 50)
    print("".join(random.sample(string.ascii_letters, jn)), file=f)
    sn = random.randint(1, 50)
    print("".join([random.choice(string.ascii_letters) for _ in range(sn)]), file=f)
