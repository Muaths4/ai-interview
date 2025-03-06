<script setup lang="ts">
import { ref } from "vue";
import PredictionHistory from "@/components/PredictionHistory.vue";

const selectedFile = ref<File | null>(null);
const predictions = ref<{ image: string; result: string; accuracy: number }[]>([]);

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    selectedFile.value = target.files[0];
  }
};

const predict = () => {
  if (selectedFile.value) {
    console.log("Predicting for:", selectedFile.value.name);

    // Simulated Prediction
    const fakePrediction = {
      image: URL.createObjectURL(selectedFile.value), // Temporary preview
      result: "0066",
      accuracy: 97,
    };
    predictions.value.unshift(fakePrediction);
  }
};
</script>

<template>
  <div class="min-h-screen bg-black text-white flex flex-col items-center p-8">
    <div class="mt-10 w-full max-w-2xl p-6 bg-gray-800 rounded-xl shadow-lg">
      <h2 class="text-lg font-semibold mb-4">Prediction Page</h2>

      <div class="border border-gray-600 p-4 rounded-lg flex justify-between items-center">
        <label class="text-gray-300">Insert image to predict</label>
        <input type="file" class="hidden" id="fileInput" @change="handleFileUpload" />
        <label for="fileInput" class="cursor-pointer bg-gray-700 text-gray-300 px-4 py-2 rounded">
          {{ selectedFile ? selectedFile.name : "File input" }}
        </label>
      </div>

      <div class="mt-4 flex justify-end">
        <UButton color="red" variant="solid" @click="predict">Predict</UButton>
      </div>
    </div>

    <!-- Using the PredictionHistory Component -->
    <PredictionHistory v-if="predictions.length > 0" :predictions="predictions" />
  </div>
</template>
