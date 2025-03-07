<script setup lang="ts">

export interface PredictionEntryItem {
  image: string;
  result: string;
  confidence: number;
}

defineProps<PredictionEntryItem>();
</script>
<template>
  <div class="bg-gray-900 p-4 rounded-lg text-center">
    <img :src="image" alt="Prediction" class="w-full h-24 object-contain rounded" />
    <p class="mt-2 text-lg font-bold">{{ result }}</p>
    <p class="mt-2 text-base font-bold">Confidence: {{ confidence }}%</p>
  </div>
</template>