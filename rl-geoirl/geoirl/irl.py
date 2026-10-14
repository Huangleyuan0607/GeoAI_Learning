"""
geoirl/irl.py — 硬/软 Bellman 的唯一实现（G03 诞生）

对应论文 §2.1（MDP 定义）与 §2.1.5（中间策略是最大熵软策略）。
规矩：Day05/06/07/08/10/16 一律从这里 import，禁止复制第二份实现。
"""


# 导包
import numpy as np


# 1.数值稳定的逐行logsumexp（每行一个状态，先减行最大值再取指数）
