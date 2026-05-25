# Implementation Guide — Map Interactive "Où acheter"

## 📍 Spécifications Techniques

### Option 1 : Google Maps (recommandée)
**Avantages :**
- API gratuite jusqu'à 25 000 requêtes/jour
- Bien connue, simple à intégrer
- Permet filtrage, recherche par code postal, reviews
- Mobile-friendly par défaut

**Setup :**
1. Créer un Google Cloud Project
2. Activer Google Maps JavaScript API
3. Créer une API key restreinte (domaines autorisés)
4. Intégrer le code

**Code de base :**
```html
<div id="map" style="width: 100%; height: 500px;"></div>

<script>
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    center: { lat: 50.5038, lng: 4.4699 } // Bruxelles
  });

  // Points de vente (à remplir)
  const locations = [
    { 
      name: "SANO SANO Shop Online", 
      lat: 50.5038, 
      lng: 4.4699,
      type: "online",
      address: "sanosanodrinks.com",
      phone: "Livraison Belgique"
    },
    {
      name: "La Caviste du Coin",
      lat: 50.4501,
      lng: 4.4699,
      type: "boutique",
      address: "123 Rue de Namur, Bruxelles",
      phone: "+32 2 XXX XXXX"
    },
    // ... autres points
  ];

  // Créer des markers avec filtrage par type
  locations.forEach(location => {
    const icon = getIcon(location.type); // Icône selon type
    const marker = new google.maps.Marker({
      position: { lat: location.lat, lng: location.lng },
      map: map,
      title: location.name,
      icon: icon
    });

    // Infowindow au clic
    marker.addListener("click", () => {
      const infowindow = new google.maps.InfoWindow({
        content: `<div>
          <h3>${location.name}</h3>
          <p>${location.address}</p>
          <p>${location.phone}</p>
        </div>`
      });
      infowindow.open(map, marker);
    });
  });
}

// Icônes par type
function getIcon(type) {
  const icons = {
    online: "🏪",
    boutique: "🍇",
    horeca: "🍽️"
  };
  return icons[type] || "📍";
}

window.initMap = initMap;
</script>
<script async defer 
  src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
</script>
```

---

### Option 2 : Mapbox (alternative moderne)
**Avantages :**
- Design plus moderne et customisable
- Gratuit jusqu'à 50 000 loads/mois
- Excellent support filtre + recherche
- Lighter than Google Maps

**Setup :** https://docs.mapbox.com/mapbox-gl-js/

---

## 🎯 Données à Collecter

**Pour chaque point de vente :**
- Nom
- Type (en ligne / boutique / HoReCa)
- Adresse complète
- Latitude / Longitude
- Téléphone / Email
- Horaires (optionnel)
- Photo (optionnel)
- URL site web (optionnel)

**Format JSON recommandé :**
```json
{
  "locations": [
    {
      "id": "sanosano-online",
      "name": "SANO SANO Shop",
      "type": "online",
      "address": "sanosanodrinks.com",
      "phone": "hello@sanosanodrinks.com",
      "lat": 50.5038,
      "lng": 4.4699,
      "url": "https://sanosanodrinks.com",
      "hours": "Livraison 24/24"
    },
    {
      "id": "caviste-bruxelles-01",
      "name": "La Caviste du Coin",
      "type": "boutique",
      "address": "123 Rue de Namur, 1000 Bruxelles",
      "phone": "+32 2 512 34 56",
      "lat": 50.4501,
      "lng": 4.4699,
      "url": "https://caviste-coin.be",
      "hours": "Lun-Sam 10h-19h"
    }
  ]
}
```

---

## 🔧 Filtres (Checkboxes)

**HTML :**
```html
<div class="filter-controls">
  <label>
    <input type="checkbox" value="online" checked> 🏪 En ligne
  </label>
  <label>
    <input type="checkbox" value="boutique" checked> 🍇 Boutique
  </label>
  <label>
    <input type="checkbox" value="horeca" checked> 🍽️ HoReCa
  </label>
</div>
```

**JavaScript :**
```javascript
const filters = document.querySelectorAll('.filter-controls input[type="checkbox"]');
filters.forEach(filter => {
  filter.addEventListener('change', () => {
    const selected = Array.from(filters)
      .filter(f => f.checked)
      .map(f => f.value);
    
    // Afficher/cacher markers selon sélection
    markers.forEach(marker => {
      marker.setVisible(selected.includes(marker.type));
    });
  });
});
```

---

## 🔍 Recherche par Code Postal

**HTML :**
```html
<div class="search-box">
  <input type="text" id="zipcode" placeholder="Entrez votre code postal" maxlength="4">
  <button onclick="searchByZipcode()">Chercher à proximité</button>
</div>
```

**JavaScript :**
```javascript
function searchByZipcode() {
  const zipcode = document.getElementById('zipcode').value;
  
  // Utiliser Google Geocoding API
  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({ address: zipcode + ", Belgium" }, (results, status) => {
    if (status === "OK") {
      const location = results[0].geometry.location;
      map.setCenter(location);
      map.setZoom(12); // Zoom sur la région
      
      // Trier les points de vente par proximité
      sortLocationsByDistance(location);
    }
  });
}

function sortLocationsByDistance(userLocation) {
  const sorted = locations.sort((a, b) => {
    const distA = google.maps.geometry.spherical.computeDistanceBetween(
      userLocation,
      new google.maps.LatLng(a.lat, a.lng)
    );
    const distB = google.maps.geometry.spherical.computeDistanceBetween(
      userLocation,
      new google.maps.LatLng(b.lat, b.lng)
    );
    return distA - distB;
  });
  
  // Afficher les points triés dans une liste à côté de la map
  displaySortedList(sorted);
}
```

---

## 📱 Responsive Design

**CSS :**
```css
#map-container {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 20px;
  min-height: 600px;
}

#map {
  width: 100%;
  height: 100%;
  border-radius: 8px;
}

.locations-list {
  overflow-y: auto;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 10px;
}

/* Mobile */
@media (max-width: 768px) {
  #map-container {
    grid-template-columns: 1fr;
  }
  
  .locations-list {
    max-height: 200px;
  }
}
```

---

## 🎨 Styling & UX

### Icônes / Markers
- 🏪 Bleu pour "En ligne"
- 🍇 Vert pour "Boutique"
- 🍽️ Orange pour "HoReCa"

### Infowindow au survol/clic
```
╔════════════════════╗
║ La Caviste du Coin ║
╠════════════════════╣
║ 123 Rue de Namur   ║
║ 1000 Bruxelles     ║
║                    ║
║ ☎ +32 2 512 34 56  ║
║ 🌐 Voir le site    ║
║ 📍 Itinéraire      ║
╚════════════════════╝
```

---

## 📊 Analytics & Tracking

Tracker les clics sur la map :
```javascript
ga('send', 'event', 'map', 'location-click', location.name);
```

---

## 🔐 Sécurité

- **API Key :** Restreindre à domaines autorisés + IP spécifiques
- **Rate limiting :** Google Maps gère automatiquement
- **HTTPS obligatoire** pour Google Maps

---

## 📋 Checklist d'implémentation

- [ ] Créer Google Cloud Project & API key
- [ ] Collecter adresses tous les points de vente
- [ ] Convertir adresses en lat/lng (Geocoding)
- [ ] Implémenter map de base
- [ ] Ajouter les 3 types de markers (icônes)
- [ ] Intégrer filtres (checkboxes)
- [ ] Intégrer recherche par code postal
- [ ] Styling responsive (desktop + mobile)
- [ ] Tester sur tous navigateurs/devices
- [ ] Intégrer avec Google Analytics
- [ ] Mettre en ligne

---

## 📝 Notes

**Données à mettre à jour :**
Prévoir un flux de mises à jour régulier pour les points de vente (ou CMS si possible).

**Localisations futures :**
Prévoir le design pour expansion en France, Pays-Bas, Luxembourg (une fois prêt).

**A/B Testing :**
Tester position de la map (avant/après CTA) et les label des CTAs (cf. content skill pour AB test).
