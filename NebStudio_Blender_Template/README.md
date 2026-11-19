# NebStudio Blender Extension Template

Reusable foundation for NebStudio Blender extensions.

## Environment

- Blender 5.1.1
- Blender Python 3.13
- VS Code
- fake-bpy-module-5.1 for editor type information

## Structure

- `__init__.py` — Extension entry point
- `blender_manifest.toml` — Extension metadata
- `operators/` — User actions
- `panels/` — Blender interface
- `core/` — Internal logic
- `icons/` — Visual resources

## Current test feature

The 3D View sidebar contains a **NebStudio** tab with a test panel and an operator button.

Operator identifier: `nebstudio.example`

## Build

Run in PowerShell:

```powershell
Start-Process -FilePath "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" -ArgumentList '--command','extension','build','--source-dir','C:\NEBSTUDIO\NebStudio_Blender_Template','--verbose' -Wait -PassThru
```

The build creates `nebstudio_template-1.0.0.zip` in the source directory.

## Install and test

1. In Blender, open **Edit → Preferences → Get Extensions**.
2. Choose **Install from Disk** and select the generated ZIP.
3. In the 3D View, press `N` and open the **NebStudio** tab.
4. Click the test button and confirm the info report appears.

## Development notes

- Keep each extension modular and small.
- Put user-triggered actions in `operators/`.
- Put interface panels in `panels/`.
- Keep reusable implementation logic in `core/`.
- Test inside the target Blender version before packaging.

---

NebStudio
