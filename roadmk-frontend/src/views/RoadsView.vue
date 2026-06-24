<template>
  <div>
    <section class="page-hero">
      <div class="page-hero-inner">
        <p class="page-eyebrow">АМСМ — РЕАЛНО ВРЕМЕ</p>
        <h1>Состојба на патиштата</h1>
        <p>Дневни информации за состојбата на патната мрежа во Македонија</p>
      </div>
    </section>

    <div class="page-body">
      <!-- Summary Bar -->
      <div class="summary-bar" v-if="summary">
        <div class="sum-item red">
          <span class="sum-n">{{ summary.red }}</span>
          <span class="sum-l">ЗАТВОРЕНО</span>
        </div>
        <div class="sum-divider"></div>
        <div class="sum-item yellow">
          <span class="sum-n">{{ summary.yellow }}</span>
          <span class="sum-l">ПРЕДУПРЕДУВАЊЕ</span>
        </div>
        <div class="sum-divider"></div>
        <div class="sum-item green">
          <span class="sum-n">{{ summary.green }}</span>
          <span class="sum-l">НОРМАЛНО</span>
        </div>
        <div class="sum-divider"></div>
        <div class="sum-item total">
          <span class="sum-n">{{ summary.total }}</span>
          <span class="sum-l">ВКУПНО</span>
        </div>
        <div class="sum-divider"></div>
        <div class="sum-item active">
          <span class="sum-n">{{ summary.active }}</span>
          <span class="sum-l">АКТИВНИ</span>
        </div>
      </div>

      <div class="roads-layout">
        <!-- Sidebar -->
        <aside class="sidebar">
          <div class="sidebar-block">
            <h3 class="sidebar-title">СТАТУС</h3>
            <button
              v-for="f in severityFilters"
              :key="f.value"
              :class="['filter-btn', f.value, { active: activeFilter === f.value }]"
              @click="setFilter(f.value)"
            >
              <span class="filter-dot" :class="f.value"></span>
              {{ f.label }}
              <span class="filter-count" v-if="summary">{{ getCount(f.value) }}</span>
            </button>
          </div>

          <div class="sidebar-block">
            <h3 class="sidebar-title">КАТЕГОРИЈА</h3>
            <button
              v-for="c in categoryFilters"
              :key="c.value"
              :class="['cat-btn', { active: activeCategory === c.value }]"
              @click="setCategory(c.value)"
            >
              {{ c.label }}
            </button>
          </div>

          <div class="sidebar-emergency">
            <div class="em-num">196</div>
            <p>Помош на пат</p>
            <a href="tel:196" class="em-btn">ЈАВЕТЕ СЕ</a>
          </div>
        </aside>

        <!-- Reports -->
        <main class="reports-main">
          <div class="results-bar">
            <span v-if="!loading">{{ reports.length }} извештаи</span>
            <span v-else>Се вчитува...</span>
          </div>

          <div v-if="loading" class="loading-state">
            <div class="loader"></div>
            <p>Се вчитуваат патните информации...</p>
          </div>

          <div v-else-if="reports.length === 0" class="empty-state">
            <h3>Нема активни извештаи</h3>
            <p>Патиштата се во нормална состојба за избраните филтри.</p>
          </div>

          <div v-else class="report-list">
            <div
              v-for="report in reports"
              :key="report.id"
              :class="['report-item', report.severity.toLowerCase()]"
            >
              <div class="report-severity-stripe" :class="report.severity.toLowerCase()"></div>
              <div class="report-content">
                <div class="report-meta">
                  <span :class="['badge', report.severity.toLowerCase()]">
                    {{ severityLabel(report.severity) }}
                  </span>
                  <span class="report-cat">{{ categoryLabel(report.category) }}</span>
                  <span class="report-date" v-if="report.scraped_at">
                    {{ formatDate(report.scraped_at) }}
                  </span>
                </div>
                <h3 class="report-title">{{ report.title }}</h3>
                <p class="report-desc">{{ report.description }}</p>
                <div class="report-validity" v-if="report.valid_from || report.valid_to">
                  <span v-if="report.valid_from">Од: {{ report.valid_from }}</span>
                  <span v-if="report.valid_to">До: {{ report.valid_to }}</span>
                </div>
              </div>
            </div>
          </div>
        </main>
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
const activeCategory = ref('all')

const severityFilters = [
  { label: 'Сите', value: 'all' },
  { label: 'Затворено', value: 'red' },
  { label: 'Предупредување', value: 'yellow' },
  { label: 'Нормално', value: 'green' },
]

const categoryFilters = [
  { label: 'Сите категории', value: 'all' },
  { label: 'Сезонски режим', value: 'SEASONAL_TRAFFIC_REGIME' },
  { label: 'Делница', value: 'ROAD_SECTION' },
  { label: 'Предупредување', value: 'WARNING' },
  { label: 'Работи на пат', value: 'ROAD_WORKS' },
]

const getCount = (val) => {
  if (!summary.value) return ''
  if (val === 'all') return summary.value.total
  if (val === 'red') return summary.value.red
  if (val === 'yellow') return summary.value.yellow
  if (val === 'green') return summary.value.green
  return ''
}

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

const formatDate = (dt) => {
  if (!dt) return ''
  const d = new Date(dt)
  return d.toLocaleDateString('mk-MK', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}

const fetchReports = async () => {
  loading.value = true
  const params = {}
  if (activeFilter.value !== 'all') params.severity = activeFilter.value.toUpperCase()
  if (activeCategory.value !== 'all') params.category = activeCategory.value
  reports.value = await getReports(params)
  loading.value = false
}

const setFilter = async (value) => {
  activeFilter.value = value
  await fetchReports()
}

const setCategory = async (value) => {
  activeCategory.value = value
  await fetchReports()
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
  background: linear-gradient(135deg, var(--dark) 0%, var(--teal) 100%);
  padding: 56px 0 48px;
  border-bottom: 4px solid var(--yellow);
}

.page-hero-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
}

.page-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  letter-spacing: 3px;
  color: var(--yellow);
  margin-bottom: 10px;
  opacity: 0.9;
}

.page-hero h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 48px;
  font-weight: 700;
  color: white;
  letter-spacing: 1px;
  margin-bottom: 8px;
}

.page-hero p { color: #8fa3b1; font-size: 15px; }

/* SUMMARY BAR */
.summary-bar {
  background: white;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}

.sum-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 20px 32px;
}

.sum-divider { width: 1px; height: 40px; background: #e8ecf0; }

.sum-n {
  font-family: 'Oswald', sans-serif;
  font-size: 32px;
  font-weight: 700;
  line-height: 1;
}

.sum-item.red .sum-n { color: var(--red); }
.sum-item.yellow .sum-n { color: #d4a900; }
.sum-item.green .sum-n { color: var(--green); }
.sum-item.total .sum-n { color: var(--dark); }
.sum-item.active .sum-n { color: var(--teal); }

.sum-l { font-size: 10px; letter-spacing: 2px; color: var(--muted); font-weight: 700; }

/* LAYOUT */
.page-body { background: var(--gray); min-height: 60vh; }

.roads-layout {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 48px 64px;
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 32px;
  align-items: start;
}

/* SIDEBAR */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 24px;
  position: sticky;
  top: 90px;
}

.sidebar-block {
  background: white;
  padding: 24px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.sidebar-title {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  letter-spacing: 2.5px;
  color: var(--muted);
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid #e8ecf0;
}

.filter-btn, .cat-btn {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: none;
  border: 1px solid transparent;
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.5px;
  color: var(--text);
  cursor: pointer;
  text-align: left;
  transition: all 0.15s;
  border-radius: 2px;
  margin-bottom: 4px;
}

.filter-btn:hover, .cat-btn:hover {
  background: var(--gray);
  border-color: #ddd;
}

.filter-btn.active, .cat-btn.active {
  background: var(--dark);
  color: var(--yellow);
  border-color: var(--dark);
}

.filter-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.filter-dot.red { background: var(--red); }
.filter-dot.yellow { background: #d4a900; }
.filter-dot.green { background: var(--green); }
.filter-dot.all { background: linear-gradient(135deg, var(--red) 0%, var(--green) 100%); }

.filter-count {
  margin-left: auto;
  font-size: 12px;
  font-weight: 700;
  color: var(--muted);
  background: var(--gray);
  padding: 1px 7px;
  border-radius: 10px;
}

.filter-btn.active .filter-count {
  background: rgba(245,195,0,0.2);
  color: var(--yellow);
}

.sidebar-emergency {
  background: var(--dark);
  padding: 28px 24px;
  text-align: center;
}

.em-num {
  font-family: 'Oswald', sans-serif;
  font-size: 56px;
  font-weight: 700;
  color: var(--yellow);
  line-height: 1;
  margin-bottom: 4px;
}

.sidebar-emergency p {
  font-size: 12px;
  letter-spacing: 2px;
  color: #6a8394;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.em-btn {
  display: block;
  background: var(--yellow);
  color: #111;
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 10px;
  text-decoration: none;
  transition: background 0.2s;
}

.em-btn:hover { background: #ffd700; }

/* REPORTS */
.reports-main { min-width: 0; }

.results-bar {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 16px;
  padding: 8px 0;
}

.report-list { display: flex; flex-direction: column; gap: 12px; }

.report-item {
  background: white;
  display: flex;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  transition: transform 0.2s, box-shadow 0.2s;
}

.report-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.09);
}

.report-severity-stripe { width: 5px; flex-shrink: 0; }
.report-severity-stripe.red { background: var(--red); }
.report-severity-stripe.yellow { background: var(--yellow); }
.report-severity-stripe.green { background: var(--green); }

.report-content { padding: 20px 24px; flex: 1; }

.report-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}

.badge {
  font-family: 'Oswald', sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  padding: 3px 10px;
  color: white;
  border-radius: 2px;
}

.badge.red { background: var(--red); }
.badge.yellow { background: #d4a900; }
.badge.green { background: var(--green); }

.report-cat { font-size: 11px; letter-spacing: 1px; color: var(--muted); text-transform: uppercase; }

.report-date { font-size: 11px; color: #aaa; margin-left: auto; }

.report-title {
  font-family: 'Oswald', sans-serif;
  font-size: 20px;
  font-weight: 600;
  color: var(--dark);
  margin-bottom: 8px;
  line-height: 1.25;
}

.report-desc { font-size: 14px; color: var(--muted); line-height: 1.7; margin-bottom: 10px; }

.report-validity {
  display: flex;
  gap: 20px;
  font-size: 12px;
  color: #8fa3b1;
  padding-top: 10px;
  border-top: 1px solid #f0f2f5;
  font-weight: 600;
}

.empty-state, .loading-state {
  text-align: center;
  padding: 80px 20px;
  background: white;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.empty-state h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  color: var(--dark);
  margin-bottom: 8px;
}

.empty-state p, .loading-state p { font-size: 14px; color: var(--muted); }

.loader {
  width: 40px;
  height: 40px;
  border: 3px solid #e0e0e0;
  border-top-color: var(--yellow);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin { to { transform: rotate(360deg); } }
</style>
