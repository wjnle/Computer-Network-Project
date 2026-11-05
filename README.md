# Online Image Description System

Computer Networks programming assignment: an IPv4 TCP server and a terminal client
for uploading images, requesting English descriptions, and retrieving files.
The instructor supplies image management and CPU AI inference. Our work is the
five server socket functions and the complete client.

**Status:** preparation only. The server still has all five original TODOs;
`ImageDescriptionClient.py` is a documentation-only placeholder. Network commands
will work only after implementation. No final report or submission exists yet.

The [assignment handout](docs/assignment.pdf) identifies the course as **CS3201 2026**,
although the original local parent folder is named CS2301. Use the official course
information when completing the report. Deadline: **11 November 2026, 23:59 HKT**.

## 1. Files and folders

```text
.
|-- ImageDescriptionServer.py   # Original server; implement only Part 1 TODOs
|-- ImageDescriptionClient.py   # Our future Python client; currently a placeholder
|-- setup_env.bat               # Original Windows setup script
|-- setup_env.sh                # Original macOS/Linux setup script
|-- requirements.txt            # Main dependency versions
|-- requirements.lock.txt       # Full pinned dependency list used by setup
|-- models/smolvlm-256m/        # AI weights, configuration, model card and licenses
|-- test_images/                # cat.jpg, flower.png, fruit_bowl.jpg and sources
|-- docs/
|   |-- assignment.pdf          # Original Canvas instructions
|   |-- REPORT_TEMPLATE.md      # Report outline; complete and export to PDF later
|   `-- screenshots/            # Evidence from our own runs
|-- demos/                      # Instructions and local instructor Windows demos
|-- submission/                 # Instructions; final named copies go here later
`-- .gitignore                  # Excludes runtime, weights and generated files
```

Setup generates `.tools/` (uv), `.runtime/` (managed Python and cache), `.venv/`
(project interpreter and libraries), and `setup.log` in this root directory.
Keep server, setup scripts, requirements, images, and model together here.
Do not move this project after installing its environment; virtual environments
can contain absolute paths. Existing supplied files were preserved without edits.

## 2. Setup

Run commands from the project root in PowerShell. Internet access and free disk
space for Python, CPU PyTorch, and the model are required. No GPU or paid AI API
is needed. The setup installs **uv 0.10.9** and **Python 3.11.15** locally, so the
machine's existing Python does not need to be replaced.

```powershell
.\setup_env.bat
```

Wait for `Setup complete`. If Windows blocks the uv installer because of its
execution policy, use a temporary PowerShell process:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command 'cmd.exe /d /c .\setup_env.bat'
```

This applies only to that process. Do not edit the supplied setup scripts or
upgrade pinned packages. The main dependencies are torch 2.2.2, transformers
4.49.0, Pillow 10.4.0, NumPy 1.26.4, huggingface-hub 0.29.3, safetensors 0.5.3,
and tokenizers 0.21.4. The lock file also specifies their supporting libraries.

Verify the local environment:

```powershell
.\.venv\Scripts\python.exe --version
.\.tools\uv\uv.exe --cache-dir .\.runtime\uv-cache pip check --python .\.venv\Scripts\python.exe
.\.venv\Scripts\python.exe ImageDescriptionServer.py --check-ai .\test_images\cat.jpg
```

The last command should print an actual image description and does not require
the five socket TODOs to be complete. In VS Code, select
`${workspaceFolder}\.venv\Scripts\python.exe` with **Python: Select Interpreter**.
Activation is optional because commands above use the interpreter directly.

On macOS/Linux, run `bash setup_env.sh`, then use `.venv/bin/python` in place of
`.\.venv\Scripts\python.exe` throughout the commands.

**On a teammate's Windows computer:** Git must be installed first. Clone the repo
into its permanent working location, then install the environment and restore the
pinned model (internet is needed for both setup and model download):

```powershell
git clone https://github.com/wjnle/Computer-Network-Project.git
cd Computer-Network-Project
.\setup_env.bat
.\.venv\Scripts\python.exe ImageDescriptionServer.py --download-model
.\.venv\Scripts\python.exe ImageDescriptionServer.py --check-ai .\test_images\cat.jpg
```

Git includes the model configuration and licenses, but not the approximately
513 MB weights or this computer's Python environment. After these steps the
teammate has the same pinned runtime and model as this machine. Network features
still require completing the server and client code. For macOS/Linux, use the
platform-specific setup and interpreter paths described above.

If setup fails, inspect `setup.log`. For an incompatible existing uv/environment,
or missing/damaged course files, follow the handout's TA guidance. Local setup
status and any installation blocker are recorded in [SETUP_STATUS.md](docs/SETUP_STATUS.md).

## 3. Run after implementing the socket code

First start a mock server for faster network debugging:

```powershell
# Terminal 1
.\.venv\Scripts\python.exe ImageDescriptionServer.py --backend mock
```

Wait for `READY host=0.0.0.0 port=18333`. In another terminal, the planned client
invocation is below; the current placeholder does not implement it yet:

```powershell
# Terminal 2, once the client is implemented
.\.venv\Scripts\python.exe ImageDescriptionClient.py 127.0.0.1 18333
```

For real AI, stop the mock server with Ctrl+C and start:

```powershell
.\.venv\Scripts\python.exe ImageDescriptionServer.py
```

Reconnect the client. On another computer use the server's reachable IPv4 address
instead of `127.0.0.1`. Images and IDs are shared by clients and cleared when the
server restarts. `QUIT` closes only the issuing client's connection.

## 4. Commands and protocol

Enter each command and each subsequent value on separate lines. Follow the exact
`client:` and `server:` prefixes in the handout, including every line of replies.

| Command | Subsequent client input | Result |
| --- | --- | --- |
| `UPLOAD` | Local JPEG/PNG path | Upload original bytes and display assigned ID |
| `LIST` | None | Show IDs, filenames, upload times, and description status |
| `DESCRIBE` | Image ID | Generate a description once, then use its cached value |
| `DOWNLOAD` | Image ID, then local output path | Save original bytes without overwriting a file |
| `REMOVE` | Image ID | Delete image and its cached description |
| `QUIT` | None | Display `OK`, close connection, and exit |

Each socket message has a **10-byte zero-padded ASCII length header**, then its
payload. Count UTF-8 encoded bytes for text. Payload length must be 1–5,242,880
bytes; command text must not exceed 1,024 bytes. Handle partial TCP reads/writes.
`UPLOAD` sends command/filename and image as two messages before reading a reply.
Successful `DOWNLOAD` receives a text reply then a separate image message; errors
have no image message. Finish each exchange before sending another command.

Upload only the basename and original image bytes. Check local file existence,
readability, and the 5 MiB limit before upload. Images must be JPEG/PNG, at most
20 million pixels. The supplied server limits storage to 20 images / 50 MiB.

## 5. Implementation and verification checklist

- [ ] Complete `create_listener`, `accept_client`, `receive_message`,
      `send_message`, and `close_client`; preserve provided helper and Parts 2–4.
- [ ] Implement the Python client using only the standard library.
- [ ] Implement all six commands, persistent TCP, framing, and exact terminal I/O.
- [ ] Check LIST and QUIT first in mock mode; then add UPLOAD, DESCRIBE, REMOVE,
      and DOWNLOAD in the handout's suggested order.
- [ ] Compare original/downloaded bytes, for example with `Get-FileHash` on both
      files; check that existing output files are never overwritten.
- [ ] Check missing/unreadable/oversized uploads, invalid image bytes, invalid
      IDs, unknown commands, and continued use after recoverable errors.
- [ ] Check fragmented messages, malformed headers, truncated messages, and
      disconnect handling.
- [ ] Check cached descriptions, shared image state across multiple clients,
      and QUIT affecting only one connection.
- [ ] Repeat all six commands with the real AI backend; capture our own results.
- [ ] Complete the English report with members, environment, exact run commands,
      and screenshots, then export it to PDF.
- [ ] Follow [submission instructions](submission/README.md), including Canvas
      group registration and filenames containing every member's student ID.

The report is worth 10/100; the remaining marks cover connection setup, message
exchange, the six commands, and basic error handling. GitHub and README do not
replace the required Canvas source-file and PDF submission.

## 6. GitHub and submission boundaries

Keep source, documentation, setup scripts, lock files, sample images, and model
metadata in Git. Keep the approximately 513 MB model weights, local runtimes,
installer logs, demo binaries, and generated submission copies out of Git.
Weights remain available locally and can be restored using `--download-model`.
The original model licenses and image source attribution are retained.

For Canvas submit only completed source/build files and the final PDF, using the
required names. The full development directory is not the submission package.
