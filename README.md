# Serial block drivers and Serial Port / Atomwide hardware driver

Original RISC OS serial driver sources by Hugo Fiennes, recovered from an Acorn Risc PC development hard disk. This follows the layout of [blockdriver-pipe](https://github.com/hfiennes/blockdriver-pipe): each BASIC source has its original tokenised `,ffb` file and a readable `.bas.txt` listing.

| Source | Description | Source header |
| --- | --- | --- |
| [Internal](Internal.bas.txt) | Internal serial port, Acorn and PC wiring variants | 1.20, 2 October 1996 |
| [Dummy](Dummy.bas.txt) | Null serial device | 1.02, 16 August 1994 |
| [SP_Dual](SP_Dual.bas.txt) | Block-driver interface to Serial Port / Atomwide 1/2/3-port cards, Acorn and PC cable variants | 1.14, 9 January 1997 |
| [Serial](Serial.bas.txt) | Underlying serial-card hardware module, including Atomwide issue 1/2 cards | 0.55, 10 August 1998 |

The BASIC programs contain inline ARM assembler and save their own assembled outputs. `Serial` supplies the `SPSerial_*` SWIs used by `SP_Dual`; it is a separate hardware module, rather than another block driver.

## Contents

- `Internal,ffb`, `Dummy,ffb`, `SP_Dual,ffb`, `Serial,ffb`: byte-for-byte original BASIC files. The accompanying `.bas.txt` files are listings for reading on GitHub.
- [`!SerialDev/`](!SerialDev/): original `!Boot`, `!Run` and `!Sprites`, with recovered binaries for Internal, InternalPC, Dummy, SP_Dual and SP_DualPC. Other drivers from the original application have been omitted.
- [`BlockSpec.txt`](BlockSpec.txt): original block-driver specification, revision 12, 11 June 1996.
- [`docs/Changes.txt`](docs/Changes.txt) and [`docs/DriverNrs.txt`](docs/DriverNrs.txt): original revision history and driver-number assignments.
- [`examples/`](examples/): original BASIC client example and C interface/header files. The C example references an external `os.h`; that dependency is not included.
- [`SerialModules/`](SerialModules/): recovered serial-card modules and slot-specific variants, including the original Hardcoded notes.
- [`provenance.json`](provenance.json): original paths, load/execute addresses, attributes, lengths and SHA-256 hashes for every preserved original file.

The comma suffix records the RISC OS filetype: `ffb` BASIC, `ffa` Module, `ffd` Data, `feb` Obey, `ff9` Sprite, `fff` Text. Restore these filetypes and remove the suffixes when transferring to RISC OS if your transfer tool does not do so automatically. In particular, the application must contain files named `!Boot`, `!Run` and `!Sprites` on RISC OS.

## Binary provenance

The block-driver binaries were recovered from the adjacent `$.Cdev.Seven.!SerialDev` application. Their embedded versions agree with the constants emitted by the source: Internal/InternalPC 1.19, Dummy 1.02, SP_Dual/SP_DualPC 1.14. Internal's source comment says 1.20, but its actual version word still says 1.19; both have been preserved unchanged. Matching version words do not establish a byte-for-byte source/binary match.

The recovered `!Serial0`–`!Serial3` modules identify themselves as **0.55 (03 Apr 1998)**, while `Serial` explicitly sets its build date to **10 Aug 1998**. These are historical binaries, not verified builds of the included source. `!Serial2` identifies itself as the Atomwide issue 1/2 variant. No source has been rebuilt or tested on hardware as part of this recovery.

See [BUILD.md](BUILD.md) for the original build arrangement and packaging commands.

## Recovery

Sources came from `$.Cdev.Seven.Driver` and `$.Projects.Serial`. File contents and Acorn metadata are retained in this repository; the disk image itself is not included. Text listings were generated with [riscos-basic-detokenise](https://github.com/gerph/riscos-basic-detokenise), using `bastotxt -i INPUT -o OUTPUT`.

Original copyright and distribution statements are retained. The specification describes the standard as public domain and the supplied drivers as freely distributable. No new blanket license has been added to the recovered collection.
