# NebStudio Blender — Project Status

## Current environment

- Blender: 5.1.1
- Operating system: Windows 11
- Editor: Visual Studio Code
- Blender Python: bundled Python 3.13.9
- Main project: `C:\\NEBSTUDIO\\NebStudio_Blender_Template`
- VS Code development extension: Blender Development by Jacques Lucke (installed and configured by the user)

## Completed

- [x] Development workspace created
- [x] Blender Python interpreter configured in VS Code
- [x] Reusable extension folder structure created
- [x] Example operator and UI panel implemented
- [x] Extension successfully built with Blender 5.1.1
- [x] Extension installed and manually tested in Blender
- [x] Centralized class registration system implemented
- [x] Operator and panel modules migrated to the central registry
- [x] Registration rollback and reverse unregistration added
- [x] Updated extension installed and tested successfully in Blender 5.1.1
- [x] VS Code Blender Development extension installed and configured for the development workflow

## Development workflow

Use the Blender Development extension in VS Code to start the Blender session and reload the project during development:

1. Open the NebStudio extension project folder in VS Code.
2. Run `Blender: Start` from the Command Palette and use Blender 5.1.1.
3. After code changes, use `Blender: Reload Addons`; automatic reload-on-save can be used when enabled in the VS Code setting `blender.addon.reloadOnSave`.
4. Use the VS Code Blender output channel/terminal to inspect startup and reload errors.

The extension manages its own development link for the project. The old manual ZIP build remains useful for packaging and release validation, not as the normal edit-test loop.

## Current state

The template is a working technical baseline. The VS Code development integration has been configured, but its reload-on-save behavior should only be considered fully validated after a code edit is saved and the updated extension is confirmed working in Blender.

Further work remains before production release, including lifecycle edge cases, validation, packaging checks, and release documentation.

## Working rule

Keep product decisions and scope explicit. Implement and validate changes incrementally. Do not mark a feature complete until it has been tested in Blender.
