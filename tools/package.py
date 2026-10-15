#!/usr/bin/env python3
"""Package the archive; retain RISC OS comma filetype suffixes."""
from zipfile import ZipFile, ZIP_DEFLATED
from verify import ROOT, verify

verify()
dist = ROOT / 'dist'
dist.mkdir(exist_ok=True)
dest = dist / 'blockdriver-serial.zip'
excluded = {'.git', 'build', 'dist', '__pycache__', '.DS_Store'}
with ZipFile(dest, 'w', compression=ZIP_DEFLATED) as archive:
    for path in sorted(ROOT.rglob('*')):
        relative = path.relative_to(ROOT)
        if path.is_file() and not any(part in excluded for part in relative.parts):
            archive.write(path, 'blockdriver-serial/' + relative.as_posix())
with ZipFile(dest) as archive:
    assert archive.testzip() is None
print(dest)
