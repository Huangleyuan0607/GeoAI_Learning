# rl-geoirl

> GeoIRL论文复现与学习工程；计划2026.10.14—2026.10.29。  
> 总体计划统筹阶段任务，每日计划记录学习、源码测试和实际成果。

# 项目简介

复现 Zi Hen Lin、A. Yair Grinberger、Daniel Felsenstein 的 *Generating geospatial trajectories with incomplete data using graph inverse reinforcement learning*，IJGIS，2026。
[论文DOI](https://doi.org/10.1080/13658816.2026.2658065) · [本地论文](../papers/Generating%20geospatial%20trajectories%20with%20incomplete%20data%20using%20graph%20inverse%20reinforcement%20learning.pdf) · [官方材料来源](https://doi.org/10.6084/m9.figshare.29554394) · [官方说明](thirdparty/geoirl-official/README.md)

论文在建筑访问资料不完整时学习建筑奖励，再生成总体统计接近真实出行的建筑访问序列。图卷积表达奖励，IRL根据行为统计提供奖励学习依据。图节点是建筑，输出不是连续GPS补全或逐条轨迹复刻。

**保护目录**：thirdparty/geoirl-official/全部文件及子目录严格不移动、重命名、删除、覆盖或修改。

# 学习目标

[总体学习计划V2](docs/GeoIRL论文复现学习计划_V2.md) · [当前N01每日计划](notes/N01（2026.10.14）每日计划.md) · [N01截图建议](notes/N01（2026.10.14）每日计划.md)

每天先视频/教材原理及必要代码，再论文应用；一天一个源码测试。“参考代码”直接给测试程序，不放教材入口。
P0必须；P1条件允许；P2汇报后。最低交付是可解释模型、可复查验证或阻塞、来源清楚的PPT；完整复现不因小测试通过自动成立。

## 第一阶段（N01—N04）

### MDP、价值函数与迭代

10/14–10/17：从N01认识IRL框架，学习MDP、奖励/V/Q、标准Bellman与Soft策略；对照转移、奖励和价值算子。N04周六轻量。

## 第二阶段（N05—N07）

### IRL 与 MaxEnt IRL

10/19–10/21：访问量、专家目标、最大熵IRL和外部梯度；完成单轮Linear验证或定位阻塞。P1再做稳定正式训练。

## 第三阶段（N08—N09）

### 图结构、拉普拉斯与GNN

10/22–10/23：图表示、必要归一化、聚合和GCN/GraphConv奖励；不扩展完整谱图课程，不将作者图算子命名视为标准定义。

## 第四阶段（N10—N14）

### 数据、全链路与复现报告

10/24–10/29：限时采样、可靠指标、冻结成果；最后两天PPT与演练。复查已有结果，不在汇报前新开大实验。

# 当前进度

当前学习日：N01（2026.10.14）；状态：未开始；更新日期2026-10-14。
学习进度按当天验收更新。

```bash
学习进度：0 / 14（0%）
□□□□□□□□□□□□□□
核心学习：0 / 12
汇报准备：0 / 2
```

全部当日P0通过验收后计完成，P1不影响计数；休息日不计分母。状态：未开始、进行中、已完成、阻塞；证据写每日文件。
工作日4–5小时；10/17、10/24周六2–3小时；10/18、10/25周日休息不生成计划。10/30至月底缓冲；10/31周六仍控制2–3小时。

# 每日学习进度

只生成首日N01，后续在前一学习日结束、收到真实反馈后细化并添加链接。周六结束生成周一，旧勾选不迁入。以下未勾选不代表文件已经生成。

## 第一阶段：MDP、价值函数与迭代（N01—N04）

- [ ] [N01（2026.10.14）：IRL全貌、MDP与建筑转移](notes/N01（2026.10.14）每日计划.md)
- [ ] N02（2026.10.15）：奖励、回报、策略与V/Q
- [ ] N03（2026.10.16）：Bellman与动态规划
- [ ] N04（2026.10.17）：熵、Soft策略与停止选项；周六2–3小时

## 第二阶段：IRL与MaxEnt IRL（N05—N07）

- [ ] N05（2026.10.19）：IRL与访问量
- [ ] N06（2026.10.20）：最大熵IRL与奖励更新
- [ ] N07（2026.10.21）：单轮IRL与Linear验证

## 第三阶段：图与GNN（N08—N09）

- [ ] N08（2026.10.22）：图表示、边方向与消息传递
- [ ] N09（2026.10.23）：GCN、GraphConv与IRL连接

## 第四阶段：数据、管线与报告（N10—N14）

- [ ] N10（2026.10.24）：生成策略、轨迹与结束规则
- [ ] N11（2026.10.26）：距离统计与指标核对
- [ ] N12（2026.10.27）：可靠指标与成果冻结
- [ ] N13（2026.10.28）：制作汇报PPT
- [ ] N14（2026.10.29）：演练、复查与修订

# 模块诞生日程

沿用原栏目，**本轮不安排新包模块诞生或重构geoirl/**。下表只是每日小测试位置，不是已创建文件。测试代码放在每日“参考代码”，学习时保存；额外自选练习以后另行讨论。

| 学习日 | 测试脚本位置 | 状态 |
| --- | --- | --- |
| N01 | `rl/N01/test_simple_gravity.py` | 待实际学习时保存 |
| N02 | `rl/N02/test_linear_reward.py` | 待实际学习时保存 |
| N03 | `rl/N03/test_value_update.py` | 待实际学习时保存 |
| N04 | `rl/N04/test_soft_policy.py` | 待实际学习时保存 |
| N05 | `rl/N05/test_expected_svf.py` | 待实际学习时保存 |
| N06 | `rl/N06/test_irl_gradient.py` | 待实际学习时保存 |
| N07 | `rl/N07/test_irl_step.py` | 待实际学习时保存 |
| N08 | `rl/N08/test_graph_aggregation.py` | 待实际学习时保存 |
| N09 | `rl/N09/test_graph_reward.py` | 待实际学习时保存 |
| N10 | `rl/N10/test_trajectory_sampling.py` | 待实际学习时保存 |
| N11 | `rl/N11/test_segment_statistics.py` | 待实际学习时保存 |
| N12 | `rl/N12/test_cpc.py` | 待实际学习时保存 |
| N13 | `rl/N13/test_report_metric.py` | 待实际学习时保存 |
| N14 | `rl/N14/test_reward_replay.py` | 待实际学习时保存 |

# 仓库目录

```text
rl-geoirl/
├── README.md
├── docs/
│   ├── GeoIRL论文复现学习计划_V2.md
│   └── history/
├── notes/
│   ├── N01（2026.10.14）每日计划.md
│   ├── history/
│   └── Screenshot/
│       └── history/
├── rl/
│   └── history/
├── geoirl/
├── results/
├── thirdparty/
│   └── geoirl-official/
└── requirements.txt
```

仅展示学习相关目录，.idea/等原目录仍原位。history保存旧资料；目录按实际学习需要创建。
每日计划、理解与收获记录在同一文件；测试在rl/Nxx/，截图在notes/Screenshot/Nxx/。正式results/实验名称/记录入口、数据范围、参数、种子、样本、时间、状态，不创建空指标。
PPT在docs/GeoIRL_导师汇报_2026年10月.pptx，N13/N14同一文件。[完整文件约定](docs/GeoIRL论文复现学习计划_V2.md)

# 技术路线

```text
专家行为/建筑属性 → 预计算CSV → 研究区对齐 → 图与边界
                                            ↓
建筑特征/图 → 奖励模型 → 奖励 → 内部策略 → 期望访问量
                 ↑                          ↓
                 └──────── 与专家目标比较后更新 ┘
训练结束 → 另行构造生成策略 → 建筑访问序列 → 集合评价
```

基础RL解释奖励怎样产生行为；IRL还需行为统计匹配和奖励更新。每天把知识定位到这条路线，标准原理、论文说明和源码分别核对。

# 学习资源

[总计划附录A](docs/GeoIRL论文复现学习计划_V2.md)汇总精读范围与源码导航。

- [张伟楠视频合集](https://space.bilibili.com/3546754433681656/lists/4126508?type=season) / [教师课程与课件](https://wnzhang.net/teaching/sjtu-rl-2024/index.html)：简介选看、MDP/动态规划重点、模仿学习选IRL相关。时长按课程目录，内部段落在观看时定位。
- [动手学强化学习](https://hrl.boyuai.com/)：第3/4章必要部分、14.2–14.3、15.1。视频讲次与教材章号分别标注；教材代码作原理对照，不重做完整课程。
- [最大熵IRL](https://www.cs.cmu.edu/~bziebart/publications/maximum-entropy-inverse-reinforcement-learning.html)：补统计匹配和奖励更新；教材主要BC/GAIL，不能替代本论文算法。
- [GCN入门](https://tkipf.github.io/graph-convolutional-networks/) / [PyG入门](https://pytorch-geometric.readthedocs.io/en/latest/get_started/introduction.html)：补图表示、聚合与前向。

# 风险与降级预案

[总计划附录B](docs/GeoIRL论文复现学习计划_V2.md)保留已核实疑点和测试方向。
优先检查专家目标/ESVF尺度、价值算子、图归一化/density、训练与生成折扣、NFM索引/固定5005、补零距离平均、最佳奖励与最终模型来源。
以上问题来自源码分析。研究区1014栋建筑、10维特征已由材料核查；完整上游特征与长度权重程序仍需确认。
小测试有规模/停止限制；不能用1epoch保证所有while停止。问题未解时交付可解释步骤、阻塞与下一步，不编造结果。N12后冻结范围。

# 开发环境

历史解释器为D:\conda_envs\geoirl\python.exe（Python3.11）；文件目前存在，NumPy/Pandas/PyTorch/PyG导入与GPU性能在正式运行前检查。历史记录的显卡为RTX3060 Laptop，GPU流程需另行验证。
[项目依赖](requirements.txt) / [官方依赖](thirdparty/geoirl-official/requirement.txt)不同，后续按实际问题检查，不整套重装。管理员权限或系统配置操作先征求同意。
N01参考代码只使用官方simple_gravity原样节选，避开整个模块的地图绘图导入；不表示全量模块导入成功。

# 复现能力建设

目标是能解释、会验证、能记录。每天一个源码小测试，先手算或预测，再运行、对照与解释。“参考代码”给出测试程序，学习笔记整理原理与论文对应。
[现有复用实现说明](geoirl/README.md)保留，历史任务约定不表示模块已完成。必要源文件和正式记录保留，不以文件数量判断学习成果。

# Commit规范

提交可沿用G前缀并附N编号，例如G-N01: 验证建筑移动权重。是否提交/推送由实际需要决定，不计P0；
提交前核对变更范围，只加入当天需要保存的学习文件。

# 与 V4.0 计划的关系

旧总计划记录了与GeoAI主线的历史衔接，本轮优先GeoIRL。其他课程、GAN/U-Net或后续安排不自动沿用、不擅自改动；11月工作根据导师反馈和本轮问题再确定。

# 说明

总体计划在docs/，每日计划在notes/。按四阶段和N编号组织；首日先有计划，其他根据真实反馈逐日生成。
“今日收获”自由填写；截图说明内容、时机、用途与文件名，通常2–4张以内、按需，不代替实际结果。未保存图片不插入无效链接。
论文图、官方旧输出与本人执行区分；全部P0验收后更新进度。后续目录架构变更先提方案，官方目录保持完全不变。
任务结束仅清理本次生成且不再需要的临时产物；正式成果、必要源码/配置/依赖和历史资料保留。

**历史资料入口**

历史内容可查阅；旧任务规则、旧勾选和示例输出不作为当前成果。原归档位置保持不变。

- [旧总体计划V1](docs/history/GeoIRL论文复现30天学习计划V1.0（每日具体任务安排）.md)
- [旧两页汇报PPT](docs/history/组会复现进展_两页.pptx)

| 旧笔记 | 旧练习 | 旧截图 |
| --- | --- | --- |
| [G00](notes/history/G00（2026.09.29）Note.md) | — | — |
| [G01](notes/history/G01（2026.09.30）Note.md) | [Day01](rl/history/Day01/) | [G01](notes/Screenshot/history/G01/) |
| [G02](notes/history/G02（2026.10.08）Note.md) | [Day02](rl/history/Day02/) | [G02](notes/Screenshot/history/G02/) |
| [G03](notes/history/G03（2026.10.09）Note.md) | [Day03](rl/history/Day03/) | [G03](notes/Screenshot/history/G03/) |
