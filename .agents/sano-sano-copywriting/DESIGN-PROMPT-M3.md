# PROMPT — SANO SANO LANDING PAGE (Material Design 3)

> Copy-paste ce prompt complet dans ton outil de design (Figma AI, Claude, ChatGPT, Cursor, V0, Lovable, etc.)

---

## 🎯 PROMPT COMPLET

```
Design a premium, single-page landing site for "Sano Sano" — a Belgian non-alcoholic botanical beverage brand. Implement the design using Material Design 3 (M3) principles and tokens, adapted to fit the brand's premium, refined, non-AI-generated aesthetic.

═══════════════════════════════════════════════════════════
1. PROJECT CONTEXT
═══════════════════════════════════════════════════════════

Brand: Sano Sano
Tagline: "Zero compromis. 100% festif."
Type: Vitrine (showcase) website — NO e-commerce, NO ordering buttons
Audience: Premium restaurants, hotels, sommeliers, celebration venues
Origin: Foster Farm, Wallonia, Belgium (first Slow Food Farm in Belgium)
Language: French (primary)
Goal: Establish premium brand authenticity, generate B2B partnership inquiries

Brand Personality:
- Poetic but precise
- Confident without arrogance  
- Sensory-focused (tasting notes, sensations)
- Philosophical (why it exists, not just what)
- Botanical, natural, refined
- NEVER trendy, glassmorphic, or "AI-generated" feeling

═══════════════════════════════════════════════════════════
2. MATERIAL DESIGN 3 ADAPTATION
═══════════════════════════════════════════════════════════

Apply M3 token system with custom brand palette. Use M3 shape, elevation, motion, and typography systems — but customize tokens to match Sano Sano brand identity.

▸ M3 COLOR TOKENS (Custom Brand Mapping)

Source Color: #1a3a28 (Sano Green — generate full M3 tonal palette from this)

Custom Brand Palette:
- md.sys.color.primary           → #1a3a28 (Sano Green — natural, earth-tied)
- md.sys.color.on-primary        → #FFFFFF
- md.sys.color.primary-container → #D7E5DC (light green tint)
- md.sys.color.on-primary-container → #0A1F14

- md.sys.color.secondary           → #8B3A42 (Sano Rose — celebration, warmth)
- md.sys.color.on-secondary        → #FFFFFF
- md.sys.color.secondary-container → #F3DCDE
- md.sys.color.on-secondary-container → #2E0F12

- md.sys.color.tertiary            → #9D7C2B (Sano Gold — premium marker)
- md.sys.color.on-tertiary         → #FFFFFF
- md.sys.color.tertiary-container  → #F0E3C0
- md.sys.color.on-tertiary-container → #2A1F00

- md.sys.color.surface             → #F4F1EC (Cream — primary background)
- md.sys.color.on-surface          → #1A1A18 (Deep charcoal)
- md.sys.color.surface-variant     → #FFFFFF
- md.sys.color.on-surface-variant  → #4A4A42 (Muted text)
- md.sys.color.surface-container   → #FBFAF6
- md.sys.color.surface-container-high → #FFFFFF
- md.sys.color.outline             → rgba(26,26,24,0.12)
- md.sys.color.outline-variant     → rgba(26,26,24,0.08)

Color Philosophy:
- Dense, intentional use — colors carry meaning, not decoration
- Green = nature, trust, earth
- Rose = celebration, warmth, festivity  
- Gold = premium craftsmanship, luxury
- Cream = warm, elegant, sophisticated background
- AVOID gradients except subtle hero overlays for video readability

▸ M3 TYPOGRAPHY (Custom Font)

Replace Roboto with Satoshi (Google Fonts). Apply M3 type scale:

- md.sys.typescale.display-large   → Satoshi 900, clamp(3.6rem, 8.5vw, 7.8rem), line 0.95, tracking -0.02em
- md.sys.typescale.display-medium  → Satoshi 900, clamp(2.4rem, 6vw, 4rem), line 1.05, tracking -0.015em
- md.sys.typescale.display-small   → Satoshi 700, clamp(1.8rem, 4vw, 2.8rem), line 1.1, tracking -0.01em
- md.sys.typescale.headline-large  → Satoshi 700, 2rem, line 1.2
- md.sys.typescale.headline-medium → Satoshi 700, 1.5rem, line 1.25
- md.sys.typescale.headline-small  → Satoshi 700, 1.25rem, line 1.3
- md.sys.typescale.title-large     → Satoshi 600, 1.1rem, line 1.4
- md.sys.typescale.body-large      → Satoshi 400, 1.05rem, line 1.7
- md.sys.typescale.body-medium     → Satoshi 400, 0.95rem, line 1.6
- md.sys.typescale.label-large     → Satoshi 600, 0.85rem, tracking 0.08em, UPPERCASE
- md.sys.typescale.label-small     → Satoshi 600, 0.72rem, tracking 0.18em, UPPERCASE

▸ M3 SHAPE TOKENS

- md.sys.shape.corner.none       → 0
- md.sys.shape.corner.extra-small → 4px
- md.sys.shape.corner.small      → 8px
- md.sys.shape.corner.medium     → 12px
- md.sys.shape.corner.large      → 16px
- md.sys.shape.corner.extra-large → 24px
- md.sys.shape.corner.full       → 9999px (for pills/badges)

Cards: shape.large (16px)
Buttons: shape.full (pill shape, 100px)
Inputs: shape.small (8px)

▸ M3 ELEVATION

Use SPARINGLY. Premium feel = less shadow, more typography hierarchy.
- Level 0: Default (no shadow)
- Level 1: 0 1px 3px rgba(0,0,0,0.05) — subtle cards
- Level 2: 0 4px 12px rgba(0,0,0,0.06) — saveur cards
- Level 3: 0 8px 24px rgba(0,0,0,0.08) — hover states
- AVOID Level 4+ (too heavy for premium aesthetic)

▸ M3 MOTION

- md.sys.motion.duration.short2  → 100ms (micro-interactions)
- md.sys.motion.duration.medium2 → 300ms (transitions)
- md.sys.motion.duration.long2   → 500ms (reveals)
- md.sys.motion.duration.extra-long2 → 700ms (scroll reveals)
- md.sys.motion.easing.standard  → cubic-bezier(0.2, 0, 0, 1)
- md.sys.motion.easing.emphasized → cubic-bezier(0.2, 0, 0, 1)

═══════════════════════════════════════════════════════════
3. PAGE STRUCTURE & SECTIONS
═══════════════════════════════════════════════════════════

▸ MARQUEE TOPBAR (fixed top, z-index 101)
- Height: 32px
- Background: md.sys.color.primary (Green)
- Text: md.sys.color.on-primary (White), label-small
- Content scrolling horizontally, infinite loop:
  "0,00% Alcool · Bio Certifié FR-BIO-01 · < 6 kcal / 100 ml · Jamais fermentée · Slow Food Farm Belgique · Sans gluten · Sans sulfites · Procédé exclusif de dynamisation"
- Speed: 40 seconds full loop

▸ TOP APP BAR (Navigation) — M3 Center-Aligned variant
- Position: fixed, top: 32px (below marquee)
- Background: rgba(244, 241, 236, 0.95) with backdrop-filter blur(16px)
- Border-bottom: 1px solid md.sys.color.outline-variant
- Height: 72px
- Logo (left): "Sano Sano" — Satoshi 900, 1.2rem
- Navigation links (center, desktop): "Notre histoire · Nos saveurs · Le procédé"
  - md.sys.typescale.label-large
  - Hover: color shifts to primary
- Mobile: Hamburger icon (right), full-screen menu overlay

▸ HERO SECTION (full viewport, after navbar)
- Height: 100vh, min 600px
- Background: FULL-SCREEN VIDEO (Foster Farm footage, autoplay, muted, loop)
- Overlay: Linear gradient rgba(26,26,24,0.65) → rgba(0,0,0,0.4)
- Content: Centered, max-width 720px, padding 130px 24px 80px
- z-index hierarchy: video (0) → overlay (1) → content (2)

Content Stack (top to bottom):
1. Eyebrow label: "Boisson botanique belge premium"
   - md.sys.typescale.label-small
   - Color: rgba(255,255,255,0.8)
   - Precedes with horizontal line (28px, rgba(255,255,255,0.6))
   - Margin-bottom: 28px

2. H1 Display headline:
   "Zero compromis."
   "100% festif." (where "100%" is in md.sys.color.secondary — Rose — italic)
   - md.sys.typescale.display-large
   - Color: White
   - Text-shadow: 0 4px 20px rgba(0,0,0,0.5)
   - Margin-bottom: 28px

3. Badges row (M3 Chips, "assist" variant):
   [○ 0,00% Alcool] [✿ Bio Certifié FR-BIO-01] [◇ < 6 kcal / 100ml]
   - Background: rgba(255,255,255,0.12) with backdrop-blur
   - Border: 1px solid rgba(255,255,255,0.2)
   - Text: White
   - Padding: 8px 16px
   - Border-radius: full (pill)
   - Margin-bottom: 44px

4. CTA button (M3 Outlined variant):
   "Découvrir nos saveurs"
   - Border: 1.5px solid rgba(255,255,255,0.6)
   - Text: White
   - Background: transparent
   - Hover: background rgba(255,255,255,0.1)

5. Scroll indicator (bottom center, animated bounce)
   - White chevron-down, opacity 0.6
   - Animation: subtle 2s vertical bounce

═════════════════════

▸ SECTION 2 — POURQUOI (Why)
- Background: md.sys.color.surface (Cream)
- Padding: 100px 0
- Container: max-width 1200px, padding 0 24px

Content:
1. Eyebrow label: "Fondée sur un refus simple"
   - md.sys.typescale.label-small
   - Color: md.sys.color.tertiary (Gold)
   - Margin-bottom: 16px

2. Section title (H2):
   "Nous refusons les compromis."
   "Vous aussi, méritez mieux."
   - md.sys.typescale.display-small
   - Color: md.sys.color.on-surface
   - Margin-bottom: 64px

3. Philosophy Card (M3 Filled Card):
   - Background: md.sys.color.surface-container-high (White)
   - Border-radius: 20px
   - Padding: 56px
   - Margin-bottom: 64px
   - Elevation: Level 1
   - Content:
     "Pendant des années, les boissons sans alcool vous obligeaient à choisir : la santé *ou* le plaisir. Le goût réel *ou* la responsabilité."
     
     "Sano Sano arrive quand vous en avez assez de cette fausse dichotomie."
     
     [In italic, color: primary green]
     "Nous ne désalcoolisons rien. Nous ne diluons rien. Nous ne cachons rien derrière du sucre ou des arômes artificiels.
     Nous révélons simplement ce que chaque plante a à dire — et vous l'écoutez en bouteille."

4. Citation Block:
   - Background: md.sys.color.primary-container (light green tint)
   - Border-radius: 16px
   - Padding: 48px
   - Left border: 4px solid md.sys.color.primary
   - Quote text: Italic, body-large
   - Author: "— Thomas V., Chef sommelier · Bruxelles"
   - Margin-bottom: 64px
   - Content:
     "Une complexité aromatique que je n'aurais pas cru possible sans fermentation. L'attaque est nette, la longueur surprenante. Sano Sano redéfinit ce qu'un accord mets-boissons peut être pour les convives qui ne boivent pas d'alcool."

5. Certifications Band (M3 Chip row, horizontal scroll on mobile):
   [○ Alcohol-Free 0,00%] [✿ Bio FR-BIO-01] [◎ Gluten-Free] [◇ Sulphite-Free] [❧ Veggie Friendly] [◈ < 6 kcal]
   - Chip variant: M3 Filter Chips (unselected state)
   - Padding: 8px 16px
   - Gap between chips: 12px

═════════════════════

▸ SECTION 3 — NOS SAVEURS (Flavors)
- Background: md.sys.color.surface (Cream)
- Padding: 100px 0

Content:
1. Eyebrow label: "Deux caractères, une même âme"
2. Section title (H2):
   "Fermez les yeux."
   "Laissez les plantes parler."
   - md.sys.typescale.display-small

3. Saveurs Grid (2 columns desktop, 1 column mobile, gap 32px)

CARD 1 — BULLES BLANCHES (M3 Elevated Card):
   - Background: md.sys.color.surface-container-high (White)
   - Border-radius: 24px
   - Overflow: hidden
   - Elevation: Level 2
   - Hover: Elevation Level 3, translateY(-4px) (transition 300ms)
   
   Visual section (top, 280px height):
   - Background: linear-gradient(135deg, #F4F1EC 0%, #E8E5DD 100%)
   - Centered bottle illustration (CSS-drawn or SVG, white/cream tinted, with subtle shine)
   - Floating bubbles animation (4 small circles, varied opacity)
   
   Body section (padding: 40px 32px):
   - Badge (M3 Tonal): "Bulles Blanches"
     - Background: md.sys.color.primary-container
     - Text: md.sys.color.on-primary-container
     - Padding: 6px 14px, border-radius: full
   - Flavor name (H3): "Basilic · Gingembre"
     - md.sys.typescale.headline-medium
     - Color: md.sys.color.on-surface
     - Margin: 12px 0 8px
   - Subtitle: "Quand l'herbacée franc rencontre l'épice subtile"
     - md.sys.typescale.body-medium
     - Color: md.sys.color.on-surface-variant
     - Italic
     - Margin-bottom: 28px
   
   Tasting Notes (3 entries with labeled left column):
   ┌─────────┬────────────────────────────────┐
   │ Attaque │ La verdeur herbacée du basilic │
   │         │ s'impose avec franchise, vive  │
   │         │ et presque végétale — comme un │
   │         │ jardin en été après la pluie.  │
   ├─────────┼────────────────────────────────┤
   │ Corps   │ Le gingembre prend la relève   │
   │         │ avec une chaleur épicée et     │
   │         │ tonique, structurée, sans      │
   │         │ jamais dominer.                │
   ├─────────┼────────────────────────────────┤
   │ Finale  │ Longue, fraîche, équilibrée.   │
   │         │ Extra brute. Élégante comme    │
   │         │ une entrée réussie.            │
   └─────────┴────────────────────────────────┘
   - Labels: md.sys.typescale.label-large, color: primary (Green), uppercase
   - Text: md.sys.typescale.body-medium
   - Dividers: 1px solid md.sys.color.outline-variant between entries

   Ingredients block:
   "Ingrédients : Eau, basilic*, miel d'acacia*, gingembre*, acide ascorbique, acide citrique. *Biologique"
   - md.sys.typescale.body-medium
   - Color: md.sys.color.on-surface-variant
   - Background: md.sys.color.surface
   - Padding: 16px
   - Border-radius: 12px
   - Margin-top: 32px

CARD 2 — BULLES ROSÉES (same M3 Elevated Card structure):
   Visual section:
   - Background: linear-gradient(135deg, #FDE8EA 0%, #F0D0D4 100%)
   - Centered bottle illustration (rose-tinted)
   
   Badge: "Bulles Rosées" — uses secondary-container (rose tint)
   Flavor name: "Thym · Fraise"
   Subtitle: "L'inattendu qui ravit : sucré et herbacé en harmonie"
   
   Tasting Notes:
   - Attaque: "Une note herbacée de thym s'ouvre délicatement, aromatique, presque florale — inattendue et captivante."
   - Corps: "La fraise s'invite avec douceur et acidité maîtrisée, arrondissant l'herbe, créant une complexité rare."
   - Finale: "Désaltérante, nuancée, extra brute. Vous ne vous attendiez pas à ça — et c'est exactement ça."
   - Labels color: md.sys.color.secondary (Rose) instead of primary
   
   Ingredients: "Eau, fraise*, framboise*, miel d'acacia*, thym*, acide ascorbique, acide citrique. *Biologique"

═════════════════════

▸ SECTION 4 — LE PROCÉDÉ (Process)
- Background: md.sys.color.surface (Cream)
- Padding: 100px 0
- Layout: 2-column grid (text left, visual right), gap 80px, 1 column on mobile

Left column:
1. Eyebrow label: "La révélation, pas l'invention"
   - Color: md.sys.color.tertiary (Gold)
2. Section title (H2):
   "La dynamisation : quand la plante parle, nous l'écoutons."
   - md.sys.typescale.display-small
3. Body copy (5 paragraphs, md.sys.typescale.body-large):
   "Chaque plante a un moment précis — une seconde dans le temps — où elle exprime complètement sa nature. C'est comme un musicien qui trouve la note parfaite. Nous attendons ce moment exact."
   
   "À Foster Farm, une Slow Food Farm certifiée en Belgique, nous capturons les plantes à cet instant de grâce. Pas une seconde avant. Pas une seconde après."
   
   [In italic, color: primary Green]
   "Ce que vous ressentez en bouteille, c'est cette perfection figée dans le temps."
   
   "Par un procédé exclusif — jamais de chaleur, jamais d'alcool — nous libérons ce qu'il y a de plus vrai dans chaque tige, chaque feuille. Juste la plante, à son apogée, figée dans le temps."
   
   "Le résultat en bouteille : bulles fines, ultra-légères, moins de 6 kcal, une finale longue comme une conversation qui s'éternise sur votre table. Authentique."

Right column — Animated Dynamo Visual:
- Container: 480x480px, centered
- 3 concentric rings (SVG/CSS), rotating at different speeds
   - Outer ring: 480px, 1.5px solid rgba(26,58,40,0.2), rotates 60s
   - Middle ring: 360px, 1.5px solid rgba(26,58,40,0.3), rotates -45s
   - Inner ring: 240px, 1.5px solid rgba(26,58,40,0.4), rotates 30s
- Each ring has 1 small dot (8px, primary green) at top, creating rotation indicator
- Center: 120px circle, md.sys.color.primary-container background
  - Inside: ❧ icon (large) + label "Dynamisation"
  - md.sys.typescale.label-large

═════════════════════

▸ SECTION 5 — FOSTER FARM (Origins)
- Background: md.sys.color.primary-container (light green tint)
- Padding: 100px 24px
- Layout: 2-column grid (text left, visual right), gap 80px

Left column:
1. Eyebrow label: "Nos origines" — Color: md.sys.color.primary
2. Section title (H2):
   "Née à Foster Farm."
   "Portée par la terre belge."
   - md.sys.typescale.display-small
   - Color: md.sys.color.on-primary-container
3. Body copy:
   "Sano Sano prend racine à Foster Farm, la première Slow Food Farm de Belgique, nichée en Wallonie. Ici, l'agriculture régénérative n'est pas un argument marketing — c'est une philosophie de vie. Les sols sont nourris, l'eau respectée, chaque plante cultivée avec la même intention que celle qui finira dans votre verre."
   
   "Tous nos ingrédients sont bio certifiés. L'énergie consommée est renouvelable. Et l'eau qui entre dans chaque bouteille vient directement d'une source naturelle. Boire Sano Sano, c'est choisir un système alimentaire différent."

4. Icon Feature List (3 items, M3 List Items):
   💧 Eau de source — "Issue d'une source naturelle belge, non traitée chimiquement."
   ☀ Énergie 100% verte — "Toute la production fonctionne à l'énergie renouvelable."
   🌿 Agriculture régénérative — "Foster Farm, 1ère Slow Food Farm de Belgique. Les sols donnent plus qu'ils ne reçoivent."
   
   Each item:
   - Icon: 48px in circle, surface background
   - Title: md.sys.typescale.title-large, color: primary
   - Body: md.sys.typescale.body-medium

Right column — Botanical Art:
- Container: 480x480px
- SVG/CSS botanical illustration:
  - 4 hand-drawn leaves (varied sizes, organic positions)
  - 1 stylized flower with 5 petals (center)
  - Color palette: primary (green) and tertiary (gold)
  - Gentle floating animation on individual elements

═════════════════════

▸ SECTION 6 — CONTACT
- Background: md.sys.color.surface (Cream)
- Padding: 100px 0
- Content centered, max-width 600px

Content:
1. Eyebrow label: "Pour en savoir plus"
   - Color: md.sys.color.tertiary (Gold)
2. Section title (H2):
   "Nous aimerions vous rencontrer." 
   (where "rencontrer" is in md.sys.color.secondary — Rose — italic)
   - md.sys.typescale.display-small
3. Body copy:
   "Sano Sano est actuellement en développement auprès de partenaires premium : restaurants, hôtels, et lieux de célébration qui partagent nos valeurs."
   
   "Pour découvrir nos saveurs, des questions, ou des partenariats — contactez-nous directement."

4. Contact Methods (vertical stack, centered):
   [📧] jerome@osandrinks.com (M3 Text Button, primary color)
   [📞] +32 475 95 46 33 (M3 Text Button, primary color)
   📍 Wavre, Belgique (plain text, on-surface-variant)
   
   Buttons: Large M3 Text Button variant, 1rem font-size, 14px gap

═════════════════════

▸ FOOTER
- Background: md.sys.color.on-surface (Dark)
- Color: md.sys.color.surface (Cream)
- Padding: 48px 24px
- Content centered

1. Sano Sano logo wordmark (Satoshi 900)
2. Brand statement: "Botanical Bubbles · Zero Compromise. Full Celebration."
   - md.sys.typescale.body-medium
   - Opacity: 0.7
3. Bottom row (split):
   Left: "OSAN SRL © 2025"
   Right links: "Mentions légales · Confidentialité · Contact"
   - md.sys.typescale.label-large
4. Divider: 1px rgba(244,241,236,0.1)

═══════════════════════════════════════════════════════════
4. INTERACTIONS & MOTION (M3 Motion System)
═══════════════════════════════════════════════════════════

▸ Scroll Reveal Animations
- Trigger: Element enters viewport (IntersectionObserver, threshold 0.15)
- Effect: opacity 0→1 + translateY(32px→0)
- Duration: 700ms (md.sys.motion.duration.extra-long2)
- Easing: cubic-bezier(0.2, 0, 0, 1) (md.sys.motion.easing.emphasized)
- Stagger children: 100ms delay per element

▸ Button States
- Default → Hover: 100ms, bg/color transition + translateY(-1px)
- Hover → Pressed: 80ms, scale(0.97)
- M3 State Layer: 8% opacity overlay on hover, 12% on pressed

▸ Card Hover
- Elevation: Level 2 → Level 3
- transform: translateY(-4px)
- Duration: 300ms emphasized easing

▸ Video Hero
- Autoplay, muted, loop, playsinline
- object-fit: cover
- Fade-in on load: opacity 0→1, duration 1000ms

▸ Marquee Loop
- Animation: translateX(0% → -50%) infinite
- Duration: 40s linear

▸ Dynamo Animation
- Each ring rotates independently
- Outer: 60s clockwise
- Middle: 45s counter-clockwise  
- Inner: 30s clockwise
- All infinite, linear easing

═══════════════════════════════════════════════════════════
5. RESPONSIVE BREAKPOINTS
═══════════════════════════════════════════════════════════

- Mobile:    < 600px  (M3 compact window class)
- Tablet:    600-839px (M3 medium window class)
- Desktop:   840-1199px (M3 expanded window class)
- Wide:      1200px+ (M3 large window class)

Mobile Adjustments:
- Hero: maintain 100vh, smaller display headline
- Saveurs grid: 2 cols → 1 col
- Procédé layout: 2 cols → 1 col, visual goes above
- Foster Farm layout: 2 cols → 1 col
- Navigation: switch to M3 Navigation Drawer (hamburger trigger)
- Padding: 100px → 72px on sections
- Cards: padding 56px → 32px

═══════════════════════════════════════════════════════════
6. ACCESSIBILITY (M3 Standards)
═══════════════════════════════════════════════════════════

- Color contrast: WCAG AA minimum (4.5:1 body, 3:1 large text)
- Touch targets: minimum 48x48px
- Focus indicators: 2px outline, primary color, 2px offset
- Semantic HTML: header, nav, main, section, article, footer
- ARIA labels on all interactive elements
- Skip-to-content link (visually hidden, visible on focus)
- Reduced motion: respect prefers-reduced-motion media query
- Video: muted by default, captions if voice present
- All images: descriptive alt attributes

═══════════════════════════════════════════════════════════
7. WHAT TO AVOID
═══════════════════════════════════════════════════════════

❌ Trendy effects: glassmorphism, neumorphism, heavy gradients
❌ AI-generated stock imagery or generic Unsplash photos
❌ E-commerce elements: "Add to cart", "Buy now", price displays
❌ Excessive shadows or heavy elevation
❌ Inconsistent border-radius across components
❌ Off-brand colors (anything outside the defined palette)
❌ Roboto, Inter, or other generic sans-serifs (Satoshi only)
❌ Emojis as decoration (only as functional icons in foster icons section)
❌ Empty/orphan sections without strong purpose
❌ Fake testimonials or made-up data (only real assets)

═══════════════════════════════════════════════════════════
8. DELIVERABLES
═══════════════════════════════════════════════════════════

Generate:
1. Complete responsive single-page landing in HTML + CSS + JS
2. M3 design tokens defined as CSS custom properties
3. All sections fully functional with content
4. Scroll-triggered reveal animations
5. Hover/focus states for all interactive elements
6. Mobile menu with navigation drawer
7. Foster Farm video background (use placeholder URL: ./images/foster-farm-hero.mp4)
8. All copy in French exactly as specified

Tech stack: Pure HTML/CSS/JS (no framework needed). Use Google Fonts CDN for Satoshi. Optimize for performance: lazy-load video, defer non-critical JS.

═══════════════════════════════════════════════════════════
END OF PROMPT
═══════════════════════════════════════════════════════════
```

---

## 🚀 COMMENT UTILISER CE PROMPT

### Pour Figma (avec plugins AI)
1. Ouvrir Figma → Plugins → AI design tool (e.g., Anima, Galileo AI)
2. Coller le prompt complet
3. Spécifier "Material Design 3 with custom brand tokens"

### Pour V0 (Vercel)
1. https://v0.dev → New project
2. Coller le prompt
3. V0 génère React + Tailwind avec M3 principles

### Pour Lovable / Bolt
1. New project → Paste prompt
2. Spécifier "Vanilla HTML/CSS/JS" si vous voulez le code direct

### Pour Cursor / Claude / ChatGPT
1. Coller le prompt entier
2. Demander : "Génère le HTML/CSS complet en respectant strictement ce brief"
3. Itérer section par section si besoin

### Pour designer humain en Figma
1. Créer un fichier Figma avec une bibliothèque M3 (template officiel)
2. Customiser les tokens selon section 2 du prompt
3. Suivre la structure section par section

---

## 📦 FICHIERS À FOURNIR AVEC LE PROMPT

- `landing-page-v3.html` (référence structure actuelle)
- `foster-farm-hero.mp4` (vidéo asset hero)
- `brand-guidelines.md` (specs PDF originales)
- `DESIGN-BRIEF.md` (contexte business)

---

**Prompt Version:** 1.0  
**Date:** May 2026  
**Design System:** Material Design 3 (custom-tokened)  
**Brand:** Sano Sano — Botanical Bubbles
