import numpy.random as random
from sample import ProgrammingProblemDesc, ProgrammingProblemSTD


def generatorProblemDesc() -> ProgrammingProblemDesc:
    return ProgrammingProblemDesc("最富有客户的资产总量", """
给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的资产总量 。
客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。


示例 1：
输入：
2 3
1 2 3
3 2 1
输出：
6
解释：
第 1 位客户的资产总量 = 1 + 2 + 3 = 6
第 2 位客户的资产总量 = 3 + 2 + 1 = 6
两位客户都是最富有的，资产总量都是 6 ，所以返回 6 。


示例 2：
输入：
3 2
1 5
7 3
3 5
输出：
10
解释：
第 1 位客户的资产总量 = 6
第 2 位客户的资产总量 = 10 
第 3 位客户的资产总量 = 8
第 2 位客户是最富有的，资产总量是 10


示例 3：
输入：
3 3
2 8 7
7 1 3
1 9 5
输出：
17


限制
m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
    """)


def generatorProblemSTD() -> ProgrammingProblemSTD:
    return ProgrammingProblemSTD("Java", """
class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < accounts.length; i++) {
            int t = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                t += accounts[i][j];
            }
            ans = Math.max(ans, t);
        }
        return ans;
    }
}
    """)


def generatorProblemTestSingle(f, seed: int = 2021):
    random.seed(seed)
    n = random.randint(1, 50)
    m = random.randint(1, 50)
    print(n, m, file=f)
    s = "\n".join([" ".join([str(random.randint(1, 100)) for _ in range(m)]) for _ in range(n)])
    print(s, file=f)
