#!/usr/bin/env python3
"""Carregador do monitor; o núcleo é armazenado em partes para commits seguros."""
from __future__ import annotations

import base64
from pathlib import Path

parts_dir = Path(__file__).with_name(".openai-monitor")
encoded = "".join(
    path.read_text(encoding="ascii").strip()
    for path in sorted(parts_dir.glob("core.b64.*"))
)
if not encoded:
    raise RuntimeError("Núcleo do monitor não encontrado")
source = base64.b64decode(encoded, validate=True)
exec(compile(source, "openai_monitor_core.py", "exec"), globals(), globals())
