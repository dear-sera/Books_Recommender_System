<template>
  <div class="searchbox">
    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    <v-form v-model="isValid">
      <v-flex>
        <v-layout>
          <v-text-field
            class="textfield"
            prepend-inner-icon="mdi-book"
            label="Enter keyword"
            rounded
            solo
            clearable
            v-model="target"
            color="teal accent-4"
            :rules="custom_rules"
            @keydown.enter.prevent="[sendTarget(), (overlay = !overlay)]"
          >
            <template v-slot:append>
              <v-btn
                x-large
                icon
                @click="[sendTarget(), (overlay = !overlay)]"
                style="margin-right: -10px"
                :disabled="!isValid"
                ><v-icon>mdi-magnify</v-icon>
              </v-btn>
            </template>
          </v-text-field>
        </v-layout>
      </v-flex>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";

let url = "http://localhost:8000/api/book/"; // drf server addr
export default {
  data: () => {
    return {
      isValid: false,
      target: "",
      books: [],
      overlay: false,
      custom_rules: [
        (v) => /^[가-힣 ]*$/.test(v) || "Keyword must korean",
        (v) => !/\s/.test(v) || "Please enter only one word",
      ],
    };
  },
  methods: {
    sendTarget: function () {
      axios
        .post(url + "predict/", { target: this.target })
        .then((response) => {
          console.log(response.data);
          this.books = response.data;
          this.overlay = false;
          this.$router
            .push({
              name: "Predict",
              params: { predictedBooks: this.books },
              query: { str: this.target },
            })
            .catch((err) => {
              // Ignore the vuex err regarding  navigating to the page they are already on.
              if (
                err.name !== "NavigationDuplicated" &&
                !err.message.includes(
                  "Avoided redundant navigation to current location"
                )
              ) {
                // But print any other errors to the console
                console.log(err);
              }
            });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.searchbox {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto;
}
.bookItem {
  padding: 15px;
  margin: 10px;
}
.bookList {
  margin: 30px 0px 30px 0px;
}
.textfield {
  width: 586px;
}
</style>