import pypandoc

content = r"""# SCALE STEP PIE � PROJECT HANDOFF

## Project Name
Scale Step Pie

## Type
Blender Add-on

## Target Blender Version
Blender 5.0+

## Purpose
Professional Blender add-on for fast Scale control through Pie Menu.

Goals:
- quick scale steps;
- hotkey-driven workflow;
- editable slots;
- scalable transform toolkit architecture.

---

# Development History

## Version 1.x � Prototype
Initial monolithic Pie Menu implementation.

Features:
- scale changing;
- fixed steps;
- hotkey launch.

Problem:
- all code in one file;
- difficult to extend.

---

## Version 2.3.x � Modularization

Created structure:

scale_step_pie/

- __init__.py
- preferences.py
- operators.py
- pie_menu.py
- keymap.py
- utils.py
- icons/

Added:
- operators;
- preferences;
- keymap system;
- modular Pie Menu.

---

## Version 2.4.0 Alpha

Implemented:

### Preferences
Editable slots:

- BIG +
- MEDIUM +
- SMALL +
- FINE +
- FINE -
- SMALL -
- MEDIUM -
- BIG -

Each slot:
- label;
- value;
- mode.

### Operators

Created:

- object.scale_step_v240
- object.scale_reset_v240
- object.apply_scale_v240

Functions:
- scale step change;
- reset scale to 1,1,1;
- apply scale.

---

# Important Blender 5.0 Issue

Main error:

TypeError:
object of type '_PropertyDeferred' has no len()

Cause:
incorrect registration of CollectionProperty.

Rule:
Do not mix incompatible property declaration styles.

Preferred stable approach:
- register PropertyGroup first;
- then register AddonPreferences;
- use verified CollectionProperty registration.

---

# Stable State

Last confirmed working state:

Scale Step Pie v2.4.0 alpha2 fix3

Working:
- Add-on loads;
- Preferences opens;
- slots editable;
- Keymap works;
- Pie opens.

---

# Current Development Goal

Move to:

Scale Step Pie v2.5.0 Professional Architecture

---

# New Architecture

scale_step_pie/

- __init__.py

core/
- registry.py
- constants.py
- settings.py

operators/
- scale.py
- transform.py
- presets.py

ui/
- pie_menu.py
- preferences.py
- panels.py

keymap.py

utils/
- scale_utils.py
- json_utils.py

presets/
- default.json
- jewelry.json
- cad.json

icons/

---

# New Pie System

Replace fixed slots with PieItem.

Each item stores:

- name
- label
- position
- type
- value
- mode
- icon

Example:

{
 "label": "BIG +",
 "position": "TOP",
 "type": "SCALE",
 "value": 0.5,
 "mode": "ADD"
}

---

# Default Layout

Target layout:

                 BIG +

        MEDIUM +       MEDIUM -

 FINE +                          FINE -

        APPLY          RESET

                 BIG -

---

# Supported Commands

Future system:

- SCALE
- RESET_SCALE
- APPLY_SCALE
- MIRROR
- CUSTOM_OPERATOR
- SEPARATOR

---

# Future Features

Profiles:
- Default
- Jewelry
- CAD
- Modeling

Export/import:
- JSON profiles

Additional tools:
- Apply Rotation
- Apply Location
- Mirror Scale
- Freeze Transform
- Zero Scale
- Random Scale

---

# Development Rules

Important:

Always provide complete files.

Avoid:
- manual fragments;
- partial replacements;
- instructions requiring many edits.

Before changing architecture:
- verify registration;
- verify keymap;
- verify preferences;
- preserve working modules.

Never break stable modules without reason.

---

# Current Roadmap

1. Stabilize v2.4.0 alpha3:
   - registry;
   - PropertyGroup;
   - CollectionProperty.

2. Start v2.5.0 alpha1:
   - new registry;
   - new Pie engine;
   - new settings system.

---

# Repository Goal

Final repository:

Scale-Step-Pie/

- README.md
- CHANGELOG.md
- DEVELOPMENT.md
- SCALE_STEP_PIE_HANDOFF.md
- scale_step_pie/
- blender_manifest.toml
- LICENSE

---

END
"""

path = "/mnt/data/SCALE_STEP_PIE_HANDOFF.md"

pypandoc.convert_text(
    content,
    'md',
    format='md',
    outputfile=path,
    extra_args=['--standalone']
)

path
