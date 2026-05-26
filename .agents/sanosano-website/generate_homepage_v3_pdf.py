#!/usr/bin/env python3
"""Generate PDF for SANO SANO Homepage v3 (7 sections)."""

import sys
sys.path.insert(0, "/home/user/Osan-drinks/.agents/sanosano-website")

from generate_original_pdf import (
    parse_markdown, build_story, title_style, h1_style, quote_style, body_style
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

OUTPUT = "/home/user/Osan-drinks/.agents/sanosano-website/SANO-SANO-HOMEPAGE-V3.pdf"
SOURCE = "/home/user/Osan-drinks/.agents/sanosano-website/homepage-v3.md"


def main():
    with open(SOURCE, "r", encoding="utf-8") as f:
        md = f.read()

    blocks = parse_markdown(md)

    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="SANO SANO — Homepage v3 (7 sections)",
        author="SANO SANO"
    )

    cover = [
        Spacer(1, 4 * cm),
        Paragraph("SANO SANO", title_style),
        Paragraph("Homepage v3 — 7 sections", h1_style),
        Spacer(1, 0.5 * cm),
        Paragraph("<i>Structure resserree pour le design</i>", quote_style),
        Spacer(1, 0.5 * cm),
        Paragraph(
            "Press bar integre au Hero. Section Moments supprimee. "
            "Instagram positionne apres les produits. 3 fusions internes pour un scroll digeste.",
            body_style
        ),
        PageBreak(),
    ]

    story = cover + build_story(blocks)
    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
