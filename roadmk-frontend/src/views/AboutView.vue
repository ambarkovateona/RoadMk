<template>
  <div class="page">
    <div class="page-hero">
      <h1>ЗА НАС</h1>
      <p>Авто-Мото Сојуз на Македонија</p>
    </div>

    <div class="page-content">
      <div class="about-grid">
        <div class="about-main">
          <h2>Кои сме ние?</h2>
          <p>Авто-Мото Сојузот на Македонија (АМСМ) е национална организација која ги застапува интересите на возачите и сопствениците на моторни возила во Република Северна Македонија.</p>
          <p>Основана со цел да обезбеди безбедност на патиштата, АМСМ нуди широк спектар на услуги — од помош на пат и техничко советување, до обука и едукација за безбедно возење.</p>
          <p>Денес, АМСМ е препознатлива организација со долгогодишна традиција, посветена на унапредување на сообраќајната безбедност и квалитетот на услугите за возачите.</p>

          <h2>Нашата мисија</h2>
          <p>Да обезбедиме безбедни и удобни услови за сите учесници во сообраќајот, преку навремено информирање, стручна помош и постојано подобрување на патната инфраструктура.</p>
        </div>

        <div class="about-side">
          <div class="info-card">
            <div class="info-icon">📞</div>
            <h3>ПОМОШ НА ПАТ</h3>
            <p class="big-number">196</p>
            <p>Достапни 24/7</p>
          </div>
          <div class="info-card">
            <div class="info-icon">📍</div>
            <h3>АДРЕСА</h3>
            <p>Бул. Партизански одреди 56</p>
            <p>1000 Скопје</p>
          </div>
          <div class="info-card">
            <div class="info-icon">🕐</div>
            <h3>РАБОТНО ВРЕМЕ</h3>
            <p>Пон – Пет: 08:00 – 16:00</p>
            <p>Сab – Нед: Затворено</p>
          </div>
        </div>
      </div>

      <div class="stats-row">
        <div class="stat">
          <span class="stat-num">50+</span>
          <span class="stat-label">ГОДИНИ ИСКУСТВО</span>
        </div>
        <div class="stat">
          <span class="stat-num">100K+</span>
          <span class="stat-label">ЧЛЕНОВИ</span>
        </div>
        <div class="stat">
          <span class="stat-num">24/7</span>
          <span class="stat-label">ПОДДРШКА</span>
        </div>
        <div class="stat">
          <span class="stat-num">196</span>
          <span class="stat-label">ПОМОШ НА ПАТ</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.page-hero {
  background: #111;
  color: white;
  padding: 48px 40px;
}

.page-hero h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 36px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #F5C300;
}

.page-hero p { margin-top: 8px; color: #aaa; font-size: 15px; }

.page-content {
  max-width: 960px;
  margin: 0 auto;
  padding: 48px 20px;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 40px;
  margin-bottom: 48px;
}

.about-main h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  font-weight: 600;
  color: #111;
  margin: 28px 0 12px;
  padding-bottom: 8px;
  border-bottom: 3px solid #F5C300;
}

.about-main h2:first-child { margin-top: 0; }

.about-main p {
  font-size: 15px;
  line-height: 1.8;
  color: #444;
  margin-bottom: 12px;
}

.info-card {
  background: white;
  border-radius: 4px;
  padding: 24px;
  margin-bottom: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  border-left: 4px solid #F5C300;
}

.info-icon { font-size: 24px; margin-bottom: 8px; }

.info-card h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  letter-spacing: 2px;
  color: #888;
  margin-bottom: 8px;
}

.info-card p { font-size: 14px; color: #333; margin-bottom: 4px; }

.big-number {
  font-family: 'Oswald', sans-serif;
  font-size: 40px !important;
  font-weight: 700;
  color: #F5C300 !important;
  line-height: 1;
}

.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.stat {
  background: #111;
  color: white;
  padding: 32px 20px;
  text-align: center;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat-num {
  font-family: 'Oswald', sans-serif;
  font-size: 36px;
  font-weight: 700;
  color: #F5C300;
}

.stat-label {
  font-size: 11px;
  letter-spacing: 2px;
  color: #aaa;
}
</style>
