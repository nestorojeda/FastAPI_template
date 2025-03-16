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
        const { data, error } = await apiFetch<User & { api_key: string }>('/api/v1/users/', {
          method: 'POST',
          body: userData,
        })

        if (error.value) {
          throw error.value
        }

        if (data.value) {
          const apiKey = useCookie('api_key')
          apiKey.value = data.value.api_key
          this.user = data.value
        }

        return data.value
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
        const { data, error } = await apiFetch<User>('/api/v1/users/me/')

        if (error.value) {
          throw error.value
        }

        if (data.value) {
          this.user = data.value
        }

        return data.value
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
        const { data, error } = await apiFetch<User[]>('/api/v1/users/')

        if (error.value) {
          throw error.value
        }

        return data.value
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