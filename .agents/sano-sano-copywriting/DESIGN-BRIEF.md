# SANO SANO — LANDING PAGE DESIGN BRIEF

## PROJECT OVERVIEW

**Brand:** Sano Sano  
**Type:** Showcase/Vitrine Website (non-commercial)  
**Target Audience:** Premium restaurants, hotels, celebration venues, health-conscious professionals  
**Primary Goal:** Establish brand authenticity and premium positioning through elegant, non-"AI-generated" design

---

## BRAND IDENTITY

### Core Positioning
- **Premium non-alcoholic botanical beverage**
- **Belgian origin** (Foster Farm, Wallonie)
- **Zero compromise philosophy** — health + taste, no sacrifices
- **Authenticity over trends** — real plants, real craftsmanship

### Tone of Voice
- Poetic but precise
- Confident without arrogance
- Sophisticated, refined
- Sensory-focused (tasting notes, sensations)
- Philosophical (why it exists, not just what it is)

### Key Messages
1. **No fermentation, no shortcuts** — born directly from plants
2. **Dynamisation process** — exclusive technique capturing plants at their peak
3. **Foster Farm heritage** — first Slow Food Farm in Belgium
4. **Sustainability** — regenerative agriculture, renewable energy, natural water source
5. **Uncompromising quality** — 0.00% alcohol, <6 kcal, organic certified

---

## COLOR PALETTE

All colors from PDF brand guidelines — maintain strict fidelity.

| Color | Hex | Usage | Notes |
|-------|-----|-------|-------|
| Cream | #F4F1EC | Primary background | Warm, elegant, premium |
| Text Dark | #1A1A18 | Primary text | Deep charcoal |
| Text Muted | #4A4A42 | Secondary text | For body copy |
| Green | #1a3a28 | Accent, CTA, emphasis | Natural, earth-tied |
| Green Light | #2D5C3F | Hover states, depth | Richer variant |
| Rose | #8B3A42 | Accent, emphasis, "100% festif" | Warm, celebratory |
| Rose Light | #A85460 | Hover states | Lighter variant |
| Gold | #9D7C2B | Accent, premium marker | Luxury signifier |
| White | #FFFFFF | Cards, overlays | High contrast elements |

**Palette Philosophy:**  
Dense, intentional. Not minimalist. Colors carry meaning and emotion. Green = nature/trust, Rose = celebration/warmth, Gold = premium/craftsmanship.

---

## TYPOGRAPHY

**Font Family:** Satoshi (sans-serif)  
**Weights Required:** 400, 600, 700, 900  
**Import:** Google Fonts CDN (included in current code)

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing |
|---------|------|--------|-------------|-----------------|
| H1 (Hero) | clamp(3.6rem, 8.5vw, 7.8rem) | 900 | 0.95 | -0.02em |
| H2 (Section titles) | clamp(1.8rem, 4vw, 2.8rem) | 900 | 1.1 | -0.01em |
| H3 (Subheadings) | 1.4–1.6rem | 700 | 1.2 | -0.005em |
| Body Copy | 1rem–1.05rem | 400–500 | 1.6–1.8 | 0em |
| Small Text | 0.9rem–0.95rem | 400 | 1.6 | 0em |
| Labels/Tags | 0.75rem | 600 | 1 | 0.08–0.18em |

**Typographic Principles:**
- Generous line-height for readability
- Tight letter-spacing on headlines for impact
- Hierarchy through weight + size, not color
- Avoid all-caps except for micro-labels

---

## LAYOUT & STRUCTURE

### Page Sections (Top to Bottom)

1. **Marquee Topbar** (Fixed, looping)
   - Key attributes: 0% alcohol, bio cert, <6 kcal, never fermented, etc.
   - Scrolls continuously, subtle, informational

2. **Navigation Bar** (Fixed, sticky)
   - Logo: "Sano Sano"
   - Links: Notre histoire | Nos saveurs | Le procédé
   - Mobile hamburger menu
   - Background: Semi-transparent cream with backdrop blur

3. **Hero Section** (Full viewport)
   - **Video background:** Foster Farm footage (17 sec, looping, muted, autoplay)
   - **Overlay:** Gradient (dark, for text readability)
   - **Content:** Centered text (left-aligned on desktop, responsive)
     - Label: "Boisson botanique belge premium"
     - Headline: "Zero compromis. / 100% festif." (100% in rose color)
     - Badges: 0% alcohol, Bio cert, <6 kcal (with icons)
     - CTA: "Découvrir nos saveurs" (outline button)
   - **Scroll indicator:** Bottom center, animated bounce

4. **Section: Pourquoi (Why)**
   - Background: White card (56px padding, rounded)
   - Headline: "Nous refusons les compromis. / Vous aussi, méritez mieux."
   - Copy: Philosophy statement + italic closing
   - Quote block: Chef sommelier testimonial (italic, attributed)
   - Certifications band: Icons + labels (6 items)

5. **Section: Saveurs (Flavors)**
   - Grid: 2 columns (responsive to 1 on mobile)
   - Two cards: Bulles Blanches (white/cream) + Bulles Rosées (rose)
   - Each card contains:
     - Visual: CSS-drawn bottle illustration or product photo
     - Badge: "Bulles Blanches" or "Bulles Rosées"
     - Name: "Basilic · Gingembre" or "Thym · Fraise"
     - Subtitle: Poetic descriptor
     - Tasting notes: 3 labeled sections (Attaque, Corps, Finale)
     - Ingredients list
     - CTA button (green for white, rose for pink)

6. **Section: Procédé (Process)**
   - Headline: "La dynamisation : quand la plante parle, nous l'écoutons."
   - Copy: Poetic explanation of the process
   - Visual: Animated dynamo illustration (spinning rings with plant icon)
   - Layout: Text left, visual right (stack on mobile)

7. **Section: Foster Farm (Origins)**
   - Headline: "Née à Foster Farm. / Portée par la terre belge."
   - Copy: Farm story + sustainability message
   - Icon blocks: 3 items (Water source, Green energy, Regenerative agriculture)
   - Visual: CSS botanical illustration (leaves, flowers)
   - Layout: Text left, visual right (stack on mobile)

8. **Section: Contact**
   - Headline: "Nous aimerions vous *rencontrer*." (*rencontrer* in rose)
   - Copy: Partnership message
   - Contact info: Email (jerome@osandrinks.com), Phone, Location
   - No form — direct contact links only

9. **Footer**
   - Background: Very light gray (rgba(26,26,24,0.05))
   - Text: Brand statement + copyright
   - Links: Legal, privacy, contact, press kit

---

## DESIGN PRINCIPLES

### Visual Language
- **Refined, not trendy** — avoid gradients, glassmorphism, heavy shadows
- **Botanical elements** — subtle leaf/plant illustrations (CSS or SVG, not photos)
- **Dense color use** — intentional placement, not scattered
- **White space** — generous margins, breathing room
- **Cards over full-width** — clear content containers for readability

### Animations & Interactions
- **Reveal animations:** Content fades in + slides up on scroll (gentle, 0.7s)
- **Hover states:** Subtle color shift, slight scale (for buttons/cards)
- **Scroll indicators:** Animated bounce, visible on hero
- **Video:** Auto-muted, loops seamlessly, responsive scaling

### Accessibility
- Sufficient color contrast (WCAG AA minimum)
- Semantic HTML structure maintained
- All images have alt text
- Keyboard navigation supported
- Form labels properly associated

### Responsiveness
- Mobile-first approach
- Breakpoints: 1024px (tablet), 768px (mobile), 480px (small phone)
- Hero: Full viewport on desktop, 80vh min on mobile
- Grid layouts: 2→1 column on mobile
- Font sizes: clamp() for fluid scaling

---

## SPECIFIC DESIGN DECISIONS

### Why No E-Commerce?
This is a **vitrine/showcase site**. Sano Sano is in development with premium partners (restaurants, hotels). No "Commander" buttons. Contact info only for B2B inquiries.

### Why Authentic Visuals?
- Foster Farm video in hero (real footage, authentic)
- Botanical CSS illustrations (intentional, not AI-generated)
- Tasting notes with sommelier language (elevates perception)
- Chef quote (social proof from authority)

### Why Dense Colors?
- Each color has meaning: Green (nature/trust), Rose (celebration), Gold (premium)
- Creates visual richness, opposite of "sterile AI feel"
- Premium brands use confident color choices

### Why Poetic Copy?
- Plants deserve poetic language (sensory, emotional)
- Differentiation from clinical "health drink" messaging
- Aligns with target audience (restaurants, chefs, refined palates)

---

## ASSETS PROVIDED

✅ **Copywriting:** Complete, organized by section (this file included)  
✅ **Video:** Foster Farm hero background (foster-farm-hero.mp4, 8.4 MB)  
✅ **Brand Guidelines:** Full PDF specifications (brand-guidelines.md)  
✅ **HTML Structure:** Landing page v3 (landing-page-v3.html)  
✅ **Color Palette:** CSS variables defined in code  
✅ **Typography:** Satoshi font family, all weights  

---

## DESIGN DELIVERABLES EXPECTED

1. **High-fidelity mockup** (desktop + mobile)
   - Figma, Adobe XD, or similar format
   - All sections, responsive states
   - Hover/active states for interactive elements

2. **Design system documentation**
   - Component library (buttons, badges, cards, forms)
   - Spacing scale, shadows, border-radius standards
   - Icon/illustration guidelines

3. **Implementation-ready specs**
   - CSS values for custom properties
   - Spacing/padding documentation
   - Animation specifications (timing, easing)

4. **High-resolution assets** (if custom illustrations)
   - SVG or PNG @2x for botanical elements
   - Optimized for web

---

## NEXT STEPS

1. Designer reviews this brief + copywriting
2. Concept sketches / mood board (optional but recommended)
3. High-fidelity mockup created
4. Implementation handoff to development
5. A/B test if needed (optional for vitrine)

---

## CONTACT FOR QUESTIONS

**Brand Owner:** Jerome (jerome@osandrinks.com, +32 475 95 46 33)  
**Location:** Wavre, Belgique  
**Reference:** Foster Farm, Wallonie, Belgium

---

**Brief Prepared:** May 18, 2026  
**Status:** Ready for design phase
