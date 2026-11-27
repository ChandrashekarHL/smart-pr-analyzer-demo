"""Monthly invoice exports for the accounts team."""

from __future__ import annotations

import os
import subprocess

EXPORT_DIR = "/srv/shop/exports"


def export_month(month: str) -> str:
    """Bundle a month's invoices into one archive and return its path."""
    archive = os.path.join(EXPORT_DIR, f"invoices-{month}.tar.gz")
    subprocess.run(f"tar czf {archive} /srv/shop/invoices/{month}", shell=True, check=True)
    return archive


def download_export(file_name: str) -> bytes:
    """Return an export the accounts team asked for by file name."""
    with open(os.path.join(EXPORT_DIR, file_name), "rb") as f:
        return f.read()
