<template>
  <div>
    <!-- HERO -->
    <section class="hero">
      <div class="hero-content">
        <p class="hero-eyebrow">АМСМ — АВТО-МОТО СОЈУЗ НА МАКЕДОНИЈА</p>
        <h1 class="hero-title">Состојба<br>на патиштата</h1>
        <p class="hero-sub">Дневни информации за патната мрежа во Република Македонија. Ажурирано на секои 30 минути.</p>
        <router-link to="/roads" class="hero-btn">ПРЕГЛЕДАЈ ПАТИШТА</router-link>
      </div>
      <div class="hero-stats" v-if="summary">
        <div class="hstat red">
          <span class="hstat-n">{{ summary.red }}</span>
          <span class="hstat-l">ЗАТВОРЕНО</span>
        </div>
        <div class="hstat yellow">
          <span class="hstat-n">{{ summary.yellow }}</span>
          <span class="hstat-l">ПРЕДУПРЕДУВАЊЕ</span>
        </div>
        <div class="hstat green">
          <span class="hstat-n">{{ summary.green }}</span>
          <span class="hstat-l">НОРМАЛНО</span>
        </div>
        <div class="hstat total">
          <span class="hstat-n">{{ summary.total }}</span>
          <span class="hstat-l">ВКУПНО</span>
        </div>
      </div>
    </section>

    <!-- SERVICES ICON ROW -->
    <section class="services-row">
      <div class="services-inner">
        <router-link to="/roads" class="svc">
          <div class="svc-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 12h18M3 6l9-3 9 3M3 18l9 3 9-3"/></svg>
          </div>
          <span>Состојба на патишта</span>
        </router-link>
        <router-link to="/roads" class="svc">
          <div class="svc-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          </div>
          <span>Предупредувања</span>
        </router-link>
        <router-link to="/roads" class="svc">
          <div class="svc-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg>
          </div>
          <span>Работи на пат</span>
        </router-link>
        <router-link to="/roads" class="svc">
          <div class="svc-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <span>Сезонски режим</span>
        </router-link>
        <router-link to="/about" class="svc">
          <div class="svc-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.0 1.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92v2z"/></svg>
          </div>
          <span>Помош на пат 196</span>
        </router-link>
        <router-link to="/contact" class="svc">
          <div class="svc-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          </div>
          <span>Контакт</span>
        </router-link>
      </div>
      <div class="services-cta">
        <span>Преземи итна помош на пат низ целата држава</span>
        <router-link to="/contact" class="cta-btn">ПОВИК 196</router-link>
      </div>
    </section>

    <!-- INTRO SECTION -->
    <section class="intro-section">
      <div class="intro-inner">
        <div class="intro-visual">
          <div class="intro-card dark">
            <span class="intro-big-num" v-if="summary">{{ summary.total }}</span>
            <span class="intro-big-num" v-else>—</span>
            <span class="intro-big-label">АКТИВНИ ИЗВЕШТАИ</span>
          </div>
          <div class="intro-card yellow">
            <span class="intro-big-num">30</span>
            <span class="intro-big-label">МИН. ОСВЕЖУВАЊЕ</span>
          </div>
        </div>
        <div class="intro-text">
          <p class="intro-eyebrow">ЗА ПЛАТФОРМАТА</p>
          <h2 class="intro-heading">Информации за патна мрежа во реално време</h2>
          <p class="intro-body">RoadMk е официјалната платформа на АМСМ за следење на состојбата на патната мрежа во Македонија. Информациите се прибираат директно од изворите на АМСМ и се ажурираат автоматски.</p>
          <ul class="intro-checks">
            <li>Автоматско прибирање на податоци од АМСМ</li>
            <li>Класификација по тежина — Затворено / Предупредување / Нормално</li>
            <li>Дневни и сезонски информации за патиштата</li>
            <li>Покриеност на целата патна мрежа</li>
          </ul>
          <router-link to="/roads" class="intro-btn">ПРЕГЛЕДАЈ СИТЕ ПАТИШТА</router-link>
        </div>
      </div>
    </section>

    <!-- STATS BANNER -->
    <section class="stats-banner">
      <div class="stats-inner">
        <div class="stat-item">
          <span class="stat-num" v-if="summary">{{ summary.total }}</span>
          <span class="stat-num" v-else>—</span>
          <span class="stat-label">Вкупно извештаи</span>
        </div>
        <div class="stat-item">
          <span class="stat-num" v-if="summary">{{ summary.red }}</span>
          <span class="stat-num" v-else>—</span>
          <span class="stat-label">Затворени делници</span>
        </div>
        <div class="stat-item">
          <span class="stat-num" v-if="summary">{{ summary.yellow }}</span>
          <span class="stat-num" v-else>—</span>
          <span class="stat-label">Предупредувања</span>
        </div>
        <div class="stat-item">
          <span class="stat-num" v-if="summary">{{ summary.green }}</span>
          <span class="stat-num" v-else>—</span>
          <span class="stat-label">Нормални делници</span>
        </div>
      </div>
    </section>

    <!-- LATEST REPORTS -->
    <section class="latest-section">
      <div class="latest-inner">
        <div class="section-head">
          <div>
            <p class="section-eyebrow">ПОСЛЕДНИ ИНФОРМАЦИИ</p>
            <h2 class="section-title">Актуелни извештаи</h2>
          </div>
          <router-link to="/roads" class="see-all">Сите извештаи →</router-link>
        </div>
        <div v-if="loading" class="loading-state">
          <div class="loader"></div>
          <p>Се вчитуваат податоците...</p>
        </div>
        <div v-else class="reports-grid">
          <div v-for="report in latestReports" :key="report.id" class="rcard">
            <div :class="['rcard-badge', report.severity.toLowerCase()]">
              {{ severityLabel(report.severity) }}
            </div>
            <div class="rcard-cat">{{ categoryLabel(report.category) }}</div>
            <h3 class="rcard-title">{{ report.title }}</h3>
            <p class="rcard-desc">{{ report.description.slice(0, 110) }}...</p>
            <div class="rcard-footer" v-if="report.valid_from">
              <span>Од: {{ report.valid_from }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EMERGENCY BAND -->
    <section class="emergency-band">
      <div class="emergency-inner">
        <div class="emergency-text">
          <h3>Потребна ви е итна помош на пат?</h3>
          <p>Достапни 24 часа, 7 дена во неделата низ целата Македонија.</p>
        </div>
        <a href="tel:196" class="emergency-btn">ЈАВЕТЕ СЕ НА 196</a>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { getReports, getSummary } from '../api/reports'

const reports = ref([])
const summary = ref(null)
const loading = ref(true)

const latestReports = computed(() => reports.value.slice(0, 6))

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

onMounted(async () => {
  const [r, s] = await Promise.all([getReports(), getSummary()])
  reports.value = r
  summary.value = s
  loading.value = false
})
</script>

<style scoped>
/* HERO */
.hero {
  position: relative;
  min-height: 560px;
  background: linear-gradient(135deg, #0d1b2a 0%, #0f2d3d 50%, #162032 100%);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 80px 48px;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 70% 50%, rgba(245,195,0,0.06) 0%, transparent 60%);
  pointer-events: none;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 580px;
}

.hero-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--yellow);
  margin-bottom: 16px;
  font-weight: 500;
}

.hero-title {
  font-family: 'Oswald', sans-serif;
  font-size: 72px;
  font-weight: 700;
  color: #fff;
  line-height: 1.0;
  letter-spacing: -1px;
  margin-bottom: 20px;
}

.hero-sub {
  color: #8fa3b1;
  font-size: 16px;
  line-height: 1.7;
  margin-bottom: 36px;
}

.hero-btn {
  display: inline-block;
  background: var(--yellow);
  color: #111;
  font-family: 'Oswald', sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 16px 36px;
  text-decoration: none;
  transition: background 0.2s, transform 0.15s;
  clip-path: polygon(0 0, calc(100% - 12px) 0, 100% 100%, 12px 100%);
}

.hero-btn:hover {
  background: #ffd700;
  transform: translateY(-2px);
}

.hero-stats {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.hstat {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.08);
  border-left: 4px solid;
  padding: 16px 28px;
  display: flex;
  align-items: center;
  gap: 20px;
  min-width: 220px;
}

.hstat.red { border-left-color: var(--red); }
.hstat.yellow { border-left-color: var(--yellow); }
.hstat.green { border-left-color: var(--green); }
.hstat.total { border-left-color: #4a6070; }

.hstat-n {
  font-family: 'Oswald', sans-serif;
  font-size: 42px;
  font-weight: 700;
  line-height: 1;
  color: #fff;
}

.hstat.red .hstat-n { color: var(--red); }
.hstat.yellow .hstat-n { color: var(--yellow); }
.hstat.green .hstat-n { color: var(--green); }

.hstat-l {
  font-size: 11px;
  letter-spacing: 2px;
  color: #6a8394;
  font-weight: 600;
}

/* SERVICES ROW */
.services-row {
  background: var(--white);
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
}

.services-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: flex;
  justify-content: space-between;
}

.svc {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 28px 16px;
  text-decoration: none;
  color: var(--text);
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-align: center;
  border-bottom: 3px solid transparent;
  transition: color 0.2s, border-color 0.2s;
  flex: 1;
}

.svc:hover {
  color: var(--dark);
  border-bottom-color: var(--yellow);
}

.svc-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--gray);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--teal);
  transition: background 0.2s, color 0.2s;
}

.svc:hover .svc-icon {
  background: rgba(245,195,0,0.15);
  color: var(--dark);
}

.services-cta {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid #e8ecf0;
  background: var(--gray);
}

.services-cta span { font-size: 14px; color: var(--muted); }

.cta-btn {
  background: var(--yellow);
  color: #111;
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 12px 28px;
  text-decoration: none;
  transition: background 0.2s;
}

.cta-btn:hover { background: var(--yellow-dark); }

/* INTRO SECTION */
.intro-section {
  background: var(--white);
  padding: 96px 0;
}

.intro-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 80px;
  align-items: center;
}

.intro-visual {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.intro-card {
  padding: 40px 24px;
  border-radius: 2px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.intro-card.dark { background: var(--dark); grid-column: 1 / -1; }
.intro-card.yellow { background: var(--yellow); }

.intro-big-num {
  font-family: 'Oswald', sans-serif;
  font-size: 64px;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 8px;
}

.intro-card.dark .intro-big-num { color: var(--yellow); }
.intro-card.yellow .intro-big-num { color: #111; }

.intro-big-label { font-size: 11px; letter-spacing: 2.5px; font-weight: 700; }
.intro-card.dark .intro-big-label { color: #4a6070; }
.intro-card.yellow .intro-big-label { color: #555; }

.intro-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--yellow-dark);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.intro-eyebrow::before {
  content: '';
  display: inline-block;
  width: 28px;
  height: 3px;
  background: var(--yellow);
}

.intro-heading {
  font-family: 'Oswald', sans-serif;
  font-size: 40px;
  font-weight: 700;
  color: var(--dark);
  line-height: 1.15;
  margin-bottom: 24px;
}

.intro-body {
  font-size: 15px;
  color: var(--muted);
  line-height: 1.8;
  margin-bottom: 28px;
}

.intro-checks {
  list-style: none;
  margin-bottom: 36px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.intro-checks li {
  font-size: 14px;
  color: var(--text);
  padding-left: 18px;
  position: relative;
}

.intro-checks li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--yellow);
}

.intro-btn {
  display: inline-block;
  background: var(--dark);
  color: var(--yellow);
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 14px 32px;
  text-decoration: none;
  border: 2px solid var(--dark);
  transition: background 0.2s, color 0.2s;
}

.intro-btn:hover {
  background: var(--yellow);
  color: #111;
  border-color: var(--yellow);
}

/* STATS BANNER */
.stats-banner { background: var(--dark2); padding: 64px 48px; }

.stats-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 0 40px;
  border-left: 1px solid rgba(255,255,255,0.06);
}

.stat-item:first-child { padding-left: 0; border-left: none; }

.stat-num {
  font-family: 'Oswald', sans-serif;
  font-size: 56px;
  font-weight: 700;
  color: var(--yellow);
  line-height: 1;
}

.stat-label {
  font-size: 12px;
  color: #4a6070;
  letter-spacing: 1px;
  text-transform: uppercase;
}

/* LATEST REPORTS */
.latest-section { background: var(--gray); padding: 80px 0; }

.latest-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
}

.section-head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 40px;
}

.section-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--yellow-dark);
  margin-bottom: 6px;
}

.section-title {
  font-family: 'Oswald', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: var(--dark);
}

.see-all {
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  letter-spacing: 1px;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s;
}

.see-all:hover { color: var(--dark); }

.reports-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.rcard {
  background: var(--white);
  padding: 28px;
  border-top: 4px solid #ddd;
  box-shadow: 0 2px 12px rgba(0,0,0,0.05);
  transition: transform 0.2s, box-shadow 0.2s;
}

.rcard:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 28px rgba(0,0,0,0.1);
}

.rcard-badge {
  display: inline-block;
  font-family: 'Oswald', sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 4px 10px;
  color: white;
  margin-bottom: 10px;
}

.rcard-badge.red { background: var(--red); }
.rcard-badge.yellow { background: #d4a900; }
.rcard-badge.green { background: var(--green); }

.rcard:has(.rcard-badge.red) { border-top-color: var(--red); }
.rcard:has(.rcard-badge.yellow) { border-top-color: var(--yellow); }
.rcard:has(.rcard-badge.green) { border-top-color: var(--green); }

.rcard-cat {
  font-size: 11px;
  letter-spacing: 1.5px;
  color: var(--muted);
  text-transform: uppercase;
  margin-bottom: 10px;
}

.rcard-title {
  font-family: 'Oswald', sans-serif;
  font-size: 18px;
  font-weight: 600;
  color: var(--dark);
  margin-bottom: 10px;
  line-height: 1.3;
}

.rcard-desc { font-size: 13px; color: var(--muted); line-height: 1.7; margin-bottom: 14px; }

.rcard-footer {
  font-size: 12px;
  color: #9ab;
  padding-top: 12px;
  border-top: 1px solid #eee;
}

/* LOADING */
.loading-state { text-align: center; padding: 60px; color: var(--muted); }

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

/* EMERGENCY BAND */
.emergency-band { background: var(--red); padding: 40px 48px; }

.emergency-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
}

.emergency-text h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 24px;
  font-weight: 700;
  color: white;
  margin-bottom: 4px;
}

.emergency-text p { font-size: 14px; color: rgba(255,255,255,0.7); }

.emergency-btn {
  background: white;
  color: var(--red);
  font-family: 'Oswald', sans-serif;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 16px 40px;
  text-decoration: none;
  white-space: nowrap;
  transition: transform 0.15s;
}

.emergency-btn:hover { transform: scale(1.04); }
</style>
