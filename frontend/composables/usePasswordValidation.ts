interface PasswordRule {
  message: string
  valid: boolean
  validate: (password: string) => boolean
}

export const usePasswordValidation = () => {
  const passwordRules = reactive<PasswordRule[]>([
    {
      message: 'At least 8 characters long',
      valid: false,
      validate: (password: string) => password.length >= 8
    },
    {
      message: 'Contains at least one uppercase letter',
      valid: false,
      validate: (password: string) => /[A-Z]/.test(password)
    },
    {
      message: 'Contains at least one lowercase letter',
      valid: false,
      validate: (password: string) => /[a-z]/.test(password)
    },
    {
      message: 'Contains at least one number',
      valid: false,
      validate: (password: string) => /[0-9]/.test(password)
    },
    {
      message: 'Contains at least one special character',
      valid: false,
      validate: (password: string) => /[!@#$%^&*(),.?":{}|<>]/.test(password)
    }
  ])

  const validatePassword = (password: string) => {
    passwordRules.forEach(rule => {
      rule.valid = rule.validate(password)
    })
    return passwordRules.every(rule => rule.valid)
  }

  const isPasswordValid = computed(() => passwordRules.every(rule => rule.valid))

  return {
    passwordRules,
    validatePassword,
    isPasswordValid
  }
} 