export function formatRupees(cents) {
  return `₹${(cents / 100).toFixed(2)}`;
}
