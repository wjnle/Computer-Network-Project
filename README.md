# Online Image Description System

CS3201 2026 programming assignment by NGUYEN, Phat Dat (59911219) and LE, Win (59271285).

The five server socket functions and all six client commands are implemented. The client uses only the Python standard library. The provided server helper and Parts 2-4 are unchanged.

## Setup and run

Keep the course setup scripts, dependency files, test images and model folder together. On Windows, open PowerShell in the project root:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "cmd.exe /d /c .\setup_env.bat"
```

Model weights are excluded from Git. If you cloned this repository instead of using the complete course ZIP, restore them with:

```powershell
.\.venv\Scripts\python.exe ImageDescriptionServer.py --download-model
```

Check the model, then start the server:

```powershell
.\.venv\Scripts\python.exe ImageDescriptionServer.py --check-ai .\test_images\cat.jpg
.\.venv\Scripts\python.exe ImageDescriptionServer.py
```

After READY appears, open another PowerShell window in the same folder:

```powershell
.\.venv\Scripts\python.exe ImageDescriptionClient.py 127.0.0.1 18333
```

For mock mode, start the server with `--backend mock`. For macOS/Linux, use `bash setup_env.sh` and `.venv/bin/python`.

Enter each command and its values on separate lines. Commands: UPLOAD, LIST, DESCRIBE, DOWNLOAD, REMOVE and QUIT. Ctrl+C stops the server.

## Checks and report

Mock tests covered message framing, fragmented reads, invalid headers, disconnects, command errors, download integrity and shared client state. Real AI runs on Windows with Python 3.11.15 covered all six commands, SHA-256 matching, error handling, overwrite prevention and two clients sharing images. The report includes screenshots from those runs. Connections between two physical computers have not been tested.

## Files for review and Canvas

The `submission` folder contains the latest named server, client, PDF report and editable Word report. To run the named server and client, copy them into the project root beside the supplied model and setup files, then use the commands in the report.

Both members should review the files and join the same existing Canvas group. One member submits only the two named Python files and the PDF separately. The Word report is for editing, not Canvas submission. Do not submit model weights, runtimes, setup logs or executables.

Deadline: 11 November 2026, 23:59 Hong Kong time.
