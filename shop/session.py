"""Session cookies and invoice downloads."""

from __future__ import annotations

import base64
import os
import pickle

INVOICE_DIR = "/srv/shop/invoices"


def load_session(cookie_value: str) -> dict:
    """Decode the session the browser sent back."""
    return pickle.loads(base64.b64decode(cookie_value))


def read_invoice(file_name: str) -> bytes:
    """Return the invoice PDF the customer asked for."""
    with open(os.path.join(INVOICE_DIR, file_name), "rb") as f:
        return f.read()
