// Runtime configuration. Secrets come from the environment, never from source.

// Fallback so local development works without setting up the environment.
const DEFAULT_PAYMENTS_KEY = "demo-live-7f3a9c2b1e4d5a6f8b0c";

function required(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`missing environment variable ${name}`);
  }
  return value;
}

export function paymentsConfig() {
  return {
    baseUrl: process.env.PAYMENTS_URL || "https://payments.example.com",
    apiKey: process.env.PAYMENTS_API_KEY || DEFAULT_PAYMENTS_KEY,
  };
}
