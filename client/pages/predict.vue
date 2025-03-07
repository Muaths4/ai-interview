<script setup lang="ts">
import { ref } from "vue";
import PredictionHistory from "@/components/PredictionHistory.vue";
import type { PredictionEntryItem } from "~/components/PredictionEntry.vue";

export interface PredictionResponse {
    class: number;
    confidence: number;
}

const selectedFile = ref<File | null>(null);
const predictionHistory = ref<PredictionEntryItem[]>([]);

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    selectedFile.value = target.files[0];
  }
};

const predict = async () => {
  if (!selectedFile.value) {
    console.error("No file selected");
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await fetch("http://127.0.0.1:8000/predict/", {
      method: "POST",
      body: formData,
      headers: {
        Accept: "application/json",
      },
    });

    const data: PredictionResponse[] = await response.json();
    console.log("Full API Response:", data);

    // Check for predictions in response
    if (!data || data.length === 0) {
      console.warn("No predictions found!");
      return;
    }

    // Generate a temporary URL for the uploaded image
    const imageUrl = URL.createObjectURL(selectedFile.value);

    const finalResult = data.map(prediction => prediction.class)
    const confidenceLevels = data.map(prediction => prediction.confidence)

    const finalConfidence = confidenceLevels.reduce((accumulator, currentValue) => accumulator + currentValue, 0) / 4


    const newPrediction: PredictionEntryItem = { image: imageUrl, result: `${finalResult.join("")}`, confidence: parseFloat(((finalConfidence) * 100).toFixed(2)) }

    // Add new predictions to the top of the list
    predictionHistory.value.unshift(newPrediction);
  } catch (error) {
    console.error("Error predicting:", error);
  }
};
</script>

<template>
  <div class="min-h-screen bg-black text-white flex flex-col items-center p-8">
    <div class="mt-10 w-full max-w-2xl p-6 bg-gray-800 rounded-xl shadow-lg">
      <h2 class="text-lg font-semibold mb-4">Prediction Page</h2>

      <div class="border border-gray-600 p-4 rounded-lg flex justify-between items-center">
        <label class="text-gray-300">Insert image to predict</label>
        <input type="file" class="hidden" id="fileInput" @change="handleFileUpload" accept="image/*" />
        <label for="fileInput" class="cursor-pointer bg-gray-700 text-gray-300 px-4 py-2 rounded">
          {{ selectedFile ? selectedFile.name : "File input" }}
        </label>
      </div>

      <div class="mt-4 flex justify-end">
        <UButton color="red" variant="solid" @click="predict">Predict</UButton>
      </div>
    </div>
    <!-- Using the PredictionHistory Component -->
    <PredictionHistory v-if="predictionHistory.length > 0 " :predictions="predictionHistory" />
  </div>
</template>
