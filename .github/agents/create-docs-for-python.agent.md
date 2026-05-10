---
name: create-docs-for-python
description: Generate a docs markdown file for each executable Python script and update README.md with links to those docs.
---

Create or refresh documentation for every executable Python file in the project by doing the following:

1. Identify executable Python files in the workspace. This should include top-level scripts and any Python files intended to be run, not just library modules.
2. For each such file, create or update `docs/<basename>.md` with:
   - a short summary of what the script does
   - the main components or behavior implemented in the file
   - exact steps to execute it from the project root
   - any environment or dependency notes specific to that script
3. Update `README.md` so it remains concise and project-level, and include:
   - a `Documentation` section linking to each generated docs file under `docs/`
   - general setup and execution guidance
   - a note that the `/create-docs-for-python` custom agent can be used to generate docs for new executable Python scripts
4. If a docs file already exists for a Python file, refresh it rather than creating duplicate files.

Use this agent whenever a new executable Python file is added so the docs folder and README stay synchronized.
