<template>
  <form class="space-y-6" @submit.prevent="handleSubmit">
    <FormInput
      id="username"
      label="Username"
      v-model="form.username"
      type="text"
      required
    />

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
      :password-rules="passwordRules"
      :show-validation="true"
      :toggleable="true"
      @input="handlePasswordInput"
    />

    <PasswordInput
      id="confirmPassword"
      label="Confirm Password"
      v-model="form.confirmPassword"
      @input="validatePasswordMatch"
    />

    <div v-if="passwordMismatch" class="mt-1 text-sm text-red-600">
      Passwords do not match
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
        {{ loading ? 'Creating account...' : 'Create account' }}
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import FormInput from './FormInput.vue'
import PasswordInput from './PasswordInput.vue'

const router = useRouter()
const userStore = useUserStore()
const { passwordRules, validatePassword, isPasswordValid } = usePasswordValidation()

const form = reactive({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
})

const loading = ref(false)
const error = ref('')
const passwordMismatch = ref(false)

const handlePasswordInput = (value: string) => {
  validatePassword(value)
  validatePasswordMatch()
}

const validatePasswordMatch = () => {
  passwordMismatch.value = form.password !== form.confirmPassword
}

const isFormValid = computed(() => {
  return (
    form.username &&
    form.email &&
    form.password &&
    form.confirmPassword &&
    isPasswordValid.value &&
    !passwordMismatch.value
  )
})

const handleSubmit = async () => {
  if (!isFormValid.value) {
    error.value = 'Please fix all validation errors before submitting'
    return
  }
  
  loading.value = true
  error.value = ''

  try {
    await userStore.createUser({
      username: form.username,
      email: form.email,
      password: form.password,
    })
    await router.push('/')
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'An error occurred'
  } finally {
    loading.value = false
  }
}
</script> 