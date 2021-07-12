<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn width="100%" height="200px" @click="updateDB">UPDATE DB</v-btn>
      </v-col>
      <v-col>
        <v-btn width="100%" height="200px" @click="updateBests"
          >UPDATE BEST</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

let url = "http://localhost:8000/api/"; // drf server addr

export default {
  props: ["propsdata"],
  data: () => {
    return {};
  },
  methods: {
    updateDB: function () {
      axios
        .get(url + "book/updateDB/")
        .then((response) => {
          console.log(response.data);
          this.books = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateBests: function () {
      axios
        .get(url + "best/updateBests/")
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>