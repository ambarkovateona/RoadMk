<template>
  <div class="page">
    <div class="page-hero">
      <h1>СОСТОЈБА НА ПАТИШТА</h1>
      <p>Дневни информации за состојбата на патната мрежа во Македонија</p>
    </div>

    <div class="page-content">
      <!-- Summary -->
      <div class="summary-banner" v-if="summary">
        <div class="summary-item red">
          <span class="count">{{ summary.red }}</span>
          <span class="label">ЗАТВОРЕНО</span>
        </div>
        <div class="summary-item yellow">
          <span class="count">{{ summary.yellow }}</span>
          <span class="label">ПРЕДУПРЕДУВАЊЕ</span>
        </div>
        <div class="summary-item green">
          <span class="count">{{ summary.green }}</span>
          <span class="label">НОРМАЛНО</span>
        </div>
        <div class="summary-item total">
          <span class="count">{{ summary.total }}</span>
          <span class="label">ВКУПНО</span>
        </div>
      </div>

      <!-- Filters -->
      <div class="filter-bar">
        <button
          v-for="f in filters"
          :key="f.value"
          :class="['filter-btn', f.value, { active: activeFilter === f.value }]"
          @click="setFilter(f.value)"
        >
          {{ f.label }}
        </button>
      </div>

      <!-- Reports -->
      <div v-if="loading" class="loading">Се вчитува...</div>
      <div v-else>
        <div
          v-for="report in reports"
          :key="report.id"
          :class="['report-card', report.severity.toLowerCase()]"
        >
          <div :class="['severity-bar', report.severity.toLowerCase()]"></div>
          <div class="card-body">
            <div class="card-meta">
              <span :class="['badge', report.severity.toLowerCase()]">
                {{ severityLabel(report.severity) }}
              </span>
              <span class="category">{{ categoryLabel(report.category) }}</span>
            </div>
            <h3 class="card-title">{{ report.title }}</h3>
            <p class="card-desc">{{ report.description }}</p>
            <div class="card-footer" v-if="report.valid_from || report.valid_to">
              <span v-if="report.valid_from">Од: {{ report.valid_from }}</span>
              <span v-if="report.valid_to">До: {{ report.valid_to }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getReports, getSummary } from '../api/reports'

const reports = ref([])
const summary = ref(null)
const loading = ref(true)
const activeFilter = ref('all')

const filters = [
  { label: 'СВЕ', value: 'all' },
  { label: 'ЗАТВОРЕНО', value: 'red' },
  { label: 'ПРЕДУПРЕДУВАЊЕ', value: 'yellow' },
  { label: 'НОРМАЛНО', value: 'green' },
]

const severityLabel = (s) =>
  s === 'RED' ? 'ЗАТВОРЕНО' : s === 'YELLOW' ? 'ПРЕДУПРЕДУВАЊЕ' : 'НОРМАЛНО'

const categoryLabel = (c) => {
  const map = {
    SEASONAL_TRAFFIC_REGIME: 'Сезонски режим',
    ROAD_SECTION: 'Делница',
    WARNING: 'Предупредување',
    ROAD_STATE: 'Состојба',
    TRAFFIC_FREQUENCY: 'Фреквенција',
    ROAD_WORKS: 'Работи на пат',
  }
  return map[c] || c
}

const setFilter = async (value) => {
  activeFilter.value = value
  loading.value = true
  const params = value !== 'all' ? { severity: value.toUpperCase() } : {}
  reports.value = await getReports(params)
  loading.value = false
}

onMounted(async () => {
  const [r, s] = await Promise.all([getReports(), getSummary()])
  reports.value = r
  summary.value = s
  loading.value = false
})
</script>

<style scoped>
.page-hero {
  background: #111;
  color: white;
  padding: 48px 40px;
  margin-bottom: 0;
}

.page-hero h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 36px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #F5C300;
}

.page-hero p {
  margin-top: 8px;
  color: #aaa;
  font-size: 15px;
}

.page-content {
  max-width: 960px;
  margin: 0 auto;
  padding: 32px 20px;
}

.summary-banner {
  display: flex;
  gap: 12px;
  margin-bottom: 28px;
}

.summary-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border-radius: 4px;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.summary-item .count {
  font-family: 'Oswald', sans-serif;
  font-size: 36px;
  font-weight: 700;
}

.summary-item .label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 6px;
  color: #555;
}

.summary-item.red .count { color: #c0392b; }
.summary-item.yellow .count { color: #d4a017; }
.summary-item.green .count { color: #27ae60; }
.summary-item.total .count { color: #111; }

.filter-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.filter-btn {
  padding: 10px 20px;
  border: 2px solid #ddd;
  background: white;
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.2s;
  border-radius: 2px;
}

.filter-btn.active.all { background: #111; color: white; border-color: #111; }
.filter-btn.active.red { background: #c0392b; color: white; border-color: #c0392b; }
.filter-btn.active.yellow { background: #d4a017; color: white; border-color: #d4a017; }
.filter-btn.active.green { background: #27ae60; color: white; border-color: #27ae60; }

.report-card {
  display: flex;
  background: white;
  border-radius: 4px;
  margin-bottom: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.report-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}

.severity-bar { width: 6px; }
.severity-bar.red { background: #c0392b; }
.severity-bar.yellow { background: #F5C300; }
.severity-bar.green { background: #27ae60; }

.card-body { padding: 16px 20px; flex: 1; }

.card-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.badge {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 2px;
  color: white;
}

.badge.red { background: #c0392b; }
.badge.yellow { background: #d4a017; }
.badge.green { background: #27ae60; }

.category { font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; }

.card-title {
  font-family: 'Oswald', sans-serif;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 6px;
}

.card-desc { font-size: 14px; color: #444; line-height: 1.6; }

.card-footer {
  display: flex;
  gap: 16px;
  margin-top: 10px;
  font-size: 12px;
  color: #888;
  font-weight: 600;
}

.loading {
  text-align: center;
  padding: 40px;
  font-family: 'Oswald', sans-serif;
  font-size: 18px;
  color: #888;
}
</style>
