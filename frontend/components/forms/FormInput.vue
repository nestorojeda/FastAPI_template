<template>
  <div>
    <label :for="id" class="block text-sm font-medium text-gray-700">
      {{ label }}
    </label>
    <div class="mt-1">
      <input
        :id="id"
        :value="model"
        :type="type"
        :required="required"
        class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        @input="handleInput"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const model = defineModel()

defineProps<{
  id: string
  label: string
  type?: string
  required?: boolean
}>()

const handleInput = (event: Event) => {
  model.value = (event.target as HTMLInputElement).value
}
</script> 