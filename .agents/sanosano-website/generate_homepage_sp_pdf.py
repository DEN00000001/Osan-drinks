#!/usr/bin/env python3
"""Generate PDF for SANO SANO Homepage with Social Proof."""

import sys
sys.path.insert(0, "/home/user/Osan-drinks/.agents/sanosano-website")

from generate_original_pdf import (
    parse_markdown, build_story, title_style, h1_style, quote_style, body_style
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

OUTPUT = "/home/user/Osan-drinks/.agents/sanosano-website/SANO-SANO-HOMEPAGE-SOCIAL-PROOF.pdf"
SOURCE = "/home/user/Osan-drinks/.agents/sanosano-website/homepage-social-proof.md"


def main():
    with open(SOURCE, "r", encoding="utf-8") as f:
        md = f.read()

    blocks = parse_markdown(md)

    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="SANO SANO — Homepage avec Social Proof",
        author="SANO SANO"
    )

    cover = [
        Spacer(1, 4 * cm),
        Paragraph("SANO SANO", title_style),
        Paragraph("Homepage avec Social Proof", h1_style),
        Spacer(1, 0.5 * cm),
        Paragraph("<i>Copy intégré avec les 8 modules social proof placés dans le flow</i>", quote_style),
        Spacer(1, 0.5 * cm),
        Paragraph(
            "Les blocs &laquo; SOCIAL PROOF &raquo; sont les ajouts proposes. Le copy original n'est pas modifie.",
            body_style
        ),
        PageBreak(),
    ]

    story = cover + build_story(blocks)
    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
