# Instructor demos

`windows-x64/` contains the original Windows client/server demo executables and
their sample images. These files are local references, excluded from Git.
After cloning elsewhere, obtain `windows-x64.zip` from Section 3.3 of the assignment
on Canvas and extract its `win64` contents here as `windows-x64/`.

From the project root, open two PowerShell terminals:

```powershell
# Terminal 1
cd demos\windows-x64
.\ImageDescriptionServerDemo.exe
```

```powershell
# Terminal 2
cd demos\windows-x64
.\ImageDescriptionClientDemo.exe 127.0.0.1 18333
```

The demo uses a fixed description, not the real AI model. Stop its server before
starting the student server on the same port. Do not submit these executables.
