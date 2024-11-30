<template>
  <!-- 使用示例 -->
  <div>
    <div>
      <p>style：{{ style }}</p>
      <button v-text="'Left Top'" @click="style = LeftTop" />
      <button v-text="'Left Bot'" @click="style = LeftBot" />
      <button v-text="'Right Top'" @click="style = RighTop" />
      <button v-text="'Right Bot'" @click="style = RighBot" />
      <button v-text="'At Center'" @click="style = AtCentr" />
      <button v-text="'Unset'" @click="style = Unset" />
    </div>
    <div>
      <p>isLeft：{{ isLeft }}</p>
      <button @click="isLeft = false">Right</button>
      <button @click="isLeft = true">Left</button>
    </div>
    <div>
      <p>resolution：</p>
      <input type="number" v-model.lazy="resolution" />
    </div>
    <div>
      <p>width：</p>
      <input type="number" v-model.lazy="width" />
    </div>
    <div>
      <p>height：</p>
      <input type="number" v-model.lazy="height" />
    </div>
    <live2d
      class="live2d"
      v-model:width="width"
      v-model:height="height"
      v-model:resolution="resolution"
      :style="style"
      :api-path="'/vue3-live2d-static-api/indexes'"
      :model="['Potion-Maker/Pio', 'school-2017-costume-yellow']"
      :is-left="isLeft"
      :tips="tips"
    ></live2d>
  </div>
</template>

<script setup lang="ts">
/*
 * 项目中引用包时，将 import 内容替换
 * import live2d from 'vue-live2d'
 */
import live2d from "./index.vue";
import { ref, computed } from "vue";

const Unset = {};
const LeftTop = { position: "fixed", left: 0, top: 0, zIndex: 1 };
const LeftBot = { position: "fixed", left: 0, bottom: 0, zIndex: 1 };
const RighTop = { position: "fixed", right: 0, top: 0, zIndex: 1 };
const RighBot = { position: "fixed", right: 0, bottom: 0, zIndex: 1 };
const AtCentr = computed(() => {
  return {
    position: "fixed",
    left: `calc(50% - ${width.value / 2}px)`,
    top: `calc(50% - ${height.value / 2}px)`,
  };
});

let isLeft = ref(false);
let style = ref<any>(RighBot);
let width = ref(500);
let height = ref(600);
let resolution = ref(3);
let tips = ref({
  mouseover: [
    {
      selector: ".vue-live2d",
      texts: ["Meow"],
    },
  ],
});
</script>

<style>
.live2d {
  margin-right: 1rem;
  margin-left: 1rem;
}
</style>
