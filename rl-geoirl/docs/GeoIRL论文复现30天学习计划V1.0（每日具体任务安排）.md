# 《GeoIRL 论文复现30天学习计划 V1.0》

## 每日具体任务安排表

> **计划版本说明（V1.0 · 2026.09.29）**
>
> **任务来源**：导师要求**一个月内**完成论文复现。目标论文为
> Zi Hen Lin, A. Yair Grinberger, Daniel Felsenstein, *Generating geospatial trajectories with incomplete data using graph inverse reinforcement learning*, **IJGIS**, 2026（DOI: 10.1080/13658816.2026.2658065，PDF 见 `../../papers/`）。
>
> **有效学习日约束**：国庆（10.01—10.07）不在校，正经学习时间只有 **09.30（周三）＋ 10 月工作日，共 18 个学习日**。假期只安排"纯看不写"的碎片任务。
>
> **唯一主线**（不按"强化学习完整课程"学）：
>
> ```text
> MDP → 价值与 Bellman → 值/策略迭代（矩阵幂迭代）
>     → IRL → MaxEnt IRL → 软策略与 ESVF
>     → 转移矩阵 / 图与 Laplacian → GCN / GraphConv
>     → 论文四件套（Feature / Transition / Reward / Policy）→ 复现报告
> ```
>
> **目录约定**：`rl-geoirl/rl/DayNN/` 放每日 demo；`rl-geoirl/geoirl/` 放可复用的包；`rl-geoirl/notes/GNN（日期）Note.md` 放每日计划与日志；截图放 `rl-geoirl/notes/Screenshot/GNN/`。
>
> **本计划正文不附代码**：每天只给"创建哪些文件 ＋ 每个文件要实现什么 ＋ 验收判据"。需要实现参考时按当天需求单独索取。
>
> **与《GeoAI预研60天学习计划 V4.0》的衔接**：Day44/45 暂停；Day46—48 的核心 KPI（最简 GAN）已于 2026.09.29 完成；Day49—52 GAN 先修（导师 2026.09.30 更正为 **C-GAN＋流模型**，原 CycleGAN 取消）移到国庆碎片时间；Day53—62 U-Net 顺延 2026.11；Day63—74 顺延或放弃；`矩阵论`课程继续上（与 G02／G08／G11 同步）；LeetCode 降频为每周 3 次。
>
> **三条铁律**：① 学一点立刻复现一点；② **10.08 起理论输入换轨**：主线改为"官方代码精读（`thirdparty/geoirl-official/`，每个函数对应论文一个公式）＋短文献精读（Ziebart 2008／Kipf & Welling 2017）"，每天 ≤55 分钟；③ 原视频清单（张伟楠／王琦／李宏毅／CS285／子豪兄／生存分析，合计约 7.8 h，附录 A）整体转为 **🎞 存档**——暂不看、不计任务与封顶，有空或卡壳时按存档行回看。《动手学强化学习》同步降为字典：卡壳才翻对应小节。
>
> **组会交付口径（10.08 合流）**：这趟要交的是三样东西——① **一张自己话画的流程图**（数据→特征→转移→奖励→策略→ESVF→采样→指标，不抄 Figure 1）；② **一组跑得出来的结果**（部分实验即可，证明动过手）；③ **一段能讲明白的知识点串讲**（四个必懂知识点见 Day18 口试自检）。组会考懂不懂，不考表格数量——敏感性实验不必全跑（附录 B 有压缩预案）。

------

## 阶段总览

| 阶段 | 日期 | 学习日 | 核心目标 | 关键产出 |
| --- | --- | --- | --- | --- |
| 一：MDP·价值·迭代 | 09.30—10.13 | Day01—Day05 | 建立 MDP 语言与"奖励→策略"的矩阵递推直觉 | `irl.py`、`esvf.py` 与三套 numpy 迭代实现 |
| 二：IRL·MaxEnt·ESVF | 10.14—10.20 | Day06—Day10 | 从"学行为"切换到"从行为反推奖励" | 从零实现的 6×6 MaxEnt IRL ＋ 发散复现实验 |
| 三：图·Laplacian·GNN | 10.21—10.26 | Day11—Day14 | 图结构进奖励函数，读懂论文 §2 | dense GCN 对齐 PyG ＋ 四种奖励网络 ＋ 骨架 |
| 四：数据·管线·报告 | 10.27—10.30 | Day15—Day18 | 全链路跑通并产出可交付结果 | 特征/转移矩阵、结果表、`REPRODUCE.md`、组会 PPT＋讲稿 |

> 时间预算：18 天 × 约 4.5 h ≈ 81 h，其中代码精读与短文献约 7 h（官方仓库 5 个 .py 共约 900 行＋Ziebart/Kipf 两篇短文＋data 三份 CSV）、写代码约 65 h、阅读与笔记约 9 h；视频 7.8 h 已转 🎞 存档，不计入必修进度。

------

## 国庆期间（10.01—10.07，不在校·不计学时的碎片任务）

### 任务目标

用旅途与睡前时间清掉两笔"只看不写"的债，把 10 月的整块时间全部留给代码。

### 碎片任务一：C-GAN 与流模型原理（约 4.5 小时）

> 导师 2026.09.30 更正：GAN 先修要补的是 **C-GAN 与流模型**，不再要 CycleGAN。

**C-GAN（约 2 小时）**

- - [ ] 读 Mirza & Osindero《Conditional Generative Adversarial Nets》（arXiv 1411.1784，4 页）：只搞懂标签 y 是怎么同时进 G 和 D 的
- - [ ] 李宏毅《机器学习2021》生成式对抗网络（三）生成器效能评估与条件式生成 `BV1By4y1A7K8`（50 min，只看条件式生成一节）

**流模型（约 2.5 小时）**

- - [ ] 什么是归一化流（中配）`BV1hu4y1H7xg`（12 min）：先建立"流＝一串可逆变换"的直觉
- - [ ] 标准化流与 INN `BV1Pm4y1X7yN`（30 min）：跟着推变量替换公式，记下"可逆＋Jacobian 易算＋堆叠出表达力"三条
- - [ ] 手推一个一维变量替换（写出 p(x) = p(z)·|dz/dx|），并用一句话说清耦合层为什么让 Jacobian 成了三角阵

笔记只回答三问（`rl-geoirl/notes/生成模型先修销账.md`）：条件标签分别从 G 和 D 的哪两处进入、加了标签为什么仍会模式坍塌；流模型要同时满足哪三条、得精确似然付了什么架构约束；GAN／流模型／本文 IRL 三条路线在"学分布→生成样本"谱系上各站哪。

### 碎片任务二：IRL 概念预热（约 1.4 小时）

- - [ ] 李宏毅 `BV1JA411c7VT` P34 逆向强化学习（27 min）
- - [ ] CS285 `BV1NjH4eYEyZ` P82 IRL Part 1（24 min）
- - [ ] CS285 `BV1NjH4eYEyZ` P83 Part 2（13 min）

只看不记公式，目标是让 Day06 开场时"IRL"不再是新词。

------

## 第一阶段：MDP、价值函数与迭代（Day01—Day05）

### 时间：2026.09.30—2026.10.13

### 阶段目标

> 用论文的实体（建筑、转移矩阵、奖励）建立 MDP 语言，而不是用"小车走迷宫"建立；
> 理解 Return、γ、V、Q、Bellman 递推；
> 把值迭代／策略迭代理解成**矩阵幂迭代**——这一步直接通向论文 §2.1.6；
> 会写 max 版与 soft（log-sum-exp）版两套更新式；
> 建立 `rl-geoirl/` 复现工程，与 V4.0 的 `pytorch/` 彻底分开。

------

# Day01（2026.09.30）

## 今日目标

复核已搭好的复现环境（G00＝09.29 完成），建立 MDP 五要素与论文实体的对应关系，跑通第一个转移矩阵。

## 今日任务

### 视频学习

#### 代码主线：《动手学强化学习》第 1、3 章（SJTU APEX·张伟楠／沈键／俞勇）

在线免费全文＋每章可跑 Notebook：`hrl.boyuai.com`；书源码 GitHub `boyu-ai/Hands-on-RL`

- - [x] 第 1 章 初探强化学习：通读（约 25 min）
- - [x] 第 3 章 马尔可夫决策过程：精读＋在线跑 notebook（约 45 min）——五要素在代码里各是哪一行，逐条对照今天的 `mdp_vocab.py`

#### 理论视频：张伟楠《上交强化学习课》（官方 UP「张伟楠SJTU」·课堂实录·与主线书同一作者逐讲对应）

- - [x] 第 1 讲 I 强化学习简介（36 min，`BV1jUHdePEUZ`）——先看片建整体框架，再读第 1 章
- - [x] 第 3 讲 I 马尔可夫决策过程（22 min，`BV1ZaHfekEyL`）——配今天精读第 3 章，符号与书完全一致

预计时长：书＋码约 1 小时，视频 58 分钟

> 卡壳回查（选看·不计封顶）：王琦《强化学习的数学原理》`BV1sd4y167NS` P1–P3——白板推导最细，概念抠不平时回看对应段。

看的时候不记 RL 定义，只做一件事：每出现一个术语，写下"它在这篇论文里是谁"。

### 理论学习

六个词的论文对应（必须手写一遍）：

| RL 术语 | 本论文中的实体 |
| --- | --- |
| State | 一栋建筑（图上节点），学习子集 1,014 栋 |
| Action | 从当前建筑前往另一栋建筑（＝矩阵该行的非零列） |
| Transition | SGS 行归一化后的转移矩阵 P（稀疏化到 10% 密度） |
| Reward | `W·F` 或 MLP/GCN/GraphConv 的输出——**待反演** |
| Policy | π(a\|s)，最终体现为"更新后的转移矩阵" |
| Episode | 一条 home-based tour（平均 4.92 个停留点） |

重点理解：**论文全程没有"智能体与环境试错"**。环境（转移矩阵）由面积与距离算出，要学的是奖励。这决定了后面绝大多数 RL 算法课对本文没用。

### 代码实验

创建：

```text
rl/Day01/
├── mdp_vocab.py
└── make_transition.py
```

实现要求（`mdp_vocab.py`）：

- 用 `dataclass` 描述论文的 MDP，字段：`n`（状态数）、`P`（n×n 行归一化转移矩阵）、`terminal`（n 维布尔，终止状态）、`expert_visits`（n 维，专家期望访问次数＝ESVF 观测版）、`F`（n×k 特征矩阵，reward＝W·F）
- 造一个 50 节点的随机 P 做自检：对角必须为 0、每行和必须为 1
- 打印：行和是否全为 1、对角是否全为 0、终止状态数
- 备注：`terminal` 此日用随机占位即可——论文训练用"非信息性"初/终态（§2.1.4），与生成阶段（§2.2）是两套设定，这个差异要留在心里

实现要求（`make_transition.py`）：

- 函数 `gravity_transition(V, D)`：实现论文式(1) `SGS_ij = V_i / D_ij²`（i＝j 时为 0），再按行归一化
- 陷阱：**对角不能直接除**，要用 `np.where(D == 0, np.inf, D**2)` 之类写法，否则 0/0 → nan → 整行 nan，后面所有现象都会被误认为"算法坏了"
- 自造数据：1,014 个二维点（模拟 3 km×3 km 城区）＋ 长尾面积（对数正态），算质心欧氏距离矩阵 D
- 产出三样：① 转移矩阵的两个自检（行和为 1、对角为 0）；② **面积五分位 vs 平均入流（列和）表**；③ 一张"面积 vs 入流"散点图存 `rl/Day01/sgs_area_vs_inflow.png`
- 判据：入流随面积档单调上升；能用一句话说清为什么必然如此

### 输出成果

- `rl/Day01/mdp_vocab.py`、`rl/Day01/make_transition.py`、`sgs_area_vs_inflow.png`
- `rl-geoirl/notes/G01（2026.09.30）Note.md`：手写六行对照表 ＋ 一段话回答"论文里有没有试错交互"
- 删除 `rl/Day01/.gitkeep`

### GitHub提交

```bash
git add rl-geoirl
git commit -m "G01: 完成MDP实体对照与SGS转移矩阵"
git push
```

## 今日成果验收

- - [x] 两个脚本都跑通，两个自检都为 True
- - [x] 五分位表呈现入流随面积单调上升，并能解释原因
- - [x] 不看资料写出六行对照表（误差 ≤ 1 项）
- - [x] 说得出"转移矩阵本身已经把面积编码进去了"这句话的含义

------

# Day02（2026.10.08）

## 今日目标

理解 Return 与折扣，掌握 Bellman 方程的**矩阵解**与**迭代解**两种求法。

## 今日任务

### 代码精读（主线·10.08 换轨）

- - [x] 读 `thirdparty/geoirl-official/causal_maxent.py` 的 `stochastic_value_iteration`（L8 起）——官方版值迭代只有十几行：找出 γ、收敛判据 `eps`、更新式各在哪一行，与今天 `value_bellman.py` 的迭代解逐行对照（约 20 min）

预计时长：约 20 分钟

> 🎞 **视频与读物存档（暂不看·有空或卡壳时回看）**
>
> - 《动手学强化学习》第 3 章后半"状态价值与动作价值""贝尔曼方程"小节（约 30 min）——书里 V 更新与 `value_bellman.py` 的矩阵解、迭代解逐行对上
> - 张伟楠 第 3 讲 II 马尔可夫决策过程（25 min，`BV1D2HfewEmk`）——Return、折扣、V／Q 与贝尔曼方程全在这里，与书同一套符号
> - 王琦 P4–P8（61 min 纯推导，想抠数学细节时回看）

### 理论学习

$$
G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots
$$

$$
V^\pi = R^\pi + \gamma P^\pi V^\pi
\quad\Longrightarrow\quad
V^\pi = (I - \gamma P^\pi)^{-1} R^\pi
$$

两个必须记住的事实：

1. Bellman 方程既是**线性方程组**（可直接解），也是**不动点迭代**（可反复代）——这正是 Day04 两种算法的同一来源；
2. 本文的 γ **不是超参**，而是 §2.2 用 Kaplan–Meier 生存概率算出的逐停留点折扣（Day17 兑现）。

### 代码实验

创建：

```text
rl/Day02/value_bellman.py
```

实现要求：

- 造 n＝40 的随机行归一化矩阵 P 与随机奖励向量 R（均值 0、方差 1）
- 解法一（解析）：`numpy.linalg.solve(I - γP, R)`
- 解法二（迭代）：`V ← R + γPV`，直到最大变化 < 1e-12，打印收敛轮数
- 打印两解的最大误差；打印 `numpy.linalg.eigvals(γP)` 的模最大值（谱半径）
- 判据：误差 < 1e-6；并能回答"谱半径与收敛条件的关系"——这是 Day08 发散的伏笔
- 附加：把行归一化矩阵换成"行和不为 1"的矩阵再跑一次，观察现象并解释（γP 的谱半径何时 ≥ 1）

### 输出成果

- `rl/Day02/value_bellman.py`
- 笔记：Bellman 的方程形式与矩阵形式各配一个 3×3 手推例

### GitHub提交

```bash
git commit -am "G02: Bellman 解析解与迭代解，谱半径判据"
```

## 今日成果验收

- - [x] 迭代解与解析解误差 < 1e-6
- - [x] 能说出 ρ(γP) 与收敛的关系，并用 `eigvals` 验证
- - [x] 知道本文 γ 来自生存分析而非人为设定

------

# Day03（2026.10.09）

## 今日目标

把 max 换成 log-sum-exp：从"最优策略"过渡到"最大熵软策略"。**今天写的函数是全项目唯一实现，之后所有天都复用它。**

## 今日任务

### 代码精读（主线·10.08 换轨）

- - [ ] 读 `thirdparty/geoirl-official/causal_maxent.py` 的 `local_causal_action_probabilities`（L65 起）——官方"软策略"：max 在哪一行被 log-sum-exp 顶替、归一化常数（配分函数）藏在哪一步；与今天 `soft_vs_hard_policy.py` 的 `soft_policy` 对照（约 25 min）

预计时长：约 25 分钟

> 🎞 **视频与读物存档（暂不看·有空或卡壳时回看）**
>
> - 《动手学强化学习》第 4 章前半"策略迭代"一节＋notebook（约 25 min）——硬 max 版长什么样，写软版前对照一次
> - 张伟楠 第 4 讲 动态规划（27 min，`BV1S2HfewEQa`）前半·策略迭代部分（约 13 min）
> - 刘相宇 `BV1pE41117C2` 全程（8 min，最大熵软 Q 的另一套讲法）
> - 王琦 P9–P12（策略改进与最优策略的推导）

### 理论学习

最优（硬）：

$$
Q^*(s,a) = r(s,a) + \gamma \max_{a'} Q^*(s',a')
$$

最大熵（软，目标 
$$
$\max_\pi \mathbb{E}\big[\sum_t r_t + \alpha H(\pi(\cdot|s_t))\big]$
$$
）：

$$
Q(s,a) = r(s,a) + \gamma \log \sum_{a'} e^{Q(s',a')},
\qquad
\pi(a\mid s) = \frac{e^{Q(s,a)}}{\sum_{a'} e^{Q(s,a')}}
$$

一句话抓区别：**max 让策略退化成 argmax 的确定性选择；log-sum-exp 让策略永远是一个分布。** 论文的"中间策略"是后者——所以它能生成**多样**轨迹而不是最短路，这正是论文 §1 要的"生成未见过的轨迹"。

### 代码实验

创建：

```text
rl/Day03/soft_vs_hard_policy.py
```

写好后把两个函数原样搬进 `geoirl/irl.py`：

| 函数 | 签名 | 职责 |
| --- | --- | --- |
| `hard_value_iteration` | `(P, r, gamma, iters) -> (V, pi)` | `V(s)=max_{s' 可达}[r(s')+γV(s')]`，π 为 one-hot |
| `soft_policy` | `(P, r, gamma=0.95, beta=1.0, iters) -> (pi, V)` | 软值迭代并返回策略矩阵 |

`soft_policy` 的实现要求（**这是全项目唯一的一份，后面 Day05/06/07/08/10/16 都 import 它**）：

- 递推式：$V(s) = \frac{1}{\beta}\log \sum_{s'} P(s'|s)\, e^{\beta[r(s') + \gamma V(s')]}$
- 策略：$\pi(s'|s) \propto P(s'|s)\, e^{\beta[r(s') + \gamma V(s')]}$
- 实现技巧：把 `log P` 直接加进指数里，一次性表达"哪些边允许＋转移概率多大"；零元素的 `log` 要先 `maximum(P, 1e-30)`
- 数值稳定：算 logsumexp 必须先减每行最大值，**不准出现 `exp(1000)` 这种溢出**
- 收敛判据：`|V_new − V|.max() < 1e-12`
- 本文件还要产出对比：β 取 0.2／1／5／50，打印每档的**平均策略熵**与**每行最大概率**，并与硬策略对照

### 输出成果

- `rl/Day03/soft_vs_hard_policy.py`
- `geoirl/irl.py`（含 `hard_value_iteration`、`soft_policy`，文件头注明对应论文 §2.1／§2.1.5）
- 笔记：硬／软 Bellman 两行公式对照，并写明本文用哪个、为什么

### GitHub提交

```bash
git commit -am "G03: 软/硬 Bellman 与 geoirl/irl.py 唯一实现"
```

## 今日成果验收

- - [ ] β 从 0.2 到 50，策略熵单调下降、每行最大概率单调上升，能解释原因
- - [ ] β 很大时软策略≈硬策略（肉眼验证）
- - [ ] `irl.py` 建好，且当天没有任何其它文件复制这两份实现

------

# Day04（2026.10.12）

## 今日目标

掌握值迭代与策略迭代，并把它们统一到"矩阵迭代"这一视角——论文的 ESVF 就是这个视角。

## 今日任务

### 代码精读（主线·10.08 换轨）

- - [ ] 读 `thirdparty/geoirl-official/causal_maxent.py` 的 `expected_svf_from_policy`（L27 起）——"政策评估＝幂迭代"的官方实现：π 与 P 的乘积在哪一行、迭代到哪算完、返回的向量为什么就是论文的 ESVF；对照今天 `value_policy_iteration.py` 的 `np.linalg.solve` 路线——两条路解同一个方程（约 25 min）
- - [ ] 顺手记两个问题留给 Day05：`irl_causal` 里 W 更新的梯度式长什么样？专家 ESVF 在哪一步进入？（约 10 min）

预计时长：约 35 分钟

> 🎞 **视频与读物存档（暂不看·有空或卡壳时回看）**
>
> - 《动手学强化学习》第 4 章后半"值迭代"一节＋notebook（约 20 min）——逐状态更新 vs 我们整矩阵迭代
> - 张伟楠 第 4 讲 后半·值迭代与广义策略迭代（约 14 min，`BV1S2HfewEQa`）
> - 王琦 P13–P15（三种迭代的收敛性证明最干净）

### 理论学习

```text
值迭代：   V ← max_a [ r + γ V(s') ]        每轮隐式改一次策略
策略迭代： 固定 π → 解 V^π → 改进 π → 重复   政策评估 + 政策改进
截断策略迭代：政策评估只迭代几步，工程上最常用
```

与论文的对应关系（自己写一遍）：

> 论文的中间策略 π 由"奖励＋终止状态＋转移矩阵"算出（＝一次政策评估的产物），再用 π 与 P 的乘积做幂迭代得到 ESVF，与专家 ESVF 比较后更新奖励权重——**一整轮策略迭代被改写成了矩阵乘法**。

### 代码实验

创建：

```text
rl/Day04/value_policy_iteration.py
```

实现要求：

- n＝60 的随机转移矩阵 P0、随机奖励 R，γ＝0.9
- 值迭代：`V ← max_{s'}[R[:,None] + γ (P0*V[None,:])]`，记录收敛轮数
- 策略迭代：每轮 ①用 `np.linalg.solve` 精确解当前 π 的 V^π（政策评估）②按 Q 取 argmax 改进 π；π 不变即停
- 判据一：两种方法得到的 V 一致（`allclose`，绝对误差 < 1e-6）
- 判据二：把策略 π 编码成"每行只保留所选列"的矩阵并行归一化，打印其 γP^π 的谱半径（Day08 的伏笔：策略迭代隐式依赖它 < 1）
- 附加：把策略迭代里的"精确解 V^π"改成迭代 3 次（截断版本），观察轮数与总迭代量的变化，用一句话解释工程上为什么常用截断

### 输出成果

- `rl/Day04/value_policy_iteration.py`
- 笔记：把"政策评估＋政策改进"两段话用论文词汇复述一遍

### GitHub提交

```bash
git commit -am "G04: 值迭代/策略迭代一致，理解政策评估即幂迭代"
```

## 今日成果验收

- - [ ] 两种迭代给出一致的 V
- - [ ] 能解释截断策略迭代是什么、为什么够用
- - [ ] 能不看资料写出"政策评估＝解线性方程组＝幂迭代"这条等价链

------

# Day05（2026.10.13）

## 今日目标

用一个 GridWorld 串起前四天；并**用两种方法算出同一个 ESVF**，把论文的核心计算摸通。

## 今日任务

### 代码精读（主线·10.08 换轨）

- - [ ] 通读 `causal_maxent.py` 全文（约 150 行），在纸上画调用链：`irl_causal → local_causal_action_probabilities → expected_svf_from_policy → stochastic_value_iteration`，每个函数旁标它对应论文哪一节——今天"两种方法算同一个 ESVF"，官方仓库里恰好各有一种（约 30 min）

预计时长：约 30 分钟

> 🎞 **视频与读物存档（暂不看·有空或卡壳时回看）**
>
> - 《动手学强化学习》第 4 章末 FrozenLake 示例（约 15 min）——写 `gridworld.py` 卡壳时对照环境建立与 V/Q 打印方式；**第 5 章及以后的 model-free 不读**（本文 P 已知，用不上）
> - 张伟楠 第 5 讲 I 值函数估计（17 min，`BV13yHfeeEo2`）——只为看懂"model-based（P 已知）vs model-free（从样本学）"的分界，看懂即停，**第 5 讲 II 与第 6 讲不跟**
> - 王琦 P34–P35（on／off-policy 说法最紧凑）

### 理论学习

| 方法 | 需要 P 已知 | 需要交互采样 | 与本文关系 |
| --- | --- | --- | --- |
| 值／策略迭代 | 是 | 否 | **论文用的就是这个**（P 由 SGS 构造） |
| Q-learning | 否 | 是 | 只需理解 model-free 与 model-based 的分界 |
| 行为克隆 BC | — | 否 | IRL 的对照：只模仿、不解释动机 |

> **明确不做**：Sarsa／Expected Sarsa／n-step／DQN／经验回放／目标网络／策略梯度／Actor-Critic／PPO——本文没有对应物。

### 代码实验

创建：

```text
rl/Day05/gridworld.py
```

并把 ESVF 追加进 `geoirl/esvf.py`：

实现要求（`gridworld.py`）：

- 5×5 网格，含两堵墙、一个目标格；把"可通行的相邻格"编成图的邻接矩阵，行归一化得 P（对角为 0，目标格之外都允许移动）
- 奖励：只有目标格为 1，其余为 0（状态奖励设定，符合本文"奖励挂在节点上"的口径）
- 用 `geoirl.irl.soft_policy` 求 π 与 V（**不许重写软策略**）
- 函数 `esvf_by_power_iteration(pi, start, T)`：从起点出发 `d ← d @ pi`，累计访问并取平均
- 函数 `esvf_by_sampling(pi, start, episodes, max_steps)`：按 π 逐条采样轨迹再统计
- 判据一：两者相关系数 > 0.95；目标格的访问频次两者接近
- 判据二：打印一张方向箭头策略图（每格最可能去向），整体朝目标收敛、不穿墙
- 附加：把 γ 调成 1.0 再跑一次软策略，观察是否还收敛，并解释（折扣与连通性的关系）

实现要求（`geoirl/esvf.py`）：

- 提供 `esvf(pi, start=None, T=...)`：默认从均匀分布或指定起点传播；返回访问频次向量
- 文件头注明对应论文 §2.1／§2.1.6；Day08 会在这里加"归一化稳定版"

环境准备（10.08 合流新增·为明早跑官方金标准铺路，约 15 分钟）：

- 装 `torch_geometric`（从 G12 提前）：`pip install torch_geometric` 纯 Python 包即可——现代 PyG 的 `GCNConv/GraphConv` 有原生 torch 回退，`torch_scatter` 等扩展装不上就不装；冒烟 `python -c "import torch_geometric"`
- 装失败也不阻塞：官方 notebook 的 Linear 路线不需要 PyG，dense 降级预案（附录 B）仍然成立，把失败输出记进笔记即可

### 输出成果

- `rl/Day05/gridworld.py`（含箭头策略图输出）
- `geoirl/esvf.py`
- `rl-geoirl/notes/G05（2026.10.13）Note.md`：第一阶段小结，含"哪些 RL 算法我决定不学、为什么"

### GitHub提交

```bash
git commit -am "G05: GridWorld 软策略 + ESVF 两种算法等价性验证"
```

## 今日成果验收

- - [ ] 幂迭代 ESVF 与采样 ESVF 相关系数 > 0.95
- - [ ] 策略图正确（朝目标、不穿墙）
- - [ ] 能回答："为什么 agent 知道往哪个方向走？"
- - [ ] `geoirl/` 里已有 `irl.py` 与 `esvf.py`，且散脚本没有复制它们
- - [ ] `import torch_geometric` 成功，或失败输出已记进笔记（不阻塞明早的 Linear 金标准）

------

# Day01—Day05阶段验收（2026.10.13 晚）

你应该达到：

- - [ ] 能默写 Return、V、Q、硬 Bellman、软 Bellman、softmax 策略 六个式子
- - [ ] 能用 numpy 在 30 行内实现值迭代，并解释收敛条件（谱半径）
- - [ ] 能分清 model-based（本文）与 model-free（Q-learning）
- - [ ] 知道 ESVF＝"策略传播的访问频率"，并用两种方法验证过
- - [ ] `rl-geoirl/` 结构成型，`geoirl` 包已有两个模块
- - [ ] GitHub 累计提交 ≥ 5（本月起，V4.0 的计数单独保留）

### 当前能力等级（预计）

```text
Python 开发              ★★★★☆
PyTorch / MLP / BatchNorm ★★★★☆
NumPy / 特征值 / 稀疏矩阵  ★★★★☆   ← Day02/04/05 顺手巩固
MDP / 价值 / 迭代          ★★★☆☆   ← 本阶段新得
IRL / MaxEnt IRL           ☆☆☆☆☆   ← 下一阶段
图与 GNN                   ★☆☆☆☆
GeoAI 矢量数据              ★☆☆☆☆   ← Day15 补
论文复现进度                 25%
```

------

## 第二阶段：IRL、MaxEnt IRL 与 ESVF（Day06—Day10）

### 时间：2026.10.14—2026.10.20

### 阶段目标

> 本阶段是**全月核心**——论文的难点全在这里，而不在神经网络。
>
> 彻底理解 RL 与 IRL 的正反关系；掌握最大熵原则为何能解决奖励的歧义性；
> 会推 MaxEnt IRL 的目标函数与梯度；理解配分函数如何被软值函数吸收；
> 亲历并解决 ESVF 幂迭代的发散问题（论文贡献②）；
> 最后不依赖任何库，独立实现一个端到端的 6×6 MaxEnt IRL。

------

# Day06（2026.10.14）

## 今日目标

把"已知奖励学策略"翻转成"已知策略学奖励"，并用代码亲身撞上"奖励歧义性"这堵墙。

## 今日任务

### 代码精读

- - [ ] 读 `thirdparty/geoirl-official/causal_maxent.py` 的 `irl_causal`（L102 起）——官方 IRL 主循环只有三层：算 π → 算模型 ESVF → 用"专家 ESVF − 模型 ESVF"更新 W。找出相减的那两行，并回答：今天 `irl_ambiguity.py` 撞上的"歧义性"，在这段代码里对应哪一步没有约束？（约 30 min）
- - [ ] 翻 Ziebart et al. 2008《Maximum Causal Entropy Inverse Reinforcement Learning》（AAAI，6 页）的问题设定一节——"从示范中学习"＝论文 §1 的 IRL 动机；只看设定与梯度式，推导细节留给明天（约 15 min）
- - [ ] **金标准跑通（10.08 合流新增）**：打开 `thirdparty/geoirl-official/IRL_deep.ipynb`，照官方 README 的图号→cell 对照表，**只跑 Linear 奖励的默认流程**（Figure 2 基线段），输出图与数字存进 `rl-geoirl/results/golden/`——从今晚起，自写的每一步都有一张标准答案可比（约 40 min；GCN/GraphConv 的图**不追**，那是 G12/G18 的事）

预计时长：约 1 小时 25 分钟（精读 45 min＋金标准 40 min）

> 🎞 **视频与读物存档（暂不看·有空或卡壳时回看）**
>
> - 张伟楠 第 12 讲 I 模仿学习（32 min，`BV1DfpzeLEmC`）——中文 IRL 入门首选，与书前沿篇同章同符号
> - 李宏毅 `BV1JA411c7VT` P34 如何从示范中学习？逆向强化学习（27 min）——重点"奖励歧义性"一段
> - 《动手学强化学习》前沿篇·模仿学习章（`hrl.boyuai.com`；BC／GAIL 部分可略读）

### 理论学习

```text
普通 RL ： Reward + Transition → Policy → 行为
本文 IRL： 行为(专家轨迹) + Transition → Reward → Policy → 新行为
```

1. **歧义性**：同一条专家轨迹有无穷多个 reward 能解释（轨迹没经过的状态上，奖励随便改都不影响解释力）→ IRL 是**欠定问题**，必须加选择原则；
2. **最大熵就是那个原则**：在所有"解释得动专家行为"的分布里选熵最大的——**不添加没有证据的偏好**（论文 §1 的说法是 least-wrong）。

### 代码实验

创建：

```text
rl/Day06/irl_ambiguity.py
```

实现要求：

- 场景：3×3 网格上的一条专家路径（如 0→1→2→5→8），P 用网格邻接行归一化
- 函数 `rand_reward(scale)`：路径上奖励给 0.5～1.0 的随机值，**路径外**奖励给 ±scale 的随机值
- 函数 `logprob_of_path(r)`：调用 `geoirl.irl.soft_policy` 得 π，返回专家路径的 log π（逐边相乘取对数）
- 对 scale＝3.0 采 20 组不同奖励，打印 20 个 log π 值与其标准差；再对 scale＝0.05 做同样实验做对照
- 判据：**两种 scale 的标准差都很小**，而 `r[~on]` 差别巨大 → 直观证明"不同奖励给出相近解释力"，即奖励不可唯一确定
- 笔记里回答：为什么这时必须引入最大熵原则（不许抄本文措辞，用自己的话）

### 输出成果

- `rl/Day06/irl_ambiguity.py`
- `results/golden/`：作者 Linear 路线输出（图＋数字，标注 cell 号与运行日期）
- 笔记：一段话回答"论文为什么不用行为克隆而用 IRL"（对照 §1 的表述）

### GitHub提交

```bash
git commit -am "G06: RL 与 IRL 正反关系，奖励歧义性数值演示"
```

## 今日成果验收

- - [ ] 能构造两个差异巨大的 reward，却在专家路径上给出几乎相同的解释力
- - [ ] 用自己的话说清"最大熵＝不加无证据的偏好"
- - [ ] 知道本文为何必须 IRL：真实世界的 reward structure 拿不到（论文引 Ng & Russell 1998）
- - [ ] `results/golden/` 里至少存下一张作者图，且标了来源 cell

------

# Day07（2026.10.15）

## 今日目标

写出 MaxEnt IRL 的目标函数与梯度，理解"配分函数"如何被软值函数吸收。

## 今日任务

### 文献精读

- - [ ] Ziebart 2008（续）：精读目标函数与梯度两节，手抄 ∂ log L／∂W ＝ 专家特征期望 − 当前策略特征期望，与 `irl_causal` 里 W 更新那两行逐符号对上——这一行就是全部 IRL 的引擎（约 40 min）

预计时长：约 40 分钟

> 🎞 **视频存档（暂不看·有空或卡壳时回看）**
>
> - 张伟楠 第 12 讲 II 模仿学习（33 min，`BV1Qopze2Ee1`）——MaxEnt IRL 目标函数与梯度的课堂版，配今天 `maxent_gradient.py`；GAIL 一节略读即可
> - CS285 `BV1NjH4eYEyZ` P84 IRL Part 3（8 min）＋ P85 IRL Part 4（14 min）——Levine 英文原版推导

### 理论学习

轨迹的因果最大熵分布：

$$
p(\tau) \propto \exp\Big(\sum_{(s,a)\in\tau} Q(s,a)\Big),
\qquad
\pi(a\mid s)=\frac{e^{Q(s,a)}}{\sum_{a'}e^{Q(s,a')}}
$$

对数似然梯度（IRL 的训练信号）：

$$
\nabla_W \log L(W) = \sum_{\text{专家}} \phi(s) - \mathbb{E}_{\pi}\Big[\sum_t \phi(s_t)\Big]
$$

**"专家特征期望 − 模型特征期望"**就是论文 §2.1 里"把 ESVF 与 expert ESVF 比较、据其差更新奖励权重"的数学形式，也是整个复现唯一必须记住的梯度。

> 记号对齐：本文的 feature matrix F 的每一列就是一个特征函数 φ_k（高度分组、面积分组、离市中心距离分组…），第 i 行第 k 列＝建筑 i 是否属于第 k 组（§2.1.2 的多维聚类 one-hot）。所以"特征期望"＝ **ESVF 的线性映射**；论文那句"特征矩阵是最优策略的物化"就是这个意思。

### 代码实验

创建：

```text
rl/Day07/maxent_gradient.py
```

实现要求：

- 数据：n＝25、k＝4 的二值特征矩阵 F（每列随机 30% 命中）、随机 P、随机权重 W
- 软策略**不再重写**：`from geoirl.irl import soft_policy`，线性奖励 `r = F @ W` 接在前面
- 新写 `esvf(pi, start, T)`（今天把它追加进 `geoirl/esvf.py`，供 Day08/10/16 复用）
- 计算：`model_feat = esvf(pi) @ F`（k 维模型特征期望）；`expert_feat` 先由 `model_feat` 加小扰动伪造
- 打印 `grad = expert_feat - model_feat`，并验证：沿 grad 方向走一步 W，model_feat 是否朝 expert_feat 靠近
- 判据：能指出梯度里哪一项来自"策略"（需要算 π 与幂迭代）、哪一项是"常数"（专家观测）
- 笔记：把论文 §2.1 训练流程写成**五行伪代码**钉死（奖励 → 中间策略 π → ESVF 幂迭代 → 与专家比较 → 更新权重 → 回到第一行）。Day14 的骨架就照它写

### 输出成果

- `rl/Day07/maxent_gradient.py`；`geoirl/esvf.py` 更新
- 笔记：五行伪代码 ＋ 梯度式默写

### GitHub提交

```bash
git commit -am "G07: MaxEnt IRL 目标函数与特征期望差梯度"
```

## 今日成果验收

- - [ ] 能不看资料默写梯度式并指认每一项
- - [ ] 说得出"特征矩阵 ≡ 专家 ESVF 的物化"在论文哪一节（§2.1.2）
- - [ ] 实现里 logsumexp 做了减最大值的数值稳定处理

------

# Day08（2026.10.16）

## 今日目标

攻克论文贡献②：ESVF 幂迭代的**发散**与用 Laplacian／归一化**稳定**它。今天不看视频，全是实验。

## 今日任务

### 代码精读

（无新增。今天以实验与矩阵论课程内容为主；`expected_svf_from_policy` 在 Day02/04 已精读过，写 `esvf_stability.py` 时回看它有没有收敛保护即可。）

### 理论学习

论文 §2.1.6 的逻辑链：

```text
π(·)（软策略）与中间策略 P(π) 的乘积，其【主特征值】决定幂迭代是否收敛
        ↓
迭代过程中主特征值不断长大 → 发散（Ziebart 2010 / Snoswell 2020 / Barnes 2023 都遇到）
        ↓
本文做法：把该乘积归一化成它的【左 Laplacian 矩阵】以压制增长
        ↓
附带结论：主特征值与 ESVF 匹配损失成反比；GNN 初始主特征值更大 → 收敛更快
```

左 Laplacian：$L = D - A$（D 为度对角阵），其谱与非负矩阵的谱半径相关（Perron–Frobenius）。这一段与矩阵论课同步。

### 代码实验

创建：

```text
rl/Day08/esvf_stability.py
```

实现要求：

- 规模 n＝300；γ 必须 < 1（否则软值函数本身不收敛）；**把奖励尺度放大**（如 `normal(0, 3)`），目的是让"未归一化乘积"的主特征值明显越过 1
- 中间策略**复用** `geoirl.irl.soft_policy`
- 构造迭代算子：`M = P ⊙ exp(r(s') + γV(s'))`，即**未归一化**的软权重乘积（这才是会发散的原始对象）
- 函数 `rho(M)`：返回主特征值模长
- 函数 `power_iter(M, T, mode)`，mode ∈ {`naive`, `rownorm`, `laplacian`}：
  - `naive`：直接 `d ← d @ M`
  - `rownorm`：按列（左）归一化后再乘，把主特征值钉在 1
  - `laplacian`：走 `M · D⁻¹` 的左 Laplacian 视角
  - 每轮记录 `rho`；一旦 `d` 出现 inf/nan 就报"发散"并停止
- 打印三种模式的：状态、末段 ESVF 最大值、谱半径首末值
- 判据一：`naive` 发散、另两种稳定（若 naive 没炸，加大奖励尺度或减小 n 复现；若瞬间 overflow，减小尺度）
- 判据二（**必须进报告**）：画出三条"谱半径 vs 迭代轮次"曲线存 `results/esvf_stability.png`
- 判据三：能说清 `M`（未归一化乘积）与 `π`（行归一化后）的关系＝**同一矩阵归一化前后**——于是"归一化"不是外加的工程技巧，而本来就是"从软权重里提取合法策略"那一步
- 记录选择：论文只说"归一化成左 Laplacian"，没给唯一公式。写清你最终用哪一种、为什么

### 输出成果

- `rl/Day08/esvf_stability.py`
- `results/esvf_stability.png`（复现报告必配的技术图，对应论文 Figure 3 伪代码与 §2.1.6）
- 笔记：三种归一化的对比结论 ＋ 你的选择与理由

### GitHub提交

```bash
git commit -am "G08: 复现ESVF发散与Laplacian稳定化"
```

## 今日成果验收

- - [ ] 跑出"naive 发散／两种归一化稳定"的对比
- - [ ] 能解释左 Laplacian 为什么能压主特征值
- - [ ] 能验证"主特征值与 ESVF 匹配损失成反比"在你的实验里是否成立
- - [ ] 报告素材（三条谱半径曲线）已入 `results/`

------

# Day09（2026.10.19）

## 今日目标

读一份别人的 MaxEnt IRL 实现，把它每一段对应回论文的记号，避免闭门造车。

## 今日任务

### 代码精读

（今天的精读对象就是 `qzed/irl-maxent`，见下方代码实验；读完加一步：与官方 `causal_maxent.py` 的 `irl_causal` 对照——一份枚举轨迹、一份矩阵迭代，谁的配分函数能扩到 n≈1000，今天见分晓。）

### 理论学习

参考实现的层次：

| 仓库 | 用途 | 与论文对应 |
| --- | --- | --- |
| `qzed/irl-maxent`（331★，Jupyter，MIT） | 今天主线：跑通并逐段注释 | 软策略＋配分函数＋梯度更新＝§2.1 |
| `soma11soma11/MEIRL` | 空间场景对照（行人移动） | 栅格→状态，与本文"建筑→状态"同构 |
| `G-Lauz/maxent_deep_irl` | 之后用（神经网络表示奖励） | §2.1.5 引用的 Wulfmeier 2015 那条线 |

### 代码实验

创建：

```text
rl/Day09/
├── clone_and_read.py   （可选，仅是操作记录）
└── read_notes.md
```

实现要求：

- `git clone` 到 `rl-geoirl/thirdparty/irl-maxent`（该目录已在 `.gitignore` 排除，只读参考、不入库）
- 在其 notebook 里加中文注释，指认三处，并各写一句"论文里叫什么"：
  1. **软策略／配分函数**在哪一行——特别注意它是枚举轨迹还是矩阵迭代
  2. **ESVF**（期望状态访问频率）在哪一行
  3. **更新权重 W**在哪一行，与 Day07 的梯度式是否同形
- 回答两个问题并写进 `read_notes.md`：
  - "枚举轨迹"与"幂迭代近似"的区别是什么？为什么本文（n≈1000）只能用后者？
  - 它的配分函数 Z 怎么算？你判断它能否扩到 n≈1000？依据是什么？
- 明确一条纪律：**明天开始自己写，不再抄**

### 输出成果

- `rl/Day09/read_notes.md`（三处指认 ＋ 两个回答）
- `thirdparty/irl-maxent/` 保持只读（不提交）

### GitHub提交

```bash
git commit -am "G09: 对照 qzed/irl-maxent 标注软策略-ESVF-梯度三段"
```

## 今日成果验收

- - [ ] 能说清"枚举轨迹"与"幂迭代"两种实现的分界及各自适用规模
- - [ ] 找到它算 Z 的代码位置并作出可扩展性判断
- - [ ] `read_notes.md` 里没有大段抄代码，只有"位置＋对应论文记号"

------

# Day10（2026.10.20）

## 今日目标

不依赖任何 IRL 库，端到端实现一个 6×6 的 MaxEnt IRL：给专家访问频次，学回奖励。**这是本阶段的验收日。**

## 今日任务

### 代码精读

（无新增。若假期碎片任务未完成，今晚 3 小时补 C-GAN 与流模型原理，正式销账。）

### 理论学习

端到端只有四步，缺一不可：

```text
专家访问频次 d_e  →（当前 W 算 r=F@W）→ π → 模型访问频次 d_m
                                            ↓
                        grad = d_e - d_m（映射回特征空间）→ 更新 W
```

### 代码实验

创建：

```text
rl/Day10/maxent_irl_6x6.py
```

实现要求（脚本必须只由三个函数构成，职责不重叠）：

- `policy_from_r(r)` → 转调 `geoirl.irl.soft_policy`（自己的实现，**不许 import 任何 IRL 库**）
- `esvf_of(r)` → 由 r 得 π，再按 π 传播访问频次；口径要与专家频次完全一致（同一 `start`、同一 T／同一采样条数）
- `fit(F, expert_visits, ...)` → 梯度上升更新 W，记录每轮 `‖grad‖` 直至收敛
- 数据设计（用来"假装不知道真值"）：
  - 真值奖励 `tr`：越靠右下越好，且第 2、3 行有代价（制造可学习的空间偏好）
  - 特征矩阵 `F`：**只用可观测的分组二值特征**（模拟论文的多维聚类），信息量故意低于真值
  - 专家轨迹：用 `tr` 生成 π_expert 后采样若干条，统计 `expert_visits`
- 必须打印的三个数：学到的 W、`corr(学到的奖励, 真值奖励)`、`corr(模型ESVF, 专家ESVF)`
- 必须画一张三联图存 `rl/Day10/maxent_result.png`：专家访问频次热图／学到的奖励热图／真值奖励热图
- 判据一：`corr(学到奖励, 真值) > 0.7`；若偏低，先怀疑特征矩阵信息量（这正是论文 §2.1.2 花大篇幅做信息传播的理由），**不要先去调学习率**
- 判据二：`corr(模型ESVF, 专家ESVF) > 0.8`
- 判据三：全流程只用 numpy ＋ 自己的 `geoirl`，且 `policy_from_r/esvf_of/fit` 能各自单独运行

### 输出成果

- `rl/Day10/maxent_irl_6x6.py`、`rl/Day10/maxent_result.png`
- `rl-geoirl/notes/G10（2026.10.20）Note.md`：第二阶段小结，含"我现在能 30 分钟内独立重写一个 MaxEnt IRL"
- C-GAN 与流模型先修销账确认（导师 09.30 更正后的口径）

### GitHub提交

```bash
git commit -am "G10: 从零实现 6x6 MaxEnt IRL 端到端跑通"
```

## 今日成果验收

- - [ ] 两个相关系数达标（或给出"为什么不达标"的归因分析）
- - [ ] 三函数结构清晰、无重复实现
- - [ ] 热图上"学到的奖励"与"专家常去的格子"肉眼同形
- - [ ] C-GAN 与流模型先修已销账

------

# Day06—Day10阶段验收（2026.10.20 晚）

- - [ ] 能解释：奖励歧义性 → 最大熵原则 → 概率策略 这条因果链
- - [ ] 能默写 MaxEnt 梯度式，并在代码里指认每一项
- - [ ] 理解"特征矩阵＝专家 ESVF 的物化"（§2.1.2）
- - [ ] 亲历一次幂迭代发散，并知道归一化怎么救它（论文贡献②）
- - [ ] **此刻已经拿到了这篇论文最难的那块**，剩下的 GNN 只是"换一层网络"
- - [ ] 论文复现进度：45%

------

## 第三阶段：图、拉普拉斯与 GNN（Day11—Day14）

### 时间：2026.10.21—2026.10.26

### 阶段目标

> 用 CNN 的语言理解 GCN：像素的空间邻域 → 节点拓扑邻域；
> 手写 dense GCN 并与 PyG 数值对齐（对齐＝真的懂了）；
> 说清 `GraphConv` 与 `GCN` 的差别（论文两个都用了）；
> 把论文 §2.1 全部组件翻成 Python 骨架。

### 约束

只学 GCN 与 GraphConv。**不学** GAT、GraphSAGE、GIN、GCNII、HAN、HGT——论文没用，学一个都是浪费。

------

# Day11（2026.10.21）

## 今日目标

把 Day08 的"归一化邻接／Laplacian"与 GCN 的"对称归一化邻接"接成同一件事。

## 今日任务

### 代码精读

- - [ ] 读 `thirdparty/geoirl-official/transitions.py` 的 `simple_gravity`（L20–32）／`inverse_euclidean`（L33–45）／`get_transition`（L46–56，带 `density` 参数）——式(1) SGS、IED 与 §3.1 密度稀疏化的官方实现，各约 13 行；标出对角处理与行归一化在哪一行（约 25 min）
- - [ ] 对照 Kipf & Welling 2017（arXiv 1609.02907）§2 的传播公式：对称归一化 D̃^(−1/2)(A+I)D̃^(−1/2)；写三句话说明"行归一化 P"与"对称归一化 Â"差在哪、与 Day08 的左 Laplacian 又是什么关系（约 20 min）

预计时长：约 45 分钟

> 🎞 **视频存档（暂不看·有空或卡壳时回看）**
>
> - 同济子豪兄 `BV16v4y1b7x7` 图神经网络综述和学习路径（53 min）

### 理论学习

| CNN | GCN |
| --- | --- |
| 像素的规则网格邻域 | 节点的不规则拓扑邻域 |
| 固定 3×3 卷积核 | 可学习的聚合权重（度归一化） |
| 平移不变性 | 置换不变性（邻居顺序无关） |
| Padding／Stride 控制尺寸 | 没有尺寸概念，输出维＝特征维 |

GCN 一层的归一化传播：

$$
H^{(l+1)} = \sigma\big(\tilde D^{-1/2}\tilde A\,\tilde D^{-1/2} H^{(l)} W^{(l)}\big),\qquad \tilde A = A + I
$$

> 本文的转移矩阵就是 $\tilde D^{-1/2}\tilde A\tilde D^{-1/2}$ 的近亲（行归一化 vs 对称归一化）。Day08 的左 Laplacian 与这里的对称归一化，是同一个谱图论工具的两面。

### 代码实验

创建：

```text
rl/Day11/graph_norm_compare.py
```

实现要求：

- 用 `networkx.erdos_renyi_graph(200, 0.05)` 造图，取邻接矩阵 A 与度向量
- 分别构造并打印三者的主特征值（模长）与最大实部：
  1. 行归一化 $P = D^{-1}A$（本文转移矩阵形式）
  2. 对称归一化 $\tilde D^{-1/2}(A+I)\tilde D^{-1/2}$（GCN 形式）
  3. 左 Laplacian $L = D - A$
- 判据一：能解释为什么随机矩阵恒有 ρ＝1，而对称归一化的 ρ ≤ 1（与图的正则性有关）
- 判据二：能说出"本文为什么还要人为压住乘积的主特征值"（因为乘积不再是随机矩阵）
- 附加：把图改成正则图（如环）再跑一遍，观察两者关系变化

### 输出成果

- `rl/Day11/graph_norm_compare.py`
- 笔记：三种归一化各自"让什么不变／让什么有界"的一句话总结

### GitHub提交

```bash
git commit -am "G11: 行归一化/对称归一化/左Laplacian 谱半径对比"
```

## 今日成果验收

- - [ ] 三个谱半径都算出来并解释差异
- - [ ] 能说清对称归一化不是转移矩阵（行和不为 1）
- - [ ] 把这套语言和矩阵论课的相关内容对上号

------

# Day12（2026.10.22）

## 今日目标

手写一层 dense GCN，并与 PyG 的 `GCNConv` 对齐到同一数值——对齐成功＝你真的懂这一层。

## 今日任务

### 代码精读

- - [ ] 读 `thirdparty/geoirl-official/rewards.py` 的 `GCN` 类（L51–79）——论文官方 GCN：几层、hidden 是不是 32、BatchNorm 放在激活前还是后、`forward` 里 `edge_index` 怎么传；今天手写 dense GCN 并与 PyG 对齐之后，再拿这份官方实现**对第三遍**（约 25 min）

预计时长：约 25 分钟

> 🎞 **视频存档（暂不看·有空或卡壳时回看）**
>
> - 同济子豪兄 `BV1Hs4y157Ls` 图卷积神经网络 GCN（63 min）
> - PyG 官方 `GCNConv` 文档页（写码卡壳时查，不算任务）

### 理论学习

消息传递三句：

```text
1. 每个节点收集自己＋所有邻居的特征（求和或加权平均）
2. 用一个可学习的 W 变换聚合结果
3. 过非线性（ReLU）＋ BatchNorm —— 论文的 MLP/GCN/GraphConv 用的是同一套激活与 BN
```

论文 §2.1.5 的明确设定（照抄进代码，别自由发挥）：

| 模型 | 结构 | 参数量 |
| --- | --- | --- |
| Linear | 单层前馈、无激活 | 11（＝特征数 → 需 bias=False） |
| MLP | 3 层线性＋ReLU＋BatchNorm，隐藏维 32 | 1,569 |
| GCN | 同上，Linear 换成 GCNConv | 1,569 |
| GraphConv | 同上，Linear 换成 GraphConv（每层多一个 root weight） | 2,945 |

### 代码实验

创建：

```text
rl/Day12/gcn_numpy.py
```

实现要求：

- 函数 `norm_adj(A)`：返回 $\tilde D^{-1/2}(A+I)\tilde D^{-1/2}$
- 类 `DenseGCNLayer`：`__call__(X, Ã)` 返回 `Ã @ X @ W`（先只做传播，bias 关掉）
- 自检一：n＝60、f＝11、h＝32 的随机图与特征上，打印输出形状与数值（用固定种子生成 W，方便与 PyG 对表）
- 自检二（对齐）：同一个 W 喂给 `torch_geometric.nn.GCNConv(f, h)`（`bias` 置零、`lin.weight` 用同一矩阵），比较两者输出
- 判据：`numpy` 与 `PyG` 输出最大偏差 < 1e-4；**若 PyG 装不上，本文件即降级方案**，把异常类型与信息写进笔记，不阻塞后续
- 必查的错误源（自己踩一遍再修）：对称归一化是不是"行归一化"？邻居顺序影响结果吗（置换不变性验证：随机打乱节点编号，输出应只是行的同顺序重排）？
- 结论要能说出：论文把转移矩阵当图的边输入 GCN，等于**同时使用特征与拓扑**（§2.1.5）

### 输出成果

- `rl/Day12/gcn_numpy.py`（＋对齐结果或降级说明）
- 笔记：把 $\tilde D^{-1/2}\tilde A\tilde D^{-1/2}$ 与 `norm_adj` 逐项对照

### GitHub提交

```bash
git commit -am "G12: 手写 dense GCN 并与 PyG GCNConv 对齐"
```

## 今日成果验收

- - [ ] `norm_adj` 结果行和不为 1，且能说明为什么
- - [ ] 与 PyG 对齐到 1e-4，或有明确的降级记录
- - [ ] 做过一次"打乱节点编号"的置换不变性验证

------

# Day13（2026.10.23）

## 今日目标

PyG 的最小可用集 ＋ 论文的四种奖励网络，并把参数量逐项对账。

## 今日任务

### 代码精读

- - [ ] 通读 `thirdparty/geoirl-official/rewards.py` 四个类 `Perceptron`／`MLP`／`GCN`／`GRAPHCONV`（L16–109），逐类**手数参数量**，与论文 11／1,569／1,569／2,945 对账；对不上的地方（比如 GRAPHCONV 的 root weight）就是今天笔记要写的问题（约 40 min）

预计时长：约 40 分钟

> 🎞 **存档（暂不看·卡壳时查）**
>
> - PyG 官方 Quickstart；子豪兄 GitHub 笔记 `TommyZihao/zihao_course/CS224W`

### 理论学习

只需要这五个对象：`Data`、`x`、`edge_index`、`edge_weight`、`GCNConv`／`GraphConv`。

`GCNConv` 与 `GraphConv` 的差别：前者做对称归一化聚合，后者额外保留**节点自身特征**的独立权重（root weight，即 $W_1 h_v + W_2 \sum_{u\in N(v)} h_u$），因此参数量更大——论文两个都用了 1,569 与 2,945 正源于此。

### 代码实验

创建：

```text
geoirl/rewards.py
```

实现要求（这是要复用的包内模块，不是 Day 脚本）：

- `LinearReward(k)`：单层、无激活、**`bias=False`**（→ 11 参数）
- `MLPReward(k, h=32)`：三层线性＋ReLU＋BatchNorm；给出能凑出 1,569 的具体配置并解释每一项（352＋64＋1056＋64＋33）
- `GNNReward(k, h=32, kind="gcn"|"graph")`：与 MLP 同层数同隐藏维，把 Linear 换成 `GCNConv`／`GraphConv`；forward 需要 `(x, edge_index, edge_weight)`
- 顶部用 `try/except` 处理 PyG 缺失：提供一个 dense 的降级 `GCNConv` 实现（用 `edge_index` 还原邻接矩阵、自己算对称归一化），`GraphConv` 在降级路径下用同一实现并注明"拓扑项近似等价，报告里必须标注"
- 自检脚本 `n_params(m)`：逐个网络打印总参数量＋**每个参数张量的 `numel()` 列表**，与论文 11／1569／1569／2945 对账
- 判据：Linear 必须正好 11；MLP 与 GCN 相等（论文用这一点说明"差异不来自参数量，而来自图的归纳偏置"）；GraphConv 更大，差值＝各层 root weight 之和
- 若对不上：**不许硬凑**，把每一项 `numel()` 与差异来源（bias／BN 的 γ β／root weight）写成"参数量对账单"，进复现报告的偏差清单

### 输出成果

- `geoirl/rewards.py`
- 笔记：PyG 五个对象各一句话；`Data(x=…, edge_index=…, edge_weight=…)` 的构造片段；参数量对账单

### GitHub提交

```bash
git commit -am "G13: 四种奖励网络实现与参数量对账"
```

## 今日成果验收

- - [ ] Linear＝11，MLP＝GCN（数值一致）
- - [ ] GraphConv 与 GCN 的差值能逐项解释
- - [ ] `HAS_PYG` 两条路径都能跑（降级保险有效）
- - [ ] 对账差异已写进偏差清单而不是藏在代码注释里

------

# Day14（2026.10.26）

## 今日目标

精读论文 §2 全文，把 Figure 1 流程与 Figure 3 伪代码翻成 Python 骨架——从今天起代码就是复现代码。

## 今日任务

### 代码精读

（无新增。今天的精读对象是论文 §2 全文，见下方阅读任务。）

### 阅读任务（约 2 小时，带笔记本重读）

| 论文章节 | 必须能回答的问题 |
| --- | --- |
| §2.1.1 训练数据 | 7,692 条轨迹、12,318 栋建筑、平均 4.92 停留点；学习子集为何只有 1,014 栋 |
| §2.1.2 特征矩阵 | 多维聚类如何把"只有约 1/3 建筑被访问过"的稀疏观测传播到全体状态空间；期望访问次数怎么算 |
| §2.1.3 转移矩阵 | SGS 式(1)；为何对角为 0；为何稀疏化到 10% 密度 |
| §2.1.4 初／终态 | 状态空间被重定义后为何不能按惯例从数据取初/终态；"去情境化—再情境化"指什么 |
| §2.1.5 奖励非线性 | 四种网络与参数量；MLP 是"有非线性但无图归纳偏置"的对照组 |
| §2.1.6 收敛与 Laplacian | 主特征值如何控制幂迭代；为何与 ESVF 匹配损失成反比 |
| §2.2 轨迹生成 | 马尔可夫链式采样；"回家假设"为何导致访问数虚高；K-M 生存概率当折扣因子 |

- - [ ] **核实一条外部批判**（约 10 min，10.08 合流新增）：有说法称"论文用整个城市数据训练、却在小子区域生成轨迹，空间错配可解释部分偏差"。到 §3.2／§3.3 找训练与评估区域的**原文**划分写法，判断该说法成不成立，结论写进笔记。**核实成立之前别写进组会 PPT**——被老师追问一句就露馅。

### 代码实验

创建：

```text
rl-geoirl/skeleton.py
```

实现要求（每个函数先用 Day01—Day10 已有代码填成**能跑的最小实现**，允许参数是合成的）：

- `build_features(rng, cfg)` → §2.1.2 分组 one-hot 特征矩阵
- `build_transitions(F, cfg)` → §2.1.3 SGS ＋ 行归一化 ＋ 稀疏化到 `density`
- `policy_from_reward(reward, P, terminal, cfg)` → 转调 `geoirl.irl.soft_policy`
- `esvf(pi, P, cfg)` → 转调 `geoirl.esvf`，并留出 Day08 稳定版的开关
- `loss_and_grad(F, expert_visits, model_visits)` → 特征期望差
- `train(reward_net, P, F, expert_visits, cfg)` → Day10 的 `fit` 通用化（网络版）
- `discount_from_survival(traj_lengths)` → §2.2 占位（Day17 实现）
- `sample_trajectories(...)`、`evaluate(gen, expert)` → Day17 实现，今天先返回占位结果
- 主流程：`build_features → build_transitions → … → evaluate` 一条命令跑到底，打印特征矩阵形状、矩阵密度、若干条生成轨迹长度
- 同时把 Day01—Day10 的散脚本**整理进 `geoirl/` 包**，Day 目录只留 demo

### 输出成果

- `skeleton.py` 端到端跑通
- `geoirl/` 包成型（`irl / esvf / rewards` 已就位，`geo_data / sample / metrics` 待 Day15／Day17）
- `rl-geoirl/notes/G14（2026.10.26）Note.md`：七小节各一条"我原本以为…／实际上是…"

### GitHub提交

```bash
git commit -am "G14: 论文§2精读 + skeleton 端到端跑通"
```

## 今日成果验收

- - [ ] 能不看论文画出训练流程图（Feature/Transition/Terminal → π → ESVF → 比较 → 更新 W）
- - [ ] 能说出训练用初/终态与生成用初/终态是两套设定，且这是刻意设计
- - [ ] `skeleton.py` 一条命令跑完并输出形状、密度、轨迹长度
- - [ ] 散脚本逻辑已沉淀进 `geoirl/`，无重复实现

------

# Day11—Day14阶段验收（2026.10.26 晚）

- - [ ] 能手写 dense GCN，并说清它与转移矩阵在归一化上的差别
- - [ ] 四种奖励网络的参数量对账完成（或有明确差异说明）
- - [ ] `geoirl` 包职责清晰：rewards／irl／esvf 三块可独立 import
- - [ ] 论文复现进度：60%（骨架通、核心算法通，缺真实数据与对比实验）

------

## 第四阶段：数据、管线与复现报告（Day15—Day18）

### 时间：2026.10.27—2026.10.30

### 阶段目标

> 补上 60 天计划完全没覆盖的一块：**矢量 GIS 数据工程**（建筑多边形 → 质心／面积／高度／土地利用 → 距离矩阵 → 特征矩阵）；
> 在真实或高质量合成数据上跑通四种奖励网络的对比；
> 产出可交付的复现报告与结果表。

------

# Day15（2026.10.27）

## 今日目标

做出论文的"原料"：特征矩阵 F 与转移矩阵 P。**这一天是全月性价比最高的动手日。**

## 今日任务

### 代码精读

- - [ ] 精读 `thirdparty/geoirl-official/data/` 三份原料的**表头与前 5 行**（`pandas.read_csv(..., nrows=5)`）：`stops_buildings_Jerusalem.csv`（7,692 条轨迹的停留点序列，看一条轨迹的字段格式）、`IRL_feature_matrix.csv`（作者算好的 F，形状应与 §2.1.2 对得上）、`uniq_id_translation_2.csv`（建筑 id↔聚类 id 映射）；今天 `build_features.py`／`build_transition.py` 的列名以这三份为准（约 30 min）

预计时长：约 30 分钟

> GeoPandas 用官方 Getting Started 两页即可，不找视频。

### 理论学习

- 距离必须在**投影坐标系**下算（EPSG:3857 或地方投影），否则"距离"的单位是度，SGS 的 $1/D^2$ 完全失真；
- 论文用**建筑面积**作为重力项的 V；面积由多边形几何算（`geometry.area`），不是属性表里的字段；
- 稀疏化：论文把训练矩阵降到 10% 密度；本文实现用"每行保留 top-ρ 分位"的等价做法，要在报告里写清差异。

### 代码实验

创建：

```text
geoirl/geo_data.py
```

实现要求（四个函数，能同时吃真实与合成数据）：

- `load_buildings(path)`：GeoPandas 读建筑矢量。主方案读官方数据 `thirdparty/geoirl-official/data/jerusalem_buildings_USG_region.csv`（列名以当天实查为准，别照猜写死）；OSM 导出的 shp/gpkg 保留为备选。`to_crs` 投影，剔除空几何
- `make_synthetic(n=1000, seed)`：调试辅助——原本"figshare 拿不到"的降级方案，官方数据已于 2026.09.29 下载，现在用于小规模调试与放大规模试验。随机生成 3 km×3 km 的建筑矩形，附带高度、土地利用代码（0–4）、到市中心距离，并算出 `area`
- `to_features(gdf, thresholds_per_col)`：**多维聚类**的离散化——对面积／高度／离市中心距离各按分位数切组，土地利用按类别 one-hot，返回 `(F, 特征名列表)`
- `sgs_transition(gdf, density)`：质心 → 距离矩阵 D → `SGS_ij = V_i/D_ij²`（对角为 0）→ **按行保留 top-density 后**再行归一化
- 判据一：F 的列数与分组方式写进文档（论文是 11 个特征量级，你的列数由分组决定，要在报告里说明差别）
- 判据二：P 行和恒为 1、对角为 0、非零比例≈density
- 判据三（对齐 §3.1）：用 `networkx.connected_components` 复现"密度越低、连通分量越多"——0.1% 时成百上千个，10% 以上趋于 1 个
- 产出 `results/features_transitions.md`：特征组数、矩阵密度、各密度下的连通分量数与平均邻居数

### 输出成果

- `geoirl/geo_data.py`
- 数据直接读 `thirdparty/geoirl-official/data/`（官方，不入库）；合成则为 `make_synthetic` 的产物——两者都不往仓库里拷
- `results/features_transitions.md`

### GitHub提交

```bash
git commit -am "G15: 矢量建筑→特征矩阵与SGS转移矩阵"
```

## 今日成果验收

- - [ ] 两个判据（行和／对角、密度）通过
- - [ ] 复现出"密度—连通分量"现象
- - [ ] 官方数据与合成数据同一接口：换数据源只需改 `load_buildings` 一行

------

# Day16（2026.10.28）

## 今日目标

把 Day10 的训练循环搬到大图上，跑 **Linear vs MLP vs GCN vs GraphConv** 的对比。

## 今日任务

### 代码精读

（无新增。今天的精读对象是 Day13 对过账的 `rewards.py` 四网络，写训练循环时随手回查。）

### 理论学习（今天唯一的实现关键）

Deep IRL 的标准写法，绕开"对幂迭代做反向传播"：

$$
\frac{\partial \log L}{\partial r_i} = d^{\text{expert}}_i - d^{\text{model}}_i
$$

它与奖励网络的结构无关。于是令

$$
\text{loss} = -\,\big\langle r_\theta(F),\; (d^{\text{expert}} - d^{\text{model}})_{\text{detach}} \big\rangle
$$

最小化 loss ＝ 最大化 logL，梯度自动穿过 `r = f_θ(F)` 回传到 MLP／GCN／GraphConv 的参数。**理由**：n＝1000 时对 3,000 步幂迭代做完整反传，内存与数值稳定性都会失控。

### 代码实验

创建：

```text
rl-geoirl/train_irl.py
```

实现要求：

- 用 `geoirl.geo_data` 造 F、P；GNN 需要边表：把稀疏 P 的非零位置转成 `edge_index`，转移概率本身作 `edge_weight`
- `forward_reward(net, name)` 统一入口：Linear/MLP 只吃特征；GCN/GraphConv 还要吃边表
- 训练循环：每轮 ①前向得 r ②`soft_policy` 得 π（numpy，不回传）③`esvf` 得 d_model ④mismatch＝d_expert − d_model ⑤loss＝`-(reward * mismatch).sum()` → 反传 → 更新
- 每轮记录：loss 值、`‖mismatch‖`、`rho(π ⊙ P)`
- 四种网络同一学习率、同一迭代数、同一随机种子；同时记录**初始**主特征值（验证论文"GNN 初始主特征值更大→收敛更快"）
- 输出 `results/train_curves.png`：四条 loss 曲线＋四条谱半径曲线
- 判据一：四条 loss 可比；GNN 的收敛形态是否与论文一致
- 判据二：`corr(学到的奖励, 建筑面积)` —— 论文 §3.2／图 7 主张 GNN 明显高于 Linear／MLP；若四条都很低，**先查特征矩阵信息量与 d_expert 构造**，最后才考虑调学习率

### 输出成果

- `train_irl.py`；`results/train_curves.png`；奖励-面积相关系数表
- 笔记：为什么可以用一阶代理 loss（写清它和"完整反传"的差别）

### GitHub提交

```bash
git commit -am "G16: 四种奖励网络的 IRL 训练对比与谱半径记录"
```

## 今日成果验收

- - [ ] 四条 loss 曲线齐全且可比
- - [ ] 初始主特征值的对比结论明确（是否支持论文说法）
- - [ ] 奖励-建筑面积相关系数 GNN ≥ MLP／Linear（或写出反例分析）

------

# Day17（2026.10.29）

## 今日目标

补齐论文 §2.2 与 §3.4：K-M 折扣、轨迹采样、三类评估指标，产出结果表。

## 今日任务

### 代码精读

- - [ ] 读 `thirdparty/geoirl-official/trajectories.py` 的 `generate_one_traj`（L22 起）——§2.2 的官方采样器：终止概率怎么落到 home、折扣在哪一步被乘进去、`data/discount_factor.csv`（作者的 K-M 输出）在哪一行被读进来；与你今天写的采样器对照（约 30 min）
- - [ ] 读同文件 `compute_cpc`（L313 起）与 `compute_nfm_rmse`（L361 起）——式(3) NFM 与 CPC 的官方算法，对照今天自己实现的指标函数（约 15 min）
- - [ ] lifelines 文档 `KaplanMeierFitter` 页：跑 fit／survival_function 两行示例即可，比看课快（约 10 min）

预计时长：约 55 分钟

> 🎞 **视频存档（暂不看·有空回看）**
>
> - 北美统计学博士生 `BV1sg4y1j7n9` 生存分析（1）Censored Data, Survival Function（25 min）——补生存分析概念时用

### 理论学习

$$
S(t) = P(T > t) \qquad \text{（Kaplan–Meier 估计）}
$$

论文用法：

```text
折扣因子 ＝ 生存概率 S(t)
终止概率 ＝ 1 − S(t)，赋给 agent 的家
剩余概率在其余建筑间均分
采样用分布 ＝ 上述概率 × 转移概率 × IRL 学到的奖励
 ⇒ 生成长度呈 2—25 的长尾
```

### 代码实验

创建：

```text
geoirl/discount.py
geoirl/sample.py
geoirl/metrics.py
```

实现要求（`discount.py`）：

- 手写 Kaplan–Meier，不依赖 lifelines：按步数排序，逐步乘 $(1 - d_t/n_t)$，其中 n_t 为"至少活到 t"的轨迹数、d_t 为"恰好在 t 结束"的条数
- 用 lifelines 交叉验证同一结果（相关系数≈1 即实现正确），并在报告里注明"主实现手写、库仅对答案"

实现要求（`sample.py`）：

- `sample_trajectories(policy, discount, home)`：从 home 出发按最终分布逐点采样，命中终止即停；同一建筑每 agent 只允许访问一次（论文的约束）
- 判据：加了 K-M 折扣后，生成长度分布接近专家的 2—25 长尾；不加折扣时会复现"访问数虚高"

实现要求（`metrics.py`，对齐 §3.4 与式(3)）：

- `w_dist(gen, exp)`：对跳距、总距离、访问建筑数、凸包面积四个量分别求 Wasserstein 距离（`scipy.stats.wasserstein_distance`）
- `inverse_cpc(...)`：按土地利用类别聚合 O-D 流量，返回 1−CPC（论文表 1 用 1−CPC 使所有指标同向）
- `nfm(...)`：$NFM_{ij} = \%F_{ij} / (\%LU_i \cdot \%LU_j)$，对全部类别组合取 RMSE
- 判据：结果表里必须有 **Untrained（未训练原始矩阵）** 作为基线行

### 输出成果

- `geoirl/{discount,sample,metrics}.py`
- `results/table1_like.csv`：模型 × {跳距WD, 总距离WD, 建筑数WD, 凸包面积WD, inverse CPC, NFM(RMSE)}
- `results/reward_maps.png`（四种网络的奖励空间分布，对应论文图 6／图 9）
- `results/gen_length_hist.png`（生成长度 vs 专家）

### GitHub提交

```bash
git commit -am "G17: K-M折扣、轨迹采样与Wasserstein/CPC/NFM结果表"
```

## 今日成果验收

- - [ ] K-M 曲线与"至少走 t 步"的经验比例吻合
- - [ ] 加折扣后长度分布接近专家；Untrained 基线在表里
- - [ ] 能解释为什么不做逐条轨迹相似度（生成的轨迹在数据里没有对应个体）

------

# Day18（2026.10.30）

## 今日目标

对照作者实现、跑消融、交复现报告。**导师的一个月期限在这里收口。**

## 今日任务

### 代码精读

（无新增。今天的精读对象是作者仓库本身，见下方"作者代码与数据"。）

### 代码实验

#### 1. 作者代码与数据

```text
figshare DOI: 10.6084/m9.figshare.29554394
本地位置：rl-geoirl/thirdparty/geoirl-official/（2026.09.29 已下载，只读，不入库）
```

- 文件清单（已核对）：`causal_maxent.py`（因果 MaxEnt IRL 主循环）、`rewards.py`（四种奖励网络＋绘图）、`transitions.py`（转移矩阵）、`trajectories.py`（轨迹生成与绘图）、`utils.py`、`IRL_deep.ipynb`（主流程）、`IRL_fm_sensitivity.ipynb`（特征矩阵敏感性）、`requirement.txt`、`data/` 内 9 个 CSV（`IRL_feature_matrix.csv`＋4 个敏感性变体、`stops_buildings_Jerusalem.csv` 停靠点、`jerusalem_buildings_USG_region.csv` 建筑、`discount_factor.csv` 折扣因子、`uniq_id_translation_2.csv` ID 映射）
- 官方 `README.md` 自带图号→cell 对照表（Figure 5—11、A2—A6、Table 1—2、A3—A5 都指到 `IRL_deep.ipynb` 的具体 cell）：对照日照着它逐 cell 跑论文图表，不用自己摸
- 补齐官方代码的 GNN 路线图表（GCN／GraphConv——Linear 路线的金标准 G06 已跑过，存于 `results/golden/`），把 Day16／Day17 的表换成论文同一口径（1,014 栋、11 特征、SGS 与 IED 两套矩阵）；与自写 `geoirl/` 包的差异清单写进 `REPRODUCE.md` 第 3 节
- 若官方 `requirement.txt` 与本机 `geoirl` 环境冲突：另建新 env 跑官方代码，不动本计划的环境

#### 2. 必做消融（每条 20 分钟内）

| 消融 | 论文依据 | 要回答 |
| --- | --- | --- |
| SGS vs IED 转移矩阵 | §3.2／图 6 vs 图 9 | 换矩阵后 GNN 奖励与面积／入度的相关是否如论文一样变化 |
| 图密度 0.1%→80% | §3.1 | 结果是否稳定（论文称"密度越高计算越重、结果相近"） |
| 隐藏维与层数变化 | §3.5 | GNN 是否比 Linear／MLP 更鲁棒（波动更小） |
| Laplacian 归一化开／关 | §2.1.6 | 关掉后 loss 与 ESVF 是否发散（Day08 已初步验证） |

#### 3. 交付报告

`REPRODUCE.md` 固定六节：

```text
1. 论文方法一句话概述（附生成路线对照：GAN 无似然·采样式 ／ 流模型 精确似然·架构受限 ／ 本文 IRL 学奖励后按 MDP 采样——支线销账反哺主线，各一句话）
2. 复现范围与结论对照（论文哪个图/表 → 我的哪个图/表 → 一致/不一致/不可比）
3. 实现细节与偏差（一阶代理 loss、归一化选择、特征分组、参数量对账单）
4. 消融结果与四条网络对比
5. 失败清单（没复现出什么、卡在哪、下一步）
6. 环境、随机种子、一键复现命令
```

#### 4. 组会汇报三件套（10.08 合流新增）

- - [ ] **自画流程图**：数据→特征（聚类传播）→P（SGS/IED＋密度）→W（四网络）→π（软策略）→ESVF 比较→采样（K-M 折扣）→指标；一页，明确不抄 Figure 1——这是三样交付里的第一样
- - [ ] **PPT**：图先字后——流程图 1 页、四网络 loss 对比 1 页、结果表 1 页、消融 1 页、失败清单 1 页；每页文字 ≤3 行
- - [ ] **讲稿＋一次计时模拟**：模拟一遍，记下卡壳页与被追问点，当晚补
- - [ ] **四知识点闭卷自检**（每个 2 分钟，组会最可能被问的就是这四问）：
  1. 为什么用 IRL 而不是监督学习／行为克隆——监督是模仿已有轨迹，IRL 是理解动机后生成**新的、多样的**轨迹；且地理轨迹长度不定、评估困难（对应 G06，§1）
  2. MaxEnt IRL 到底在优化什么——所有"解释得动专家行为"的分布里选熵最大（least-wrong）的那个；靠"专家 ESVF − 模型 ESVF"匹配收敛（对应 G07—G10，§2.1.4）
  3. 为什么要拉普拉斯矩阵——幂迭代收敛由 π·P 乘积的主特征值控制，把乘积归一化成左 Laplacian 稳住它；主特征值越小 ESVF 匹配损失越小，GNN 初始主特征值更高所以收敛更快（对应 G08，§2.1.6）
  4. GNN 为什么赢线性／MLP——转移矩阵当输入带来"邻居聚合"的归纳偏置，学到的奖励与 floorspace 相关更强，还识别出矩阵里隐含的动力学（对应 G13／G16，§2.1.5＋§3.3）

### 输出成果

- `REPRODUCE.md`
- `results/` 全部图表（含 `results/golden/` 与自写结果的并排对照）
- 组会三件套：自画流程图＋PPT＋讲稿（含一次计时模拟记录）
- 给导师的一页摘要：方法链条图 ＋ 结果表 ＋ 三条结论 ＋ 两个风险

### GitHub提交

```bash
git commit -am "G18: 消融与复现报告，一个月复现里程碑交付"
```

## 今日成果验收

- - [ ] 四条奖励网络的 loss 曲线在最终数据上可解释
- - [ ] 复现出两条定性结论：① GNN 奖励与建筑面积相关性更强；② Linear／MLP 主要放大原转移矩阵结构，GNN 显著改变连接的稠密化模式
- - [ ] 报告含失败清单（没有失败清单的复现报告不可信）
- - [ ] 论文复现进度：100%（方法级；数值级取决于是否拿到官方数据）
- - [ ] 四个必懂知识点闭卷各讲 2 分钟不卡壳（清单见"组会汇报三件套"）

------

# Day15—Day18阶段验收（最终验收标准·2026.10.30 晚）

一句话目标：**不是"我把强化学习学会了"，而是"我能读懂这篇论文每个模块、能改并能跑作者的代码"。**

必须达到的最低程度：

```text
MDP        → 知道 State/Action/Reward/Transition/Policy 在本文各对应什么
Bellman    → 能写硬/软两版，并知道本文用软的（策略是分布，不是最短路）
值/策略迭代 → 30 行 numpy，能解释谱半径与收敛
IRL        → 能说清与 RL 的正反关系、奖励歧义性
MaxEnt IRL → 能默写梯度式，并独立实现端到端版本
ESVF       → 知道"策略传播访问频率"＝幂迭代＝论文的核心计算
Laplacian  → 亲历一次发散并复现稳定化手段
图与 GNN    → 手写 dense GCN 对齐 PyG；GraphConv 与 GCN 的差别说得出
PyG        → Data/edge_index/x/edge_weight/GCNConv/GraphConv 会用
论文        → 能完整解释 §2.1 五小节与 §2.2 之间的数据流
复现        → 结果表 + 奖励分布图 + 消融 + 失败清单
```

### 当前能力等级（Day18 之后）

```text
Python 开发              ★★★★☆
PyTorch / MLP / BN       ★★★★★
NumPy / 特征值 / 稀疏矩阵   ★★★★★
MDP / 价值 / 迭代          ★★★★☆
IRL / MaxEnt IRL          ★★★★☆   ← 一个月从零到此，即达标
GNN / GCN / PyG           ★★★☆☆
GeoAI 矢量数据工程           ★★★★☆   ← Day15 补上的关键缺口
论文复现与消融实验           ★★★☆☆
CNN / RNN / GAN ＋ C-GAN / 流模型（V4.0 所得＋支线销账） ★★★★☆   ← 保持，本月不新增投入
```

------

# 附录 A：学习资源总清单（视频 7.8 h 全部转 🎞 存档·有空或卡壳回看）

> **10.08 换轨说明**：以下视频与读物**全部暂停**，不再计入每日任务；每日理论输入改为主线——精读 `thirdparty/geoirl-official/`（`causal_maxent.py`／`transitions.py`／`rewards.py`／`trajectories.py`，函数↔论文公式对照，见 G02—G18 各天"代码精读"栏）＋ Ziebart 2008／Kipf & Welling 2017 两篇短文。本表保留是为了：① 有空当娱乐回看；② 概念卡壳时按"只看这些"列精准补一段。

| 资源 | 标题／主讲 | 只看这些 | 时长 |
| --- | --- | --- | --- |
| `hrl.boyuai.com`（无 BV·**字典·卡壳才翻**） | 动手学强化学习｜SJTU APEX 张伟楠／沈键／俞勇·在线免费全文＋每章可跑 notebook（GitHub `boyu-ai/Hands-on-RL`） | 第 1、3、4 章（G01—G04 对应小节）＋第 4 章末 FrozenLake（G05 对照）＋前沿篇模仿学习章（G06 按需）；第 2、5 章及 DQN 以后**不读** | 约 3 h（存档·不计进度） |
| 《上交强化学习课》（官方 UP「张伟楠SJTU」·**理论视频·存档**） | 课堂实录·SJTU 2024 春·与主线书同一作者、逐讲对应（勿用搬运号合并版） | 第1讲I `BV1jUHdePEUZ`／第3讲I `BV1ZaHfekEyL`／第3讲II `BV1D2HfewEmk`／第4讲 `BV1S2HfewEQa`／第5讲I `BV13yHfeeEo2`／第12讲I `BV1DfpzeLEmC`／第12讲II `BV1Qopze2Ee1`；第 2、6–11、13–16 讲**不看** | 约 3.2 h（存档） |
| `BV1sd4y167NS`（**选看·卡壳回查**） | 强化学习的数学原理｜西湖大学 WindyLab（白板纯推导·无代码） | 概念抠不平时回看对应段（P1–P15、P34–P35），不通看 | 不计封顶 |
| `BV1Pd4y1u77J`（对照参考·**选看**） | EasyRL 蘑菇书作者手把手实现强化学习算法｜Datawhale（书 `datawhalechina.github.io/easy-rl`） | 主线卡壳时按算法回查对应段，不通看 | 选看（不计封顶） |
| `BV1JA411c7VT` | 李宏毅 2021｜Datawhale 授权国语版 | P34（对照·奖励歧义性一段） | 27 min |
| `BV1NjH4eYEyZ` | CS285 2023 中英字幕｜Berkeley | P82–P83 国庆预热；P84–P85（G07 对照·英文原版推导） | 59 min |
| `BV16v4y1b7x7` | 图神经网络综述和学习路径｜同济子豪兄 | 单集 | 53 min |
| `BV1Hs4y157Ls` | 图卷积神经网络 GCN｜同济子豪兄 | 单集 | 63 min |
| `BV1sg4y1j7n9` | 生存分析（1）｜北美统计学博士生 | 单集 | 25 min |
| `BV1pE41117C2` | 刘相宇：RL with Deep Energy-Based Policies | 单集 | 8 min |
| `BV1Vw411R7Fj` | GCN 数学原理：谱图理论与傅立叶（**选看**） | 单集 | 59 min |
| `BV1By4y1A7K8` 等 3 个 | C-GAN（李宏毅2021 GAN三·条件生成）＋归一化流入门（中配 12min／标准化流与 INN 30min）（假期碎片，销导师账·09.30 更正） | 见国庆任务 | 视频约 1.4 h（阅读与手推另计 4.5 h） |

> 若某天的视频开始出现 replay buffer、actor、critic、clip ratio——立刻停，那是走偏信号。《动手学强化学习》与《上交强化学习课》同理：第 4 章／第 4 讲以后（model-free 与深度 RL）与本文无关，不跟进度；第 12 讲只取 IRL 段，GAIL 略读。

------

# 附录 B：风险与降级预案

| 风险 | 概率 | 降级方案 |
| --- | --- | --- |
| figshare 数据／代码打不开 | **已消除**（2026.09.29 官方代码与数据已下载至 `thirdparty/geoirl-official/`） | 若官方文件格式实测不可用，Day15 的 `make_synthetic` 仍是最后防线：全程用合成建筑数据，报告改为方法级复现；案例地换成国内城市＋公开出租车轨迹 |
| `torch_geometric` 装不上 | 中 | 用 Day12／Day13 的 dense 降级实现（n≈1000 时稠密矩阵笔记本足够），报告注明实现差异 |
| 显存不足（6 GB，空闲约 5 GB） | 中 | 本任务稠密矩阵与极小网络为主；放大规模时先减 n，再考虑 `float32`→按块传播；关掉微信/QQ/浏览器等 C+G 进程 |
| IRL 不收敛（loss 不降） | 高（Day16） | 依次查：① 特征矩阵信息量；② d_expert 的构造口径；③ 幂迭代是否需归一化（回 Day08）；最后才调学习率 |
| 课程／助教任务挤占 | 高 | 优先保 Day15／16／17 三天（数据＋训练＋评估）；理论输入一律压进"代码精读＋短文献"（视频已转 🎞 存档，本就不占进度） |
| 组会日期早于 10.30 | 待定（需向导师确认） | 10.08 合流预案：G15—G17（数据＋训练＋指标）不动；G18 消融砍到"SGS vs IED＋密度"两条；汇报三件套提前到组会前两天；仍不够则 G09／G10 的 qzed 对照与发散实验降为只精读不跑码 |

------

# 附录 C：本计划的"不要"清单（同样重要）

1. **不要先学 DQN**，不要碰经验回放／目标网络／ε-贪心——本文的 P 是给定的，不做 model-free 采样。
2. **不要深入 PPO／SAC／DDPG／A3C／TRPO／Actor-Critic**——它们属于大模型对齐那条线。
3. **不要把 RNN／LSTM 继续深入**——研究对象虽是 trajectory，但论文里没有任何递归网络。
4. **不要啃完整 IRL 综述**（MaxEnt／GAIL／AIRL／Bayesian／Adversarial 全看）——只需 `RL → IRL → MaxEnt IRL`。
5. **GNN 不要学 GAT／GraphSAGE／GIN／GCNII／HAN／HGT**——论文只有 GCN 与 GraphConv。
6. **不要碰 LangChain／RAG／Agent／大模型微调**（三年规划写着"12 月前不要碰 LangChain"）。
7. **不要找"更全的 RL 视频合集"**——资源已配齐，再找就是拖延。
8. **不要相信"全 748 集／学完即可就业／拿走不谢"标题的课**，判据：UP 是否本人、有无讲义或 GitHub、分P 标题是否与其他账号逐字重复、投币收藏比。

------

# 附录 D：与 11 月计划的接口

11 月恢复 V4.0 时从 Day44（制图综合理论＋1 篇综述）起，直接接 Day53—62 的 U-Net 建筑物提取项目。本月三项能力可原样迁移：

| 本月所得 | 11 月 U-Net 项目的用法 |
| --- | --- |
| GeoPandas 矢量属性工程（Day15） | 建筑物样本的属性标注、面积／形状指标与样本分组 |
| 距离／密度矩阵与图结构 | 化简前后拓扑一致性评价（制图综合专用指标） |
| 可微的"目标函数＋期望匹配"训练范式 | 自定义评价 loss／多任务 loss 的写法模板 |
