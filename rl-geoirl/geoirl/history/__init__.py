"""GeoIRL 论文复现包（IJGIS 2026, Lin / Grinberger / Felsenstein）。

模块的诞生日程写在 geoirl/README.md 里 —— 本包是**逐步长出来的**，
每个 Day 只往里加它当天真正需要的东西，不要在 Day01 就把六个文件建满。

职责边界（对应论文 §2.1 — §2.2）：

    geo_data.py   §2.1.2 / §2.1.3   矢量建筑 → 特征矩阵 F、SGS／IED 转移矩阵 P
    irl.py        §2.1 / §2.1.5     软 Bellman、中间策略 π（全项目唯一实现）
    esvf.py       §2.1.6            访问频率传播：朴素幂迭代与归一化稳定版
    rewards.py    §2.1.5            Linear / MLP / GCN / GraphConv 四种奖励网络
    sample.py     §2.2              K-M 折扣下的轨迹采样（马尔可夫链式）
    metrics.py    §3.4              Wasserstein、inverse CPC、NFM

使用方式：在 `rl-geoirl/` 目录内运行脚本，即可 `from geoirl.irl import soft_policy`。
"""

__all__ = ["geo_data", "irl", "esvf", "rewards", "sample", "metrics"]
