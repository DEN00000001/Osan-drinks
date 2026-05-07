import mempalace from './mempalace.config.js';

// Initialiser l'optimisation de mémoire
console.log('🧠 Initialisation de Mempalace pour l\'optimisation de mémoire...');

// Activer le monitoring de mémoire
mempalace.startMonitoring();

console.log('✅ Mempalace activé avec succès');
console.log('Configuration:');
console.log(`  - Cache: activé (max ${mempalace.config.cache.maxSize / 1024 / 1024}MB)`);
console.log(`  - Garbage Collection: activé`);
console.log(`  - Compression: activé (niveau ${mempalace.config.compression.level})`);

// Afficher l'utilisation actuelle de mémoire
const memUsage = process.memoryUsage();
console.log('\nÉtat de la mémoire:');
console.log(`  - RSS: ${(memUsage.rss / 1024 / 1024).toFixed(2)}MB`);
console.log(`  - Heap Total: ${(memUsage.heapTotal / 1024 / 1024).toFixed(2)}MB`);
console.log(`  - Heap Used: ${(memUsage.heapUsed / 1024 / 1024).toFixed(2)}MB`);

export default mempalace;
