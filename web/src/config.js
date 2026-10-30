// Runtime configuration. Secrets come from the environment, never from source.

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
    apiKey: required("PAYMENTS_API_KEY"),
  };
}
