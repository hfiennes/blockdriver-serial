# Building and packaging

## Original build environment

These are BBC BASIC programs using the RISC OS ARM assembler. They are not host C or standalone assembler sources. Use the tokenised `,ffb` originals with their RISC OS filetypes restored. The listings are reference copies.

The sources contain their assembly routines and do not load separate assembler include files. `SP_Dual` uses symbolic `XSPSerial_*` SWI names, so the assembler needs those names registered by a suitable serial-driver module. Do not install an arbitrary card-specific module on unrelated hardware merely to resolve names. This repository does not include a RISC OS emulator or cross-build toolchain.

The original output paths also refer to ARCterm and distribution directories. The helper below creates those paths in a separate staging directory so the originals can be used unchanged:

```sh
python3 tools/prepare_build.py
```

Transfer `build/` to RISC OS, restoring comma filetypes throughout. It contains:

```
Seven/
  !SerialDev/                  main block-driver output application
  !Arcterm/Modules/...          historical secondary output destinations
  DistribA/!Arcterm/Modules/...
  Driver/
    Internal                   BASIC originals
    Dummy
    SP_Dual
    spec/!SerialDev/Modules/... historical secondary destinations
Serial/
  Serial                       BASIC original
  Hardcoded/                   slot-specific module output directory
```

The ARCterm paths are output directories only, not complete applications. In the transferred `Seven` directory, run the staged `!SerialDev` once to set `SerialDev$Path` to that staged copy. Then set the current directory to `Seven.Driver`, start BASIC and build each source with `LOAD "Internal"` followed by `RUN`; repeat for `Dummy` and `SP_Dual`. Internal and SP_Dual each generate both wiring variants. Running these programs overwrites the output drivers in the staged tree.

For the hardware module, use the staged `Serial` directory as the current directory. In BASIC, `LOAD "Serial"` and `RUN`. It saves `!SerialN` modules and `Hardcoded.IssN_SlotN` variants, setting their filetype to Module.

### Preserved source quirks

- Internal's header says 1.20 but its emitted version word is 1.19.
- Serial sets `Create$` to 10 August 1998 after initialising its constants; the historical binaries included here have an earlier date.
- Serial loops `cardt%` from 0 to 5, but its CASE statement defines only cases 0 through 4. Case 5 consequently reuses the state from the preceding iteration. Review this before treating a generated `!Serial5` as a distinct supported card variant. The original program is unchanged.
- The hardware-specific sources use historical ARM/RISC OS conventions; builds and operation on modern RISC OS releases have not been verified.

## Verify preserved files

```sh
python3 tools/verify.py
```

This checks every original against its recorded length and SHA-256, BASIC line framing, and the embedded block-driver version words. It does not assemble code or establish source/binary equivalence.

## Create an archive

```sh
python3 tools/package.py
```

Creates `dist/blockdriver-serial.zip` containing the sources, readable listings, documentation, metadata, tools and recovered application/modules. The ZIP preserves comma filetype suffixes; it does not add Acorn ZIP metadata. Use a transfer/extraction workflow that restores these suffixes as RISC OS filetypes, or set the types manually. `build/`, `dist/`, Git metadata and macOS metadata are excluded. The package contains the recovered binaries; newly staged builds are not automatically substituted.
