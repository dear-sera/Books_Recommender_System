<template>
  <v-container fluid>
    <v-card elevation="11">
      <v-card
        class="mb-2"
        tile
        v-for="predictedBook in predictedBooks"
        :key="predictedBook.id"
      >
        <v-row shrink>
          <v-col cols="auto">
            <v-img
              :src="predictedBook.src"
              width="150"
              height="230"
              class="ml-3 elevation-2"
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="gray lighten-3"
                  ></v-progress-circular>
                </v-row> </template
            ></v-img>
          </v-col>
          <v-col>
            <v-row>
              <v-col class="pb-0">
                <v-card-title class="font-weight-bold">{{
                  predictedBook.title
                }}</v-card-title>
              </v-col>
              <v-col cols="auto" class="pr-15">
                <v-card-title
                  class="text-right text--secondary font-weight-light"
                  style="font-size: 14px"
                  >{{ predictedBook.category }}</v-card-title
                >
              </v-col>
            </v-row>
            <v-card-subtitle class="pt-0">{{
              predictedBook.author
            }}</v-card-subtitle>
            <p class="multiLine">{{ predictedBook.summary }}</p>
          </v-col>
        </v-row>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "Predict",
  props: {
    predictedBooks: Array,
  },
};
</script>
<style>
.multiLine {
  font-size: 0.8em;
  width: auto;
  padding-left: 16px;
  padding-right: 35px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
</style>