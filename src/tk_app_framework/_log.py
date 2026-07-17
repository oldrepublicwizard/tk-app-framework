"""Replacement for PatchLogger."""
from __future__ import annotations
import logging

class PatchLogger:
    def __init__(self, *args, **kwargs):
        self._log = logging.getLogger("tk_app_framework")
    def __getattr__(self, name):
        return getattr(self._log, name)
