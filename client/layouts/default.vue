<template>
  <header>
    <nav class="navbar">
      <!-- Logo on the left -->
      <div class="logo">
        <img src="https://cdn-icons-png.flaticon.com/512/8618/8618872.png" alt="Logo" />
      </div>
      
      <!-- Title in the middle -->
      <div class="title">
        <h1>7 Segment Prediction</h1>
      </div>

      <!-- Buttons on the right -->
      <div class="buttons">
        <NuxtLink to="/" class="button">Home</NuxtLink>
        <NuxtLink to="/predict" class="button">Predict</NuxtLink>
      </div>
    </nav>
  </header>
  <main>
    <slot />
  </main>
</template>

<style scoped>
/* Styling for the navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 15px;
  background-color:rgb(0, 0, 0);
  color: white;
}

.logo img {
  height: 75px;
}

.title h1 {
  font-size: 30px;
  margin: 0;
}

.buttons {
  display: flex;
  gap: 20px;
}

.button {
  padding: 20px 30px;
  background-color:rgb(0, 110, 255);
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

.button:hover {
  background-color: #166bda;
}
</style>
