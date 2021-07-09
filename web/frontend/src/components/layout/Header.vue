<template>
  <header>
    <center>
      <h1>
        <router-link to="/" class="test amber--text text--accent-2"
          >Jasmine</router-link
        >
      </h1>
    </center>
  </header>
</template>

<script>
export default {
  name: "layout-header",
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap");
.test {
  color: rgb(30, 212, 152);
  font-size: 150px;
  text-decoration-line: none;
  font-family: "Permanent Marker", cursive;
  margin-top: 40px;
}
</style>