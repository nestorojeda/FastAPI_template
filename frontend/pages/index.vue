<template>
  <div class="min-h-screen bg-gray-100">
    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div v-if="userStore.user" class="bg-white overflow-hidden shadow rounded-lg">
          <div class="px-4 py-5 sm:p-6">
            <h1 class="text-2xl font-semibold text-gray-900">
              Welcome, {{ userStore.user.username }}!
            </h1>
            <div class="mt-4">
              <button
                @click="userStore.logout"
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
        <div v-else class="bg-white overflow-hidden shadow rounded-lg">
          <div class="px-4 py-5 sm:p-6">
            <h1 class="text-2xl font-semibold text-gray-900">
              Welcome to FastAPI Template
            </h1>
            <div class="mt-4 space-x-4">
              <NuxtLink
                to="/register"
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Register
              </NuxtLink>
              <NuxtLink
                to="/login"
                class="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                Login
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const userStore = useUserStore()

// Try to get current user if API key exists
const apiKey = useCookie('api_key')
if (apiKey.value && !userStore.user) {
  userStore.getCurrentUser().catch(() => {
    // If getting current user fails, clear the API key
    apiKey.value = null
  })
}
</script> 