import { OpenAPI } from '../generated/api'
import { env } from '../config/env'

export function configureOpenApiClient() {
  OpenAPI.BASE = env.apiBaseUrl
  OpenAPI.WITH_CREDENTIALS = false
}
