# Online Image Description System — Report Draft

Status: outline only. Complete this document using actual implementation details
and screenshots, then export it to PDF. Do not submit this outline as the report.
All submitted text, code comments, prompts, and error messages must be in English.

## 1. Members and environment

| Name | Student ID |
| --- | --- |
| TODO | TODO |

- Operating system: TODO
- Python version used for the server and client: TODO (record the actual output)
- Client language: Python, standard library only
- Other relevant tool versions: TODO

## 2. Setup and execution

Use the README setup instructions as a starting point. Record the exact commands
tested on your machine, including the final filenames containing all member IDs.

- Dependency setup: TODO
- AI component check: TODO
- Server command: TODO
- Client command with IPv4 address and port: TODO
- Compilation: not required for the planned Python client

## 3. Implementation

- Explain the five completed server socket functions: TODO
- Explain client command handling over a persistent connection: TODO
- Explain UTF-8 byte lengths, complete reads/writes, and message ordering: TODO
- Explain file validation, download safety, and error handling: TODO

## 4. Results from our own runs

Store screenshots in `docs/screenshots/`. Show the actual commands and output.
Do not claim a test passed before running it.

| Scenario | Screenshot / evidence | Result |
| --- | --- | --- |
| Server READY and client connection | TODO | Not run |
| UPLOAD and LIST before description | TODO | Not run |
| DESCRIBE with real AI and cached status | TODO | Not run |
| DOWNLOAD and matching SHA-256 hashes | TODO | Not run |
| Existing download destination is preserved | TODO | Not run |
| REMOVE and subsequent LIST | TODO | Not run |
| Unknown command, missing file, invalid image, invalid ID | TODO | Not run |
| Connection remains usable after recoverable errors | TODO | Not run |
| Multiple clients share images; QUIT closes one client | TODO | Not run |

## 5. Limitations

Describe any remaining issues honestly: TODO.

Export the completed report as `Report_<student_IDs>.pdf` for Canvas.
