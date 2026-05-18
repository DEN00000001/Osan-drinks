# PROMPT ULTIMATE — SANO SANO LANDING PAGE
## Best-of-Breed: M3 + Apple HIG + Vercel + Stripe + Linear

> Le prompt le plus optimisé possible, combinant le meilleur de tous les design systems mondiaux.  
> Copy-paste directement dans V0, Lovable, Cursor, Claude, ou Figma AI.

---

## 🎯 LE PROMPT COMPLET (Copy-Paste)

```
You are a world-class product designer combining the best practices of Material Design 3 (color science, motion), Apple Human Interface Guidelines (typography rhythm, restraint), Vercel/Linear (technical elegance), and Stripe (editorial sophistication).

Design and code a complete, production-ready single-page landing site for "Sano Sano" — a Belgian premium non-alcoholic botanical beverage brand.

═══════════════════════════════════════════════════════════════
PART 1 — STRATEGIC CONTEXT (READ FIRST, INTERNALIZE)
═══════════════════════════════════════════════════════════════

▸ THE BRAND
Name: Sano Sano
Origin: Foster Farm, Wallonia, Belgium (first Slow Food Farm in Belgium)
Category: Premium non-alcoholic botanical sparkling beverage
Founder: Jerome, Wavre, Belgium
Site language: French (primary), with English subtitle support

▸ WHAT IT IS
- Botanical beverage (basil-ginger or thyme-strawberry)
- 0.00% alcohol, never fermented, never desalcoholized
- < 6 kcal / 100 ml, organic certified (FR-BIO-01)
- Made via exclusive "dynamisation" process (ultrasonic, never heat or alcohol)
- 75cl bottle, €9.90 retail (premium positioning)

▸ WHAT IT IS NOT
- NOT a "mocktail" or "0% wine"
- NOT a health drink masquerading as a treat
- NOT another generic non-alcoholic option
- NOT for sale on this site (B2B vitrine only — restaurants, hotels)

▸ BRAND VOICE
Poetic precision. Confident restraint. Sensory-led. Philosophical.
Think: A sommelier who is also a poet. A chef who is also a scientist.
Think LESS: Marketing-speak, wellness clichés, energy-drink shouting.

▸ AESTHETIC NORTH STAR
What we want: The quiet authority of Aesop's website. The editorial restraint
of Apple's product pages. The motion finesse of Linear. The typographic
density of Stripe Press. The color confidence of Hermès.

What we reject: AI-generated stock photos, glassmorphism, gradient overlays
without purpose, generic startup minimalism, wellness pastel palettes.

═══════════════════════════════════════════════════════════════
PART 2 — DESIGN SYSTEM TOKENS
═══════════════════════════════════════════════════════════════

▸ COLOR SYSTEM (Material Design 3 tonal palette, brand-customized)

Source brand colors:
- Sano Green:  #1a3a28 (primary, earth, trust)
- Sano Rose:   #8B3A42 (secondary, celebration, warmth)
- Sano Gold:   #9D7C2B (tertiary, premium marker)
- Cream:       #F4F1EC (surface background)

Generate M3 tonal palettes (tones 0-100) from each:

/* Brand primary (Green) */
--green-0:   #000000
--green-10:  #051D10
--green-20:  #0F3320
--green-30:  #1a3a28  /* BRAND PRIMARY */
--green-40:  #2D5C3F
--green-50:  #427353
--green-60:  #5D8A6C
--green-70:  #79A287
--green-80:  #97BDA3
--green-90:  #B5D7BF
--green-95:  #D5EBDC
--green-99:  #F4FBF6

/* Brand secondary (Rose) */
--rose-30:   #8B3A42  /* BRAND SECONDARY */
--rose-40:   #A85460
--rose-90:   #F3DCDE

/* Brand tertiary (Gold) */
--gold-30:   #9D7C2B  /* BRAND TERTIARY */
--gold-40:   #B89545
--gold-90:   #F0E3C0

/* Neutral surface (Cream-based) */
--surface:        #F4F1EC
--surface-dim:    #E8E5DE
--surface-bright: #FBFAF6
--surface-container-lowest: #FFFFFF
--surface-container-low: #FBFAF6
--surface-container: #F7F4EE
--surface-container-high: #FFFFFF
--surface-container-highest: #FFFFFF
--on-surface:     #1A1A18
--on-surface-variant: #4A4A42
--outline:        rgba(26,26,24,0.12)
--outline-variant: rgba(26,26,24,0.08)
--inverse-surface: #1A1A18
--inverse-on-surface: #F4F1EC

Color application rules:
- Cream surface is ALWAYS the primary background (never pure white)
- Green is for trust/nature moments (CTAs, primary buttons, eyebrows)
- Rose is for celebration/emphasis (italic words, accents, Bulles Rosées)
- Gold is sparingly used (premium markers, special labels — max 1 per section)
- White is for elevated surfaces (cards, modals) — NOT main background
- Dark surface only in footer

▸ TYPOGRAPHY (Apple HIG type discipline + Satoshi family)

Single font family: Satoshi (Google Fonts)
Weights loaded: 300, 400, 500, 600, 700, 900
Italic: Use the italic variants for emphasis (NEVER fake-italic CSS)

Type scale (10 sizes, modular harmony 1.250 ratio):

--text-display-xl:    clamp(4rem, 9vw, 8.5rem)    /* Hero only */
--text-display-lg:    clamp(2.8rem, 6vw, 4.5rem)  /* Section titles */
--text-display-md:    clamp(2.2rem, 4.5vw, 3.2rem) /* Sub-displays */
--text-heading-lg:    1.875rem  /* H3 large */
--text-heading-md:    1.5rem    /* H3 standard */
--text-heading-sm:    1.25rem   /* H4 */
--text-body-lg:       1.125rem  /* Lead paragraphs */
--text-body-md:       1rem      /* Default body */
--text-body-sm:       0.875rem  /* Captions */
--text-label:         0.75rem   /* Eyebrows, tags */

Weight assignments:
- Display: 900 (Black) for maximum impact
- Headings: 700 (Bold)
- Body: 400 (Regular)
- Lead/Subtitles: 400 italic for sensory descriptions
- Labels/Eyebrows: 600 (Semibold)
- Buttons: 600 (Semibold)

Line-heights (golden ratio inspired):
- Display: 0.95 to 1.05 (tight, dramatic)
- Headings: 1.2
- Body: 1.65 to 1.75 (generous reading)
- Labels: 1 (no extra spacing)

Letter spacing:
- Display: -0.025em (tight, premium)
- Headings: -0.015em
- Body: 0em
- Labels: 0.12em to 0.18em (UPPERCASE, generous)

▸ SPACING SYSTEM (8px base, T-shirt sizing)

--space-3xs:  2px
--space-2xs:  4px
--space-xs:   8px
--space-sm:   12px
--space-md:   16px
--space-lg:   24px
--space-xl:   32px
--space-2xl:  48px
--space-3xl:  64px
--space-4xl:  96px
--space-5xl:  128px
--space-6xl:  160px

Section padding: --space-4xl vertical (96px), --space-lg horizontal
Component padding: --space-2xl (48px) for cards, --space-md (16px) for buttons
Element gap: --space-md (16px) default, --space-xl (32px) for hero stack

▸ SHAPE SYSTEM (M3 corners, intentional)

--radius-none:  0
--radius-xs:    4px   /* Inputs */
--radius-sm:    8px   /* Tags, small chips */
--radius-md:    12px  /* Buttons (NOT pills) */
--radius-lg:    16px  /* Cards small */
--radius-xl:    20px  /* Cards medium */
--radius-2xl:   24px  /* Hero cards */
--radius-3xl:   32px  /* Feature cards */
--radius-full:  9999px  /* Pills, chips, badges only */

▸ ELEVATION SYSTEM (Subtle, premium)

--shadow-none:  none
--shadow-xs:    0 1px 2px 0 rgba(0,0,0,0.04)
--shadow-sm:    0 1px 3px 0 rgba(0,0,0,0.06), 0 1px 2px 0 rgba(0,0,0,0.03)
--shadow-md:    0 4px 12px -2px rgba(0,0,0,0.07), 0 2px 6px -1px rgba(0,0,0,0.04)
--shadow-lg:    0 12px 24px -6px rgba(0,0,0,0.08), 0 4px 8px -2px rgba(0,0,0,0.04)
--shadow-xl:    0 24px 48px -12px rgba(0,0,0,0.1)

Usage:
- Cards default: --shadow-sm
- Cards hover: --shadow-md
- Modals/dialogs: --shadow-lg
- AVOID heavy shadows (anything darker than 0.1 alpha)

▸ MOTION SYSTEM (Linear-inspired precision)

Durations:
--duration-instant: 50ms     /* Color/opacity micro */
--duration-fast:    150ms    /* Hovers, small transitions */
--duration-base:    250ms    /* Standard transitions */
--duration-slow:    400ms    /* Card movements */
--duration-slower:  600ms    /* Section reveals */
--duration-slowest: 800ms    /* Hero animations */

Easings (named, semantic):
--ease-linear:    linear
--ease-in:        cubic-bezier(0.4, 0, 1, 1)
--ease-out:       cubic-bezier(0, 0, 0.2, 1)            /* DEFAULT for entries */
--ease-in-out:    cubic-bezier(0.4, 0, 0.2, 1)
--ease-emphasized: cubic-bezier(0.2, 0, 0, 1)            /* M3 emphasized */
--ease-spring:    cubic-bezier(0.34, 1.56, 0.64, 1)     /* Springy bounces */
--ease-anticipate: cubic-bezier(0.36, 0, 0.66, -0.56)   /* Subtle pull-back */

▸ Z-INDEX SCALE
--z-base: 0
--z-content: 10
--z-sticky: 100
--z-nav: 200
--z-marquee: 250
--z-overlay: 500
--z-modal: 1000

═══════════════════════════════════════════════════════════════
PART 3 — COMPONENT LIBRARY
═══════════════════════════════════════════════════════════════

▸ BUTTONS

Primary (filled, green):
- Background: --green-30, color: white
- Padding: 14px 28px, radius: --radius-full
- Font: 0.95rem, weight 600, letter-spacing 0.02em
- Hover: bg --green-20, translateY(-1px), shadow --shadow-md
- Active: scale 0.97
- Focus: ring 3px --green-30 at 30% opacity

Secondary (outlined):
- Background: transparent, color: --on-surface
- Border: 1.5px solid --outline
- Hover: bg --surface-container, border --on-surface

Tertiary (text only):
- No background, no border
- Color: --green-30
- Underline on hover
- Subtle slide-right on icon

Ghost (for hero on dark video):
- Background: transparent, color: white
- Border: 1.5px solid rgba(255,255,255,0.6)
- Hover: bg rgba(255,255,255,0.1)

▸ CHIPS / BADGES

Assist chip (icon + text):
- Padding: 8px 14px, radius: --radius-full
- Background: --green-90 or --rose-90 (tinted by context)
- Color: --green-20 or --rose-30
- Font: 0.85rem, weight 600
- Icon size: 0.9rem, gap 6px

Filter chip:
- Same shape, neutral by default
- Background: --surface-container, border: 1px --outline
- Selected: bg --green-30, color white

▸ CARDS

Elevated card:
- Background: --surface-container-high (white)
- Radius: --radius-2xl (24px)
- Padding: --space-2xl (48px)
- Shadow: --shadow-sm
- Hover: shadow --shadow-md, translateY(-4px), transition 400ms

Filled card:
- Background: --green-95 or --rose-90
- No shadow
- Used for emphasis/quote blocks

Outlined card:
- Background: --surface
- Border: 1px solid --outline-variant
- No shadow
- Used for stats, secondary info

▸ INPUTS (not used in this site but defined)
- Outlined variant only (cleaner than filled for premium)
- Floating label (M3 standard)
- Border: 1px --outline → focus: 2px --green-30

═══════════════════════════════════════════════════════════════
PART 4 — PAGE STRUCTURE (TOP TO BOTTOM)
═══════════════════════════════════════════════════════════════

LAYER 1 — MARQUEE TOPBAR
- Position: fixed top, z-index 250
- Height: 36px
- Background: --green-30
- Color: --green-95
- Content scrolling horizontally (40s infinite loop):
  "0,00% Alcool · Bio Certifié FR-BIO-01 · < 6 kcal · Jamais fermentée · Slow Food Farm Belgique · Sans gluten · Sans sulfites · Procédé exclusif de dynamisation"
- Typography: label-small, weight 600, uppercase, tracking 0.15em
- Dots between items: 4px circles, --green-90 at 50%

LAYER 2 — NAVIGATION BAR
- Position: fixed, top: 36px, z-index 200
- Height: 72px
- Background: rgba(244,241,236,0.85) with backdrop-filter: blur(20px) saturate(180%)
- Border-bottom: 1px solid --outline-variant
- Layout: Flexbox justify-between, max-width 1280px, padding 0 32px

Logo (left):
- Wordmark: "Sano Sano"
- Satoshi 900, 1.3rem, color: --on-surface
- Letter-spacing: -0.02em

Navigation links (center, desktop only):
- "Notre histoire · Nos saveurs · Le procédé"
- Satoshi 600, 0.9rem
- Color: --on-surface, hover: --green-30
- Underline-on-hover from center (transform-origin trick)
- Gap: 40px

Right side:
- Desktop: subtle "Contact" text link (color --green-30)
- Mobile: Hamburger icon (3 lines, 24x24px)

═════════════════════

SECTION 1 — HERO (after fixed bars)
- Min-height: 100vh
- Padding-top: 108px (offset for fixed bars)
- Position: relative, overflow: hidden

Background:
- HTML5 video element, fullscreen
- Source: ./images/foster-farm-hero.mp4
- Attributes: autoplay, muted, loop, playsinline
- object-fit: cover, opacity: 1
- Position absolute, full coverage, z-index --z-base

Overlay:
- Position absolute, full coverage, z-index --z-content
- Background: linear-gradient(
    180deg,
    rgba(26,26,24,0.55) 0%,
    rgba(26,26,24,0.45) 40%,
    rgba(0,0,0,0.65) 100%
  )

Content Container (z-index --z-content + 1):
- Max-width: 920px
- Margin: 0 auto
- Padding: 130px 32px 120px
- Display: flex column, justify-content: center
- Min-height: calc(100vh - 108px)

Content Stack (top to bottom):

1. Eyebrow Label
   "Boisson botanique belge premium"
   - text-label, color: rgba(255,255,255,0.85)
   - Preceded by: <span class="line"></span> (28px horizontal line)
   - Gap between line and text: 12px
   - Display flex align center
   - Margin-bottom: 32px

2. Hero Display Headline (H1)
   Line 1: "Zero compromis."
   Line 2: "100% festif." 
   — where "100%" is italic, color: --rose-30, NOT white
   - text-display-xl, weight 900
   - Color: white
   - Line-height: 0.95
   - Letter-spacing: -0.03em
   - Text-shadow: 0 4px 24px rgba(0,0,0,0.4)
   - Margin-bottom: 40px
   - Animate: line 1 reveals first (delay 0ms), line 2 reveals (delay 200ms)

3. Hero Description (optional, max 1 line)
   "Cueillies à leur apogée. Dynamisées sans alcool, sans chaleur. À Foster Farm, en Wallonie."
   - text-body-lg, color: rgba(255,255,255,0.85)
   - Max-width: 560px
   - Margin-bottom: 48px

4. Badges Row (3 chips, horizontal flex, gap 12px)
   [○ 0,00% Alcool] [✿ Bio FR-BIO-01] [◇ < 6 kcal / 100ml]
   - Background: rgba(255,255,255,0.10)
   - Backdrop-filter: blur(8px)
   - Border: 1px solid rgba(255,255,255,0.18)
   - Color: white
   - Padding: 9px 18px, radius: --radius-full
   - Font: 0.85rem, weight 600
   - Icon: 0.95rem, gap 8px
   - Margin-bottom: 56px

5. CTA Group (horizontal flex, gap 16px)
   Primary CTA (Ghost button on dark):
   "Découvrir nos saveurs →"
   - Border: 1.5px solid rgba(255,255,255,0.7)
   - Color: white
   - Padding: 14px 28px, radius: --radius-full
   - Hover: bg rgba(255,255,255,0.1), border white
   - Arrow icon: slides right 4px on hover

   Secondary (Text link with arrow):
   "Le procédé →"
   - Color: rgba(255,255,255,0.7)
   - Underline on hover

6. Scroll Indicator (bottom center, absolute)
   - Position: absolute, bottom: 32px, left: 50%, translateX(-50%)
   - Chevron-down icon (1.5px stroke, white at 50%)
   - "Découvrir" label below, label-small, white at 50%
   - Animation: vertical bounce 2s infinite ease-in-out

═════════════════════

SECTION 2 — POURQUOI (Why)
- Background: --surface (cream)
- Padding: 128px 0
- Container: max-width 1080px, padding 0 32px

Layout:
1. Eyebrow label (center): "Fondée sur un refus simple"
   - color: --gold-30, label, uppercase, tracking 0.15em
   - Margin-bottom: 16px

2. Section Title (H2, center):
   "Nous refusons les compromis."
   "Vous aussi, méritez mieux."
   - text-display-lg, weight 900
   - Color: --on-surface
   - Line 1 and Line 2 (stacked, separate lines)
   - Margin-bottom: 80px

3. Philosophy Card (elevated, centered, max-width 800px, margin auto)
   - Background: --surface-container-highest (white)
   - Padding: 64px 56px
   - Radius: --radius-3xl (32px)
   - Shadow: --shadow-sm

   Content (3 paragraphs, separator: 16px margin-bottom):
   P1: "Pendant des années, les boissons sans alcool vous obligeaient à choisir : la santé ou le plaisir. Le goût réel ou la responsabilité."
   - text-body-lg, color: --on-surface-variant

   P2: "Sano Sano arrive quand vous en avez assez de cette fausse dichotomie."
   - text-body-lg, color: --on-surface, weight 500

   P3 (italic, primary green): "Nous ne désalcoolisons rien. Nous ne diluons rien. Nous ne cachons rien derrière du sucre ou des arômes artificiels."
   "Nous révélons simplement ce que chaque plante a à dire — et vous l'écoutez en bouteille."
   - text-body-lg, italic, color: --green-30

4. Quote Block (sommelier testimonial)
   - Margin-top: 80px
   - Background: --green-95 (light green tint)
   - Border-left: 4px solid --green-30
   - Padding: 48px 56px
   - Radius: --radius-2xl (right-side only, left flat from border)
   - Max-width: 800px, margin: auto

   Quote text:
   "Une complexité aromatique que je n'aurais pas cru possible sans fermentation. L'attaque est nette, la longueur surprenante. Sano Sano redéfinit ce qu'un accord mets-boissons peut être pour les convives qui ne boivent pas d'alcool."
   - text-body-lg, italic, color: --green-10
   - Margin-bottom: 24px

   Attribution: "— Thomas V., Chef sommelier · Bruxelles"
   - text-body-sm, weight 600, color: --green-30, NOT italic

5. Certifications Band
   - Margin-top: 80px
   - Display: flex, justify-content center, flex-wrap wrap, gap 16px
   - 6 chips:
     [○ Alcohol-Free 0,00%] [✿ Bio FR-BIO-01] [◎ Gluten-Free]
     [◇ Sulphite-Free] [❧ Veggie Friendly] [◈ < 6 kcal]
   - Style: assist chips, --surface-container background, --on-surface text

═════════════════════

SECTION 3 — NOS SAVEURS (Flavors)
- Background: --surface-container (slightly darker cream tint, for visual rhythm)
- Padding: 128px 0
- Container: max-width 1280px, padding 0 32px

Layout:
1. Eyebrow label (center): "Deux caractères, une même âme"
   - color: --rose-30, label style

2. Section Title (center):
   "Fermez les yeux."
   "Laissez les plantes parler."
   - text-display-lg, color: --on-surface
   - Margin-bottom: 80px

3. Saveurs Grid (2 columns desktop, 1 column mobile, gap 32px)

CARD 1 — BULLES BLANCHES (Elevated card):
- Background: --surface-container-highest (white)
- Radius: --radius-3xl (32px)
- Overflow: hidden
- Shadow: --shadow-sm
- Hover: --shadow-md, translateY(-6px), transition 400ms
- Transition: all 400ms emphasized easing

Top — Visual Section (height 320px):
- Background: linear-gradient(135deg, #F4F1EC 0%, #E8E5DE 50%, #DDD8CE 100%)
- Position relative, overflow hidden
- Centered bottle illustration:
  - SVG bottle outline (elegant, narrow, tall — wine-bottle proportions)
  - Color: rgba(26,58,40,0.15) stroke, rgba(255,255,255,0.4) fill
  - Bottle has subtle vertical highlight (gradient on left edge)
  - Dimensions: 80px wide, 240px tall
- Floating bubbles (4 circles, varied sizes 4-10px):
  - Color: rgba(255,255,255,0.5)
  - Positions: randomized, animated rising slowly (8-12s loop)
- Bottle label area (white rectangle, centered on bottle):
  - 60% of bottle width
  - Background: rgba(255,255,255,0.85)
  - Border-radius: 2px
  - Contains "Sano Sano" in mini logo (1px text, --green-30)

Bottom — Body Section (padding 48px 40px):

- Badge (tonal pill, top of body):
  "BULLES BLANCHES"
  - Background: --green-95
  - Color: --green-20
  - Padding: 6px 14px, radius: full
  - Font: 0.72rem, weight 700, uppercase, tracking 0.15em
  - Inline-flex, self-aligned start

- Flavor Name (H3):
  "Basilic · Gingembre"
  - text-heading-lg (1.875rem), weight 700
  - Color: --on-surface
  - Margin: 16px 0 8px

- Subtitle (italic):
  "Quand l'herbacée franc rencontre l'épice subtile"
  - text-body-md, italic, color: --on-surface-variant
  - Margin-bottom: 32px

- Tasting Notes (3 entries, structured layout):
  Each entry is a 2-column grid (100px label / 1fr content):

  ┌─────────────────────────────────────────────┐
  │ ATTAQUE  │ La verdeur herbacée du basilic   │
  │          │ s'impose avec franchise, vive et │
  │          │ presque végétale — comme un      │
  │          │ jardin en été après la pluie.    │
  ├──────────┼───────────────────────────────────┤
  │ CORPS    │ Le gingembre prend la relève    │
  │          │ avec une chaleur épicée et       │
  │          │ tonique, structurée, sans jamais │
  │          │ dominer.                          │
  ├──────────┼───────────────────────────────────┤
  │ FINALE   │ Longue, fraîche, équilibrée.    │
  │          │ Extra brute. Élégante comme une  │
  │          │ entrée réussie.                  │
  └─────────────────────────────────────────────┘

  - Labels (left column):
    - text-label (0.72rem), weight 700, uppercase, tracking 0.18em
    - Color: --green-30
    - Vertical align: top
  - Notes (right column):
    - text-body-md, color: --on-surface-variant
    - Line-height: 1.65
  - Dividers between entries: 1px solid --outline-variant
  - Padding per row: 16px 0

- Ingredients Block:
  - Margin-top: 32px
  - Background: --surface
  - Padding: 16px 20px
  - Radius: --radius-lg
  - "Ingrédients :" label (weight 700, color --on-surface) + body
  - Full text: "Eau, basilic*, miel d'acacia*, gingembre*, acide ascorbique, acide citrique."
  - Footnote: "* Issu de l'agriculture biologique"
  - text-body-sm, color: --on-surface-variant

CARD 2 — BULLES ROSÉES (same structure, themed in rose):

Visual section:
- Background: linear-gradient(135deg, #FDE8EA 0%, #F0D0D4 50%, #E5B8BE 100%)
- Bottle illustration: rose-tinted (rgba(139,58,66,0.15) stroke)
- Floating bubbles: rgba(255,200,205,0.5)

Body:
- Badge: "BULLES ROSÉES" — bg --rose-90, color --rose-30
- Name: "Thym · Fraise" — same H3 style
- Subtitle: "L'inattendu qui ravit : sucré et herbacé en harmonie"
- Tasting Notes labels color: --rose-30 (instead of --green-30)
- Notes content:
  - Attaque: "Une note herbacée de thym s'ouvre délicatement, aromatique, presque florale — inattendue et captivante."
  - Corps: "La fraise s'invite avec douceur et acidité maîtrisée, arrondissant l'herbe, créant une complexité rare."
  - Finale: "Désaltérante, nuancée, extra brute. Vous ne vous attendiez pas à ça — et c'est exactement ça."
- Ingredients: "Eau, fraise*, framboise*, miel d'acacia*, thym*, acide ascorbique, acide citrique. * Issu de l'agriculture biologique"

═════════════════════

SECTION 4 — LE PROCÉDÉ (Process)
- Background: --surface (cream)
- Padding: 128px 0
- Container: max-width 1280px, padding 0 32px

Layout: 2-column grid (1fr 1fr) on desktop, 1 column on mobile
Gap: 96px

LEFT COLUMN (text):

1. Eyebrow: "La révélation, pas l'invention"
   - Color: --gold-30, label style

2. Section Title (H2):
   "La dynamisation : quand la plante parle, nous l'écoutons."
   - text-display-md, weight 900
   - Color: --on-surface
   - Margin-bottom: 32px

3. Body content (5 paragraphs):
   P1: "Chaque plante a un moment précis — une seconde dans le temps — où elle exprime complètement sa nature. C'est comme un musicien qui trouve la note parfaite. Nous attendons ce moment exact."
   - text-body-lg, color: --on-surface-variant

   P2: "À Foster Farm, une Slow Food Farm certifiée en Belgique, nous capturons les plantes à cet instant de grâce. Pas une seconde avant. Pas une seconde après."
   - text-body-lg, color: --on-surface-variant

   P3 (PULL QUOTE styling — italic, larger, primary green):
   "Ce que vous ressentez en bouteille, c'est cette perfection figée dans le temps."
   - text-body-lg + 2px, italic, color: --green-30, weight 500
   - Padding: 24px 0
   - Border-top/bottom: 1px solid --outline-variant
   - Margin: 32px 0

   P4: "Par un procédé exclusif — jamais de chaleur, jamais d'alcool — nous libérons ce qu'il y a de plus vrai dans chaque tige, chaque feuille. Juste la plante, à son apogée, figée dans le temps."

   P5: "Le résultat en bouteille : bulles fines, ultra-légères, moins de 6 kcal, une finale longue comme une conversation qui s'éternise sur votre table. Authentique."

RIGHT COLUMN (Dynamo Visual):

Container: aspect-ratio 1:1, max-width 480px, margin: auto
Position: sticky top 120px on desktop (scrolls with content)

3 Concentric Animated Rings (SVG or CSS):
- Outer ring (size 100%):
  - Border: 1.5px solid rgba(26,58,40,0.20)
  - Rotation: 60s clockwise infinite linear
- Middle ring (size 75%):
  - Border: 1.5px solid rgba(26,58,40,0.30)
  - Rotation: 45s counter-clockwise infinite linear
- Inner ring (size 50%):
  - Border: 1.5px solid rgba(26,58,40,0.40)
  - Rotation: 30s clockwise infinite linear

Each ring has a dot at top (translates -50% on rotation):
- Size: 8px circle
- Color: --green-30
- Position: top: -4px (overlapping ring)

Center medallion:
- Size: 25% (smallest, ~120px)
- Background: --green-95
- Border: 2px solid --green-30
- Border-radius: 50%
- Display: flex column, center
- Contents:
  - Icon: large botanical glyph (❧ or custom SVG leaf)
    - Size: 2.5rem
    - Color: --green-30
  - Label: "DYNAMISATION"
    - text-label, color: --green-20
    - Margin-top: 4px

═════════════════════

SECTION 5 — FOSTER FARM (Origins)
- Background: --green-95 (light green tint — section change for visual rhythm)
- Padding: 128px 0
- Container: max-width 1280px, padding 0 32px

Layout: 2-column grid, gap 96px, mobile stacks

LEFT COLUMN (text):

1. Eyebrow: "Nos origines"
   - Color: --green-30, label style

2. Section Title:
   "Née à Foster Farm."
   "Portée par la terre belge."
   - text-display-md
   - Color: --green-10 (dark green)
   - Margin-bottom: 32px

3. Body content (2 paragraphs):
   P1: "Sano Sano prend racine à Foster Farm, la première Slow Food Farm de Belgique, nichée en Wallonie. Ici, l'agriculture régénérative n'est pas un argument marketing — c'est une philosophie de vie. Les sols sont nourris, l'eau respectée, chaque plante cultivée avec la même intention que celle qui finira dans votre verre."
   - text-body-lg, color: --green-20

   P2: "Tous nos ingrédients sont bio certifiés. L'énergie consommée est renouvelable. Et l'eau qui entre dans chaque bouteille vient directement d'une source naturelle. Boire Sano Sano, c'est choisir un système alimentaire différent."
   - text-body-lg, color: --green-20
   - Margin-bottom: 48px

4. Feature List (3 items, stacked, each item is flex row):

Item 1:
- Icon container: 56px circle, --surface-container-highest bg, --green-30 icon
  - Icon: 💧 (water drop) or SVG equivalent (1.5rem)
- Text container (margin-left 20px):
  - Title: "Eau de source"
    - text-heading-sm, weight 700, color: --green-10
  - Description: "Issue d'une source naturelle belge, non traitée chimiquement."
    - text-body-sm, color: --green-20

Item 2:
- Icon: ☀ (sun)
- Title: "Énergie 100% verte"
- Description: "Toute la production fonctionne à l'énergie renouvelable."

Item 3:
- Icon: 🌿 (herb)
- Title: "Agriculture régénérative"
- Description: "Foster Farm, 1ère Slow Food Farm de Belgique. Les sols donnent plus qu'ils ne reçoivent."

Gap between items: 24px

RIGHT COLUMN (Botanical Art):

Container: aspect-ratio 1:1, max-width 480px
Use SVG for crisp scaling. Composition:

- 4 organic leaves (hand-drawn feel):
  - Varied sizes (60-120px)
  - Positioned organically (golden ratio spiral)
  - Colors: alternating --green-30 and --green-40
  - Stroke: 1.5px, fill: --green-90 at 50% opacity
  - Subtle individual floating animation (gentle 6s ease-in-out, independent timing)

- 1 stylized flower (center-ish):
  - 5 petals, each: ellipse 30x60px
  - Color: --rose-90 fill, --rose-30 stroke
  - Center: 16px circle, --gold-30 fill
  - Slow rotation (40s)

- 2-3 small dots/seeds:
  - 4-6px circles, --green-20

═════════════════════

SECTION 6 — CONTACT
- Background: --surface (cream)
- Padding: 128px 0 96px
- Container: max-width 720px, margin: auto, padding 0 32px, text-align: center

1. Eyebrow: "Pour en savoir plus"
   - Color: --gold-30, label style
   - Center-aligned

2. Section Title:
   "Nous aimerions vous rencontrer."
   — where "rencontrer" is italic, color: --rose-30
   - text-display-md, weight 900
   - Color: --on-surface
   - Center-aligned
   - Margin-bottom: 32px

3. Body copy:
   "Sano Sano est actuellement en développement auprès de partenaires premium : restaurants, hôtels, et lieux de célébration qui partagent nos valeurs."
   
   "Pour découvrir nos saveurs, des questions, ou des partenariats — contactez-nous directement."
   - text-body-lg, color: --on-surface-variant
   - Max-width: 540px, margin: auto
   - Margin-bottom: 64px

4. Contact Methods (vertical stack, centered, gap 20px):

Method 1 — Email:
- Display flex row, gap 14px, align center, justify center
- Icon: 24x24 SVG email icon, color --green-30
- Link: "jerome@osandrinks.com"
  - text-body-lg, weight 600, color: --green-30
  - Underline on hover

Method 2 — Phone:
- Icon: 24x24 phone SVG, color --green-30
- Link: "+32 475 95 46 33"
  - text-body-lg, weight 600, color: --green-30
  - Underline on hover

Method 3 — Location:
- Icon: 24x24 map-pin SVG, color --on-surface-variant
- Text: "Wavre, Belgique"
  - text-body-md, color: --on-surface-variant
  - NOT a link

═════════════════════

FOOTER
- Background: --on-surface (dark)
- Color: --surface
- Padding: 80px 32px 40px
- Container: max-width 1280px, margin auto

Layout: Grid 2 columns desktop (1fr 1fr), 1 column mobile, gap 64px

Left column:
- Logo wordmark "Sano Sano": Satoshi 900, 1.5rem, --surface
- Tagline below: "Botanical Bubbles · Zero Compromise. Full Celebration."
  - text-body-md, opacity 0.7
  - Margin-top: 12px
- Origin: "Made in Wallonia. Born at Foster Farm."
  - text-body-sm, opacity 0.5
  - Margin-top: 24px

Right column (3 sub-columns):
Sub 1 — Découvrir:
- Heading: "DÉCOUVRIR" (text-label, weight 700, opacity 0.5)
- Links (stacked):
  - Notre histoire
  - Nos saveurs
  - Le procédé
  - Foster Farm

Sub 2 — Partenaires:
- Heading: "PARTENAIRES"
- Links:
  - Restaurants
  - Hôtels
  - Caves
  - Press Kit

Sub 3 — Légal:
- Heading: "LÉGAL"
- Links:
  - Mentions légales
  - Confidentialité
  - Cookies
  - CGV

Bottom Bar (separated by 1px solid rgba(244,241,236,0.1)):
- Margin-top: 64px, Padding-top: 32px
- Layout: flex justify-between, align center
- Left: "© 2026 OSAN SRL · Tous droits réservés"
  - text-body-sm, opacity 0.5
- Right: Social icons (3): Instagram, LinkedIn, YouTube
  - 24x24px each, --surface color at 50% opacity
  - Hover: opacity 100%

═══════════════════════════════════════════════════════════════
PART 5 — INTERACTIONS & MICRO-INTERACTIONS
═══════════════════════════════════════════════════════════════

▸ SCROLL-TRIGGERED REVEALS (IntersectionObserver)
- Trigger: Element 15% in viewport
- Effect: opacity 0→1 + translateY(40px→0)
- Duration: 700ms
- Easing: cubic-bezier(0.2, 0, 0, 1)
- Stagger children: 120ms delay per item
- Once only (no re-trigger on scroll back)

Apply to:
- Section eyebrow labels
- Section titles (line by line)
- Body paragraphs
- Cards (with stagger across grid)
- List items (with stagger)

▸ HOVER STATES (All Interactive Elements)

Buttons:
- Color/background transition: 150ms ease-out
- Subtle lift: translateY(-1px)
- Optional state-layer: 8% black overlay

Cards:
- Shadow upgrade: --shadow-sm → --shadow-md
- Lift: translateY(-4px)
- Transition: 400ms emphasized easing
- Optional: inner image scale 1.02

Text Links:
- Underline appears from left (transform-origin: left, scale-X 0→1)
- Color shift: --on-surface → --green-30
- Duration: 250ms

Icons:
- Subtle scale: 1 → 1.1
- Color shift to brand color
- Optional rotation for chevrons

▸ HEADER BEHAVIOR ON SCROLL
- 0-80px scroll: transparent navbar
- 80px+ scroll: full backdrop blur + opacity bg
- Scroll down: hide navbar (translateY(-100%))
- Scroll up: show navbar (translateY(0))
- Transition: 300ms

▸ VIDEO HERO
- Autoplay on load
- Fade-in: opacity 0→1 over 1.2s
- IF browser blocks autoplay: fallback to static frame (extract first frame as poster)
- Lazy-load any below-fold videos

▸ MARQUEE
- CSS animation: translateX(0 → -50%) infinite, 40s linear
- Pause on hover (subtle UX)
- Duplicate content for seamless loop

▸ DYNAMO RINGS
- Pure CSS rotations (transform: rotate)
- Each ring different speed and direction
- Use will-change: transform for GPU acceleration

▸ BOTANICAL ART (Foster Farm)
- Each leaf has individual ease-in-out floating
- Use SVG with subtle filters or animate transform
- Independent timing keeps composition organic

▸ FOCUS STATES (Accessibility critical)
- All interactive elements: 3px solid ring, --green-30 color, 2px offset
- Visible only on keyboard focus (use :focus-visible)
- High contrast mode support

═══════════════════════════════════════════════════════════════
PART 6 — RESPONSIVE STRATEGY
═══════════════════════════════════════════════════════════════

Mobile-first approach. Breakpoints:

@media (min-width: 600px) { /* tablet */ }
@media (min-width: 900px) { /* desktop */ }
@media (min-width: 1280px) { /* wide */ }

▸ MOBILE (< 600px)

- Section padding: 80px 24px (vertical reduced)
- Hero: full viewport maintained, smaller display
  - Headline: clamp(2.8rem, 12vw, 4rem)
  - Badges: wrap to 2 lines if needed
  - CTAs: full width buttons
- Saveurs: 1 column, full-width cards
  - Card padding: 32px 24px
  - Tasting notes: stack labels above content (single column)
- Procédé: stack, visual goes ABOVE text
  - Dynamo: scale down to 280px max
- Foster Farm: stack, botanical art above
- Navigation: Hamburger drawer (full-screen overlay)
  - Drawer animation: slide from right
  - Items: large tap targets (56px min height)
- Marquee: smaller text (0.65rem), faster speed
- Footer: stack all columns, center text

▸ TABLET (600-899px)
- Section padding: 96px 32px
- Saveurs: 1 column still (more legible than cramped 2-col)
- Procédé/Foster: stack still
- Navigation: hamburger still

▸ DESKTOP (900px+)
- Full 2-column layouts active
- Hero: 920px max content width
- Navigation: full link bar visible

▸ WIDE (1280px+)
- Increase max-width to 1440px for hero, sections
- Larger typography on display headlines
- More generous gutters

═══════════════════════════════════════════════════════════════
PART 7 — PERFORMANCE & SEO
═══════════════════════════════════════════════════════════════

▸ Performance budgets:
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.05
- Total page weight: < 2 MB (incl. video)

▸ Optimizations:
- Video: H.264 MP4, 720p max, ~8 MB target
- Add poster image for video (extract first frame)
- Preload hero video, font subset
- Lazy-load below-fold images
- CSS: inline critical, defer rest
- JS: minimal (only IntersectionObserver, scroll handler, marquee)
- Use Intersection Observer (not scroll events) for reveals

▸ SEO:
- Title: "Sano Sano — Boisson botanique belge sans alcool premium"
- Meta description: "Sano Sano. 0,00% alcool, bio certifié, <6 kcal. Botanical bubbles nées à Foster Farm en Wallonie. Zero compromis. 100% festif."
- Open Graph image: 1200x630px brand hero shot
- Twitter card: summary_large_image
- Structured data: Schema.org Organization + Product (FoodEstablishment context)
- Canonical URL set
- Language: <html lang="fr">
- Alternate language: en (if available)

▸ Accessibility:
- WCAG 2.1 AA compliant
- All images have descriptive alt text
- Form labels properly associated (if forms added later)
- Skip-to-content link
- Color contrast verified (4.5:1 body, 3:1 large)
- Keyboard navigation: full coverage
- Screen reader testing: passes NVDA/VoiceOver
- Reduced motion: respect prefers-reduced-motion

═══════════════════════════════════════════════════════════════
PART 8 — WHAT NOT TO DO
═══════════════════════════════════════════════════════════════

❌ Glassmorphism effects (overused, dating fast)
❌ Heavy gradients (only subtle hero overlay allowed)
❌ Roboto, Inter, or generic sans (Satoshi only)
❌ Pure white backgrounds (always cream)
❌ E-commerce elements (no cart, no buy buttons, no prices)
❌ Stock photography (use only the Foster Farm video and authentic assets)
❌ AI-generated imagery (visible artifacts kill premium feel)
❌ Animated GIF backgrounds
❌ Excessive shadow depth (max alpha 0.1)
❌ Border-radius inconsistencies
❌ Off-brand colors
❌ All-caps body text (only labels)
❌ Centered body text in long paragraphs
❌ Floating action buttons
❌ Newsletter popups
❌ Cookie banner with marketing options (this is vitrine, minimal data)
❌ Generic icon sets (use custom or Lucide)
❌ Emoji as primary content (only as icon hints in Foster section)
❌ Lorem ipsum in production (only the provided French copy)

═══════════════════════════════════════════════════════════════
PART 9 — DELIVERABLES
═══════════════════════════════════════════════════════════════

Generate:
1. Complete index.html with semantic HTML5
2. style.css with all design tokens as CSS custom properties
3. script.js for IntersectionObserver reveals, mobile menu, marquee
4. All sections fully built with provided French copy
5. SVG illustrations (bottles, botanical art, dynamo) generated inline or as separate SVG files
6. Responsive across all breakpoints
7. Production-quality code (no console.logs, no commented dead code)

Tech requirements:
- Pure HTML/CSS/JS (no framework dependency)
- Google Fonts: Satoshi (300-900 + italic)
- Video placeholder: ./images/foster-farm-hero.mp4
- Modern CSS (custom properties, grid, flexbox, clamp)
- Vanilla JS (no jQuery)
- Test in Chrome, Safari, Firefox latest

Output structure:
/
├── index.html
├── styles/
│   ├── tokens.css         (design tokens)
│   ├── reset.css           (modern reset)
│   ├── typography.css      (type system)
│   ├── components.css      (buttons, cards, chips)
│   └── sections.css        (page-specific)
├── scripts/
│   ├── reveal.js           (IntersectionObserver)
│   ├── nav.js              (mobile menu)
│   └── marquee.js          (topbar loop)
├── images/
│   └── foster-farm-hero.mp4 (provided)
└── fonts/                   (if self-hosting Satoshi)

═══════════════════════════════════════════════════════════════
END OF PROMPT — Begin generation.
═══════════════════════════════════════════════════════════════
```

---

## 🎁 BONUS — ENHANCEMENTS POSSIBLES

Si tu veux pousser encore plus loin, ajoute à la fin du prompt :

### Niveau "Awwwards"
```
Make this page worthy of an Awwwards "Site of the Day" nomination. Add:
- Custom cursor on desktop (small circle that morphs near interactive elements)
- Smooth scroll-driven animations (Locomotive Scroll or native scroll-timeline)
- Image reveal masks (clip-path animations) on hero entry
- Magnetic buttons (slight cursor attraction on hover)
- Page transition between sections (subtle parallax)
- Sound design: optional subtle pour sound on hero (muted by default)
```

### Niveau "FWA Award"
```
Add:
- Three.js bottle visualization (rotatable 3D bottle on saveurs cards)
- WebGL particles on hero (subtle floating botanicals)
- Scroll-triggered video playback (control video timeline with scroll position)
- Generative botanical art (procedurally drawn each load, slight variations)
- Time-based content adaptation (different greetings morning/evening)
```

### Niveau "Studio Sophie Klein / Locomotive"
```
Make it editorial. Add:
- Magazine-style typography (large numerals as section markers: 01, 02, 03)
- Asymmetric layouts (intentional visual tension)
- Image grids with varied aspect ratios
- Editorial spreads (large image + caption combos)
- Stroke-drawn illustrations (line art, animated on entry)
- Print-inspired details (small caps, drop caps, indented paragraphs)
```

---

## 🚀 OUTILS RECOMMANDÉS POUR EXÉCUTER LE PROMPT

| Outil | Force | Idéal pour |
|-------|-------|------------|
| **V0 (Vercel)** | Génère React + Tailwind production-ready | Code direct, déployable |
| **Lovable** | App complète full-stack | MVP rapide |
| **Bolt.new** | Édition live, preview instant | Itération design |
| **Claude (claude.ai)** | Code propre, attention aux détails | Qualité du code |
| **Cursor IDE** | Édition intégrée, contexte projet | Développement long |
| **Figma AI / Galileo** | Design avant code | Mockups visuels |
| **Framer AI** | Site directement publié | No-code rapide |

**Recommandation pour Sano Sano :**
1. **Phase mockup** : Figma AI ou Framer (visuel)
2. **Phase code** : V0 (le meilleur pour ce style premium éditorial)
3. **Phase polish** : Cursor pour fine-tuner

---

## 📋 CHECKLIST AVANT D'ENVOYER LE PROMPT

- [ ] Tu as la vidéo `foster-farm-hero.mp4` prête à uploader
- [ ] Tu as un compte sur l'outil choisi (V0, Lovable, etc.)
- [ ] Tu as testé un mini-prompt d'abord pour valider la qualité de sortie
- [ ] Tu as un domaine prêt (si déploiement immédiat prévu)
- [ ] Tu as la palette PDF brand guidelines en référence

---

**Prompt Version:** 2.0 — Ultimate Edition  
**Combine:** M3 + Apple HIG + Vercel + Stripe + Linear  
**Optimisé pour:** V0, Lovable, Claude, Cursor, Figma AI  
**Date:** May 2026
