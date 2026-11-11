"""Session cookies and invoice downloads.

Invoices live under INVOICE_DIR, one folder per customer.
"""

from __future__ import annotations

import base64
import os
import pickle
import subprocess

INVOICE_DIR = "/srv/shop/invoices"


def load_session(cookie_value: str) -> dict:
    """Decode the session the browser sent back."""
    return pickle.loads(base64.b64decode(cookie_value))


def read_invoice(file_name: str) -> bytes:
    """Return the invoice PDF the customer asked for."""
    with open(os.path.join(INVOICE_DIR, file_name), "rb") as f:
        return f.read()


def archive_invoices(customer_id: str) -> str:
    """Zip a customer's invoices for download and return the archive path."""
    target = f"/tmp/invoices-{customer_id}.zip"
    subprocess.run(f"zip -r {target} {INVOICE_DIR}/{customer_id}", shell=True, check=True)
    return target
