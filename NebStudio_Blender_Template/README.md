# NebStudio Blender Extension Template

Reusable starting point for NebStudio Blender extensions.

## Requirements

- Blender 5.1+
- Python version bundled with the target Blender release
- Visual Studio Code (recommended)

## Structure

- `__init__.py` — extension entry point
- `blender_manifest.toml` — extension metadata
- `operators/` — user-triggered actions
- `panels/` — Blender interface
- `core/` — shared internal logic
- `icons/` — interface assets

## Workflow

1. Define the product scope and user workflow.
2. Implement one feature at a time.
3. Test in the target Blender version.
4. Validate the extension manifest and build.
5. Prepare release notes, documentation, and marketplace assets.

## Validation

Build the extension with Blender's command-line extension tooling:

```powershell
blender --command extension build --source-dir .\NebStudio_Blender_Template
```

---

NebStudio
