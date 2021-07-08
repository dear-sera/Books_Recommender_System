<template>
  <v-app id="app" style="background-color: #212121">
    <layout-header app></layout-header>
    <book-searchbar></book-searchbar>
    <v-main id="content" class="content">
      <router-view style="max-width: 1185px"></router-view>
    </v-main>
    <layout-footer app></layout-footer>
  </v-app>
</template>

<script>
// import axios from "axios";
import Header from "./components/layout/Header.vue";
import BookSearchBar from "./views/BookSearchBar.vue";
import Footer from "./components/layout/Footer.vue";

// let url = "http://localhost:8000/api/book/"; // drf server addr

export default {
  data: () => {
    return {
      bookList: [],
    };
  },
  created() {
    document.title = "Jasmine";
  },
  components: {
    "layout-header": Header,
    "book-searchbar": BookSearchBar,
    "layout-footer": Footer,
  },
};
</script>

<style>
</style>