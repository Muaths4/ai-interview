<script setup lang="ts">
import { defineProps } from "vue";
import PredictionEntry from "./PredictionEntry.vue";

const props = defineProps<{ 
  predictions: { image: string; result: string; accuracy: number }[];
}>();
</script>

<template>
  <div class="mt-10 w-full max-w-4xl p-6 bg-gray-800 rounded-xl shadow-lg">
    <h2 class="text-lg font-semibold mb-4">Prediction History</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
        <PredictionEntry v-for="prediction in predictions" :image="prediction.image" :result="prediction.result" :accuracy="prediction.accuracy" />

    </div>
  </div>
</template>