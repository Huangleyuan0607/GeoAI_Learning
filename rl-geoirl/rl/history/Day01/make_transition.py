"""
需求：
    用面积与距离造出SGS转移矩阵：实现论文式(1)并观察现象
"""


# 导包
from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use('Agg')       # 不弹窗，直接存图
import matplotlib.pyplot as plt


# 1.实现式(1)：SGS_ij = V_i / D_ij²  (i != j)，再按行归一化
def gravity_transition(V, D, epsilon = 1e-9):
    """
    参数：
        V: (n, ) 建筑体量 / 面积，对应式(1)的 V_i
        D: (n, n) 质心距离矩阵，对角为 0
        epsilon = 1e-9: 一个极小的阈值，后面用来判断 "某行是否全为零"

    返回：
        P: (n, n) 行归一化转移矩阵，对角为 0，每行和为 1

    陷阱：
        对角 D = 0，直接 V_i / D ** 2 会 0/0 -> nan；
        nan 再参与行归一化会让整行变 nan。症状看起来像"学习算法坏了"，其实是这里没防住
        所以先把对角设成 inf（除出来是 0），再归一化
    """
    # 1.1 关键一行：如果 D[i, j] == 0（对应对角线，即自己到自己），就用 np.inf（无穷大）替换。否则保留 D[i, j] ** 2
    D_safe = np.where(D == 0, np.inf, D ** 2)       # 先把距离矩阵每个元素平方，得到D_ij²
    with np.errstate(divide = 'ignore', invalid = 'ignore'):        # 临时关闭 numpy 的除零/无效值警告。因为 inf 参与除法时，numpy 会打印警告。
        # V[:, None]：把 V 从形状 (n,) 升维成 (n, 1)，变成列向量
        # V[:, None] / D_safe：利用 numpy 的广播机制，让每一列的距离都除以对应行的V_i
        # 结果：SGS[i, j] = V[j] / D_safe[i, j] = V[j] / D[i, j]^2 （此处初步推断是因为论文笔误）
        SGS = V[None, :] / D_safe
    SGS = np.nan_to_num(SGS, nan = 0.0, posinf = 0.0, neginf = 0.0)     # 兜底清理：保证SGS矩阵均为有限实数，且对角线全是0

    # 1.2 行归一化“极端情况下某行可能全0（比如只剩一栋建筑），兜底退回均匀分布
    row = SGS.sum(axis = 1, keepdims = True)      # 对每行求和，得到每个建筑的“总引力”。同时保持形状为 (n, 1)，方便后面做广播除法。

    # np.where(row == 0, 1.0, row)：如果某行的和是0，用1.0代替（防止除零），否则保留原值。这一步是为了让后面的除法安全。
    # SGS / np.where(...)：
        # 正常行：SGS[i, j] / row[i] → 得到该行的归一化概率。
        # 和为0的行：SGS[i, j] / 1.0 → 反正SGS也全是0，结果还是 0（后面会被外层替换）。
    # np.where(row > epsilon, ..., 1.0 / (len(V) - 1))：
        # 如果某行总和 > epsilon（说明这行有有效引力），就用归一化的结果。
        # 如果某行总和 ≤ epsilon（说明这行全为0，极端情况比如只剩一栋建筑，或者某建筑完全孤立），就用 1.0 / (len(V) - 1) 作为兜底。
        # 兜底值的含义：均匀分布。既然不知道该去哪，那就“除了自己以外的所有建筑等概率去”。分母是 n - 1，正好排除了自己。
    P = np.where(row > epsilon, SGS / np.where(row == 0, 1.0, row), 1.0 / (len(V) - 1))

    np.fill_diagonal(P, 0.0)        # 强制把对角线设回 0
    return P / P.sum(axis = 1, keepdims = True)     # 填充后再归一化一次，保证每行严格为1（因为对角线设0后行和不为0了）


# 2.自造一座 "城市"：坐标均匀，面积对数正态（真实建成环境是长尾的，不是正态）
# 参1：建筑数；参2：城市边长extent；参3：随机种子
def make_fake_city(n = 1014, extent_km = 3.0, seed = 7):
    rng = np.random.default_rng(seed)       # 固定随机种子

    # 2.1 坐标：3km x 3km，单位用米，让D与论文量级可比
    # 把 1014 栋建筑均匀地撒在 3km × 3km 的正方形地块上。
    xy = rng.uniform(0.0, extent_km * 1000.0, size = (n, 2))        #在0到3000米之间，均匀随机地生成n个点的坐标

    # 2.2 面积：对数正态 -> 长尾，少数大楼占走大部分体量
    # 给每栋建筑分配一个面积，这里用了一个非常讲究的对数正态分布
    # mean = np.log(200.0)：对数正态分布的均值，转换回正常尺度后，面积的"中位数"是200m²。即有一半建筑小于200m²，一半大于200m²。
    # sigma = 0.8：形状参数。数值越大，"长尾"越明显（极端大楼越夸张）。0.8 是一个比较符合现实城市建筑分布的经验值。
    # 结果：大部分建筑面积在100~400m²之间，但有极少数建筑会大到几千甚至上万m²（比如商场、写字楼）。
    areas = rng.lognormal(mean = np.log(200.0), sigma = 0.8, size = n)      # 单位：m²

    # 2.3 两两质心欧氏距离（对称，对角为0）
    # xy[:, None, :]：把坐标矩阵 (n, 2) 升维成 (n, 1, 2)。
    # xy[None, :, :]：把坐标矩阵升维成 (1, n, 2)。
    # 两者相减，利用 numpy 的广播机制，得到一个形状为 (n, n, 2) 的三维矩阵。
    # 这个三维矩阵里，diff[i, j] 就是第 i 栋建筑和第 j 栋建筑的坐标差值 (Δx, Δy)。
    diff = xy[:, None, :] - xy[None, :, :]

    # diff ** 2：把坐标差值平方。
    # .sum(axis = -1)：把 x 方向和 y 方向的平方和加起来，得到距离的平方 (Δx² + Δy²)。
    # np.sqrt(...)：开根号，得到欧氏距离。这是初中数学的“勾股定理”。
    # 最终 D 是一个 (n, n) 的矩阵，D[i, j] 表示第 i 栋建筑和第 j 栋建筑的实际距离（单位：米）。
    D = np.sqrt((diff ** 2).sum(axis = -1))
    np.fill_diagonal(D, 0.0)        # 强制把对角线设回 0
    return xy, areas, D


# 3.测试
if __name__ == '__main__':
    n = 1014
    xy, areas, D = make_fake_city(n)

    print("=" * 60)
    print("自造城市")
    print("=" * 60)
    print(f"建筑数                   {n}")
    print(f"面积 min / 中位 / max            {areas.min():.1f} / {np.median(areas):.1f} / {areas.max():.1f} m²")
    print(f"面积 max / min（长尾倍数）        {areas.max() / areas.min():.0f}x")
    print(f"距离矩阵对角全为0                 {bool(np.allclose(np.diag(D), 0.0))}")
    print(f"距离矩阵对称                     {bool(np.allclose(D, D.T))}")

    P = gravity_transition(areas, D)

    print()
    print("=" * 60)
    print("SGS转移矩阵自检")
    print("=" * 60)
    print(f"P形状                  {P.shape}")
    print(f"行和全为1               {bool(np.allclose(P.sum(axis = 1), 1.0))}")
    print(f"行和 min / max         {P.sum(axis = 1).min():.12f} / {P.sum(axis = 1).max():.12f}")
    print(f"对角全为0               {bool(np.allclose(np.diag(P), 0.0))}")
    print(f"含nan                  {bool(np.isnan(P).any())}")
    print(f"矩阵密度                {(P > 0).mean():.3f}")

    # 3.1 现象一：被最想去的建筑，是不是大楼？
    inflow = P.sum(axis = 0)
    rank = np.argsort(inflow)[::-1]
    area_pct = (areas[rank[:20]] < areas[:, None]).mean(axis = 0)        # top20的面积分位
    print()
    print("=" * 60)
    print("被最想去的 top-20 建筑：面积分位（1.0 = 全场最大）")
    print("=" * 60)
    print(f"平均面积分位               {area_pct.mean():.3f}")
    print(f"最小面积分位               {area_pct.min():.3f}")
    print(f"top-1 建筑：面积 {areas[rank[0]]:.0f} m² / 入流 {inflow[rank[0]]:.4f}")

    # 3.2 现象二：面积五分位 vs 平均入流
    q = np.quantile(areas, [0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    idx = np.clip(np.searchsorted(q, areas, side = 'right') - 1, 0, 4)
    print()
    print("=" * 60)
    print("面积五分位 vs 平均入流")
    print("=" * 60)
    print(f"{'档':<4}{'面积区间(m²)':<18}{'建筑数':>8}{'平均入流':>8}{'入流占比':>8}")
    for k in range(5):
        m = idx == k
        share = inflow[m].sum() / inflow.sum()
        print(f"Q{k + 1:<3}{q[k]:>9.0f} - {q[k + 1]:<11.0f}{m.sum():>8}{inflow[m].mean():>12.5f}{share:>9.1%}")

    # 3.3 现象3：出图
    fig, axes = plt.subplots(1, 2, figsize = (13, 5))

    axes[0].hist(areas, bins = 60, color = '#4C78A8', edgecolor = 'white')
    axes[0].set_yscale('log')
    axes[0].set_xlabel('building area (m²)')
    axes[0].set_ylabel('count (log)')
    axes[0].set_title('Area distribution: lognormal long tail')

    axes[1].scatter(areas, inflow, s=6, alpha=0.35, color='#E45756')
    axes[1].set_xscale('log')
    axes[1].set_xlabel('building area (m², log)')
    axes[1].set_ylabel('inflow = column sum of P')
    axes[1].set_title('Bigger building -> more inflow')

    fig.suptitle('G01 | SGS transition matrix from area x distance (n=1014, synthetic)')
    fig.tight_layout()
    # 锚定到脚本所在目录：这样无论 PyCharm 的工作目录设成什么，图都落在 rl/Day01/，
    # 不会被丢到仓库根（相对路径 savefig 是 IDE 里最常见的"图找不到了"来源）
    out = Path(__file__).resolve().parent / 'sgs_area_vs_inflow.png'
    fig.savefig(out, dpi=130)
    print()
    print(f"图已保存：{out}")

    # 一句话结论（写进笔记）：SGS_ij = V_i / D_ij² 只跟出发地面积和距离有关，
    # 行归一化后面积大的建筑在所有出发地里都拿到更大的分子，于是列和必然更高 ——入流随面积单调上升不是巧合，
    # 是式(1) 把面积直接编码进了转移矩阵。