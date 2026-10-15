#!/usr/bin/env python3
"""Stage unchanged originals with all historical output directories present."""
from pathlib import Path
import shutil
from verify import ROOT, verify

verify()
out = ROOT / 'build'
if out.exists():
    raise SystemExit('build/ already exists; move it aside before staging again.')
seven = out / 'Seven'
shutil.copytree(ROOT / '!SerialDev', seven / '!SerialDev')
driver = seven / 'Driver'
driver.mkdir()
for name in ('Internal', 'Dummy', 'SP_Dual'):
    shutil.copy2(ROOT / (name + ',ffb'), driver / (name + ',ffb'))
for target in (driver / 'spec' / '!SerialDev', seven / '!Arcterm',
               seven / 'DistribA' / '!Arcterm'):
    for name in ('Internal', 'InternalPC', 'Dummy', 'SP_Dual', 'SP_DualPC'):
        (target / 'Modules' / name).mkdir(parents=True)
serial = out / 'Serial'
(serial / 'Hardcoded').mkdir(parents=True)
shutil.copy2(ROOT / 'Serial,ffb', serial / 'Serial,ffb')
print('Staged build/; restore filetypes on RISC OS and follow BUILD.md.')
