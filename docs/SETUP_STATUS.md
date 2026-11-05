# Local preparation status

Verified on **5 November 2026** on Windows x64.
This records environment preparation, not completion of the programming assignment.

| Check | Result |
| --- | --- |
| Original course Windows setup | Completed successfully |
| Project-local uv | 0.10.9 |
| Project-local Python | 3.11.15 |
| Locked dependencies | 25 packages installed; compatibility check passed |
| Main library imports | torch 2.2.2+cpu, transformers 4.49.0, Pillow 10.4.0, NumPy 1.26.4 |
| Pinned model integrity | All 13 model files matched the server's SHA-256 manifest |
| Original server, setup scripts, requirements, handout and demo executables | Content hashes unchanged after reorganization |
| Real AI inference on `test_images/cat.jpg` | Passed; output shown below |
| Server socket implementation | Not started; all five original TODOs remain |
| Client implementation | Not started; documentation-only placeholder |
| Network / command tests | Not run; require implementation |
| Report | Outline only; no final PDF |

Actual AI check:

```powershell
.\.venv\Scripts\python.exe ImageDescriptionServer.py --check-ai .\test_images\cat.jpg
```

```text
In this image we can see a cat lying on the floor.
```

The initial installer attempts encountered network and PowerShell execution-policy
errors. Setup completed after network-enabled execution and a process-only policy
override. No permanent execution-policy change was made. The provided setup script
was not edited. Download cache rename warnings were transient; installation and
the final package compatibility check succeeded.

VS Code local settings select the project interpreter for a fresh interpreter
selection and hide `.tools`, `.runtime`, `.venv`, and Python bytecode from Explorer.
If VS Code retained an older interpreter selection, use **Python: Select
Interpreter** and choose `.venv\Scripts\python.exe`. The directories remain on
disk. Local editor settings, runtime files, logs, model weights, and Windows demo
binaries are excluded from Git.

The current machine is ready for coding. A different machine must rerun setup and
restore weights as explained in the main README.
