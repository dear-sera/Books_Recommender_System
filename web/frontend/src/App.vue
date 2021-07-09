<template>
  <v-app
    id="app"
    style="background: linear-gradient(to right top, #a15086, #6a60a9)"
  >
    <div class="circle1"></div>
    <div class="circle2"></div>
    <layout-header app></layout-header>
    <book-searchbar></book-searchbar>
    <v-main id="content" class="content">
      <router-view style="max-width: 1185px"></router-view>
    </v-main>
    <layout-footer app class="customfooter"></layout-footer>
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
.circle1,
.circle2 {
  background: #fffcf0;
  background: linear-gradient(
    to right bottom,
    rgba(255, 255, 255, 0.1),
    rgba(255, 255, 255, 0.3)
  );
  height: 30rem;
  width: 30rem;
  position: absolute;
  border-radius: 15rem;
}
.circle1 {
  top: 5%;
  right: 5%;
}
.circle2 {
  bottom: 5%;
  left: 5%;
}
</style>