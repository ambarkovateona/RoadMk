<template>
  <div>
    <section class="page-hero">
      <div class="page-hero-inner">
        <p class="page-eyebrow">АМСМ — КОНТАКТ</p>
        <h1>Поврзете се со нас</h1>
        <p>Достапни за сите Ваши прашања и потреби</p>
      </div>
    </section>

    <section class="contact-section">
      <div class="contact-inner">

        <div class="contact-info">
          <p class="section-eyebrow">ИНФОРМАЦИИ ЗА КОНТАКТ</p>
          <h2>Кажете ни како<br>можеме да помогнеме</h2>

          <div class="ci-list">
            <div class="ci-item">
              <div class="ci-label">ПОМОШ НА ПАТ</div>
              <p class="ci-big">196</p>
              <p>Достапни 24/7</p>
            </div>
            <div class="ci-item">
              <div class="ci-label">ТЕЛЕФОН</div>
              <p>+389 2 3289 777</p>
            </div>
            <div class="ci-item">
              <div class="ci-label">ЕЛЕКТРОНСКА ПОШТА</div>
              <p>info@amsm.mk</p>
            </div>
            <div class="ci-item">
              <div class="ci-label">АДРЕСА</div>
              <p>Бул. Партизански одреди 56</p>
              <p>1000 Скопје, Македонија</p>
            </div>
            <div class="ci-item">
              <div class="ci-label">РАБОТНО ВРЕМЕ</div>
              <p>Понеделник – Петок: 08:00 – 16:00</p>
              <p>Сабота – Недела: Затворено</p>
            </div>
          </div>
        </div>

        <div class="emergency-col">
          <div class="emergency-card">
            <p class="em-eyebrow">ИТНА ПОМОШ</p>
            <div class="em-number">196</div>
            <h3>Помош на пат</h3>
            <p>Достапни 24 часа, 7 дена во неделата за итна помош на патот низ целата Македонија.</p>
            <div class="em-services">
              <div class="em-svc">Влечење возила</div>
              <div class="em-svc">Техничка помош</div>
              <div class="em-svc">Гориво при нужда</div>
              <div class="em-svc">Отклучување возила</div>
            </div>
            <a href="tel:196" class="em-call-btn">ЈАВЕТЕ СЕ НА 196</a>
          </div>

          <div class="quick-links">
            <h4>БРЗИ ЛИНКОВИ</h4>
            <router-link to="/roads">Состојба на патишта</router-link>
            <router-link to="/roads">Затворени патишта</router-link>
            <router-link to="/roads">Предупредувања</router-link>
            <router-link to="/about">За нас</router-link>
          </div>
        </div>

      </div>
    </section>

    <section class="contact-band">
      <div class="contact-band-inner">
        <div class="band-item">
          <p class="band-label">ПОМОШ НА ПАТ</p>
          <p class="band-val">196</p>
        </div>
        <div class="band-item">
          <p class="band-label">ЕМАИЛ</p>
          <p class="band-val">info@amsm.mk</p>
        </div>
        <div class="band-item">
          <p class="band-label">РАБОТНО ВРЕМЕ</p>
          <p class="band-val">Пон – Пет 08:00 – 16:00</p>
        </div>
        <div class="band-item">
          <p class="band-label">АДРЕСА</p>
          <p class="band-val">Скопје, Македонија</p>
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

.contact-section { background: var(--gray); padding: 80px 0; }

.contact-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 56px;
  align-items: start;
}

.section-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
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

.contact-info h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 36px;
  font-weight: 700;
  color: var(--dark);
  line-height: 1.15;
  margin-bottom: 36px;
}

.ci-list { display: flex; flex-direction: column; gap: 2px; }

.ci-item {
  background: white;
  padding: 18px 24px;
  border-left: 3px solid transparent;
  transition: border-color 0.2s;
}

.ci-item:hover { border-left-color: var(--yellow); }

.ci-label {
  font-family: 'Oswald', sans-serif;
  font-size: 10px;
  letter-spacing: 2.5px;
  color: var(--muted);
  margin-bottom: 6px;
}

.ci-item p { font-size: 14px; color: var(--text); margin-bottom: 2px; }

.ci-big {
  font-family: 'Oswald', sans-serif;
  font-size: 36px !important;
  font-weight: 700;
  color: var(--yellow) !important;
  line-height: 1;
  margin-bottom: 2px;
}

.emergency-col { display: flex; flex-direction: column; gap: 20px; }

.emergency-card {
  background: var(--dark);
  padding: 40px 36px;
  text-align: center;
}

.em-eyebrow {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  letter-spacing: 3px;
  color: rgba(245,195,0,0.5);
  margin-bottom: 8px;
}

.em-number {
  font-family: 'Oswald', sans-serif;
  font-size: 88px;
  font-weight: 700;
  color: var(--yellow);
  line-height: 1;
  margin-bottom: 4px;
}

.emergency-card h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 14px;
  letter-spacing: 3px;
  color: rgba(255,255,255,0.5);
  margin-bottom: 16px;
  text-transform: uppercase;
}

.emergency-card > p {
  font-size: 14px;
  color: #5a7382;
  line-height: 1.7;
  margin-bottom: 28px;
}

.em-services {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 28px;
}

.em-svc {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.07);
  padding: 10px;
  font-size: 13px;
  color: #8fa3b1;
}

.em-call-btn {
  display: block;
  background: var(--yellow);
  color: #111;
  font-family: 'Oswald', sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 16px;
  text-decoration: none;
  transition: background 0.2s;
}

.em-call-btn:hover { background: #ffd700; }

.quick-links { background: white; padding: 24px 28px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }

.quick-links h4 {
  font-family: 'Oswald', sans-serif;
  font-size: 11px;
  letter-spacing: 2.5px;
  color: var(--muted);
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid #e8ecf0;
}

.quick-links a {
  display: block;
  font-size: 14px;
  color: var(--text);
  text-decoration: none;
  padding: 8px 0;
  border-bottom: 1px solid #f0f2f5;
  transition: color 0.2s, padding-left 0.2s;
  font-family: 'Oswald', sans-serif;
  letter-spacing: 0.5px;
}

.quick-links a:hover { color: var(--yellow-dark); padding-left: 6px; }

.contact-band { background: var(--dark); padding: 40px 0; }

.contact-band-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.band-item {
  padding: 16px 24px;
  border-right: 1px solid rgba(255,255,255,0.06);
}

.band-item:last-child { border-right: none; }

.band-label {
  font-family: 'Oswald', sans-serif;
  font-size: 10px;
  letter-spacing: 2px;
  color: #4a6070;
  margin-bottom: 6px;
}

.band-val {
  font-family: 'Oswald', sans-serif;
  font-size: 16px;
  font-weight: 600;
  color: var(--yellow);
}
</style>
