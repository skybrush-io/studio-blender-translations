# Skybrush Studio for Blender Translations

This repository is the main source of translations for [Skybrush Studio for Blender](https://github.com/skybrush-io/studio-blender).

The structure of the repository is similar to the main [blender-translations](https://github.com/blender/blender-translations) repository.

## How to translate strings?

TODO: setup WebLate etc.

## How to push/pull translations to/from Skybrush Studio for Blender?

1. Open Blender with the "Skybrush Studio for Blender" add-on loaded
2. Setup the "Manage UI translations" add-on properly:
    a) clone the `blender` and `blender-translations` sources from GitHub
    b) link them to the "Source Root" and "Translation Root" directories
    c) save settings to a proper "Persistent data path" as settings will be lost on next Blender execution
3. In "Blender" / "Render properties" / "I18n Update Translation" press the proper buttons under the "Add-ons" section:
    a) select this repository's `po` directory for the PO inputs/outputs
    b) move the auto-generated `translations_tuple` in the `studio-blender` add-on from `ui_skybrush_studio.py` to `modules/sbstudio/i18n/translations.py` 

