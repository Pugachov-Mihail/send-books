<template>
  <nav-panel></nav-panel>
  <main-menu>{{ seriz|json_script:"idDjango" }}</main-menu>
</template>

<script>
import NavPanel from "./components/NavPanel";
import MainMenu from "./components/MainMenu.vue";
import "./assets/reset.css";
import "./assets/style.css";
import "./assets/font.css";

export default {
  name: "App",
  data() {
    return {
      beck: {
        beck: JSON.parse(document.getElementById("idDjango").textContent),
      },
      books: {
        name: "Ivan",
        description: "das",
        categories: "dasdas",
        url: "",
        autor: "caS",
      },
    };
  },
  components: {
    "nav-panel": NavPanel,
    "main-menu": MainMenu,
  },
};
</script>

<style></style>
