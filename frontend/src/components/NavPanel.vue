<template>
  <div>
    <nav class="nav">
      <div class="logo">
        <h2>
          <span class="get">Get</span>
          <span class="book">Book</span>
        </h2>
      </div>
      <div class="main">
        <ul>
          <li><a>Главная</a></li>
          <li>Каталог</li>
          <li>
            <a href="{% url 'office' %}"> Привет, </a
            ><a href="{% url 'login' %}">Войти</a>
          </li>
          <li><a href="{% url 'createAvtor' %}">Загрузить</a></li>
        </ul>
      </div>
      <button class="regist">
        <a href="{% url 'logout' %}">Выйти</a
        ><a href="{% url 'registration' %}">Регистрация</a>
      </button>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hello: "hello",
    };
  },
};
</script>
