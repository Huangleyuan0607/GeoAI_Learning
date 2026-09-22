# -*- coding: utf-8 -*-
"""
按参考文件《2025资环写作+2025122921+李品慧.docx》的版式生成作业 .docx
版式规范（从参考文件提取）：
  * 页面 A4 11906x16838，页边距 上下 1440 / 左右 1800 twips
  * 正文字体 宋体(ascii=宋体, eastAsia=宋体)，字号 12pt (w:sz=24)
  * 表格字体 ascii=Times New Roman, eastAsia=宋体，字号 12pt
  * 表格样式 Table Grid：四周及内部单线，sz=4 (0.5pt)，color=auto
  * 表格单元格段落：spacing after=0, line=240 auto
  * 标题居中加粗；题目行加粗；答案以“答：”起首
仅用标准库构造 OOXML，不依赖 python-docx / Word。
"""
import zipfile
from xml.sax.saxutils import escape

OUT = r"D:\CCNU\PreLearning_Plan\GeoAI-Learning\作业.docx"

EA = "宋体"
LAT_P = "宋体"                     # 段落西文字体（与参考文件一致）
LAT_T = "Times New Roman"          # 表格西文字体（与参考文件一致）
SZ = 12                            # 12pt -> w:sz=24


def esc(t):
    return escape(str(t))


# ---------------------------------------------------------------- run
def R(text, bold=False, size=SZ, lat=LAT_P, ea=EA):
    rpr = ['<w:rPr>',
           '<w:rFonts w:ascii="%s" w:hAnsi="%s" w:eastAsia="%s"/>' % (lat, lat, ea)]
    if bold:
        rpr.append('<w:b/><w:bCs/>')
    rpr.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (int(size * 2), int(size * 2)))
    rpr.append('</w:rPr>')
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (''.join(rpr), esc(text))


# ---------------------------------------------------------------- paragraph
def P(runs, align=None, before=0, after=0, line=240, first=None, left=None):
    ppr = ['<w:pPr>',
           '<w:spacing w:before="%d" w:after="%d" w:line="%d" w:lineRule="auto"/>'
           % (before, after, line)]
    ind = []
    if left is not None:
        ind.append('w:left="%d"' % left)
    if first is not None:
        ind.append('w:firstLine="%d"' % first)
    if ind:
        ppr.append('<w:ind %s/>' % ' '.join(ind))
    if align:
        ppr.append('<w:jc w:val="%s"/>' % align)
    ppr.append('</w:pPr>')
    return '<w:p>%s%s</w:p>' % (''.join(ppr), runs)


def title(text):
    """居中加粗大标题（对应参考文件的“作业1”）"""
    return P(R(text, bold=True, size=16), align="center", after=120, line=300)


def question(text):
    """题目行：加粗"""
    return P(R(text, bold=True), before=140, after=40)


def answer(label="答："):
    return P(R(label))


def body(text, first=420):
    """正文说明：首行缩进 2 字符"""
    return P(R(text), first=first, after=40)


def note(text):
    """小字注释"""
    return P(R(text, size=10.5), first=420, after=40)


# ---------------------------------------------------------------- table
GRID_BORDERS = ('<w:tblBorders>'
                '<w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
                '<w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
                '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
                '<w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
                '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
                '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
                '</w:tblBorders>')


def cell(text, width, bold=False, align="left", valign="center"):
    """单元格；文本用换行符分段"""
    tcpr = ('<w:tcPr><w:tcW w:w="%d" w:type="dxa"/>'
            '<w:vAlign w:val="%s"/></w:tcPr>' % (width, valign))
    parts = str(text).split("\n")
    inner = ''.join(
        P(R(seg, bold=bold, lat=LAT_T), align=align, after=0, line=240)
        for seg in parts)
    return '<w:tc>%s%s</w:tc>' % (tcpr, inner)


def table(headers, rows, widths):
    tblpr = ('<w:tblPr><w:tblW w:w="%d" w:type="dxa"/>%s'
             '<w:tblLayout w:type="fixed"/>'
             '<w:tblCellMar>'
             '<w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
             '<w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/>'
             '</w:tblCellMar></w:tblPr>') % (sum(widths), GRID_BORDERS)
    grid = '<w:tblGrid>%s</w:tblGrid>' % ''.join('<w:gridCol w:w="%d"/>' % w for w in widths)
    trs = []
    if headers:
        trs.append('<w:tr><w:trPr><w:tblHeader/></w:trPr>%s</w:tr>' % ''.join(
            cell(h, widths[i], bold=True, align="center") for i, h in enumerate(headers)))
    for r in rows:
        trs.append('<w:tr>%s</w:tr>' % ''.join(
            cell(r[i], widths[i]) for i in range(len(widths))))
    return '<w:tbl>%s%s%s</w:tbl>' % (tblpr, grid, ''.join(trs))


# ---------------------------------------------------------------- package
def build(elements):
    sect = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
            '<w:pgMar w:top="1440" w:right="1800" w:bottom="1440" w:left="1800" '
            'w:header="851" w:footer="992" w:gutter="0"/>'
            '<w:cols w:space="425"/><w:docGrid w:type="lines" w:linePitch="312"/></w:sectPr>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            '<w:body>%s%s</w:body></w:document>') % (''.join(elements), sect)


STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults>
<w:rPrDefault><w:rPr><w:rFonts w:ascii="宋体" w:hAnsi="宋体" w:eastAsia="宋体"/>
<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault>
</w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="table" w:default="1" w:styleId="TableGrid"><w:name w:val="Table Grid"/>
<w:tblPr>%s</w:tblPr></w:style>
</w:styles>''' % GRID_BORDERS

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

DOC_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''

CORE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:title>作业</dc:title><dc:creator>品慧 李</dc:creator>
</cp:coreProperties>'''

APP = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">
<Application>Microsoft Office Word</Application>
</Properties>'''


def write_docx(elements, path=OUT):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CONTENT_TYPES)
        z.writestr('_rels/.rels', RELS)
        z.writestr('word/document.xml', build(elements))
        z.writestr('word/styles.xml', STYLES)
        z.writestr('word/_rels/document.xml.rels', DOC_RELS)
        z.writestr('docProps/core.xml', CORE)
        z.writestr('docProps/app.xml', APP)
