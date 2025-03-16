import { defineStore } from 'pinia'

interface User {
  id: number
  username: string
  email: string
  is_active: boolean
}

interface UserCreate {
  username: string
  email: string
  password: string
}

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null as User | null,
    loading: false,
    error: null as string | null,
  }),

  actions: {
    async createUser(userData: UserCreate) {
      const { apiFetch } = useApi()
      this.loading = true
      this.error = null

      try {
        const response = await apiFetch<User & { api_key: string }>('/api/v1/users/', {
          method: 'POST',
          body: userData,
        })

        if (response.error.value) {
          throw response.error.value
        }

        if (response.data.value) {
          const apiKey = useCookie('api_key')
          apiKey.value = response.data.value.api_key
          this.user = response.data.value
        }

        return response.data.value
      } catch (err) {
        this.error = err instanceof Error ? err.message : 'An error occurred'
        throw err
      } finally {
        this.loading = false
      }
    },

    async getCurrentUser() {
      const { apiFetch } = useApi()
      this.loading = true
      this.error = null

      try {
        const response = await apiFetch<User>('/api/v1/users/me/')

        if (response.error.value) {
          throw response.error.value
        }

        if (response.data.value) {
          this.user = response.data.value
        }

        return response.data.value
      } catch (err) {
        this.error = err instanceof Error ? err.message : 'An error occurred'
        throw err
      } finally {
        this.loading = false
      }
    },

    async listUsers() {
      const { apiFetch } = useApi()
      this.loading = true
      this.error = null

      try {
        const response = await apiFetch<User[]>('/api/v1/users/')

        if (response.error.value) {
          throw response.error.value
        }

        return response.data.value
      } catch (err) {
        this.error = err instanceof Error ? err.message : 'An error occurred'
        throw err
      } finally {
        this.loading = false
      }
    },

    logout() {
      const apiKey = useCookie('api_key')
      apiKey.value = null
      this.user = null
    },
  },
}) 