<template>
  <v-container class="py-5">
    <v-card class="roundedbox" color="#ffffff00" elevation="11">
      <v-img
        gradient="to bottom left, rgba(255,255,255,.33), rgba(255,255,255,.7)"
        class="pb-10"
      >
        <div v-for="(best, i) in bests" :key="i">
          <div class="whiteopactiy" style="padding-left: 68px">
            <h2 style="padding-top: 40px">{{ best[0].flag }} bestseller</h2>
            <p class="mb-0">updated {{ best[0].date }}</p>
          </div>
          <v-sheet elevation="0" class="py-5" color="#ffffff00">
            <v-slide-group class="pa-4" show-arrows>
              <v-slide-item v-for="(book, i) in best" :key="book.id">
                <v-hover
                  style="max-width: 250px; margin: 2px"
                  v-slot:default="{ hover }"
                >
                  <v-card color="#ffffff50" flat>
                    <v-img
                      class="white--text"
                      :src="book.image"
                      height="40vh"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                    >
                      <v-layout
                        column
                        align-left
                        justify-end
                        class="white--text"
                        fill-height
                      >
                        <h1
                          class="
                            white--text
                            font-weight-bold
                            ma-2
                            display-2
                            text-left
                          "
                        >
                          {{ i + 1 }}
                        </h1>
                      </v-layout>
                    </v-img>
                    <v-card-title class=""
                      ><div class="headerClass">
                        {{ book.title }}
                      </div></v-card-title
                    >

                    <v-card-subtitle class="pb-0">
                      {{ book.author }}
                    </v-card-subtitle>

                    <v-card-text class="text--primary">
                      <div>{{ book.summary }}</div>
                    </v-card-text>
                    <v-fade-transition>
                      <v-overlay
                        v-if="hover"
                        absolute
                        color="#ffffff"
                        opacity="0.8"
                      >
                        <v-btn @click="openDetail(book.url)" color="#262258"
                          >See more info</v-btn
                        >
                      </v-overlay>
                    </v-fade-transition>
                  </v-card>
                </v-hover>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
        </div>
      </v-img>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: () => {
    return {
      bests: [],
      overlay: false,
    };
  },

  created() {
    axios
      .get("http://localhost:8000/api/best/")
      .then((response) => {
        console.log(response.data[0].flag);
        var dailyBooks = this.filteredBook(response.data, "Daily");
        var weeklyBooks = this.filteredBook(response.data, "Weekly");
        var newBooks = this.filteredBook(response.data, "New Release");
        this.bests = [dailyBooks, weeklyBooks, newBooks];
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    openDetail: function (url) {
      window.open(url);
    },
    filteredBook: function (collection, f) {
      var result = new Array();
      var length = collection.length;

      for (var j = 0; j < length; j++) {
        if (collection[j].flag == f) {
          result.push(collection[j]);
        }
      }

      return result;
    },
  },
};
</script>

<style>
.headerClass {
  white-space: nowrap;
  word-break: normal;
  overflow: hidden;
  text-overflow: ellipsis;
}
.whiteopactiy,
whiteopactiy * {
  background-color: #ffffff00;
}
.roundedbox {
  border-radius: 50px !important;
}
</style>
