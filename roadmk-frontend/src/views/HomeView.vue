<template>
  <div>
    <!-- Hero -->
    <div class="hero">
      <div class="hero-content">
        <h1>СОСТОЈБА НА ПАТИШТА</h1>
        <p>Дневни информации за патната мрежа во Македонија</p>
        <router-link to="/roads" class="hero-btn">ПРЕГЛЕДАЈ ПАТИШТА</router-link>
      </div>
      <div class="hero-stats" v-if="summary">
        <div class="hero-stat red">
          <span class="n">{{ summary.red }}</span>
          <span class="l">ЗАТВОРЕНО</span>
        </div>
        <div class="hero-stat yellow">
          <span class="n">{{ summary.yellow }}</span>
          <span class="l">ПРЕДУПРЕДУВАЊЕ</span>
        </div>
        <div class="hero-stat green">
          <span class="n">{{ summary.green }}</span>
          <span class="l">НОРМАЛНО</span>
        </div>
      </div>
    </div>

    <!-- Latest reports -->
    <div class="section">
      <div class="section-inner">
        <div class="section-header">
          <h2>ПОСЛЕДНИ ИЗВЕШТАИ</h2>
          <router-link to="/roads" class="see-all">Сите извештаи →</router-link>
        </div>

        <div v-if="loading" class="loading">Се вчитува...</div>
        <div v-else class="cards-grid">
          <div
            v-for="report in latestReports"
            :key="report.id"
            :class="['card', report.severity.toLowerCase()]"
          >
            <div :class="['card-top', report.severity.toLowerCase()]">
              <span class="card-badge">{{ severityLabel(report.severity) }}</span>
            </div>
            <div class="card-body">
              <h3>{{ report.title }}</h3>
              <p>{{ report.description.slice(0, 120) }}...</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Services -->
    <div class="services-section">
      <div class="section-inner">
        <h2>НАШИ УСЛУГИ</h2>
        <div class="services-grid">
          <router-link to="/roads" class="service-card">
            <div class="service-icon">🛣️</div>
            <h3>СОСТОЈБА НА ПАТИШТА</h3>
            <p>Дневни информации за затворања, девијации и предупредувања</p>
          </router-link>
          <router-link to="/about" class="service-card">
            <div class="service-icon">🚗</div>
            <h3>ПОМОШ НА ПАТ</h3>
            <p>Итна помош на пат 24/7 на број 196</p>
          </router-link>
          <router-link to="/contact" class="service-card">
            <div class="service-icon">📞</div>
            <h3>КОНТАКТ</h3>
            <p>Поврзете се со нашиот тим за повеќе информации</p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { getReports, getSummary } from '../api/reports'

const reports = ref([])
const summary = ref(null)
const loading = ref(true)

const latestReports = computed(() => reports.value.slice(0, 3))

const severityLabel = (s) =>
  s === 'RED' ? 'ЗАТВОРЕНО' : s === 'YELLOW' ? 'ПРЕДУПРЕДУВАЊЕ' : 'НОРМАЛНО'

onMounted(async () => {
  const [r, s] = await Promise.all([getReports(), getSummary()])
  reports.value = r
  summary.value = s
  loading.value = false
})
</script>

<style scoped>
.hero {
  background: #111;
  padding: 64px 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.hero-content h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 48px;
  font-weight: 700;
  color: #F5C300;
  letter-spacing: 2px;
  margin-bottom: 12px;
}

.hero-content p {
  color: #aaa;
  font-size: 16px;
  margin-bottom: 28px;
}

.hero-btn {
  display: inline-block;
  background: #F5C300;
  color: #111;
  font-family: 'Oswald', sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 14px 32px;
  text-decoration: none;
  border-radius: 2px;
  transition: background 0.2s;
}

.hero-btn:hover { background: #e6b800; }

.hero-stats {
  display: flex;
  gap: 16px;
}

.hero-stat {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 24px 32px;
  text-align: center;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.hero-stat .n {
  font-family: 'Oswald', sans-serif;
  font-size: 48px;
  font-weight: 700;
  line-height: 1;
}

.hero-stat .l {
  font-size: 10px;
  letter-spacing: 2px;
  color: #888;
}

.hero-stat.red .n { color: #e74c3c; }
.hero-stat.yellow .n { color: #F5C300; }
.hero-stat.green .n { color: #2ecc71; }

.section { padding: 56px 0; }

.section-inner {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.section-header h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #111;
}

.see-all {
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  color: #888;
  text-decoration: none;
  letter-spacing: 1px;
  transition: color 0.2s;
}

.see-all:hover { color: #F5C300; }

.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.card {
  background: white;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}

.card-top {
  padding: 12px 16px;
}

.card-top.red { background: #c0392b; }
.card-top.yellow { background: #d4a017; }
.card-top.green { background: #27ae60; }

.card-badge {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 2px;
  color: white;
}

.card-body { padding: 16px; }

.card-body h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #111;
}

.card-body p { font-size: 13px; color: #666; line-height: 1.6; }

.services-section {
  background: #111;
  padding: 56px 0;
}

.services-section h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #F5C300;
  margin-bottom: 28px;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.service-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 4px;
  padding: 32px 24px;
  text-decoration: none;
  transition: background 0.2s, border-color 0.2s;
}

.service-card:hover {
  background: rgba(245,195,0,0.1);
  border-color: #F5C300;
}

.service-icon { font-size: 32px; margin-bottom: 16px; }

.service-card h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 15px;
  letter-spacing: 1px;
  color: #F5C300;
  margin-bottom: 8px;
}

.service-card p { font-size: 13px; color: #888; line-height: 1.6; }

.loading {
  text-align: center;
  padding: 40px;
  font-family: 'Oswald', sans-serif;
  font-size: 18px;
  color: #888;
}
</style>
