# -*- coding: utf-8 -*-
"""作业：地图制图综合 + 深度学习（按参考文件版式：题目加粗 + “答：” + 表格）"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docx import (R, P, title, question, answer, body, note, table, write_docx, OUT)

E = []
add = E.append

# ==================================================================== 标题
add(title("作业1"))

# ==================================================================== 1
add(question("1.确定研究领域。"))
add(answer("答：地图制图综合（Cartographic Generalization）+ 深度学习（Deep Learning），"
           "即“智能地图综合 / GeoAI for Map Generalization”。"))
add(body("地图制图综合是地图学与地理信息科学的核心理论问题，指当地图比例尺缩小、分辨率降低或表达目的改变时，"
         "通过选取、化简、概括与合并、典型化、位移、夸大、分类分级等综合算子，在保持地理要素空间结构特征、"
         "分布规律、拓扑关系与语义重要性的前提下，压缩地图信息量、实现多尺度地图表达的过程。"
         "本领域以矢量地图要素（建筑物、道路网、水系与河流、等高线、居民地、土地利用等）为研究对象，"
         "以 CNN、GAN、GNN、Transformer、扩散模型、强化学习及大语言模型/多模态大模型为技术手段，"
         "实现制图综合算子的自动化与智能化。"))
add(body("技术演进路线为：规则与算法驱动（1980s—1990s）→ 专家系统与知识推理（1990s—2000s）→ "
         "最优化与约束满足（2000s—2010s）→ 机器学习与模式识别（2010s）→ 深度学习端到端建模（2018 年至今）→ "
         "基础模型、生成式模型与大模型/智能体（2023 年至今）。2018 年 Sester 等首次将深度学习引入建筑物综合，"
         "2019 年 Touya 等发表《Is deep learning the new agent for map generalization?》，"
         "为该方向正式确立的标志性节点。"))

add(P(R("本领域的主要研究任务与所用的深度学习技术如下："), first=420, after=40))
q1_rows = [
    ["建筑物综合", "建筑物面要素；CNN、GAN、GNN、Transformer、扩散模型（化简、合并、典型化、群组模式识别）"],
    ["道路网综合", "道路线要素；语义分割 CNN、GAN、强化学习（选取、等级化简、线化简）"],
    ["水系与等高线综合", "河流、等高线；序列生成模型、图神经网络、强化学习（结构选取、化简）"],
    ["居民地与面状要素综合", "居民地面要素；图卷积网络、深度聚类（选取、合并、形状分类）"],
    ["综合质量评价与知识推理", "综合结果与制图规则；可解释 AI、知识图谱、大模型（质量评价、规则自动获取）"],
    ["端到端多尺度地图生成", "全要素整图；GAN、扩散模型、多模态大模型（整图综合与多尺度派生）"],
]
add(table(["主要研究任务", "研究对象与代表性深度学习技术"], q1_rows, [2200, 6106]))

# ==================================================================== 2
add(question("2.研究领域内的主要中英文期刊，根据影响力给出列表。"))
add(answer("答："))

j_rows = [
    ["英文\n（国际期刊）", "ISPRS Journal of Photogrammetry and Remote Sensing", "12.2"],
    ["", "International Journal of Geographical Information Science (IJGIS)", "5.9"],
    ["", "Geo-spatial Information Science", "5.4"],
    ["", "International Journal of Digital Earth", "4.9"],
    ["", "ISPRS International Journal of Geo-Information (IJGI)", "2.8"],
    ["", "Cartography and Geographic Information Science (CaGIS)", "2.7"],
    ["", "Computers, Environment and Urban Systems", "Q1（SCIE/SSCI）"],
    ["", "International Journal of Applied Earth Observation and Geoinformation", "Q1（SCIE）"],
    ["", "Transactions in GIS", "Q1（SCIE）"],
    ["", "IEEE Transactions on Geoscience and Remote Sensing", "Q1（SCIE）"],
    ["", "Remote Sensing (MDPI)", "Q1/Q2（SCIE）"],
    ["", "GeoInformatica", "Q2（SCIE）"],
    ["", "Geocarto International", "Q2（SCIE）"],
    ["", "Cartographica", "SSCI"],
    ["", "The Cartographic Journal", "SSCI"],
    ["", "International Journal of Cartography（ICA 会刊）", "Q3（SSCI/ESCI）"],
    ["", "Computers & Geosciences", "Q1/Q2（SCIE）"],
    ["", "Journal of Maps", "Q3（SSCI）"],
    ["", "KN - Journal of Cartography and Geographic Information", "ESCI"],
    ["", "Journal of Spatial Information Science (JOSIS)", "ESCI"],
    ["", "Journal of Geovisualization and Spatial Analysis", "ESCI"],
    ["", "ACM Transactions on Spatial Algorithms and Systems (TSAS)", "ESCI"],
    ["中文", "《遥感学报》", "4.799"],
    ["", "《测绘学报》", "4.298"],
    ["", "《武汉大学学报（信息科学版）》", "3.872"],
    ["", "《测绘通报》", "2.414"],
    ["", "《地球信息科学学报》", "北大核心 / CSCD"],
    ["", "《测绘科学技术学报》", "北大核心 / CSCD"],
    ["", "《测绘科学》", "北大核心"],
    ["", "《中国图象图形学报》", "北大核心 / CSCD"],
    ["", "《计算机辅助设计与图形学学报》", "EI / CSCD"],
    ["", "《时空信息学报》（原《地理信息世界》）", "科技核心"],
    ["", "《地理学报》", "9.926"],
    ["", "《地理研究》", "7.661"],
    ["", "《地理科学进展》", "6.513"],
    ["", "《地理与地理信息科学》", "4.120"],
    ["", "Journal of Geodesy and Geoinformation Science (JGG)（中国主办英文刊）", "ESCI"],
]
add(table(["语种", "期刊名称", "2024 JIF / 复合影响因子"], j_rows, [900, 5100, 2306]))
add(note("注：中文刊为 CNKI 复合影响因子口径（与《测绘学报》4.298、《武汉大学学报（信息科学版）》3.872 属同批数据）；"
         "英文刊为 JCR 期刊影响因子（JIF）口径。未标注具体数值者，其影响因子请在最新版 JCR 报告中核实。"))

# ==================================================================== 3
add(question("3.查找确定主题的文献，制作并提交一个文献列表。要求包含中英文文献、比较新的文献、"
             "最具代表性的文献以及中英文的综述性论文（总共50篇以内）。"))
add(answer("答：共 47 篇（英文 28 篇、中文 19 篇），其中综述性论文 10 篇、"
           "最具代表性的经典文献 11 篇、2020—2026 年新文献 19 篇、学位论文 7 篇。"))

en_cell = "\n".join([
    "【一】综述性论文（4篇）",
    "1. Touya G03, Zhang X, Lokhat I. Is deep learning the new agent for map generalization?[J]. International Journal of Cartography, 2019, 5(2-3): 142-157.",
    "2. Kang Y, Gao S, Roth R E. Artificial intelligence studies in cartography: a review and synthesis of methods, applications, and ethics[J]. Cartography and Geographic Information Science, 2024, 51(4).",
    "3. Deep learning in automatic map generalization: achievements and challenges[J]. Geo-spatial Information Science, 2025.",
    "4. GeoAI for map generalization in multi-scale cartography: foundations, a research agenda, and interdisciplinary perspectives[J]. International Journal of Geographical Information Science, 2026.",
    "【二】最具代表性的经典文献（10篇）",
    "5. Brassel K E, Weibel R. A review and conceptual framework of automated map generalization[J]. International Journal of Geographical Information Systems, 1988, 2(3): 229-244.",
    "6. McMaster R B, Shea K S. Generalization in Digital Cartography[M]. Washington D C: Association of American Geographers, 1992.",
    "7. Mackaness W A, Ruas A, Sarjakoski L T (eds.). Generalisation of Geographic Information: Cartographic Modelling and Applications[M]. Amsterdam: Elsevier, 2007.",
    "8. Weibel R, Dutton G03. Generalizing spatial data and dealing with multiple representations[M]//Geographical Information Systems: Principles, Techniques, Management and Applications. Wiley, 1999: 125-155.",
    "9. Ruas A. A method for building displacement in automated map generalisation[J]. International Journal of Geographical Information Science, 1998, 12(8): 789-803.",
    "10. Regnauld N, McMaster R B. A synoptic view of generalisation operators[M]//Generalisation of Geographic Information. Elsevier, 2007: 37-66.",
    "11. Li Z, Openshaw S. Algorithms for automated line generalization based on a natural principle of objective generalization[J]. International Journal of Geographical Information Systems, 1992, 6(5): 373-389.",
    "12. Douglas D H, Peucker T K. Algorithms for the reduction of the number of points required to represent a digitized line or its caricature[J]. Cartographica, 1973, 10(2): 112-122.",
    "13. Sester M, Feng Y, Thiemann F. Building generalization using deep learning[C]//The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 2018, XLII-4: 565-572.",
    "14. Feng Y, Thiemann F, Sester M. Learning cartographic building generalization with deep convolutional neural networks[J]. ISPRS International Journal of Geo-Information, 2019, 8(6): 258.",
    "【三】比较新的文献（2020—2026，13篇）",
    "15. Yan X, et al. Reasoning cartographic knowledge in deep learning-based map generalization with explainable AI[J]. International Journal of Geographical Information Science, 2024, 38(10): 2061-2082.",
    "16. Yan X, Ai T, Yang M, Yin H. A graph deep learning approach for urban building grouping[J]. Geocarto International, 2022, 37(10).",
    "17. Yan X, et al. Towards general-purpose representation learning of polygonal geometries[J]. GeoInformatica, 2023.",
    "18. Courtial A, Touya G03, Zhang X. Exploring the potential of deep learning segmentation for mountain roads generalisation[J]. ISPRS International Journal of Geo-Information, 2020, 9(5): 338.",
    "19. Courtial A, El Ayedi A, Touya G03, Zhang X. Deriving map images of generalised mountain roads with generative adversarial networks[J]. International Journal of Geographical Information Science, 2023, 37(3).",
    "20. Zhang X, et al. DeepMapScaler: a workflow of deep neural networks for the generation of generalised maps[J]. Cartography and Geographic Information Science, 2024, 51(1).",
    "21. A visual transformer and multi-task learning framework for building generalisation from raster maps[J]. International Journal of Digital Earth, 2026.",
    "22. DiffSimplify: a building continuous simplification model based on conditional diffusion models[J]. International Journal of Digital Earth, 2026.",
    "23. Cui L, et al. End-to-end vector simplification for building contours via a sequence generation model[J]. ISPRS International Journal of Geo-Information, 2025, 14(3): 124.",
    "24. Envisioning generative artificial intelligence in cartography: mapmaking, map use, and ethics[J]. International Journal of Cartography, 2025.",
    "25. Automated map generalization: emerging techniques and new trends (Editorial)[J]. Journal of Geovisualization and Spatial Analysis, 2024.",
    "26. Machine learning in cartography (Editorial)[J]. Cartography and Geographic Information Science, 2024.",
    "27. Weibel R, et al. Automated map generalization: is deep learning the solution?[R]. ETH Zurich, 2025.",
    "【四】学位论文（1篇）",
    "28. Fan. Towards text-conditioned multi-scale map generalization using diffusion models[D]. Cartography M.Sc. Master's Thesis, 2025.",
])

zh_cell = "\n".join([
    "【一】综述性论文（6篇）",
    "29. 武芳, 杜佳威, 钱海忠, 翟仁健, 等. 地图综合智能化研究的发展与思考[J]. 武汉大学学报（信息科学版）, 2022, 47(10).",
    "30. 艾廷华. 深度学习赋能地图制图的若干思考[J]. 测绘学报, 2021, 50(9): 1170.",
    "31. 王家耀, 等. 人工智能赋能地图科学数智化[J]. 测绘学报, 2026, 55(3): 381.",
    "32. 钱海忠, 王家耀, 王迪, 等. 综述与展望：地理空间数据的管理、多尺度变换与表达[J]. 地球信息科学学报, 2022, 24(12): 2265-2281.",
    "33. 任福, 翁杰, 王昭, 等. 关于智能地图制图的几点思考[J]. 武汉大学学报（信息科学版）, 2025.",
    "34. 从第31届国际制图大会看地图制图学的研究进展[J]. 地球信息科学学报, 2024.",
    "【二】最具代表性的经典文献（中文，1篇）",
    "35. 毋河海. 地图综合基础理论与技术方法研究[M]. 北京: 测绘出版社.",
    "【三】比较新的文献（2021—2025，6篇）",
    "36. 基于图顶点深度聚类的建筑物合并方法[J]. 测绘学报, 2024, 53(4).",
    "37. 地图综合图卷积神经网络点群简化方法[J]. 测绘学报, 2024.",
    "38. 面状居民地形状分类的图卷积神经网络方法[J]. 测绘学报, 2022, 51(11).",
    "39. 面向建筑物轮廓规则化的双路径边界约束与相对论生成对抗网络[J]. 测绘学报.",
    "40. 高晓蓉, 闫浩文, 禄小敏, 王中辉. 利用“计算区”进行建筑物短边结构识别和渐进式化简[J]. 武汉大学学报（信息科学版）, 2021.",
    "41. 利用点重要性序列的等高线间接综合[J]. 武汉大学学报（信息科学版）.",
    "【四】分任务方法与学位论文（6篇）",
    "42. 刘佩. 基于深度学习的OSM道路网智能选取模型研究[D].",
    "43. 张康. 基于深度图卷积神经网络的道路网自动选取研究[D].",
    "44. 郭溟. 基于知识学习与推理的道路网智能选取方法研究[D].",
    "45. 钟英铭. 基于深度学习的面向制图综合的建筑物群组模式识别研究[D].",
    "46. 基于地理特征知识的等高线与河流一体化综合研究[D].",
    "47. 李国贤. 建筑物群典型化的渐进式方法研究[D].",
])

add(table(["语种", "文献列表"], [["英文", en_cell], ["中文", zh_cell]], [900, 7406]))
add(note("说明：以上文献均经网络检索核实题名与来源。少数 2025—2026 年在线优先（online first）论文的作者全名与卷期页码"
         "尚在出版流程中；第 28、42—47 条为学位论文，其培养单位与年份请在中国知网学位论文库中核验后补全。"))

# ==================================================================== 4
add(question("4.分析研究领域有哪些主要的研究者以及研究组。"))
add(answer("答："))

intl = [
    "William Mackaness", "Robert Weibel", "Monika Sester", "Dirk Burghardt", "Guillaume Touya",
    "Anne Ruas", "Cécile Duchêne", "Jantien Stoter", "Marc van Kreveld", "Bettina Speckmann",
    "Jan-Henrik Haunert", "Barbara Buttenfield", "Cynthia Brewer", "Larry Stanislawski",
    "Eric Guilbert", "Paul Hardy",
]
intl_desc = [
    "英国爱丁堡大学。地图综合理论、基于 Agent 的综合、土地利用综合；地图综合概念框架与 ICA 综合系列工作坊的主要组织者。",
    "瑞士苏黎世大学。计算制图学、地图综合、机器学习制图；《Automated map generalization: is deep learning the solution?》(2025)。",
    "德国汉诺威莱布尼茨大学制图与地理信息研究所。深度学习地图综合、建筑物综合；Sester 等 (2018) 为深度学习制图综合开山之作。",
    "德国德累斯顿工业大学制图学研究所。地图综合、众源地理数据、多尺度表达；ICA 综合相关委员会成员。",
    "法国 IGN / LASTIG。深度学习地图综合、道路网综合、综合过程建模；《Is deep learning the new agent for map generalization?》(2019)。",
    "法国 IGN COGIT。基于 Agent 的综合、位移算法；Ruas (1998) 建筑物位移经典算法。",
    "法国 IGN COGIT / LASTIG。综合过程建模、多 Agent 自动综合、协同综合。",
    "荷兰代尔夫特理工大学。3D 城市建模、多尺度空间数据、自动综合。",
    "荷兰乌得勒支大学。算法制图综合、计算几何。",
    "荷兰埃因霍温理工大学。算法制图综合、地理可视化。",
    "德国波恩大学。算法与优化制图综合、路网简化。",
    "美国科罗拉多大学博尔德分校。地图综合、多尺度数据库、综合质量度量。",
    "美国宾州州立大学。制图学、地理可视化、地图综合。",
    "美国地质调查局 (USGS)。地形图综合、机器学习综合、水文综合。",
    "加拿大拉瓦尔大学。地图综合、海岸线与地形综合、折线化简。",
    "Esri（工业界）。自动综合生产流程、制图综合工程化。",
]

cn = [
    "王家耀院士团队", "武芳教授团队", "钱海忠教授团队", "翟仁健教授团队", "孙群教授团队",
    "安晓亚教授团队", "艾廷华教授团队", "郭庆胜教授团队", "应申教授团队", "李霖教授团队",
    "任福教授团队", "刘耀林教授团队", "闾国年教授团队", "汤国安教授团队", "邓敏教授团队",
    "闫浩文教授团队", "高晓蓉团队", "陈军团队", "刘万增团队", "李志林教授团队",
    "晏雄锋团队", "张翔团队", "段伟伟团队", "徐永洋团队",
]
cn_desc = [
    "信息工程大学。地图学理论、地图制图综合、地理信息工程；中国地图学与制图综合理论体系的奠基人之一。",
    "信息工程大学。地图综合智能化、制图综合算法与知识、多尺度表达；《地图综合智能化研究的发展与思考》(2022)。",
    "信息工程大学。地图自动综合、道路网智能选取、综合知识推理；《综述与展望：地理空间数据的管理、多尺度变换与表达》(2022)。",
    "信息工程大学。地图综合、空间数据多尺度表达与级联更新。",
    "信息工程大学。地图制图学、智能制图、空间数据尺度变换。",
    "信息工程大学 / 西安测绘研究所。地图综合、智能制图、空间数据尺度变换。",
    "武汉大学资源与环境科学学院。地图综合、地图代数、多尺度表达、智能制图；《深度学习赋能地图制图的若干思考》(2021)。",
    "武汉大学。制图综合理论与方法、地图综合知识、空间数据挖掘。",
    "武汉大学。地图学、空间数据多尺度表达与可视化、泛地图。",
    "武汉大学。地图学理论、空间数据多尺度表达、地理本体。",
    "武汉大学。智能地图制图、地图可视化与地图设计；《关于智能地图制图的几点思考》(2025)。",
    "武汉大学。地理信息科学、空间数据综合与优化决策。",
    "南京师范大学。地理信息科学、全空间信息系统、虚拟地理环境。",
    "南京师范大学。数字地形分析、DEM 与地貌综合。",
    "中南大学。空间数据挖掘、空间关系、制图综合与综合质量评价。",
    "兰州交通大学。地图综合、空间关系、地图语言学；建筑物短边结构识别与渐进式化简。",
    "兰州交通大学。建筑物化简、地图综合。",
    "国家基础地理信息中心。多尺度空间数据库、全球地理信息资源建设、地理信息标准。",
    "国家基础地理信息中心。地图综合、空间数据更新与质量控制。",
    "香港理工大学。地图学、空间数据质量、地图综合。",
    "中国地质大学（武汉）。深度学习地图综合、图神经网络、可解释 AI、几何表示学习；IJGIS 2024 可解释 AI 制图综合。",
    "中国科学院空天信息创新研究院（原法国 IGN）。深度学习自动综合、多尺度地图生成；DeepMapScaler (CaGIS 2024)。",
    "中国地质大学（武汉）。地图综合深度学习、建筑物综合。",
    "中国地质大学（武汉）。遥感与制图综合的深度学习方法。",
]

p_rows = []
for i, (a, b) in enumerate(zip(intl, intl_desc)):
    p_rows.append(["国外" if i == 0 else "", a, b])
for i, (a, b) in enumerate(zip(cn, cn_desc)):
    p_rows.append(["国内" if i == 0 else "", a, b])
add(table(["国别", "研究者 / 研究组", "单位与主要研究方向"], p_rows, [700, 1800, 5806]))

add(P(R("主要研究学派/团队汇总："), first=420, after=40))
add(body("①信息工程大学学派（王家耀—武芳—钱海忠—翟仁健—孙群—安晓亚）：中国地图综合研究的核心力量，"
         "近年重点转向综合知识推理与深度学习；②武汉大学学派（艾廷华—郭庆胜—应申—李霖—任福—刘耀林）："
         "以地图代数、多尺度表达与智能制图为特色，是国内“深度学习+制图综合”论文的主要产出方之一；"
         "③南京师范大学（闾国年—汤国安）：全空间信息系统与数字地形分析；④兰州交通大学（闫浩文—高晓蓉）："
         "建筑物化简与空间关系；⑤中国地质大学（武汉）（晏雄锋—段伟伟—徐永洋）：图神经网络、几何表示学习与"
         "可解释 AI 的新锐力量；⑥中国科学院空天信息创新研究院（张翔）：端到端多尺度地图生成；"
         "⑦法国 IGN COGIT / LASTIG 学派（Ruas—Duchêne—Touya—Zhang）：国际上该方向最具影响力的团队；"
         "⑧德语区计算制图学派（苏黎世大学 Weibel—汉诺威大学 Sester—德累斯顿工大 Burghardt）："
         "2026 年联合发表 GeoAI 制图综合纲领性综述，主导方向议程；"
         "⑨荷兰算法制图学派（TU Delft—Utrecht—TU Eindhoven—波恩大学）：以计算几何与组合优化提供理论基础；"
         "⑩美国 USGS 与北美学术界（Stanislawski—Buttenfield—Brewer）：面向国家地形图生产的综合研究。"
         "此外，国际制图协会（ICA）下设的“综合与多表达委员会”每年举办专题工作坊，是本领域最核心的学术共同体。"))

write_docx(E, OUT)
print("OK ->", OUT, os.path.getsize(OUT), "bytes")
print("elements:", len(E))
