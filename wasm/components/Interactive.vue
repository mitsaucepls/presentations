<template>
  <div :height=350 :items="items">
    <template v-for="(item, index) in items" :key="index">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Task: {{ item.group_id }} {{ item.submitted_at.timestamp.time.hour }}:{{ item.submitted_at.timestamp.time.min }}:{{ item.submitted_at.timestamp.time.sec }} 🕑
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Data container for tasks
  const items = ref([]);
  setInterval(load, 1000);

  async function api () {
    return axios.get("http://80.158.78.228/api/v1/tasks");
  }

// Infinite scroll loader function
async function load() {
  try {
    // Perform API call
    //const response = await axios.get("http://80.158.78.228/api/v1/tasks");
    const response = await api()
    console.log(...response.data.data)

    // Check if data is present
    //if (response.data && Array.isArray(response.data)) {
     // items.value.push(...response.data);
    //}
    items.value = response.data.data

    // Signal completion to the infinite scroll component
  } catch (error) {
    console.error("Failed to load tasks:", error);
  }
}
</script>
