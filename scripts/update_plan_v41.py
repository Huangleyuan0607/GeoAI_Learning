# -*- coding: utf-8 -*-
"""按方案A修订《GeoAI预研60天学习计划》：
   插入第四阶段 GAN基础（Day46-52），原第四阶段顺延为第五阶段（Day53-67），
   原GAN专题改为第六阶段 GAN项目实战与文献调研（Day68-73），选学 Day74。"""
import re
import shutil
from datetime import date, timedelta

P = r"D:\CCNU\PreLearning_Plan\GeoAI-Learning\docs\GeoAI预研60天学习计划V4.0（每日具体任务安排）.md"
BAK = P + ".bak"

def dstr(d):
    return f"{d.year}.{d.month:02d}.{d.day:02d}"

def shift(s, days):
    y, m, dd = map(int, s.split("."))
    return dstr(date(y, m, dd) + timedelta(days=days))

text = open(P, encoding="utf-8").read()
shutil.copyfile(P, BAK)

A_S4 = "# 第四阶段：地图制图综合与Transformer入门（Day46-Day60）"
A_S5 = "# 第五阶段：GAN生成对抗网络专题（Day61-Day66）"
A_D61 = "# Day61（2026.08.27）"
A_D63 = "# Day63（2026.08.29）"
A_D64 = "# Day64（2026.08.30）"
A_D65 = "# Day65（2026.08.31）"
A_D66 = "# Day66（2026.09.01）"
A_D67 = "# Day67（选学，2026.09.02）"
A_S5A = "# 第五阶段验收（Day61-Day66）"

for a in [A_S4, A_S5, A_D61, A_D63, A_D64, A_D65, A_D66, A_D67, A_S5A]:
    assert text.count(a) == 1, f"anchor not unique: {a}"

i_s4, i_s5 = text.index(A_S4), text.index(A_S5)
i_d61, i_d63, i_d64, i_d65, i_d66, i_d67, i_s5a = (
    text.index(A_D61), text.index(A_D63), text.index(A_D64),
    text.index(A_D65), text.index(A_D66), text.index(A_D67), text.index(A_S5A))

head = text[:i_s4]
s4 = text[i_s4:i_s5]
d63, d64, d65 = text[i_d63:i_d64], text[i_d64:i_d65], text[i_d65:i_d66]
d67 = text[i_d67:i_s5a]
tail = text[i_s5a:]

# ---------- head：版本说明 + “下一阶段”衔接 ----------
old_hdr_start = head.index("> **计划版本说明")
old_hdr_end = head.index("**\n", head.index("即：**实际学习周期")) + 2
new_hdr = """> **计划版本说明（V4.0 · 方案A修订，2026.08.08）**
>
> 因导师要求“**尽快学习 GAN**”，经沟通确认采用方案A：将原第五阶段 GAN 专题的**原理部分整体提前**为一周先修阶段，主体计划顺延，现修订如下：
>
> - **Day01—Day45**：Python → PyTorch → CNN → 制图综合理论，编号与内容不变。
> - **Day46—Day52**：**新增第四阶段「GAN 基础专题（先修）」**：GAN 原理与最简 GAN 实战、CycleGAN 无配对图像翻译原理（原 Day61—Day62 内容前移并扩充）。
> - **Day53—Day67**：原第四阶段「地图制图综合与 Transformer 入门」（语义分割 / U-Net / Transformer / 导师论文）整体顺延 +7 天，内容不变。
> - **Day68—Day73**：原第五阶段改为第六阶段「**GAN 项目实战与文献调研**」：CycleGAN / starGAN 开源项目实战、图像补全、GAN×制图综合文献调研与专题总结。
> - **Day74（选学）**：GAN 图像超分辨率。
>
> 即：**实际学习周期为 Day01—Day73（73 天），选学上限 Day74。**
"""
head = head[:old_hdr_start] + new_hdr + head[old_hdr_end:]

head = head.replace("# 下一阶段 Day46-Day60", "# 下一阶段 Day46-Day67")
head = head.replace("进入最贴近地图制图综合研究方向的阶段：",
                    "先用一周完成导师要求的 GAN 基础先修，再进入最贴近地图制图综合研究方向的阶段：")
head = head.replace("主要内容：\n\n- FCN实现", "主要内容：\n\n- GAN原理与最简GAN实战（Day46—Day52）\n- FCN实现")
head = head.replace("CNN基础\n    ↓\n语义分割", "CNN基础\n    ↓\nGAN基础\n    ↓\n语义分割")

# ---------- 新第四阶段：GAN 基础专题（Day46-Day52） ----------
S4_NEW = """# 第四阶段：GAN基础专题·先修（Day46-Day52）

### 时间：2026.08.12—2026.08.18

## 阶段目标

> 本阶段按导师要求**提前学习 GAN**（原第五阶段的前半部分前移）。
>
> 从“判别式模型”进入“生成式模型”，本阶段先解决**原理与最简实战**，开源项目实战与文献调研保留在第六阶段（Day68—Day73）完成。
>
> 完成后应达到：
>
> - 理解生成器与判别器的对抗训练机制
> - 掌握 GAN 损失函数与训练不稳定的成因
> - 独立完成最简 GAN（MNIST）实战
> - 理解 CycleGAN 的**无配对图像翻译**思想与三类损失
> - 能说明 GAN 与地图制图综合的结合点

## 视频资源

```
GAN对抗生成网络
```

> **观看范围说明**：
>
> - **本阶段**：第一章全部（GAN原理与最简实战）、第二章 1-5（CycleGAN 数据、整体架构、PatchGAN、项目简介、数据读取）
> - **留给第六阶段**：第二章 6-10（CycleGAN 模块与实战）、第三章（starGAN架构）、第四章（starGAN实战）、第八章（图像补全）
> - **跳过**：第五章（除 5、6 两节）、第六章（变声器项目，与地图方向无关）
> - **选学**：第七章（图像超分辨率，Day74）

------

# Day46（2026.08.12）

## 今日目标

理解GAN的基本原理，掌握生成器与判别器的对抗机制。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第一章 1-对抗生成网络通俗解释
-  - [ ] 第一章 2-GAN网络组成
-  - [ ] 第一章 3-损失函数解释说明

预计时长：1小时

------

### 理论学习

理解：

GAN核心机制：

```
随机噪声
    ↓
生成器 G
    ↓
生成样本
    ↓
判别器 D
    ↓
真 / 假
```

重点理解：

- 生成器与判别器的博弈关系
- minimax 目标函数
- 损失函数与 JS 散度的关系

------

### 代码实验

创建：

```
gan_mnist/gan_data.py
```

实现：

- GAN 项目环境配置
- MNIST 数据读取模块（DataLoader，reshape 为 784 维向量）

------

### GitHub提交

```
git add .
git commit -m "Day46：完成GAN基本原理学习"
git push
```

------

# Day47（2026.08.13）

## 今日目标

掌握生成器与判别器的网络定义，完成最简GAN的代码搭建。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第一章 4-数据读取模块
-  - [ ] 第一章 5-生成与判别网络定义

预计时长：1小时

------

### 理论学习

理解：

- 生成器：噪声向量 → 全连接 → 784 维图像（输出层 Sigmoid）
- 判别器：图像向量 → 全连接 → 真/假概率（输出层 Sigmoid）
- 两个优化器**交替更新**的训练循环

------

### 代码实验

创建：

```
gan_mnist/mnist_gan.py
```

实现：

- 生成器 G 与判别器 D 定义
- 对抗训练循环骨架（先跑通 1 个 epoch）

------

### GitHub提交

```
git add .
git commit -m "Day47：完成最简GAN网络搭建"
git push
```

------

# Day48（2026.08.14）

## 今日目标

完成最简GAN完整训练，观察并分析GAN的训练不稳定问题。

## 今日任务

### 视频学习

#### 复习与自由调试

重听第一章 3-损失函数，对照训练日志理解 D/G loss 曲线含义。

预计时长：0.5小时

------

### 理论学习

重点理解：

- **训练不稳定与模式崩塌（mode collapse）**
- D loss 与 G loss 此消彼长的读法
- 常用稳定技巧：较小学习率、Adam(β1=0.5)、真实标签软标签（label smoothing）、平衡 G/D 训练步数

------

### 代码实验

完善：

```
gan_mnist/mnist_gan.py
```

实现：

- 完整训练 50+ epoch，定期保存生成样例（epoch 1 / 10 / 50 对比）
- 调参实验至少 2 组，记录现象

输出：

```
GAN训练问题记录.md
```

------

### GitHub提交

```
git add .
git commit -m "Day48：完成最简GAN实战与训练问题分析"
git push
```

------

# Day49（2026.08.15）

## 今日目标

理解CycleGAN的无配对图像翻译思想，掌握其网络组成。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第二章 1-CycleGan网络所需数据
-  - [ ] 第二章 2-CycleGan整体网络架构
-  - [ ] 第二章 3-PatchGan判别网络原理

预计时长：1小时

------

### 理论学习

理解：

无配对图像翻译：

```
域 A 图像 ──G_AB──→ 域 B 图像
                        │
                      G_BA
                        ↓
                   重建回域 A
```

重点理解：

- 为什么需要**循环一致性损失**
- PatchGAN 判别器（对局部patch判真假）
- 与制图综合的联系：**不同比例尺地图难以严格配对，正适合无配对方法**

------

### 输出成果

笔记：CycleGAN 整体架构图（手绘或 mermaid），标注两个生成器、两个判别器、三条损失的作用位置。

------

### GitHub提交

```
git add .
git commit -m "Day49：完成CycleGAN原理学习"
git push
```

------

# Day50（2026.08.16）

## 今日目标

理解CycleGAN开源项目的数据组织形式，完成数据准备。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第二章 4-Cycle开源项目简介
-  - [ ] 第二章 5-数据读取与预处理操作

预计时长：1小时

------

### 理论学习

理解：

- 无配对数据集的组织方式（trainA / trainB 两个目录）
- 图像尺寸、归一化与随机翻转等预处理策略
- 与 Day42 数据增广知识的呼应：**几何变换不需要标签同步（翻译任务无像素标签）**

------

### 代码实验

创建：

```
cyclegan_prepare.py
```

实现：

- 下载并整理一个示例数据集（如 horse2zebra，或自制的地图瓦片风格 A/B 两组图）
- 验证数据集目录结构与读取流程

------

### GitHub提交

```
git add .
git commit -m "Day50：完成CycleGAN数据准备"
git push
```

------

# Day51（2026.08.17）

## 今日目标

吃透CycleGAN三类损失与核心模块，手写验证关键计算。

## 今日任务

### 理论学习

理解：

CycleGAN三类损失：

| 损失             | 作用                         |
| ---------------- | ---------------------------- |
| 对抗损失         | 让生成结果逼近目标域分布     |
| 循环一致性损失   | 保证 A→B→A 能重建回原图      |
| identity loss    | 保持颜色/风格，抑制无谓改动  |

重点理解：

- 三类损失的权重设置（λ_cycle / λ_identity）
- 生成器主干（ResNet 风格块，呼应 Day38 残差连接）

------

### 代码实验

创建：

```
cyclegan_modules.py
```

实现：

- 手写循环一致性损失与 identity loss，随机张量验证数值正确
- 搭一个缩小版 PatchGAN 与 ResNet 生成器，验证输入输出形状

------

### GitHub提交

```
git add .
git commit -m "Day51：完成CycleGAN核心模块手写验证"
git push
```

------

# Day52（2026.08.18）

## 今日目标

完成GAN基础阶段复习与成果沉淀，为进入语义分割/U-Net主线做准备。

## 今日任务

### 理论复习

输出：

```
GAN基础总结.md
```

包含：

- GAN 原理与训练难点（附 mnist_gan 训练曲线）
- CycleGAN 无配对翻译思想与三类损失
- GAN 与制图综合、多尺度表达的结合点清单（供导师派任务时参考）

### 阶段衔接

- 预习第五阶段：语义分割任务定义（Day53 起）
- 整理本周 GAN 笔记与代码，准备向导师做一次 GAN 基础专题的小型进度汇报

------

### GitHub提交

```
git add .
git commit -m "Day52：完成GAN基础阶段总结"
git push
```

------

# GAN基础阶段验收（Day46-Day52）

完成后：

## 生成式模型基础能力

- ✅ 理解GAN的对抗训练机制
- ✅ 理解GAN训练不稳定的成因与表现
- ✅ 独立完成最简GAN（MNIST）实战
- ✅ 理解CycleGAN的无配对图像翻译思想与三类损失
- ✅ 完成PatchGAN/生成器模块与循环一致性损失的手写验证

------

"""

# ---------- 原第四阶段 → 第五阶段（Day53-Day67，顺延+7） ----------
s4 = s4.replace(A_S4, "# 第五阶段：地图制图综合与Transformer入门（Day53-Day67）")
s4 = s4.replace("### 时间：2026.08.12—2026.08.26", "### 时间：2026.08.19—2026.09.02")
s4 = s4.replace("# 第四阶段验收（Day46-Day60）", "# 第五阶段验收（Day53-Day67）")
s4 = s4.replace("本阶段是整个60天主体计划最核心的阶段。", "本阶段是整个主体计划（Day01—Day67）最核心的阶段。")
s4 = s4.replace("完成60天主体阶段（Day01—Day60）总结，形成开学前成果。", "完成主体阶段（Day01—Day67）总结，形成开学前成果。")
s4 = s4.replace("总结60天学习路线：", "总结主体阶段学习路线：")
s4 = s4.replace("60天学习路线", "主体阶段学习路线")
s4 = s4.replace("完成60天GeoAI预研总结", "完成主体阶段GeoAI预研总结")
s4 = s4.replace("- U-Net项目\n- Transformer结构", "- U-Net项目\n- Transformer结构\n- GAN图像翻译与实战")
s4 = s4.replace("- PyTorch\n- CNN\n- U-Net\n- Transformer", "- PyTorch\n- CNN\n- GAN\n- U-Net\n- Transformer")
s4 = re.sub(r"(CNN\n\n↓\n\n)(语义分割)", r"\1GAN基础\n\n↓\n\n\2", s4)
s4 = s4.replace("├── Transformer\n│\n└── README.md", "├── Transformer\n├── GAN\n│\n└── README.md")
s4 = re.sub(r"^# Day(\d+)（(2026\.\d{2}\.\d{2})）$",
            lambda m: f"# Day{int(m.group(1)) + 7}（{shift(m.group(2), 7)}）", s4, flags=re.M)
s4 = re.sub(r'^git commit -m "Day(\d+)：',
            lambda m: f'git commit -m "Day{int(m.group(1)) + 7}：', s4, flags=re.M)

# ---------- 原第五阶段 → 第六阶段（Day68-Day73） ----------
S6_INTRO = """# 第六阶段：GAN项目实战与文献调研（Day68-Day73）

### 时间：2026.09.03—2026.09.08

## 阶段目标

> 本阶段为 GAN 专题的后半部分。**GAN 原理与最简实战、CycleGAN 原理已在第四阶段（Day46—Day52）提前完成**（导师要求尽快学 GAN），本阶段聚焦**开源项目实战、多域翻译与制图综合结合**。
>
> 完成后应达到：
>
> - 跑通 CycleGAN 开源项目
> - 理解 starGAN 的**多域翻译**思想（对应“多尺度”问题），并完成项目实战
> - 掌握图像补全（要素补齐）的基本方法
> - 能阅读 GAN 相关论文
> - 完成 GAN 与制图综合结合的文献调研与专题总结

## 视频资源

```
GAN对抗生成网络
```

> **观看范围说明**：
>
> - **已学**（第四阶段，Day46—Day52）：第一章（GAN原理）、第二章 1-5（CycleGAN 数据与架构）
> - **本阶段必看**：第二章 6-10（CycleGAN 模块与训练）、第三章（starGAN架构）、第八章（图像补全）
> - **建议**：第四章（starGAN项目实战）、第五章第 5、6 节（InstanceNorm、AdaIn，共约 13 分钟）
> - **跳过**：第五章（其余）、第六章（变声器项目，与地图方向无关）
> - **选学**：第七章（图像超分辨率，Day74）

------

"""

def bump(block, old, new, olddate, newdate):
    b1 = f"# Day{old}（{olddate}）"
    b2 = f"# Day{new}（{newdate}）"
    assert block.count(b1) == 1, b1
    block = block.replace(b1, b2)
    c1 = f'git commit -m "Day{old}：'
    assert block.count(c1) == 1, c1
    return block.replace(c1, f'git commit -m "Day{new}：')

d63 = bump(d63, 63, 68, "2026.08.29", "2026.09.03")
d64 = bump(d64, 64, 69, "2026.08.30", "2026.09.04")
d65 = bump(d65, 65, 70, "2026.08.31", "2026.09.05")

D66_NEW = """# Day71（2026.09.06）

## 今日目标

掌握基于GAN的图像补全方法。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第八章 1-论文概述
-  - [ ] 第八章 2-网络架构
-  - [ ] 第八章 3-细节设计
-  - [ ] 第八章 4-论文总结
-  - [ ] 第八章 5-数据与项目概述
-  - [ ] 第八章 6-参数基本设计
-  - [ ] 第八章 7-网络结构配置
-  - [ ] 第八章 8-网络迭代训练
-  - [ ] 第八章 9-测试模块

预计时长：2小时

------

### 理论学习

理解：

图像补全：

```
残缺图像
    ↓
上下文编码
    ↓
生成缺失区域
    ↓
判别器判断整体真实性
```

**与制图综合的连接**：

- 要素补齐：断裂道路连接、河流连通性修复
- 要素缺失恢复

------

### GitHub提交

```
git add .
git commit -m "Day71：完成图像补全方法学习"
git push
```

------

# Day72（2026.09.07）

## 今日目标

完成GAN与制图综合结合的文献调研。

## 今日任务

### 文献阅读

阅读：

- 制图综合 × 深度学习/GAN 论文 2~3 篇

重点关注：

- 研究问题与数据表示（矢量 / 栅格）
- 是否使用生成式方法（GAN / Diffusion）
- 多尺度评价指标
- 与课程中方法的异同

------

### 输出成果

创建：

```
GAN制图综合文献调研.md
```

每篇论文记录：研究问题、方法、数据、与 CycleGAN / starGAN / 图像补全的对应关系、可借鉴点。

------

### GitHub提交

```
git add .
git commit -m "Day72：完成GAN与制图综合文献调研"
git push
```

------

# Day73（2026.09.08）

## 今日目标

完成GAN专题总结，形成GAN×制图综合研究方向清单。

## 今日任务

### 输出成果

完成：

```
GAN学习总结.md
```

包含：

- GAN 原理与训练难点（Day46—Day48 部分并入）
- CycleGAN / starGAN / 图像补全 三类方法对比
- 与制图综合、多尺度表达的结合点分析
- 后续可探索方向（供研一选题参考）

------

### GitHub提交

```
git add .
git commit -m "Day73：完成GAN专题总结"
git push
```

------

"""

assert d67.count("# Day67（选学，2026.09.02）") == 1
d67 = d67.replace("# Day67（选学，2026.09.02）", "# Day74（选学，2026.09.09）")
assert d67.count('git commit -m "Day67：') == 1
d67 = d67.replace('git commit -m "Day67：', 'git commit -m "Day74：')

# ---------- tail：验收与收尾 ----------
tail = tail.replace(A_S5A, "# 第六阶段验收（Day68-Day73）")
tail = tail.replace("- ✅ 理解GAN的对抗训练机制\n- ✅ 理解GAN训练不稳定的成因与表现\n- ✅ 掌握CycleGAN的无配对图像翻译\n- ✅ 掌握starGAN的多域翻译\n- ✅ 掌握图像补全的基本方法\n- ✅ 掌握GAN项目开发流程",
                    "- ✅ 巩固GAN对抗训练机制（原理与最简实战见第四阶段）\n- ✅ 跑通CycleGAN开源项目\n- ✅ 掌握starGAN的多域翻译并完成项目实战\n- ✅ 掌握图像补全的基本方法\n- ✅ 掌握GAN项目开发流程")
tail = tail.replace("# 66天最终验收", "# 73天最终验收")
tail = tail.replace("我完成了GeoAI预研计划（Day01—Day66）", "我完成了GeoAI预研计划（Day01—Day73）")
tail = tail.replace("# 66天最终能力评估", "# 73天最终能力评估")
tail = tail.replace("66天路线逻辑", "73天路线逻辑")
tail = tail.replace("Day46-Day55\n地图要素语义分割 + U-Net建筑物提取与化简", "Day53-Day62\n地图要素语义分割 + U-Net建筑物提取与化简")
tail = tail.replace("Day56-Day60\nTransformer + 导师论文", "Day63-Day67\nTransformer + 导师论文")
tail = tail.replace("Day61-Day66\nGAN生成对抗网络专题", "Day68-Day73\nGAN项目实战与文献调研")
tail = tail.replace("CNN + CV基础 + 制图综合理论\n\n↓\n\nDay53-Day62", "CNN + CV基础 + 制图综合理论\n\n↓\n\nDay46-Day52\nGAN基础专题（导师要求提前）\n\n↓\n\nDay53-Day62")
tail = tail.replace("GAN生成对抗网络     ★★★☆☆", "GAN生成对抗网络     ★★★★☆")

new_text = head + S4_NEW + s4 + S6_INTRO + d63 + d64 + d65 + D66_NEW + d67 + tail
open(P, "w", encoding="utf-8").write(new_text)

# 校验：不应再残留旧编号锚点
for probe in [A_S4, A_S5, A_D61, A_D63, A_D66, A_D67, A_S5A, "第五阶段：GAN", "（Day46-Day60）", "（Day61-Day66）"]:
    assert probe not in new_text, f"residual: {probe}"
import subprocess
lines = new_text.splitlines()
print("total lines:", len(lines))
for i, l in enumerate(lines, 1):
    if re.match(r"^# (第[一二三四五六]阶段|.*阶段验收|Day\d+|73天|当前能力|阶段成果)", l) and (re.match(r"^# Day", l) or "阶段" in l or "验收" in l):
        print(i, l)
