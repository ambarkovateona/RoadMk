<template>
  <div>
    <!-- Top Bar -->
    <div class="topbar">
      <div class="topbar-left">
        <span>Помош на пат: <strong>196</strong></span>
        <span>Пон – Пет: 08:00 – 16:00</span>
      </div>
      <div class="topbar-right">
        <span>info@amsm.mk</span>
        <span>+389 2 3289 777</span>
      </div>
    </div>

    <!-- Header -->
    <header class="main-header">
      <router-link to="/" class="logo">
        <span class="logo-text">Road<span class="logo-accent">Mk</span></span>
      </router-link>
      <nav class="main-nav">
        <router-link to="/">ПОЧЕТНА</router-link>
        <router-link to="/roads">СОСТОЈБА НА ПАТИШТА</router-link>
        <router-link to="/about">ЗА НАС</router-link>
        <router-link to="/contact">КОНТАКТ</router-link>
      </nav>
    </header>

    <router-view />

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-inner">
        <div class="footer-brand">
          <div class="footer-logo">RoadMk</div>
          <p>Авто-Мото Сојуз на Македонија</p>
          <p class="footer-tagline">Информирај се пред да тргнеш.</p>
        </div>
        <div class="footer-col">
          <h4>НАВИГАЦИЈА</h4>
          <router-link to="/">Почетна</router-link>
          <router-link to="/roads">Состојба на патишта</router-link>
          <router-link to="/about">За нас</router-link>
          <router-link to="/contact">Контакт</router-link>
        </div>
        <div class="footer-col">
          <h4>СТАТУСИ</h4>
          <span class="footer-status red">Затворено</span>
          <span class="footer-status yellow">Предупредување</span>
          <span class="footer-status green">Нормално</span>
        </div>
        <div class="footer-col">
          <h4>КОНТАКТ</h4>
          <p>Помош на пат: <strong class="accent">196</strong></p>
          <p>+389 2 3289 777</p>
          <p>info@amsm.mk</p>
          <p>Бул. Партизански одреди 56</p>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 АМСМ — Авто-Мото Сојуз на Македонија</span>
        <span>Состојбата на патиштата се освежува на секои 30 минути</span>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap');

*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --yellow: #F5C300;
  --yellow-dark: #d4a900;
  --dark: #0d1b2a;
  --dark2: #162032;
  --teal: #0f2d3d;
  --teal2: #1a3a4d;
  --white: #ffffff;
  --gray: #f5f6f8;
  --text: #2c3e50;
  --muted: #7f8c9a;
  --red: #e74c3c;
  --green: #27ae60;
}

html { scroll-behavior: smooth; }

body {
  font-family: 'Inter', sans-serif;
  background: var(--white);
  color: var(--text);
  line-height: 1.6;
}

/* TOP BAR */
.topbar {
  background: var(--dark);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 48px;
  font-size: 12px;
  color: #8fa3b1;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.topbar-left, .topbar-right {
  display: flex;
  gap: 24px;
  align-items: center;
}

.topbar strong {
  color: var(--yellow);
  font-weight: 700;
}

/* HEADER */
.main-header {
  background: var(--white);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 48px;
  height: 72px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 16px rgba(0,0,0,0.08);
  border-bottom: 3px solid var(--yellow);
}

.logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo-text {
  font-family: 'Oswald', sans-serif;
  font-size: 30px;
  font-weight: 700;
  color: var(--dark);
  letter-spacing: 1px;
}

.logo-accent { color: var(--yellow); }

.main-nav {
  display: flex;
  gap: 2px;
  align-items: center;
}

.main-nav a {
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 1.2px;
  color: var(--text);
  text-decoration: none;
  padding: 10px 18px;
  transition: color 0.2s, background 0.2s;
  border-radius: 2px;
  position: relative;
}

.main-nav a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 3px;
  background: var(--yellow);
  transition: width 0.25s;
}

.main-nav a:hover::after,
.main-nav a.router-link-active::after {
  width: 100%;
}

.main-nav a.router-link-active {
  color: var(--dark);
  font-weight: 700;
}

/* FOOTER */
.footer {
  background: var(--teal);
  color: #a0b4c0;
}

.footer-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 64px 48px;
  display: grid;
  grid-template-columns: 2.5fr 1fr 1.2fr 1.5fr;
  gap: 48px;
}

.footer-logo {
  font-family: 'Oswald', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--yellow);
  margin-bottom: 12px;
}

.footer-brand p {
  font-size: 14px;
  margin-bottom: 4px;
  color: #8fa3b1;
}

.footer-tagline {
  font-style: italic;
  color: #6a8394 !important;
  margin-top: 12px !important;
  font-size: 13px !important;
}

.footer-col h4 {
  font-family: 'Oswald', sans-serif;
  font-size: 12px;
  letter-spacing: 2.5px;
  color: var(--yellow);
  margin-bottom: 20px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(245,195,0,0.2);
}

.footer-col a,
.footer-col span,
.footer-col p {
  display: block;
  font-size: 13px;
  color: #8fa3b1;
  text-decoration: none;
  margin-bottom: 10px;
  transition: color 0.2s;
}

.footer-col a:hover { color: var(--yellow); }

.footer-status {
  display: flex !important;
  align-items: center;
  gap: 8px;
  padding-left: 14px;
  position: relative;
}

.footer-status::before {
  content: '';
  position: absolute;
  left: 0;
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.footer-status.red::before { background: var(--red); }
.footer-status.yellow::before { background: var(--yellow); }
.footer-status.green::before { background: var(--green); }

.accent { color: var(--yellow) !important; font-size: 18px !important; }

.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.06);
  max-width: 1200px;
  margin: 0 auto;
  padding: 18px 48px;
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #4a6070;
  letter-spacing: 0.5px;
}
</style>
