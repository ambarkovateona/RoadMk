<template>
  <div class="page">
    <div class="page-hero">
      <h1>КОНТАКТ</h1>
      <p>Поврзете се со нас</p>
    </div>

    <div class="page-content">
      <div class="contact-grid">

        <div class="contact-info">
          <h2>Информации за контакт</h2>

          <div class="contact-item">
            <div class="contact-icon">📞</div>
            <div>
              <h4>ПОМОШ НА ПАТ</h4>
              <p>196</p>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon">📱</div>
            <div>
              <h4>ТЕЛЕФОН</h4>
              <p>+389 2 3289 777</p>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon">✉️</div>
            <div>
              <h4>ЕМАИЛ</h4>
              <p>info@amsm.mk</p>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon">📍</div>
            <div>
              <h4>АДРЕСА</h4>
              <p>Бул. Партизански одреди 56</p>
              <p>1000 Скопје, Македонија</p>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon">🕐</div>
            <div>
              <h4>РАБОТНО ВРЕМЕ</h4>
              <p>Понеделник – Петок: 08:00 – 16:00</p>
              <p>Сабота – Недела: Затворено</p>
            </div>
          </div>
        </div>

        <div class="emergency-card">
          <div class="emergency-number">196</div>
          <h3>ПОМОШ НА ПАТ</h3>
          <p>Достапни 24 часа, 7 дена во неделата за итна помош на патот низ целата држава.</p>
          <div class="emergency-services">
            <div class="service">🚗 Влечење возила</div>
            <div class="service">🔧 Техничка помош</div>
            <div class="service">⛽ Гориво при нужда</div>
            <div class="service">🔑 Отклучување возила</div>
          </div>
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

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.contact-info h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 28px;
  padding-bottom: 8px;
  border-bottom: 3px solid #F5C300;
}

.contact-item {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
  padding: 16px;
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}

.contact-icon { font-size: 24px; }

.contact-item h4 {
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  letter-spacing: 2px;
  color: #888;
  margin-bottom: 4px;
}

.contact-item p { font-size: 15px; color: #222; }

.emergency-card {
  background: #111;
  color: white;
  border-radius: 4px;
  padding: 40px;
  text-align: center;
  align-self: start;
}

.emergency-number {
  font-family: 'Oswald', sans-serif;
  font-size: 96px;
  font-weight: 700;
  color: #F5C300;
  line-height: 1;
  margin-bottom: 8px;
}

.emergency-card h3 {
  font-family: 'Oswald', sans-serif;
  font-size: 18px;
  letter-spacing: 3px;
  color: #F5C300;
  margin-bottom: 16px;
}

.emergency-card p {
  font-size: 14px;
  color: #aaa;
  line-height: 1.7;
  margin-bottom: 28px;
}

.emergency-services {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.service {
  background: rgba(245,195,0,0.1);
  border: 1px solid rgba(245,195,0,0.3);
  padding: 10px;
  border-radius: 4px;
  font-size: 13px;
  color: #ddd;
}
</style>
