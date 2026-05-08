<template>
  <div>
    <nav class="top-bar">
      <span>ПОМОШ НА ПАТ 196</span>
      <span>info@amsm.mk</span>
      <span>+389 2 3289 777</span>
    </nav>
    <header class="main-header">
      <router-link to="/" class="logo">АМСМ</router-link>
      <nav class="main-nav">
        <router-link to="/">ПОЧЕТНА</router-link>
        <router-link to="/roads">СОСТОЈБА НА ПАТИШТА</router-link>
        <router-link to="/about">ЗА НАС</router-link>
        <router-link to="/contact">КОНТАКТ</router-link>
      </nav>
    </header>
    <router-view />
    <footer class="footer">
      <div class="footer-inner">
        <div class="footer-col">
          <div class="footer-logo">АМСМ</div>
          <p>Авто-Мото Сојуз на Македонија</p>
        </div>
        <div class="footer-col">
          <h4>БРЗИ ЛИНКОВИ</h4>
          <router-link to="/">Почетна</router-link>
          <router-link to="/roads">Состојба на патишта</router-link>
          <router-link to="/about">За нас</router-link>
          <router-link to="/contact">Контакт</router-link>
        </div>
        <div class="footer-col">
          <h4>КОНТАКТ</h4>
          <p>Помош на пат: 196</p>
          <p>Тел: +389 2 3289 777</p>
          <p>info@amsm.mk</p>
        </div>
      </div>
      <div class="footer-bottom">
        © 2026 АМСМ — Авто-Мото Сојуз на Македонија
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Source+Sans+3:wght@400;600&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Source Sans 3', sans-serif;
  background-color: #f2f2f2;
  color: #1a1a1a;
}

/* Top bar */
.top-bar {
  background-color: #111111;
  color: #aaa;
  display: flex;
  gap: 32px;
  padding: 7px 40px;
  font-size: 12px;
  letter-spacing: 1px;
}

/* Header */
.main-header {
  background-color: #F5C300;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  height: 70px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.logo {
  font-family: 'Oswald', sans-serif;
  font-size: 38px;
  font-weight: 700;
  color: #111;
  text-decoration: none;
  letter-spacing: 2px;
}

.main-nav {
  display: flex;
  gap: 4px;
}

.main-nav a {
  font-family: 'Oswald', sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1px;
  color: #111;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 2px;
  transition: background 0.2s;
}

.main-nav a:hover {
  background: rgba(0,0,0,0.1);
}

.main-nav a.router-link-active {
  background: #111;
  color: #F5C300;
}

/* Footer */
.footer {
  background: #111;
  color: #ccc;
  margin-top: 60px;
}

.footer-inner {
  max-width: 960px;
  margin: 0 auto;
  padding: 48px 20px;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 40px;
}

.footer-logo {
  font-family: 'Oswald', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: #F5C300;
  margin-bottom: 8px;
}

.footer-col h4 {
  font-family: 'Oswald', sans-serif;
  font-size: 13px;
  letter-spacing: 2px;
  color: #F5C300;
  margin-bottom: 16px;
}

.footer-col p,
.footer-col a {
  display: block;
  font-size: 14px;
  color: #aaa;
  text-decoration: none;
  margin-bottom: 8px;
  transition: color 0.2s;
}

.footer-col a:hover { color: #F5C300; }

.footer-bottom {
  border-top: 1px solid #333;
  text-align: center;
  padding: 16px;
  font-size: 12px;
  color: #555;
  letter-spacing: 1px;
}
</style>
