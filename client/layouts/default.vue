<template>
  <header class="border-b bg-black">
    <UContainer>
      <nav class="flex items-center justify-between py-3">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center gap-2">
          <img src="https://cdn-icons-png.flaticon.com/512/8618/8618872.png" alt="Logo" class="h-12 w-auto" />
        </NuxtLink>

        <!-- Title -->
        <h1 class="text-white text-xl font-bold">7 Segment Prediction</h1>

        <!-- Navigation Buttons -->
        <div class="flex items-center gap-4">
          <UButton to="/" color="primary" variant="solid">Home</UButton>
          <UButton to="/predict" color="primary" variant="solid">Predict</UButton>
        </div>
      </nav>
    </UContainer>
  </header>

  <main>
    <slot />
  </main>
</template>