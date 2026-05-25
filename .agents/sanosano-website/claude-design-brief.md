# BRIEF CLAUDE DESIGN — SANO SANO
# Prêt à coller directement dans Claude Design

---

## PROMPT PRINCIPAL

Crée le site web complet de **SANO SANO** en t'inspirant de la structure et du layout de https://larevoltosa.es — en remplaçant entièrement l'identité visuelle, les couleurs, les textes et les illustrations par ceux de SANO SANO définis ci-dessous.

---

## 1. IDENTITÉ DE LA MARQUE

**Nom :** SANO SANO
**Tagline :** *Zero compromis. 100% festif.*
**Headline principal :** *Célébrez. Sans une goutte.*
**URL :** sanosanodrinks.com
**Pays :** Belgique

**Ce que c'est :**
Boisson botanique pétillante, 00,00 % d'alcool absolu, jamais fermentée. Produite par dynamisation de plantes fraîches biologiques. Deux variétés : Bulles Blanches (Basilic × Gingembre) et Bulles Rosées (Thym × Fraise). Format 75 cl, bouchon liège + muselet. Prix : 9,90 €.

**Ce que ce n'est PAS :** Un vin sans alcool. Un soda. Un mocktail. Une alternative. Une imitation.

**Ton :** Festif sans excès. Élégant sans prétention. Confiant sans bruit. Gastronomique sans élitisme.

---

## 2. DESIGN SYSTEM

### Palette de couleurs

```
Fond global        : #FAF7F0  (crème chaud — jamais blanc pur)
Couleur principale : #1C3D2E  (vert feuille profond)
Couleur accent     : #2D6A4F  (basilic frais)
Or premium         : #C9A84C  (muselet, accents, labels)
Texte principal    : #1A1A1A  (encre botanique)
Texte secondaire   : #6B7C6E  (mousse)

Produit 1 — Bulles Blanches (Basilic × Gingembre)
  Background card  : #F2EDE4
  Gradient         : linear-gradient(135deg, #F2EDE4, #E8F5EE)
  Accent texte     : #2D5A3D

Produit 2 — Bulles Rosées (Thym × Fraise)
  Background card  : #F9E8EA
  Gradient         : linear-gradient(135deg, #F9E8EA, #E8D0D3)
  Accent texte     : #8B3A45

Hero background    : linear-gradient(180deg, #1C3D2E 0%, #2D6A4F 100%)
```

### Typographie

```
Titres (display, H1, H2) : Cormorant Garamond — weight 300 italic pour display, 400 pour H1/H2
Corps de texte           : DM Sans — weight 400 regular
Boutons & labels         : DM Sans — weight 600, letter-spacing 0.08em, uppercase
Specs techniques         : DM Mono — weight 400

Tailles :
  Display (hero)  : 80px desktop / 48px mobile — light italic
  H1              : 56px / 36px
  H2              : 40px / 28px
  H3              : 22px / 20px — DM Sans semibold
  Body large      : 18px
  Body            : 16px
  Caption/label   : 12px — DM Mono
```

### Composants

```
Boutons :
  Primaire   → bg #1C3D2E, texte #FAF7F0, border-radius 2px, padding 14px 32px, uppercase
  Secondaire → bg transparent, border 1.5px solid #1C3D2E, même shape
  Or/Gold    → bg #C9A84C, texte #1A1A1A

Cards produit :
  border-radius  : 12px
  border         : 1px solid rgba(28,61,46,0.08)
  box-shadow     : 0 2px 24px rgba(28,61,46,0.06)
  overflow       : hidden

Navigation :
  Logo à gauche
  5 items : Nos Bulles · Notre Histoire · Le Procédé · Acheter · Pro
  Style : minimaliste, sticky, transparent → #1C3D2E au scroll

Spacing :
  Section padding : 100px 0 desktop, 60px 0 mobile
  Container max   : 1280px, gutter 32px
  Base unit       : 8px
```

---

## 3. STRUCTURE DU SITE (9 SECTIONS)

### SECTION 1 — HERO (full-screen)
```
Background        : Gradient vert #1C3D2E → #2D6A4F
Visuel            : Photo ou animation — verre de SANO SANO avec bulles montantes,
                    lumière dorée, fond végétal flou
Headline          : "Célébrez. Sans une goutte."
                    (Cormorant Garamond, 80px, Light Italic, couleur #FAF7F0)
Sous-titre        : "SANO SANO, c'est la bulle botanique pour adultes — 00,00 % d'alcool,
                     jamais fermentée, dynamisée à partir de plantes fraîches."
                    (DM Sans, 18px, #FAF7F0 à 80% opacité)
CTA principal     : [ Découvrir nos bulles → ]  (bouton primaire crème)
CTA secondaire    : [ Voir le procédé ]         (bouton outline crème)
Scroll indicator  : flèche animée vers le bas
```

### SECTION 2 — LE CONSTAT (fond crème #FAF7F0)
```
Layout            : Texte centré, max-width 720px
H2                : "Trinquer, c'est un rituel. Pas une obligation de boire."
Body              : "À table, lors d'un toast, à l'apéro — la personne qui ne boit pas
                     se retrouve avec un jus d'orange ou un verre d'eau.
                     C'est inconfortable. C'est exclusif. C'est révolu.
                     SANO SANO existe pour celles et ceux qui veulent lever leur verre
                     comme tout le monde, sans rien y ajouter qu'ils n'auraient pas choisi."
```

### SECTION 3 — 4 PILIERS LIFESTYLE (fond #FAF7F0)
```
H2                : "Pour les moments qui comptent."
Layout            : 4 colonnes égales sur desktop, 2×2 sur mobile

Pilier 1 — L'apéritif
  Icône : 🥂
  Titre : "L'apéritif"
  Texte : "Trinquer sans subir."

Pilier 2 — Le repas
  Icône : 🍽️
  Titre : "Le repas"
  Texte : "La bulle qui s'accorde au plat."

Pilier 3 — L'inclusion
  Icône : 🌿
  Titre : "L'inclusion"
  Texte : "Pour ceux qui choisissent de ne pas boire."

Pilier 4 — La célébration
  Icône : 🎉
  Titre : "La célébration"
  Texte : "Lever son verre — sans exception."
```

### SECTION 4 — LES PRODUITS (fond #FAF7F0)
```
H2                : "Deux bulles. Deux mondes."
Layout            : 2 cards côte à côte, égales

CARD 1 — Bulles Blanches
  Background      : gradient #F2EDE4 → #E8F5EE
  Overline        : "BULLES BLANCHES" (DM Mono, uppercase, #2D5A3D)
  Titre           : "Basilic × Gingembre"  (Cormorant Garamond, 36px)
  Sous-titre      : "Frais, vibrant, tonique."  (italic)
  Texte           : "La verdeur du basilic en attaque, la chaleur du
                     gingembre en finale. Extra brut, élégant, parfaitement équilibré."
  Badges          : [ 00,00 % alcool ] [ Bio ] [ < 6 kcal ]
  Prix            : 9,90 €
  CTA             : [ Découvrir → ] (bouton vert #2D5A3D)
  Visuel          : Illustration botanique ligne fine — feuilles basilic + racine gingembre
                    OU photo macro bouteille avec condensation

CARD 2 — Bulles Rosées
  Background      : gradient #F9E8EA → #E8D0D3
  Overline        : "BULLES ROSÉES" (DM Mono, uppercase, #8B3A45)
  Titre           : "Thym × Fraise"  (Cormorant Garamond, 36px)
  Sous-titre      : "Surprenant, désaltérant, tout en nuances."  (italic)
  Texte           : "Le thym ouvre la dégustation. La fraise l'arrondit.
                     Une composition complexe, ronde, légèrement fruitée."
  Badges          : [ 00,00 % alcool ] [ Bio ] [ < 6 kcal ]
  Prix            : 9,90 €
  CTA             : [ Découvrir → ] (bouton rose #8B3A45)
  Visuel          : Illustration botanique — branche thym + fraises
                    OU photo macro bouteille rosée
```

### SECTION 5 — DIFFÉRENCIATION (fond vert sombre #1C3D2E)
```
H2                : "Une bulle pensée comme un grand effervescent.
                     Sauf qu'il n'y a rien dedans à regretter."
                    (Cormorant Garamond, blanc #FAF7F0)
Layout            : 4 colonnes sur fond vert

Colonne 1 — 🌿 100% botanique
  Titre : "100% botanique"
  Texte : "Plantes fraîches, biologiques, dynamisées à leur apogée. Aucun arôme ajouté."

Colonne 2 — 💧 00,00 % alcool
  Titre : "00,00 % alcool"
  Texte : "Pas 'presque'. Pas 'low'. Zéro absolu, vérifié."

Colonne 3 — 🔬 Jamais fermentée
  Titre : "Jamais fermentée"
  Texte : "Notre procédé exclusif extrait le goût sans fermentation."

Colonne 4 — ⚡ < 6 kcal
  Titre : "< 6 kcal / 100ml"
  Texte : "Indice glycémique bas. Léger comme une eau, complexe comme un grand vin."

Tous textes en #FAF7F0 / accents en or #C9A84C
```

### SECTION 6 — LE PROCÉDÉ (fond crème #FAF7F0, split 50/50)
```
Layout            : Gauche = texte, Droite = visuel illustration procédé

H2                : "La dynamisation, notre signature."
Body              : "Pas de fermentation. Pas d'arômes. Pas de raccourcis.
                     Nous sélectionnons des plantes fraîches à leur apogée.
                     Une infusion ultrasonique capte leur quintessence aromatique.
                     Une filtration délicate la préserve.
                     Le résultat : la pureté d'une plante qui vient d'être cueillie, mise en bulles."
CTA               : [ Voir comment c'est fait → ]

Visuel droite     : Schéma simplifié du procédé en 3 étapes
                    Étape 1 : Sélection des plantes (icône plante)
                    Étape 2 : Infusion ultrasonique (icône ondes)
                    Étape 3 : Filtration + mise en bulles (icône bulle)
```

### SECTION 7 — ORIGINE / SOCIAL PROOF (fond crème, large image)
```
Layout            : Image pleine largeur en background (Foster Farm)
                    Overlay sombre semi-transparent
                    Texte centré en blanc

H2                : "Né à Foster Farm.
                     Première Slow Food Farm de Belgique."
Body              : "Aux portes de Bruxelles, un écosystème agricole régénératif.
                     Eau de source. Énergie verte. Ingrédients 100% bio, tracés, certifiés."

Logos/badges (rangée horizontale) :
  [ Bio Garantie Belgique ] [ FR-BIO-01 ] [ Slow Food ] [ Halal en cours ]
```

### SECTION 8 — OÙ ACHETER (fond crème)
```
H2                : "SANO SANO près de chez toi."
Sous-titre        : "En ligne, en boutique, ou dans tes restaurants préférés."

Layout            : Map à gauche (60%) + Panel filtres à droite (40%)

Map               : Google Maps centrée sur Bruxelles, zoom 9
                    3 types de pins colorés :
                    🏪 Vert = En ligne
                    🍇 Or = Boutiques physiques
                    🍽️ Rose = Restaurants/HoReCa

Panel droite :
  Filtres (checkboxes) :
    ✅ En ligne
    ✅ Points de vente physiques
    ✅ Restaurants / HoReCa
  Champ recherche : "Votre code postal"
  Bouton          : [ Chercher à proximité ]
```

### SECTION 9 — CTA FINAL (fond vert #1C3D2E)
```
Layout            : Split 2 colonnes

Colonne gauche — Pour vous :
  H3              : "Célébrez autrement."
  Body            : "75 cl. Bouchon liège. Muselet. À partir de 9,90 €."
  CTA             : [ Commander en ligne → ]  (bouton or #C9A84C)
  CTA 2           : [ Pack découverte (2 bouteilles) — 18,90 € ]
  Badges          : "Livraison gratuite dès 50 € · Belgique"

Colonne droite — Pour votre établissement :
  H3              : "Pour les tables qui n'oublient personne."
  Body            : "Restaurants, hôtels, cavistes — ajoutez SANO SANO à votre carte.
                     Échantillon gratuit sur demande."
  CTA             : [ Demander un échantillon → ]  (bouton outline crème)
  Contact         : "Jérôme Goffinet — +32 475 95 46 33"

Couleurs textes : #FAF7F0 / accents : #C9A84C
```

### FOOTER
```
Background        : #1A1A1A (encre botanique)
Texte             : #FAF7F0

Colonne 1 — Logo + baseline
  Logo SANO SANO
  "Zero compromis. 100% festif."
  Instagram / LinkedIn

Colonne 2 — Nos bulles
  Basilic × Gingembre
  Thym × Fraise
  Pack Découverte
  SANO Club

Colonne 3 — La marque
  Notre Histoire
  Le Procédé
  Foster Farm
  Certifications

Colonne 4 — Contact
  hello@sanosanodrinks.com
  Jérôme Goffinet (Pro)
  +32 475 95 46 33
  ch. de Vieusart 35, 1300 Wavre

Bas du footer :
  © 2025 OSAN SRL · Belgique · Mentions légales · Politique de confidentialité
```

---

## 4. NAVIGATION

```
Logo : "SANO SANO" à gauche (Cormorant Garamond, or #C9A84C sur fond vert, encre sur fond crème)
Items : Nos Bulles · Notre Histoire · Le Procédé · Acheter · Pro
CTA nav : [ Commander ] (bouton or #C9A84C)
Comportement : Sticky · Transparent au top · Fond #1C3D2E au scroll
Mobile : Hamburger menu
```

---

## 5. ANIMATIONS

```
Hero      : Bulles qui montent lentement (CSS keyframes, opacity 0→1→0, translateY)
Sections  : Fade-in + translateY(24px) au scroll (Intersection Observer)
Boutons   : translateY(-1px) + box-shadow au hover (0.2s ease)
Cards     : Scale(1.02) au hover (0.3s ease)
Map pins  : Bounce léger à l'apparition
```

---

## 6. IMAGES REQUISES (placeholders)

```
hero-bg.jpg         : Verre SANO SANO — bulles montantes, lumière dorée, fond végétal
produit-blanc.jpg   : Bouteille Bulles Blanches — fond #F2EDE4 ou végétal vert
produit-rose.jpg    : Bouteille Bulles Rosées — fond #F9E8EA ou végétal rose
foster-farm.jpg     : Foster Farm, Wavre — paysage agricole, lumière naturelle
lifestyle-1.jpg     : Apéritif — mains tenant verres SANO SANO, terrasse
lifestyle-2.jpg     : Repas — verre servi à table gastronomique
lifestyle-3.jpg     : Célébration — groupe de personnes, verres levés (cadrage partiel)
procede.jpg         : Plantes fraîches en infusion / laboratoire artisanal
```

---

## 7. RESPONSIVE

```
Desktop  : ≥ 1024px — 2 cols produits, 4 cols piliers, map large
Tablette : 768–1023px — 2 cols produits, 2×2 piliers, map compacte
Mobile   : < 768px — 1 col tout, sections empilées, map plein écran
```

---

## 8. SEO META

```html
<title>SANO SANO — Bulles botaniques 00,00 % alcool · Bio · Belge</title>
<meta name="description"
  content="Célébrez sans une goutte. SANO SANO, la première bulle botanique dynamisée
  — 00,00 % alcool, bio, moins de 6 kcal. Basilic-Gingembre & Thym-Fraise.
  Made in Belgium. À partir de 9,90 €.">
<meta property="og:title" content="SANO SANO — Célébrez. Sans une goutte.">
<meta property="og:image" content="https://sanosanodrinks.com/og-image.jpg">
<meta name="theme-color" content="#1C3D2E">
```

---

## 9. STACK TECHNIQUE RECOMMANDÉE

```
Framework   : Next.js 14+ (App Router)
Styling     : Tailwind CSS + tokens custom
Composants  : shadcn/ui (customisé)
Map         : Google Maps JS API ou Mapbox GL JS
Animations  : Framer Motion ou CSS natif
Fonts       : Google Fonts (Cormorant Garamond + DM Sans + DM Mono)
Deploy      : Vercel
CMS         : Sanity.io (pour gérer les points de vente et le contenu)
```

---

## 10. FICHIERS DU PROJET (référence)

Tous les documents détaillés sont dans `.agents/sanosano-website/` :
- `copywriting.md`         → Tous les textes du site (8 pages)
- `design-system.md`       → Design system complet avec 4 options
- `larevoltosa-adaptation.md` → Mapping La Revoltosa → SanoSano
- `map-implementation.md`  → Guide technique pour la map
- `locations-data.json`    → Données points de vente (JSON)
