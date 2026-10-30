export interface CartLine {
  sku: string;
  qty: number;
  priceCents: number;
}

export function cartTotal(lines: CartLine[]): number {
  return lines.reduce((sum, l) => sum + l.qty * l.priceCents, 0);
}
