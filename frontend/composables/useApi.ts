export const useApi = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const apiFetch = async <T>(
    endpoint: string,
    options: Parameters<typeof useFetch>[1] = {}
  ) => {
    const apiKey = useCookie('api_key')
    const headers = {
      ...(apiKey.value && { 'X-API-Key': apiKey.value }),
      ...options.headers,
    }

    return await useFetch<T>(endpoint, {
      baseURL: apiBase,
      ...options,
      headers,
      immediate: false,
    })
  }

  return {
    apiFetch,
  }
} 