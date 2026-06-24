<template>
  <div>
    <section class="page-hero">
      <div class="page-hero-inner">
        <p class="page-eyebrow">АВТО-МОТО СОЈУЗ НА МАКЕДОНИЈА</p>
        <h1>За нас</h1>
        <p>Национална организација за безбедност на патиштата</p>
      </div>
    </section>

    <section class="about-stats">
      <div class="about-stats-inner">
        <div class="astat">
          <span class="astat-n">50+</span>
          <span class="astat-l">Години искуство</span>
        </div>
        <div class="astat">
          <span class="astat-n">100K+</span>
          <span class="astat-l">Членови</span>
        </div>
        <div class="astat">
          <span class="astat-n">24/7</span>
          <span class="astat-l">Поддршка</span>
        </div>
        <div class="astat">
          <span class="astat-n">196</span>
          <span class="astat-l">Помош на пат</span>
        </div>
      </div>
    </section>

    <section class="about-section">
      <div class="about-inner">
        <div class="about-text">
          <p class="section-eyebrow">КОИ СМЕ НИЕ</p>
          <h2>Авто-Мото Сојуз<br>на Македонија</h2>
          <p>Авто-Мото Сојузот на Македонија (АМСМ) е национална организација која ги застапува интересите на возачите и сопствениците на моторни возила во Република Северна Македонија.</p>
          <p>Основана со цел да обезбеди безбедност на патиштата, АМСМ нуди широк спектар на услуги — од помош на пат и техничко советување, до обука и едукација за безбедно возење.</p>
          <p>Денес, АМСМ е препознатлива организација со долгогодишна традиција, посветена на унапредување на сообраќајната безбедност и квалитетот на услугите за возачите.</p>
          <div class="about-divider"></div>
          <h3>Нашата мисија</h3>
          <p>Да обезбедиме безбедни и удобни услови за сите учесници во сообраќајот, преку навремено информирање, стручна помош и постојано подобрување на патната инфраструктура.</p>
          <p>RoadMk е дел од нашата дигитална иницијатива — реално-временска платформа за состојба на патната мрежа, достапна бесплатно за сите граѓани.</p>
        </div>

        <div class="about-cards">
          <div class="info-card">
            <h4>ПОМОШ НА ПАТ</h4>
            <p class="ic-big">196</p>
            <p>Достапни 24/7</p>
          </div>
          <div class="info-card">
            <h4>АДРЕСА</h4>
            <p>Бул. Партизански одреди 56</p>
            <p>1000 Скопје, Македонија</p>
          </div>
          <div class="info-card">
            <h4>РАБОТНО ВРЕМЕ</h4>
            <p>Пон – Пет: 08:00 – 16:00</p>
            <p>Саб – Нед: Затворено</p>
          </div>
          <div class="info-card">
            <h4>ЕЛЕКТРОНСКА ПОШТА</h4>
            <p>info@amsm.mk</p>
            <p>+389 2 3289 777</p>
          </div>
        </div>
      </div>
    </section>

    <section class="services-section">
      <div class="services-inner">
        <div class="services-head">
          <p class="section-eyebrow light">НАШИ УСЛУГИ</p>
          <h2>Што нудиме</h2>
        </div>
        <div class="services-grid">
          <div class="svc-card">
            <div class="svc-num">01</div>
            <h3>Состојба на патишта</h3>
            <p>Дневни информации за затворања, девијации и предупредувања на патната мрежа.</p>
          </div>
          <div class="svc-card">
            <div class="svc-num">02</div>
            <h3>Помош на пат</h3>
            <p>Итна помош на пат 24/7 на број 196 — влечење, техничка помош, гориво.</p>
          </div>
          <div class="svc-card">
            <div class="svc-num">03</div>
            <h3>Техничко советување</h3>
            <p>Стручна помош и совети за одржување и безбедно управување со возилото.</p>
          </div>
          <div class="svc-card">
            <div class="svc-num">04</div>
            <h3>Едукација за возачи</h3>
            <p>Обуки и едукативни материјали за безбедно возење и сообраќај.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
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
}

.page-hero h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 48px;
  font-weight: 700;
  color: white;
  margin-bottom: 8px;
}

.page-hero p { color: #8fa3b1; font-size: 15px; }

.about-stats {
  background: var(--yellow);
  padding: 48px 0;
}

.about-stats-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}

.astat {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 6px;
  padding: 8px 0;
  border-right: 1px solid rgba(0,0,0,0.1);
}

.astat:last-child { border-right: none; }

.astat-n {
  font-family: 'Oswald', sans-serif;
  font-size: 48px;
  font-weight: 700;
  color: #111;
  line-height: 1;
}

.astat-l {
  font-size: 12px;
  letter-spacing: 1.5px;
  color: #555;
  text-transform: uppercase;
  font-weight: 600;
}

.about-section { background: white; padding: 80px 0; }

.about-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 64px;
  align-items: start;
}

.section-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--yellow-dark);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-eyebrow::before {
  content: '';
  display: inline-block;
  width: 28px;
  height: 3px;
  background: var(--yellow);
}

.section-eyebrow.light { color: rgba(255,255,255,0.5); }
.section-eyebrow.light::before { background: rgba(255,255,255,0.3); }

.about-text h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 40px;
  font-weight: 700;
  color: var(--dark);
  line-height: 1.1;
  margin-bottom: 24px;
}

.about-text h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  font-weight: 600;
  color: var(--dark);
  margin-bottom: 12px;
}

.about-text p { font-size: 15px; color: var(--muted); line-height: 1.8; margin-bottom: 16px; }

.about-divider { height: 3px; width: 48px; background: var(--yellow); margin: 32px 0; }

.about-cards { display: flex; flex-direction: column; gap: 12px; }

.info-card {
  background: var(--gray);
  padding: 24px;
  border-left: 4px solid var(--yellow);
}

.info-card h4 {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  letter-spacing: 2.5px;
  color: var(--muted);
  margin-bottom: 8px;
}

.info-card p { font-size: 14px; color: var(--text); margin-bottom: 2px; }

.ic-big {
  font-family: 'Oswald', sans-serif;
  font-size: 36px !important;
  font-weight: 700;
  color: var(--yellow) !important;
  line-height: 1;
  margin-bottom: 4px;
}

.services-section { background: var(--dark2); padding: 80px 0; }

.services-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
}

.services-head { margin-bottom: 48px; }

.services-head h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 36px;
  font-weight: 700;
  color: white;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2px;
}

.svc-card {
  background: rgba(255,255,255,0.04);
  padding: 36px 28px;
  border: 1px solid rgba(255,255,255,0.07);
  transition: background 0.2s, border-color 0.2s;
}

.svc-card:hover {
  background: rgba(245,195,0,0.07);
  border-color: rgba(245,195,0,0.2);
}

.svc-num {
  font-family: 'Oswald', sans-serif;
  font-size: 40px;
  font-weight: 700;
  color: rgba(245,195,0,0.15);
  line-height: 1;
  margin-bottom: 20px;
}

.svc-card h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 16px;
  font-weight: 600;
  color: white;
  margin-bottom: 10px;
}

.svc-card p { font-size: 13px; color: #6a8394; line-height: 1.7; }
</style>
