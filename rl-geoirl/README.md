# rl-geoirl

> GeoIRL 论文复现工程（IJGIS 2026）
>
> 有效学习日：2026.09.30 ＋ 10 月工作日，共 18 天

---

# 📖 项目简介

本目录用于复现预研阶段选定的图逆强化学习论文，完整走通"从人类轨迹反推奖励，再用学习到的策略生成新轨迹"这条方法链。

复现对象：

> Zi Hen Lin, A. Yair Grinberger, Daniel Felsenstein.
> *Generating geospatial trajectories with incomplete data using graph inverse reinforcement learning*.
> International Journal of Geographical Information Science, 2026.
> DOI：[10.1080/13658816.2026.2658065](https://doi.org/10.1080/13658816.2026.2658065)
> 官方数据与代码：[10.6084/m9.figshare.29554394](https://doi.org/10.6084/m9.figshare.29554394)（2026.09.29 已下载至 `thirdparty/geoirl-official/`，只读参考，不入库）
> 本地 PDF：`../papers/Generating geospatial trajectories with incomplete data using graph inverse reinforcement learning.pdf`

配套任务书：[docs/GeoIRL论文复现30天学习计划V1.0（每日具体任务安排）.md](docs/GeoIRL论文复现30天学习计划V1.0（每日具体任务安排）.md)

论文四要素：

- 案例地：耶路撒冷，7,692 条 GPS 出行轨迹，学习子集 1,014 栋建筑
- 状态空间：建筑节点；转移矩阵由 Simple Gravity Score（面积／距离²）行归一化并稀疏化到 10% 密度
- 奖励模型：Linear / MLP / GCN / GraphConv 四种，参数量 11 / 1569 / 1569 / 2945
- 评估方式：聚合指标（Wasserstein 距离、inverse CPC、NFM），不做逐条轨迹相似度

---

# 🎯 学习目标

## 第一阶段（G01-G05）

### MDP、价值函数与迭代

State、Action、Reward、Transition、Policy

Return 与折扣因子 γ

Bellman 方程（解析解与迭代解）

软 Bellman 与 softmax 策略

值迭代与策略迭代

ESVF＝策略传播的访问频率


↓

## 第二阶段（G06-G10）

### IRL 与 MaxEnt IRL

RL 与 IRL 的正反关系

奖励歧义性与最大熵原则

特征期望匹配梯度

ESVF 幂迭代的发散与左 Laplacian 稳定

从零实现 6×6 MaxEnt IRL


↓

## 第三阶段（G11-G14）

### 图结构、拉普拉斯与 GNN

邻接矩阵与三种归一化

谱半径与消息传递

GCN 的 dense 实现

PyTorch Geometric：Data、edge_index、GCNConv、GraphConv

四种奖励网络参数量对账

论文 §2 精读与伪代码骨架


↓

## 第四阶段（G15-G18）

### 数据、全链路与复现报告

GeoPandas 矢量建筑 → 特征矩阵与转移矩阵

四种网络的 IRL 训练对比

Kaplan-Meier 折扣因子与轨迹采样

Wasserstein、inverse CPC、NFM 结果表

figshare 官方实现对照与消融

交付 REPRODUCE.md ＋ 组会三件套（自画流程图、PPT、讲稿）


↓

向导师提交复现报告

---

# 📊 当前进度

GeoIRL 论文复现计划（共 18 个学习日）

```bash
██□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
Day 02 / Day 18
```

最近更新时间：

**2026-10-09**

------

# 📅 每日学习进度

## 第一阶段：MDP、价值函数与迭代（G01-G05）

- - [x] G01（09.30）MDP 五要素与论文实体对照，SGS 转移矩阵最小版
- - [x] G02（10.08）Bellman 方程的解析解与迭代解，谱半径判据
- - [ ] G03（10.09）软 Bellman 与 softmax 策略，`geoirl/irl.py` 诞生
- - [ ] G04（10.12）值迭代、策略迭代与截断策略迭代
- - [ ] G05（10.13）GridWorld 实战，验证 ESVF 两种算法等价；装 `torch_geometric`（从 G12 提前）

------

## 第二阶段：IRL 与 MaxEnt IRL（G06-G10）

- - [ ] G06（10.14）RL 与 IRL 的正反关系，奖励歧义性；**金标准**：跑 `IRL_deep.ipynb` Linear 流程 → `results/golden/`
- - [ ] G07（10.15）最大熵原理，特征期望差梯度
- - [ ] G08（10.16）ESVF 幂迭代发散与左 Laplacian 稳定（论文贡献②）
- - [ ] G09（10.19）读 `qzed/irl-maxent`，标注三段实现
- - [ ] G10（10.20）从零实现 6×6 端到端 MaxEnt IRL

------

## 第三阶段：图与 GNN（G11-G14）

- - [ ] G11（10.21）行归一化／对称归一化／左 Laplacian 的谱半径对比
- - [ ] G12（10.22）手写 dense GCN 并与 PyG 数值对齐
- - [ ] G13（10.23）四种奖励网络实现与参数量对账
- - [ ] G14（10.26）论文 §2 精读，Figure 1／3 翻成 `skeleton.py`；核实"空间错配"批评成不成立

------

## 第四阶段：数据、管线与报告（G15-G18）

- - [ ] G15（10.27）矢量建筑 → 特征矩阵与 SGS／IED 转移矩阵
- - [ ] G16（10.28）四网络 IRL 训练对比（loss 与主特征值曲线）
- - [ ] G17（10.29）K-M 折扣、轨迹采样、Wasserstein／CPC／NFM 结果表
- - [ ] G18（10.30）figshare 对照、消融实验、`REPRODUCE.md`；组会三件套（流程图＋PPT＋讲稿）＋四知识点自检

------

# 🧩 模块诞生日程

`geoirl/` 是逐步长出来的包，每个文件只在指定那天创建。

| 模块文件 | 创建于 | 对应论文小节 | 职责 |
| ------------------- | ---------- | ------------------ | -------------------------------- |
| `irl.py` | G03（10.09） | §2.1、§2.1.5 | 软 Bellman 与中间策略，全项目唯一实现 |
| `esvf.py` | G05（10.13） | §2.1、§2.1.6 | 按策略传播访问频率，含归一化稳定版 |
| `rewards.py` | G13（10.23） | §2.1.5 | Linear、MLP、GCN、GraphConv |
| `geo_data.py` | G15（10.27） | §2.1.2、§2.1.3 | 矢量建筑 → 特征矩阵 F、转移矩阵 P |
| `sample.py` | G17（10.29） | §2.2 | K-M 折扣下的轨迹采样 |
| `metrics.py` | G17（10.29） | §3.4、式(3) | Wasserstein、inverse CPC、NFM |

判断规则：这段代码明天还会被 `import` 吗？会就进 `geoirl/`，不会就留在 `rl/DayNN/`。

------

# 📂 仓库目录

```text
rl-geoirl/
│
├── docs/                    本任务书（每日具体任务安排）
│
├── notes/                   每日计划与日志：G00（日期）Note.md …G18
│   └── Screenshot/          当日截图，按 GNN 分目录
│
├── rl/                      每天的具体文件夹：rl/Day01 … rl/Day18（用到再建，不预造空壳）
│
├── geoirl/                  复现包本体（模块诞生日程见上表）
│
├── data/                    建筑矢量与合成数据（被根目录 .gitignore 排除，不入库）
│
├── results/                 结果表与图表（.csv 已单独放行，交付用）
│
├── thirdparty/              只读参考仓库（已在 .gitignore 排除）：geoirl-official/ 官方代码＋数据（09.29 已下载）、irl-maxent/（G09 起）
│
├── requirements.txt          本项目依赖（不覆盖根目录 V4.0 那份）
│
├── REPRODUCE.md             复现报告（G18 产出，目前还没有）
│
└── README.md                本文件
```

------

# 🗺️ 技术路线

```text
经验 GPS 轨迹（专家行为）
        │
        ↓
把城市建筑抽象为状态空间（MDP）
        │
        ↓
构建转移矩阵（SGS／IED → 行归一化 → 稀疏化）
        │
        ↓
构建特征矩阵（多维度分组，传播稀疏观测）
        │
        ↓
MaxEnt IRL：软策略 → ESVF 幂迭代 → 特征期望匹配
        │
        ↓
反演奖励函数（Linear／MLP／GCN／GraphConv）
        │
        ↓
K-M 生存概率作折扣因子 → 采样生成新轨迹
        │
        ↓
聚合指标评估（Wasserstein／inverse CPC／NFM）
```

------

# 📚 学习资源

| 内容 | 来源 |
| -------------------- | ---------------------------------- |
| **理论输入主线（10.08 换轨）** | 官方代码精读：`thirdparty/geoirl-official/`（`causal_maxent.py`／`transitions.py`／`rewards.py`／`trajectories.py`，函数↔论文公式对照）＋ Ziebart 2008、Kipf & Welling 2017 两篇短文 |
| 强化学习字典（卡壳才翻） | 《动手学强化学习》SJTU APEX（`hrl.boyuai.com` 第 1／3／4 章；GitHub `boyu-ai/Hands-on-RL`） |
| 🎞 理论视频存档（暂不看） | 张伟楠《上交强化学习课》（官方 UP「张伟楠SJTU」·只看第 1／3／4／5I／12 讲；勿用搬运号合并版） |
| 🎞 数学推导存档（卡壳回查） | 西湖大学 WindyLab（`BV1sd4y167NS`·白板纯推导无代码·不通看） |
| 🎞 逆向强化学习存档 | 李宏毅 2021（`BV1JA411c7VT`，只看 P34） |
| 🎞 MaxEnt IRL 存档 | CS285 2023 中英字幕（`BV1NjH4eYEyZ`，P82–P85） |
| 🎞 图神经网络存档 | 同济子豪兄 CS224W 中文精讲（`BV16v4y1b7x7`、`BV1Hs4y157Ls`） |
| 🎞 谱图理论与 GCN 数学存档 | 日常半躺（`BV1Vw411R7Fj`，选看） |
| 🎞 生存分析与 K-M 存档 | 北美统计学博士生（`BV1sg4y1j7n9`） |
| 🎞 最大熵值函数（soft Q）存档 | 刘相宇（`BV1pE41117C2`） |
| IRL 参考实现 | `qzed/irl-maxent`、`G-Lauz/maxent_deep_irl`、`soma11soma11/MEIRL` |
| 图与稀疏计算 | networkx、scipy.sparse、PyTorch Geometric 官方文档 |

每日理论输入＝代码精读＋短文献，≤55 分钟；原视频清单（合计约 7.8 h）10.08 起全部转 🎞 存档——暂不看、不计进度，有空或卡壳时按任务书附录 A 回看。其余时间全部用于写代码。

------

# ⚠️ 风险与降级预案

| 风险 | 降级方案 |
| ---------------------- | ---------------------------------------------- |
| figshare 数据或代码拿不到 | **已消除**：官方代码与数据已在 `thirdparty/geoirl-official/`（2026.09.29 下载）；若格式实测不可用再退回合成建筑数据，报告改为方法级复现 |
| `torch_geometric` 装不上 | 用 G12／G13 的 dense 降级实现（n≈1000 稠密矩阵笔记本足够），报告注明差异 |
| 显存只有 6 GB | 最大矩阵 1,014×1,014（float32 约 8 MB）远小于显存，实测 CUDA 比 CPU 快约 19×；真溢出就把该步退回 CPU，不阻塞 |
| IRL 不收敛 | 先查特征矩阵信息量与专家期望口径，最后才调学习率 |
| 课程或助教任务挤占时间 | 优先保 G15／G16／G17 三天，视频压到 1.5 倍速或砍选看项 |

------

# 💻 开发环境

| 软件 | 版本／说明 |
| ------------ | --------------------------------- |
| conda 环境 | `geoirl`（`D:\conda_envs\geoirl`，Python 3.11.16） |
| NumPy、SciPy | 2.4.6 / 1.17.1 —— 数值计算、稀疏矩阵、特征值 |
| pandas、matplotlib | 3.0.6 / 3.11.2 |
| GeoPandas、Shapely | 1.2.0 / 2.1.2（GEOS 3.14.1）；pyogrio 0.13.0（GDAL 3.13.3／PROJ 9.8.1） |
| networkx | 3.6.1 —— 图结构与连通分量分析 |
| lifelines | 0.30.0 —— Kaplan-Meier 交叉验证（主实现手写） |
| PyTorch | 2.11.0+cu128（CUDA 12.8，RTX 3060 Laptop 6 GB；torch_geometric 到 G12／G13 再装） |
| Git、PyCharm | Community Edition；解释器 `D:\conda_envs\geoirl\python.exe`，`rl-geoirl/` 已标 Sources Root |

装机时记下的两条规则：

- torch 必须走官方源 `pip install torch --index-url https://download.pytorch.org/whl/cu128`，清华 PyPI 镜像的 torch 会多拖约 2 GB 的 nvidia 依赖
- 被 pip 接管过的包不要再 `conda install` 去升（torch 钉住 setuptools<82，混管会互相破坏）

------

# 🔬 复现能力建设

本目录不仅记录代码，同时训练科研工作的完整闭环：

- 论文公式到代码的翻译
- 合成数据先行验证方法正确性
- 与官方实现的对照与差异说明
- 消融实验设计（转移矩阵类型、图密度、网络结构）
- 结果可视化与聚合指标评估
- 复现报告与失败清单撰写

------

# 📌 Commit规范

统一采用：

```text
G01: 完成MDP实体对照与SGS转移矩阵

G08: 复现ESVF发散与Laplacian稳定

G15: 完成特征矩阵与转移矩阵数据管线

G18: 交付复现报告与消融结果
```

用 `G` 前缀与 V4.0 主线的 `DayNN：` 区分，方便日后按研究线过滤提交历史。

------

# 🔗 与 V4.0 计划的关系

本目录期间，`python_basic/`、`pytorch/`、`notebooks/` 的 V4.0 主线冻结。

- 导师要求的 GAN 先修：最简 GAN（MNIST）已于 2026.09.29 在 `../pytorch/Day43/GAN_MNIST.py` 完成；余下先修按导师 09.30 更正为 **C-GAN 与流模型**（不再要 CycleGAN），排在国庆假期碎片时间，10.20 晚兜底销账
- V4.0 从 Day44（制图综合理论）恢复，U-Net 建筑物提取顺延至 2026.11
- 本月可迁移回主线的能力：GeoPandas 矢量属性工程、距离与密度矩阵、可微的期望匹配训练范式

------

# 📜 说明

本目录仅用于个人科研预研与论文复现练习。

> 复现的目标不是把强化学习学会，
>
> 而是能把这篇论文每个核心模块读懂、改得动、跑得起来。
