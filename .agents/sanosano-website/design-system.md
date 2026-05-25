# Design System — SANO SANO
> *Basé sur le benchmark : Seedlip · Fever-Tree · Aesop · Ruinart · San Pellegrino*
> *Positionnement : Botanique · Festif · Premium · Belge · Contemporain*

---

## 🎨 4 OPTIONS DE DESIGN SYSTEM

---

### OPTION A — "BOTANICA VIVANTE" ⭐ RECOMMANDÉE

> *Aesop meets Seedlip modernisé. L'intelligence botanique, mise en fête.*

**Concept :** La plante comme matière première visuelle. Élégance terrestre, pas champagne. Le vert profond de l'herbier, illuminé par la bulle.

#### Palette

| Token | Nom | HEX | Usage |
|-------|-----|-----|-------|
| `--color-primary` | Feuille Profonde | `#1C3D2E` | Hero backgrounds, nav, footers |
| `--color-secondary` | Basilic Frais | `#2D6A4F` | Accents, boutons primaires |
| `--color-blush` | Thym-Fraise | `#E8B4B8` | Produit Rosé — backgrounds doux |
| `--color-blanc` | Bulles Blanches | `#F2EDE4` | Produit Blanc — off-white chaud |
| `--color-gold` | Muselet Or | `#C9A84C` | Accents premium, icônes, labels |
| `--color-cream` | Cire d'Acacia | `#FAF7F0` | Page background global |
| `--color-dark` | Encre Botanique | `#1A1A1A` | Corps de texte |
| `--color-muted` | Mousse | `#6B7C6E` | Textes secondaires, captions |

```css
/* Gradients produits */
--gradient-blanc: linear-gradient(135deg, #F2EDE4, #E8F5EE);
--gradient-rose: linear-gradient(135deg, #F9E8EA, #E8D0D3);
--gradient-hero: linear-gradient(180deg, #1C3D2E 0%, #2D6A4F 100%);
```

#### Typographie

```css
/* Headings : Cormorant Garamond — élégance, légèreté, gastronomie */
--font-display: 'Cormorant Garamond', Georgia, serif;

/* Body : DM Sans — contemporain, accessible, lisible */
--font-body: 'DM Sans', -apple-system, sans-serif;

/* Accents : DM Mono — labels, valeurs nutritionnelles, codes */
--font-mono: 'DM Mono', monospace;
```

**Hiérarchie typographique :**

| Niveau | Font | Size | Weight | Usage |
|--------|------|------|--------|-------|
| Display | Cormorant Garamond | 72–96px | 300 (Light Italic) | Hero headlines |
| H1 | Cormorant Garamond | 48–64px | 400 | Page titles |
| H2 | Cormorant Garamond | 36–48px | 400 | Section headers |
| H3 | DM Sans | 24–28px | 600 | Sous-titres, cards |
| Body L | DM Sans | 18px | 400 | Paragraphes larges |
| Body | DM Sans | 16px | 400 | Corps de texte |
| Caption | DM Mono | 12–13px | 400 | Labels, specs techniques |
| CTA | DM Sans | 15px | 600 | Boutons |

#### Spacing & Grid

```css
/* Base unit : 8px */
--space-1: 4px;   --space-2: 8px;   --space-3: 12px;
--space-4: 16px;  --space-6: 24px;  --space-8: 32px;
--space-12: 48px; --space-16: 64px; --space-24: 96px;

/* Border radius */
--radius-sm: 4px;   --radius-md: 8px;
--radius-lg: 16px;  --radius-pill: 9999px;

/* Grid : 12 colonnes, max-width 1280px, gutter 32px */
```

#### Composants clés

**Boutons :**
```css
/* Primaire */
.btn-primary {
  background: #1C3D2E;
  color: #FAF7F0;
  border-radius: 2px;          /* très peu arrondi = premium */
  padding: 14px 32px;
  font: 600 15px 'DM Sans';
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
/* Secondaire */
.btn-secondary {
  background: transparent;
  color: #1C3D2E;
  border: 1.5px solid #1C3D2E;
}
/* Gold accent */
.btn-gold {
  background: #C9A84C;
  color: #1A1A1A;
}
```

**Cards produits :**
```css
.product-card {
  background: var(--gradient-blanc) ou var(--gradient-rose);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(28, 61, 46, 0.08);
  box-shadow: 0 2px 24px rgba(28, 61, 46, 0.06);
}
```

**Mood visuel :**
- Photos lifestyle naturalistes — lumière dorée, plantes en macro
- Arrières-plans texturés (lin, béton poli, bois clair)
- Pas de fond blanc pur — toujours crème ou vert
- Bouteilles photographiées sur fond végétal ou avec condensation

---

### OPTION B — "FESTIVE ÉPURÉE"

> *San Pellegrino meets Champagne Deutz. L'effervescence avec classe.*

**Concept :** La bulle comme métaphore centrale. Légèreté, célébration, premiumness sans lourdeur. Utilise les deux couleurs produits directement.

#### Palette

| Token | HEX | Usage |
|-------|-----|-------|
| `--color-primary` | `#FFFFFF` | Backgrounds dominants |
| `--color-dark` | `#0D1F17` | Textes, headers |
| `--color-vert` | `#3A7D5E` | Couleur signature, navbar |
| `--color-rose` | `#D4818B` | Produit Thym-Fraise |
| `--color-bulle` | `#E8F4EE` | Fond blanc-vert très doux |
| `--color-gold` | `#B8963E` | Accents (muselet, labels) |
| `--color-muted` | `#8A9E94` | Textes secondaires |

**Typographie :** `Playfair Display` (display) + `Inter` (body)

**Mood visuel :**
- Beaucoup d'espace blanc
- Bulles en overlay photographique
- Pack-shots sur fond blanc
- Lignes fines, iconographie minimaliste

---

### OPTION C — "HERBIER BELGE"

> *Seedlip gravure meets artisanat belge. Authenticité du terroir.*

**Concept :** L'herbier botanique comme language visuel. Illustrations de plantes, textures papier, encre, estampe. Premium par l'authenticité, pas par le luxe.

#### Palette

| Token | HEX | Usage |
|-------|-----|-------|
| `--color-primary` | `#F5F0E8` | Background papier herbier |
| `--color-ink` | `#2C2416` | Encre botanique |
| `--color-vert` | `#4A7C59` | Plantes, accents |
| `--color-terre` | `#8B6914` | Ton naturel, chaud |
| `--color-rose` | `#C4887A` | Produit fruité |
| `--color-gold` | `#D4AA47` | Dorure, accents premium |

**Typographie :** `EB Garamond` (tout) — Renaissance, botanique, intemporel

**Mood visuel :**
- Illustrations botaniques détaillées (style herbier 18e siècle)
- Textures : papier, gravure, tampon
- Photography : film argentique, grain léger
- Packaging style "label de qualité" — filets, cadres fins

---

### OPTION D — "NUIT VÉGÉTALE"

> *Haut de gamme nocturne. La célébration, à l'heure de l'apéro.*

**Concept :** Le fond sombre met en valeur les couleurs vivantes des plantes. Luxe discret, sophistiqué, contemporain. Pour une image très premium et mystérieuse.

#### Palette

| Token | HEX | Usage |
|-------|-----|-------|
| `--color-bg` | `#0F1F15` | Background dark vert-noir |
| `--color-surface` | `#1A2F20` | Cards, modals |
| `--color-text` | `#F0EBE1` | Texte principal |
| `--color-vert` | `#5DBF86` | Accent vert vif |
| `--color-rose` | `#F0A0AB` | Accent rose vif |
| `--color-gold` | `#D4AA47` | Premium, highlights |
| `--color-muted` | `#7A9980` | Textes secondaires |

**Typographie :** `Libre Baskerville` (display) + `Outfit` (body)

**Mood visuel :**
- Sombre comme une cave ou un grand restaurant
- Bouteilles éclairées par en-dessous
- Effets de lumière sur les bulles
- Très impactant — risque d'être trop "bar à cocktails"

---

## ⭐ RECOMMANDATION FINALE

### Option A — "BOTANICA VIVANTE" pour SanoSano

**Pourquoi :**

| Critère | Option A | Option B | Option C | Option D |
|---------|----------|----------|----------|----------|
| Correspond au "festif sans excès" | ✅ ++ | ✅ + | ✅ + | ⚠️ trop bar |
| Premium sans élitisme | ✅ ++ | ✅ ++ | ✅ + | ✅ ++ |
| Botanique authentique | ✅ ++ | ✅ + | ✅ ++ | ⚠️ décoratif |
| Différenciation Seedlip | ✅ + | ✅ ++ | ❌ trop proche | ✅ ++ |
| Applicable web + packaging | ✅ ++ | ✅ ++ | ✅ + | ✅ + |
| Public 28–55 ans CSP+ | ✅ ++ | ✅ + | ✅ + | ✅ + |

---

## 🛠️ STACK TECHNIQUE RECOMMANDÉE

### shadcn/ui + Tailwind CSS + Next.js

**Pourquoi cette stack :**
- Composants entièrement personnalisables (tokens CSS natifs)
- 100% ownership du code — pas de dépendance à un éditeur
- Accessible WCAG 2.1 nativement (Radix primitives)
- Figma kit officiel disponible
- Standard DTC premium en 2026

**Configuration `tailwind.config.js` pour SanoSano :**

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Palette SANO SANO
        feuille:   '#1C3D2E',
        basilic:   '#2D6A4F',
        blush:     '#E8B4B8',
        bulles:    '#F2EDE4',
        muselet:   '#C9A84C',
        cream:     '#FAF7F0',
        encre:     '#1A1A1A',
        mousse:    '#6B7C6E',
      },
      fontFamily: {
        display: ['Cormorant Garamond', 'Georgia', 'serif'],
        body:    ['DM Sans', 'sans-serif'],
        mono:    ['DM Mono', 'monospace'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '120': '30rem',
      },
      borderRadius: {
        'xs': '2px',   // boutons premium
        'card': '12px',
      },
    },
  },
}
```

**Installation :**
```bash
npx create-next-app@latest sanosano --typescript --tailwind --app
cd sanosano
npx shadcn-ui@latest init
# Choisir: New York style, zinc base → override avec tokens Sano Sano
```

---

## 📐 COMPOSANTS PRIORITAIRES À CRÉER

### Phase 1 — Launch
- [ ] `<HeroSection>` — headline animé (bulles qui montent)
- [ ] `<ProductCard>` — blanc et rosé avec switch couleur
- [ ] `<NavBar>` — sticky, transparent → dark au scroll
- [ ] `<CTAButton>` — primaire, secondaire, gold
- [ ] `<ProofBadge>` — 00,00% / Bio / Jamais fermentée
- [ ] `<MapSection>` — intégration Google Maps (voir map-implementation.md)

### Phase 2 — Product pages
- [ ] `<TastingProfile>` — visualisation des 3 temps de dégustation
- [ ] `<IngredientCard>` — plante + description + provenance
- [ ] `<FoodPairing>` — liste d'accords avec icônes
- [ ] `<NutritionTable>` — valeurs nutritionnelles stylisées

### Phase 3 — Conversion
- [ ] `<CartDrawer>` — panier latéral
- [ ] `<SubscriptionToggle>` — unité vs abonnement SANO Club
- [ ] `<ReassuranceBand>` — livraison / paiement / retours
- [ ] `<ReviewCard>` — témoignages sommeliers/clients

---

## 🎯 ANIMATIONS & MICRO-INTERACTIONS

```css
/* Bulles qui montent — effet signature */
@keyframes bubble-rise {
  0%   { transform: translateY(100px) scale(0.8); opacity: 0; }
  50%  { opacity: 1; }
  100% { transform: translateY(-120px) scale(1.1); opacity: 0; }
}

/* Hover sur boutons — très subtil */
.btn-primary:hover {
  background: #2D6A4F;         /* léger éclaircissement */
  transform: translateY(-1px); /* micro-lift */
  box-shadow: 0 4px 16px rgba(28, 61, 46, 0.2);
  transition: all 0.2s ease;
}

/* Apparition des sections */
.section-reveal {
  animation: fadeInUp 0.6s ease-out forwards;
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## 📱 BREAKPOINTS RESPONSIFS

```css
/* Mobile-first */
sm:  640px   /* Petits mobiles */
md:  768px   /* Tablettes */
lg:  1024px  /* Desktop petit */
xl:  1280px  /* Desktop standard */
2xl: 1536px  /* Large desktop */
```

**Règle UX :** 60% du trafic botanique premium vient du mobile. Hero texte max 40px sur mobile. Map filtre : accordion sur mobile.

---

## 🖼️ SYSTÈME D'IMAGES

### Ratio canons
- Hero : 16:9 ou 3:2 (paysage)
- Produits : 3:4 ou 1:1 (portrait/carré)
- Team/farm : 4:3 (naturaliste)
- Lifestyle : 9:16 (vertical, mobile/stories)

### Style photographique (brief pour photographe)
```
Ambiance : Lumière naturelle dorée, heure dorée ou overcast doux
Fond : Jamais blanc pur. Crème, lin, ardoise, bois, pierre belge
Plantes : En macro, eau sur les feuilles, texture visible
Bouteilles : Avec condensation, sur fond végétal, muselet visible
Personnes : De côté ou de dos. Jamais sourire forcé. Geste naturel.
Interdit : Studio blanc, lumière froide, prise alimentaire typique
Couleurs : Saturation -10%, légère dominante chaude/verte selon produit
Format : RAW, minimum 4000x3000px
```

---

## 🔗 RESSOURCES

### Fonts (Google Fonts — gratuit)
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=DM+Sans:wght@400;500;600&family=DM+Mono&display=swap" rel="stylesheet">
```

### Design system reference
- **shadcn/ui** : https://ui.shadcn.com
- **Tailwind CSS** : https://tailwindcss.com
- **Radix UI** : https://radix-ui.com
- **Cormorant** : https://fonts.google.com/specimen/Cormorant+Garamond
- **DM Sans** : https://fonts.google.com/specimen/DM+Sans

### Outils Figma recommandés
- shadcn Figma kit officiel
- Unsplash (photos placeholder botaniques)
- Figma Variables pour les tokens CSS

---

## ✅ CHECKLIST DESIGN SYSTEM

### Fondations
- [ ] Définir les tokens dans Figma (couleurs, typo, spacing)
- [ ] Configurer Tailwind avec les tokens SanoSano
- [ ] Installer shadcn/ui et initialiser le thème
- [ ] Tester accessibilité contrastes (AA minimum sur tout texte)

### Composants
- [ ] Créer les 6 composants Phase 1
- [ ] Documenter chaque composant (props, variantes)
- [ ] Tester responsive (mobile + tablette + desktop)
- [ ] Valider avec le brand voice (cf. copywriting.md)

### Validation
- [ ] Test utilisateur (5 personnes dans la cible 28–55 CSP+)
- [ ] Lighthouse score ≥ 90 (Performance, Accessibility, SEO)
- [ ] Cross-browser (Chrome, Firefox, Safari, mobile iOS/Android)
