<template>
  <form class="space-y-6" @submit.prevent="handleSubmit">
    <FormInput
      id="email"
      label="Email address"
      v-model="form.email"
      type="email"
      required
    />

    <PasswordInput
      id="password"
      label="Password"
      v-model="form.password"
      :toggleable="true"
    />

    <div class="flex items-center justify-between">
      <div class="flex items-center">
        <input
          id="remember-me"
          v-model="form.rememberMe"
          type="checkbox"
          class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
        />
        <label for="remember-me" class="ml-2 block text-sm text-gray-900">
          Remember me
        </label>
      </div>

      <div class="text-sm">
        <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">
          Forgot your password?
        </a>
      </div>
    </div>

    <div v-if="error" class="text-red-600 text-sm">
      {{ error }}
    </div>

    <div>
      <button
        type="submit"
        :disabled="loading || !isFormValid"
        class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        :class="{ 'opacity-50 cursor-not-allowed': loading || !isFormValid }"
      >
        {{ loading ? 'Signing in...' : 'Sign in' }}
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import FormInput from './FormInput.vue'
import PasswordInput from './PasswordInput.vue'

const router = useRouter()
const userStore = useUserStore()

const form = reactive({
  email: '',
  password: '',
  rememberMe: false
})

const loading = ref(false)
const error = ref('')

const isFormValid = computed(() => {
  return form.email && form.password
})

const handleSubmit = async () => {
  if (!isFormValid.value) {
    error.value = 'Please fill in all required fields'
    return
  }
  
  loading.value = true
  error.value = ''

  try {
    // TODO: Implement login functionality in userStore
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simulated delay
    console.log('Login attempt with:', {
      email: form.email,
      password: form.password,
      rememberMe: form.rememberMe
    })
    await router.push('/')
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'An error occurred during sign in'
  } finally {
    loading.value = false
  }
}
</script> 