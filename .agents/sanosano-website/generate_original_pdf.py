#!/usr/bin/env python3
"""Generate a clean PDF of the original SANO SANO copywriting (no social proof)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor, black, grey
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether
)
import re

OUTPUT = "/home/user/Osan-drinks/.agents/sanosano-website/SANO-SANO-COPYWRITING-ORIGINAL.pdf"
SOURCE = "/home/user/Osan-drinks/.agents/sanosano-website/copywriting.md"

PRIMARY = HexColor("#1C3D2E")
GOLD = HexColor("#C9A84C")
BG = HexColor("#FAF7F0")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "Title", parent=styles["Title"],
    fontName="Helvetica-Bold", fontSize=22, leading=28,
    textColor=PRIMARY, spaceAfter=14, alignment=TA_LEFT
)
h1_style = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontName="Helvetica-Bold", fontSize=18, leading=22,
    textColor=PRIMARY, spaceBefore=18, spaceAfter=10
)
h2_style = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontName="Helvetica-Bold", fontSize=14, leading=18,
    textColor=PRIMARY, spaceBefore=14, spaceAfter=8
)
h3_style = ParagraphStyle(
    "H3", parent=styles["Heading3"],
    fontName="Helvetica-Bold", fontSize=11, leading=15,
    textColor=black, spaceBefore=10, spaceAfter=4
)
body_style = ParagraphStyle(
    "Body", parent=styles["BodyText"],
    fontName="Helvetica", fontSize=10, leading=14,
    textColor=black, spaceAfter=6, alignment=TA_LEFT
)
quote_style = ParagraphStyle(
    "Quote", parent=body_style,
    fontName="Helvetica-Oblique", textColor=grey,
    leftIndent=14, spaceAfter=8
)
small_style = ParagraphStyle(
    "Small", parent=body_style,
    fontSize=8, textColor=grey
)


def clean(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r'<font color="#1C3D2E"><b>[\1]</b></font>', s)
    s = s.replace("→", "&rarr;").replace("×", "x")
    return s


def parse_markdown(md_text: str):
    """Return list of (kind, content) tuples."""
    out = []
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            out.append(("space", ""))
            continue
        if line.startswith("# "):
            out.append(("title", line[2:].strip()))
        elif line.startswith("## "):
            out.append(("h1", line[3:].strip()))
        elif line.startswith("### "):
            out.append(("h2", line[4:].strip()))
        elif line.startswith("#### "):
            out.append(("h3", line[5:].strip()))
        elif line.startswith("---"):
            out.append(("hr", ""))
        elif line.startswith("> "):
            out.append(("quote", line[2:].strip()))
        elif line.startswith("- "):
            out.append(("li", line[2:].strip()))
        elif line.startswith("|"):
            out.append(("table_row", line))
        else:
            out.append(("p", line.strip()))
    return out


def build_story(blocks):
    story = []
    pending_list = []
    pending_table = []

    def flush_list():
        nonlocal pending_list
        if pending_list:
            for item in pending_list:
                story.append(Paragraph("&bull; " + clean(item), body_style))
            story.append(Spacer(1, 0.2 * cm))
            pending_list = []

    def flush_table():
        nonlocal pending_table
        if pending_table:
            rows = []
            for r in pending_table:
                cells = [c.strip() for c in r.strip("|").split("|")]
                if all(re.match(r"^[-:\s]+$", c) for c in cells):
                    continue
                rows.append([Paragraph(clean(c), body_style) for c in cells])
            if rows:
                t = Table(rows, colWidths=[(17 * cm) / len(rows[0])] * len(rows[0]))
                t.setStyle(TableStyle([
                    ("GRID", (0, 0), (-1, -1), 0.25, grey),
                    ("BACKGROUND", (0, 0), (-1, 0), BG),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.append(t)
                story.append(Spacer(1, 0.3 * cm))
            pending_table = []

    for kind, content in blocks:
        if kind != "li":
            flush_list()
        if kind != "table_row":
            flush_table()

        if kind == "title":
            story.append(Paragraph(clean(content), title_style))
        elif kind == "h1":
            story.append(Paragraph(clean(content), h1_style))
        elif kind == "h2":
            story.append(Paragraph(clean(content), h2_style))
        elif kind == "h3":
            story.append(Paragraph(clean(content), h3_style))
        elif kind == "p":
            story.append(Paragraph(clean(content), body_style))
        elif kind == "quote":
            story.append(Paragraph(clean(content), quote_style))
        elif kind == "li":
            pending_list.append(content)
        elif kind == "table_row":
            pending_table.append(content)
        elif kind == "hr":
            story.append(Spacer(1, 0.3 * cm))
        elif kind == "space":
            story.append(Spacer(1, 0.15 * cm))

    flush_list()
    flush_table()
    return story


def main():
    with open(SOURCE, "r", encoding="utf-8") as f:
        md = f.read()

    blocks = parse_markdown(md)

    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="SANO SANO — Copywriting (Version Originale)",
        author="SANO SANO"
    )

    cover = [
        Spacer(1, 4 * cm),
        Paragraph("SANO SANO", title_style),
        Paragraph("Copywriting du site web", h1_style),
        Spacer(1, 0.5 * cm),
        Paragraph("<i>Version originale — sans flow social proof</i>", quote_style),
        Spacer(1, 0.5 * cm),
        Paragraph(
            "Document de référence pour révision copywriter. "
            "À comparer avec <b>social-proof-flow.md</b> pour voir la couche UX additionnelle proposée.",
            body_style
        ),
        PageBreak(),
    ]

    story = cover + build_story(blocks)
    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
