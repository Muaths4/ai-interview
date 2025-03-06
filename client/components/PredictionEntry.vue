<script setup lang="ts">
import { defineProps } from "vue";
const props = defineProps<{
image: string
result: string
accuracy: number
}>()
</script>
<template>
    <div
        class="bg-gray-900 p-4 rounded-lg text-center"
      >
        <img :src="image" alt="Prediction" class="w-full h-24 object-contain rounded" />
        <p class="mt-2 text-lg font-bold">{{result }}</p>
        <p class="text-gray-400">Accuracy: {{ accuracy }}%</p>
      </div>
</template>