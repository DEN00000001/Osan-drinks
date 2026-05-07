import Mempalace from 'mempalace';

// Configuration d'optimisation de mémoire pour Osan Drinks
const mempalaceConfig = {
  // Activer le cache en mémoire
  cache: {
    enabled: true,
    maxSize: 100 * 1024 * 1024, // 100MB max
    ttl: 3600000 // 1 heure
  },

  // Optimisation de mémoire
  memory: {
    enableGarbageCollection: true,
    checkInterval: 30000, // Vérifier toutes les 30 secondes
    maxMemoryUsage: 500 * 1024 * 1024 // 500MB max
  },

  // Compression des données
  compression: {
    enabled: true,
    level: 6 // Niveau de compression (1-9)
  },

  // Indexation pour performance
  indexing: {
    enabled: true,
    autoIndex: true
  }
};

// Initialiser Mempalace
const mempalace = new Mempalace(mempalaceConfig);

export default mempalace;
