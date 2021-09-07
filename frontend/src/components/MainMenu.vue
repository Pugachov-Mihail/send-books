<template>
  <div class="main">
    <div class="main_block">
      <img src="{{ imgBook }}" alt="Book" />
      <h1 class="heading">{{ book.name }}</h1>
      <h3 class="autor">{{ book.autor }}</h3>
      <p class="description"></p>
      <button class="btn"></button>
      <div class="reit">
        <h2>Рейтинг</h2>
        <span class="starts">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
        <button class="download">
          <a href="" download="">Скачать</a>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  imgBook: "/src/assets/book.jpg",
};
</script>
