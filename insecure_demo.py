"""INTENTIONALLY INSECURE — a target for SAST scanners (Bandit, Semgrep).

Nothing here is imported by the running app; it exists so the scanners Aegis
generates have real findings to report. Do not copy any of this into real code.
"""

from __future__ import annotations

import hashlib
import os
import pickle
import subprocess

import yaml

# Hardcoded secrets — secret scanners (Gitleaks, TruffleHog) should flag these.
# Deliberately generic (not a real provider format) so GitHub push protection
# does not block the commit, while pattern/entropy scanners still catch them.
API_KEY = "a3f8b1c9d7e2f4a6b8c0d2e4f6a8b0c2e1d3f5a7"  # noqa
DB_PASSWORD = "SuperSecret123!"  # noqa


def run_command(user_input: str) -> bytes:
    # B602: subprocess with shell=True and untrusted input -> command injection.
    return subprocess.check_output("echo " + user_input, shell=True)  # noqa: S602


def load_config(raw: str) -> object:
    # B506: yaml.load without SafeLoader -> arbitrary object construction.
    return yaml.load(raw)  # noqa


def deserialize(blob: bytes) -> object:
    # B301: pickle of untrusted data -> arbitrary code execution.
    return pickle.loads(blob)  # noqa


def weak_hash(password: str) -> str:
    # B324: MD5 for a password digest -> broken hashing.
    return hashlib.md5(password.encode()).hexdigest()  # noqa


def evaluate(expr: str) -> object:
    # B307: eval on untrusted input.
    return eval(expr)  # noqa


def render_temp() -> str:
    # B108: predictable temp path.
    return os.path.join("/tmp", "session.tmp")  # noqa
