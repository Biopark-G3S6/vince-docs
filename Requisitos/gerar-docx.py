#!/usr/bin/env python3
"""Converte um documento Markdown deste repositório em .docx formatado para publicação.

O .docx é artefato derivado: a fonte da verdade é sempre o Markdown. Ver README.md,
seção "Documentos oficiais".

Dependência: python-docx. Em ambiente isolado, para não sujar o Python do sistema:

    python3 -m venv .venv
    .venv/bin/pip install python-docx

Uso:

    .venv/bin/python Requisitos/gerar-docx.py Requisitos/URS.md Requisitos/URS.docx

Formatado para importar limpo no Google Docs: fonte monoespaçada nativa do catálogo do
Google, sumário estático (o campo TOC do Word chega vazio na importação) e diagramas
dimensionados para não quebrar linha em A4.
"""

import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HEADING_COLOR = RGBColor(0x1F, 0x38, 0x64)
SUBHEADING_COLOR = RGBColor(0x2E, 0x5A, 0x88)
CODE_COLOR = RGBColor(0xC7, 0x25, 0x4E)
CODE_FILL = "F7F2F4"
TABLE_HEADER_FILL = "DEE6F1"
CODEBLOCK_FILL = "F5F5F5"

# Courier New existe nativamente no Google Docs; Consolas não, e seria substituída na importação.
MONO_FONT = "Courier New"

INLINE_RE = re.compile(r"(\*\*.+?\*\*|`[^`]+`|\[[^\]]+\]\([^)]*\))")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
BULLET_RE = re.compile(r"^(\s*)-\s+(.*)$")
ORDERED_RE = re.compile(r"^(\s*)(\d+)\.\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


# --------------------------------------------------------------------------- blocos


def parse_blocks(lines):
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        line = raw.rstrip("\n")
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            blocks.append(("code", buf))
            continue

        m = HEADING_RE.match(stripped)
        if m:
            blocks.append(("heading", (len(m.group(1)), m.group(2).strip())))
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1].strip()):
            header = split_row(stripped)
            aligns = [cell_align(c) for c in split_row(lines[i + 1].strip())]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            blocks.append(("table", (header, aligns, rows)))
            continue

        if BULLET_RE.match(line) or ORDERED_RE.match(line):
            items = []
            while i < n:
                cur = lines[i].rstrip("\n")
                if not cur.strip():
                    break
                mb = BULLET_RE.match(cur)
                mo = ORDERED_RE.match(cur)
                if mb:
                    items.append([len(mb.group(1)) // 2, False, mb.group(2).strip()])
                elif mo:
                    items.append([len(mo.group(1)) // 2, True, mo.group(3).strip()])
                elif cur.startswith("  ") and items:
                    items[-1][2] += " " + cur.strip()
                else:
                    break
                i += 1
            blocks.append(("list", items))
            continue

        buf = []
        while i < n:
            cur = lines[i].rstrip("\n")
            s = cur.strip()
            if not s or s == "---" or HEADING_RE.match(s) or s.startswith("|") or s.startswith("```"):
                break
            if BULLET_RE.match(cur) or ORDERED_RE.match(cur):
                break
            buf.append(s)
            i += 1
        if buf:
            blocks.append(("para", buf))
    return blocks


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def cell_align(sep):
    sep = sep.strip()
    if sep.startswith(":") and sep.endswith(":"):
        return WD_ALIGN_PARAGRAPH.CENTER
    if sep.endswith(":"):
        return WD_ALIGN_PARAGRAPH.RIGHT
    return WD_ALIGN_PARAGRAPH.LEFT


# --------------------------------------------------------------------------- runs


def shade_run(run, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    run._element.get_or_add_rPr().append(shd)


def add_inline(paragraph, text, bold=False, size=None):
    for token in INLINE_RE.split(text):
        if not token:
            continue
        if token.startswith("**") and token.endswith("**") and len(token) > 4:
            add_inline(paragraph, token[2:-2], bold=True, size=size)
        elif token.startswith("`") and token.endswith("`") and len(token) > 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = MONO_FONT
            run.font.size = Pt(9) if size is None else size - Pt(1)
            run.font.color.rgb = CODE_COLOR
            run.bold = bold
            shade_run(run, CODE_FILL)
        elif token.startswith("["):
            label = token[1 : token.index("]")]
            add_inline(paragraph, label, bold=bold, size=size)
        else:
            run = paragraph.add_run(token)
            run.bold = bold
            if size is not None:
                run.font.size = size


# --------------------------------------------------------------------------- estilos


def configure_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    spec = {
        "Title": (24, HEADING_COLOR, 0, 6),
        "Heading 1": (16, HEADING_COLOR, 20, 8),
        "Heading 2": (13, HEADING_COLOR, 14, 6),
        "Heading 3": (11.5, SUBHEADING_COLOR, 12, 4),
        "Heading 4": (10.5, SUBHEADING_COLOR, 10, 4),
    }
    for name, (size, color, before, after) in spec.items():
        st = doc.styles[name]
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = color
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True

    for name in ("List Bullet", "List Bullet 2", "List Bullet 3", "List Number", "List Number 2"):
        try:
            st = doc.styles[name]
        except KeyError:
            continue
        st.font.name = "Calibri"
        st.font.size = Pt(10.5)
        st.paragraph_format.space_after = Pt(2)


def configure_page(doc):
    for section in doc.sections:
        section.page_width = Cm(21)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)


def add_field(paragraph, instruction):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for el in (begin, instr, sep, end):
        run._r.append(el)
    return run


def add_footer(doc):
    for section in doc.sections:
        p = section.footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("VinceArt · URS 0.1 · ")
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        field = add_field(p, "PAGE")
        field.font.size = Pt(8)
        field.font.color.rgb = RGBColor(0x80, 0x80, 0x80)


def add_toc(doc, headings):
    """Sumário estático: campo TOC do Word chega vazio no Google Docs e parece defeito."""
    doc.add_heading("Sumário", level=1)
    for level, text in headings:
        if level > 3:
            continue
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(0 if level == 2 else 0.7)
        run = p.add_run(text)
        run.bold = level == 2
        run.font.size = Pt(10.5 if level == 2 else 10)
        if level > 2:
            run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    doc.add_page_break()


# --------------------------------------------------------------------------- render


def render_table(doc, header, aligns, rows):
    table = doc.add_table(rows=1, cols=len(header))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    for idx, text in enumerate(header):
        cell = table.rows[0].cells[idx]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = aligns[idx] if idx < len(aligns) else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(2)
        add_inline(p, text, bold=True, size=Pt(9.5))
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), TABLE_HEADER_FILL)
        cell._tc.get_or_add_tcPr().append(shd)

    for row in rows:
        cells = table.add_row().cells
        for idx, text in enumerate(row[: len(header)]):
            cell = cells[idx]
            cell.text = ""
            p = cell.paragraphs[0]
            p.alignment = aligns[idx] if idx < len(aligns) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_after = Pt(2)
            add_inline(p, text, size=Pt(9.5))
    doc.add_paragraph()


def render_code(doc, lines):
    table = doc.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    cell = table.rows[0].cells[0]
    cell.text = ""
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), CODEBLOCK_FILL)
    cell._tc.get_or_add_tcPr().append(shd)
    for idx, line in enumerate(lines):
        p = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(line if line else " ")
        run.font.name = MONO_FONT
        run.font.size = Pt(7.5)
    doc.add_paragraph()


BULLET_STYLES = ["List Bullet", "List Bullet 2", "List Bullet 3"]
NUMBER_STYLES = ["List Number", "List Number 2", "List Number 3"]


def render_list(doc, items):
    for level, ordered, text in items:
        level = min(level, 2)
        styles = NUMBER_STYLES if ordered else BULLET_STYLES
        try:
            p = doc.add_paragraph(style=styles[level])
        except KeyError:
            p = doc.add_paragraph(style=styles[0])
            p.paragraph_format.left_indent = Cm(0.8 * (level + 1))
        add_inline(p, text)


def render(blocks, out_path):
    doc = Document()
    configure_styles(doc)
    configure_page(doc)

    doc.core_properties.title = "URS — Especificação de Requisitos do Usuário"
    doc.core_properties.subject = "VinceArt"
    doc.core_properties.comments = "Gerado a partir de Requisitos/URS.md"

    headings = [payload for kind, payload in blocks if kind == "heading" and payload[0] > 1]

    toc_inserted = False
    for kind, payload in blocks:
        if kind == "heading":
            level, text = payload
            if level == 1:
                p = doc.add_paragraph(style="Title")
                add_inline(p, text)
            else:
                p = doc.add_heading(level=level - 1)
                add_inline(p, text)
        elif kind == "para":
            if all(line.startswith("**") for line in payload):
                for line in payload:
                    p = doc.add_paragraph()
                    p.paragraph_format.space_after = Pt(2)
                    add_inline(p, line)
                if not toc_inserted:
                    doc.add_paragraph()
                    add_toc(doc, headings)
                    toc_inserted = True
            else:
                p = doc.add_paragraph()
                add_inline(p, " ".join(payload))
        elif kind == "list":
            render_list(doc, payload)
        elif kind == "table":
            render_table(doc, *payload)
        elif kind == "code":
            render_code(doc, payload)

    add_footer(doc)
    doc.save(out_path)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as fh:
        lines = fh.readlines()
    render(parse_blocks(lines), dst)
    print(f"gerado: {dst}")


if __name__ == "__main__":
    main()
