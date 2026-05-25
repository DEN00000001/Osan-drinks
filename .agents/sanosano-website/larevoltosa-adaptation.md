# La Revoltosa → SANO SANO
# Analyse & Adaptation du Design

---

## ✅ CE QUI FONCTIONNE — À CONSERVER

### Structure des sections
La Revoltosa a une architecture narrative parfaite pour une marque de boissons :
```
Hero (tagline + identité)
  ↓
4 piliers lifestyle (contextes d'usage)
  ↓
Produits (visuels + descriptions)
  ↓
CTA / Contact
  ↓
Footer
```
→ **Conserver exactement cette structure** pour SanoSano.

### Éléments UX à garder
- Navigation minimaliste (4-5 items max)
- Sections full-width modulaires
- Formulaire progressif multi-étapes (pour B2B HoReCa)
- Cards produits avec illustrations thématiques propres à chaque variété
- Intégration réseaux sociaux (Instagram)
- Tone familier & humain (pas corporate)

---

## 🔄 CE QUI DOIT CHANGER — Adaptations SanoSano

| Élément | La Revoltosa | SANO SANO |
|---------|-------------|-----------|
| **Couleur dominante** | Rouge vif / illustrations dragon | Vert botanique `#1C3D2E` |
| **Fond** | Blanc pur | Crème `#FAF7F0` |
| **Style illustrations** | Rétro-vintage, dragon, crocodile | Botanique contemporain, plantes en macro |
| **Ton** | Nostalgique "70 ans dans les mêmes verres" | Contemporain "Jamais fermentée, 00,00%" |
| **Produits** | Sifón / Limón / Cola (3) | Bulles Blanches / Bulles Rosées (2) |
| **Ambiance** | Convivial espagnol, chaleureux | Premium belge, festif conscient |
| **Couleur par produit** | Bleu / Jaune / Marron | Vert-blanc / Rose-blush |
| **Typography display** | Sans-serif moderne (approx.) | Cormorant Garamond (élégance botanique) |
| **Navigation labels** | Mis Bebidas, Mi Gente, Mi Vida | Nos Bulles, Notre Histoire, Acheter, Pro |

---

## 📐 MAPPING SECTION PAR SECTION

### SECTION 1 — HERO
**La Revoltosa :** "La burbuja Ibérica" + 70 años
**SANO SANO :**
```
Headline :  "Célébrez. Sans une goutte."
Sous-titre : Bulles botaniques 00,00 % alcool — jamais fermentées.
             Dynamisées à partir de plantes fraîches biologiques.
CTA :        [ Découvrir nos bulles → ]   [ Voir le procédé ]
Visuel :     Vidéo ou animation — bulles qui montent sur fond vert feuille
             OU photo lifestyle — verre servi sur terrasse, lumière dorée
```

---

### SECTION 2 — 4 PILIERS LIFESTYLE
**La Revoltosa :** sobremesas · picoteo · compañía · brindis

**SANO SANO — 4 moments SANO :**
```
🥂  L'apéritif               → "Trinquer sans subir."
🍽️  Le repas                 → "La bulle qui s'accorde au plat."
👩‍🤰 L'inclusion               → "Pour ceux qui choisissent de ne pas boire."
🎉  La célébration            → "Lever son verre — sans exception."
```
*Visuels : Lifestyle mains, verres, moments naturels — pas de mise en scène forcée*

---

### SECTION 3 — PRODUITS
**La Revoltosa :** 3 cartes (bleu Sifón / jaune Limón / marron Cola)

**SANO SANO — 2 cartes avec couleur signature :**

```
┌─────────────────────┐    ┌─────────────────────┐
│  BULLES BLANCHES    │    │  BULLES ROSÉES       │
│  Basilic×Gingembre  │    │  Thym×Fraise         │
│                     │    │                      │
│  Fond : #F2EDE4     │    │  Fond : #F9E8EA      │
│  Illustration :     │    │  Illustration :      │
│  Basilic en macro   │    │  Thym + fraises      │
│                     │    │                      │
│  Frais·Tonique·Sec  │    │  Floral·Rond·Vif     │
│  [ Découvrir ]      │    │  [ Découvrir ]       │
│  [ 9,90 € →  ]      │    │  [ 9,90 € →  ]       │
└─────────────────────┘    └─────────────────────┘
```

---

### SECTION 4 — DIFFÉRENCIATION (NOUVEAU — absent chez La Revoltosa)
*À insérer entre produits et CTA*
```
"Jamais fermentée. Jamais compromise."

3 colonnes :
00,00 % alcool    |   < 6 kcal/100ml   |   Jamais fermentée
absolu, vérifié   |   indice glycémique |   procédé exclusif
                  |   bas               |   dynamisation
```

---

### SECTION 5 — MAP "OÙ ACHETER" (NOUVEAU)
*Inspiré du layout contact La Revoltosa — section full-width*
```
"SANO SANO près de chez toi."

[ 🗺️ Map interactive Google Maps ]
[ Filtres : En ligne / Boutique / HoReCa ]
[ Recherche par code postal ]
```

---

### SECTION 6 — CTA / CONTACT
**La Revoltosa :** Formulaire progressif multi-étapes

**SANO SANO — Split en 2 parcours :**
```
┌──────────────────────┬──────────────────────┐
│   Pour vous          │   Pour votre table    │
│                      │                       │
│  Commandez en ligne  │  HoReCa / Cavistes    │
│  SANO Club           │  Demande d'échantillon│
│  [ Commander → ]     │  [ Nous contacter ]   │
└──────────────────────┴──────────────────────┘
```

---

## 🎨 PALETTE ADAPTÉE (tokens prêts à coder)

```css
:root {
  /* Reprise structure La Revoltosa — couleurs SanoSano */
  --color-bg:        #FAF7F0;   /* crème (remplace blanc pur) */
  --color-primary:   #1C3D2E;   /* vert feuille (remplace rouge) */
  --color-accent:    #2D6A4F;   /* basilic (remplace rouge clair) */
  --color-gold:      #C9A84C;   /* muselet or (accent premium) */

  /* Couleurs produits (comme La Revoltosa colore par saveur) */
  --color-blanc:     #F2EDE4;   /* Bulles Blanches bg */
  --color-rose:      #F9E8EA;   /* Bulles Rosées bg */
  --color-blanc-txt: #2D5A3D;   /* Texte sur card Blanches */
  --color-rose-txt:  #8B3A45;   /* Texte sur card Rosées */

  /* Textes */
  --color-text:      #1A1A1A;
  --color-muted:     #6B7C6E;

  /* Typographie (remplace font La Revoltosa) */
  --font-display:    'Cormorant Garamond', Georgia, serif;
  --font-body:       'DM Sans', sans-serif;

  /* Spacing (garder le rythme de La Revoltosa) */
  --section-padding: 100px 0;
  --container-max:   1280px;
  --gutter:          32px;
}
```

---

## 📝 NAVIGATION ADAPTÉE

| La Revoltosa | SANO SANO |
|-------------|-----------|
| Mis Bebidas | Nos Bulles |
| Mi Gente | Notre Histoire |
| Mi Vida | Le Procédé |
| Contacto | Acheter |
| *(pas de B2B visible)* | Pro / HoReCa |

---

## 🖼️ ILLUSTRATIONS — BRIEF

La Revoltosa utilise des illustrations SVG rétro (dragon, crocodile) qui donnent une personnalité forte.

**Pour SanoSano, 3 options :**

### Option 1 — Illustrations botaniques (recommandée)
Style herbier contemporain — plantes en line art fin, en couleur douce.
- Basilic (bulles blanches) : illustration feuilles de basilic + infusion
- Thym-Fraise (bulles rosées) : illustration thym fleuri + fraises

### Option 2 — Photographies macro
Photos très rapprochées des plantes dans l'eau, bulles, dynamisation.
→ Authentique, premium, pas d'illustration nécessaire.

### Option 3 — Abstraction végétale
Formes géométriques inspirées des plantes, style contemporain.
→ Moderne mais risque de perdre l'authenticité botanique.

---

## ⚡ ANIMATIONS À REPRENDRE + ADAPTER

| La Revoltosa | SANO SANO |
|-------------|-----------|
| Transitions douces entre sections | ✅ Garder |
| Formulaire progressif multi-étapes | ✅ Adapter pour B2B |
| Vidéo embeddée | ✅ Mini-doc dynamisation |
| Hover sur produits | ✅ Révèle profil aromatique |

**Animations propres à SanoSano :**
```js
// Bulles qui montent — signature animée
// Au scroll sur la section Hero
const bubbles = document.querySelectorAll('.bubble');
bubbles.forEach((b, i) => {
  b.style.animationDelay = `${i * 0.3}s`;
  b.classList.add('rising');
});
```

---

## 🚀 PLAN D'IMPLÉMENTATION

### Phase 1 — Cloner la structure (Semaine 1)
- [ ] Reproduire la structure HTML de La Revoltosa
- [ ] Remplacer les couleurs par les tokens SanoSano
- [ ] Intégrer les polices Cormorant + DM Sans
- [ ] Remplacer le contenu par le copywriting SanoSano

### Phase 2 — Adapter les sections (Semaine 2)
- [ ] Section 4 : Différenciation (nouvelle)
- [ ] Section 5 : Map interactive (voir map-implementation.md)
- [ ] Section 6 : Split CTA B2C / B2B
- [ ] Illustrations botaniques ou photos macro

### Phase 3 — Finitions (Semaine 3)
- [ ] Animation bulles
- [ ] Responsive mobile
- [ ] SEO meta (voir copywriting.md)
- [ ] Intégration analytics
- [ ] Tests performances (Lighthouse ≥ 90)

---

## ✅ VERDICT FINAL

**Oui, le design de La Revoltosa est une excellente base pour SanoSano.**

Ce qui les rapproche :
- Même secteur (boissons premium)
- Même approche narrative (lifestyle + produit)
- Même structure modulaire efficace
- Même priorité aux moments de vie (convivialité)

Ce qui les différencie :
- La Revoltosa = nostalgie espagnole, rouge, dragon
- SanoSano = botanique belge, vert profond, plantes vivantes

L'adaptation est **minimaliste côté structure, maximale côté identité**.
