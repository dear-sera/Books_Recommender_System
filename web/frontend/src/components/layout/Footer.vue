<template>
  <v-layout align-center justify-center fill-width class="mt-16">
    <v-footer dark padless style="max-width: 1185px">
      <v-card flat tile class="zeroopacity white--text text-center">
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4 white--text"
            icon
          >
            <v-icon size="24px">
              {{ icon }}
            </v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quidem dicta
          amet voluptas exercitationem eos autem, soluta qui quaerat rem velit
          ea natus sapiente ab repellendus maxime nostrum ut dolore cum. Lorem
          ipsum dolor, sit amet consectetur adipisicing elit. Quidem dicta amet
          voluptas exercitationem eos autem, soluta qui quaerat rem velit ea
          natus sapiente ab repellendus maxime nostrum ut dolore cum. Lorem
          ipsum dolor, sit amet consectetur adipisicing elit. Quidem dicta amet
          voluptas exercitationem eos autem, soluta qui quaerat rem velit ea
          natus sapiente ab repellendus maxime nostrum ut dolore cum.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>천김박조심</strong>
        </v-card-text>
      </v-card>
    </v-footer></v-layout
  >
</template>

<script>
export default {
  data: () => ({
    icons: ["mdi-facebook", "mdi-twitter", "mdi-linkedin", "mdi-instagram"],
  }),
};
</script>

<style>
footer,
footer * {
  background-color: #fffcf000 !important;
}
</style>