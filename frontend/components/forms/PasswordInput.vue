<template>
  <div>
    <label :for="id" class="block text-sm font-medium text-gray-700">
      {{ label }}
    </label>
    <div class="mt-1 relative">
      <input
        :id="id"
        :value="model"
        :type="showPassword ? 'text' : 'password'"
        required
        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        @input="handleInput"
      />
      <button
        v-if="toggleable"
        type="button"
        class="absolute inset-y-0 right-0 pr-3 flex items-center"
        @click="showPassword = !showPassword"
      >
        <span class="text-sm text-gray-500">{{ showPassword ? 'Hide' : 'Show' }}</span>
      </button>
    </div>
    <div v-if="showValidation" class="mt-2 space-y-2">
      <div v-for="(rule, index) in passwordRules" :key="index" class="flex items-center text-sm">
        <span
          class="mr-2"
          :class="rule.valid ? 'text-green-500' : 'text-gray-400'"
        >
          {{ rule.valid ? '✓' : '○' }}
        </span>
        <span :class="rule.valid ? 'text-green-600' : 'text-gray-500'">{{ rule.message }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const model = defineModel()

const props = defineProps<{
  id: string
  label: string
  showValidation?: boolean
  toggleable?: boolean
  passwordRules?: Array<{ message: string; valid: boolean }>
}>()

const emit = defineEmits<{
  input: [value: string]
}>()

const showPassword = ref(false)

const handleInput = (event: Event) => {
  const value = (event.target as HTMLInputElement).value
  model.value = value
  emit('input', value)
}
</script> 