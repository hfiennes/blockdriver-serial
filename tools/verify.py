#!/usr/bin/env python3
"""Verify preserved file contents and structural metadata; no execution."""
from pathlib import Path
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parents[1]

def verify():
    entries = json.loads((ROOT / 'provenance.json').read_text())
    for item in entries:
        data = (ROOT / item['file']).read_bytes()
        assert len(data) == item['size'], item['file']
        assert hashlib.sha256(data).hexdigest() == item['sha256'], item['file']
        if item['filetype'] == 'ffb':
            pos = 0
            while data[pos:pos + 2] != b'\r\xff':
                assert data[pos] == 13 and data[pos + 3] >= 4, item['file']
                pos += data[pos + 3]
                assert pos < len(data), item['file']
            assert pos + 2 == len(data), item['file']
    for name, version in [('Internal', 0x10013), ('InternalPC', 0x10013),
                          ('Dummy', 0x10002), ('SP_Dual', 0x1000e), ('SP_DualPC', 0x1000e)]:
        data = (ROOT / '!SerialDev' / 'Modules' / name / 'Driver,ffd').read_bytes()
        assert struct.unpack_from('<I', data, 0xc0)[0] == version, name
    print(f'Verified {len(entries)} originals, BASIC framing and block-driver version words.')

if __name__ == '__main__':
    verify()
