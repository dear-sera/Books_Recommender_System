import Vue from "vue";
import VueRouter from "vue-router";
import BestList from "./views/BestList.vue";
import PredictedList from "./views/PredictedList.vue";
import UpdateBooks from "./views/UpdateBooks.vue"

Vue.use(VueRouter)

export default new VueRouter({
    mode: "history",
    routes: [
        { path: "/", name: 'Main', component: BestList },
        { path: "/predict", name: 'Predict', component: PredictedList, props: true },
        { path: "/update", name: 'Update', component: UpdateBooks },
    ]
})