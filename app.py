"""Run the complete, tested project bundled alongside this cloud entrypoint."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import runpy
import sys
import tempfile
import zipfile


archive = Path(__file__).resolve().with_name("project-source.zip")
source_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
source_root = Path(tempfile.gettempdir()) / f"modelbench-source-{source_hash}"

if not source_root.is_dir():
    # Extract into a staging directory, then publish it atomically so concurrent
    # visitor sessions cannot observe an incomplete source tree.
    with tempfile.TemporaryDirectory(prefix="modelbench-unpack-") as staging:
        with zipfile.ZipFile(archive) as bundle:
            bundle.extractall(staging)
        try:
            os.rename(Path(staging) / "AI-Model-Evaluation", source_root)
        except OSError:
            if not source_root.is_dir():
                raise

# Drop imports from older source bundles after a source update in a live server.
for name, module in list(sys.modules.items()):
    filename = str(getattr(module, "__file__", "") or "")
    if name.split(".")[0] in {"database", "evaluation", "models"}:
        if "modelbench-source-" in filename and not filename.startswith(str(source_root) + os.sep):
            del sys.modules[name]

if str(source_root) not in sys.path:
    sys.path.insert(0, str(source_root))
runpy.run_path(str(source_root / "app.py"), run_name="__main__")
