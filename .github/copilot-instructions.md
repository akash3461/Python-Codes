# Copilot / AI Agent Instructions — 100-Codes-of-Python (Basic)

Purpose
- Help an AI coding agent be productive in this repository: a small collection of single-file Python examples under the `Basic/` folder.

Big picture
- This repo contains short, independent Python scripts (learning examples) in `Basic/` named with a numeric prefix (e.g. `01_Hello_world.py`, `07_Swap_numbers.py`).
- There is no package layout, tests, or CI configuration. Each file is intended to run directly with the system Python interpreter.

Typical developer workflows
- Run a single example from the workspace root with:
  - `python "Basic/07_Swap_numbers.py"`
  - On Windows PowerShell use the full Python path if needed (e.g. `& C:/Path/To/python.exe "Basic/07_Swap_numbers.py"`).
- Debug in VS Code by opening the file and using the Python debugger; treat scripts as top-level run targets.

Project-specific conventions and patterns
- Filenames: `NN_Description.py` where `NN` is two-digit index. Keep this naming when adding new examples.
- Script style: prefer simple, imperative top-level code and small helper functions. Avoid introducing package-level complexity without asking the maintainer.
- I/O: many examples use `print()` and `input()` for interactivity — preserve this pattern for beginner-friendly examples.
- Keep changes minimal and local to a single example unless the change is an explicit refactor requested by the user.

When editing or adding files
- If you add new examples, follow the `Basic/` naming pattern and include a one-line comment at the top describing intent.
- Run the file locally after edits to ensure no SyntaxError or runtime exceptions for typical inputs.
- Avoid adding new runtime dependencies. If a dependency is required, propose it and ask before adding `requirements.txt` or virtualenv configuration.

Integration points and external dependencies
- This repository currently has none. Treat external libraries as disallowed unless the user asks.

Safety and style decisions for the AI
- Keep edits minimal and backwards-compatible. Do not reformat unrelated files.
- When in doubt, ask the user before making repository-wide changes (adding packaging, tests, or CI).
- When producing examples, mirror the repository's simple, beginner-friendly style (clear names, few lines, explicit prints/inputs).

Examples (explicit)
- To run `07_Swap_numbers.py` from the workspace root:
  - `python "Basic/07_Swap_numbers.py"`
- When updating `03_Additon.py`, keep the single-responsibility nature (one small example per file).

If anything is unclear or you want additional agent behaviors (e.g., add tests, create a package layout, or standardize formatting), ask before proceeding.
