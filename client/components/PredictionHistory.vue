<script setup lang="ts">
import { defineProps } from "vue";
import PredictionEntry, { type PredictionEntryItem } from "./PredictionEntry.vue";

defineProps<{ 
  predictions: PredictionEntryItem[];
}>();
</script>

<template>
  <div class="mt-10 w-full max-w-4xl p-6 bg-gray-800 rounded-xl shadow-lg">
    <h2 class="text-lg font-semibold mb-4">Prediction History</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">

      <PredictionEntry 
        v-for="(prediction, index) in predictions" 
        :key="index"
        :image="prediction.image" 
        :result="prediction.result" 
        :confidence="prediction.confidence"
      />
    </div>
  </div>
</template>
