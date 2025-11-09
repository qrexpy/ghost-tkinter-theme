# Ghost Tkinter Theme 👻

Modern, production-ready Tkinter UI components with hexagonal rounded containers, smooth hover effects, and a stunning dark theme. Drop it into any Python project and build beautiful interfaces in minutes.

![Ghost Theme](https://img.shields.io/badge/Theme-Ghost-433dfb)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **🎯 Hexagonal Rounded Containers** - Smooth polygonal shapes with per-corner radius control
- **🖱️ Hover Animations** - 10% color darkening on interactive elements
- **🎨 Ghost Dark Theme** - Signature purple (#433dfb) with 8-color palette
- **� Themed Scrollbars** - Auto-hiding scrollbars that match your design
- **� Zero Dependencies** - Only ttkbootstrap required
- **💪 Production Ready** - Used in real projects, tested and documented

## 🚀 Quick Start

```bash
# Install
pip install -r requirements.txt

# See it in action
python showcase.py

# Use in your project
from components import RoundedFrame, RoundedButton
```

Copy `components/` and `theme.json` to your project and you're ready to go.

## 📦 Components

### RoundedFrame
Hexagonal container with smooth rounded corners.

```python
from components import RoundedFrame

frame = RoundedFrame(parent, radius=15, bootstyle="secondary.TFrame")
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add your widgets inside
ttk.Label(frame, text="Content here").pack(pady=10)
```

**Options:**
- `radius` - Corner radius: int or tuple (TL, TR, BR, BL)
- `bootstyle` - Theme color: `primary`, `secondary`, `dark`, etc.
- `min_width`, `min_height` - Size constraints

### RoundedButton
Interactive button with hover effects.

```python
from components import RoundedButton

button = RoundedButton(
    parent,
    text="Click Me",
    bootstyle="primary.TButton",
    command=lambda e: print("Clicked!"),
    radius=8,
    padx=20,
    pady=10
)
button.pack()
```

**Features:**
- Automatic 10% darkening on hover
- Text, image, or both
- All theme colors supported

## 🎨 Theme Colors

| Color      | Hex       | Use Case              |
|------------|-----------|-----------------------|
| Primary    | `#433dfb` | Actions, highlights   |
| Secondary  | `#222324` | Cards, containers     |
| Success    | `#0abf34` | Confirmations         |
| Info       | `#2b6eff` | Information           |
| Warning    | `#f39c12` | Warnings              |
| Danger     | `#ff341f` | Errors, destructive   |
| Dark       | `#1a1c1c` | Nested containers     |
| Background | `#121111` | App background        |

Edit `theme.json` to customize.

## 📁 Structure

```
template/
├── showcase.py           # Demo app
├── example.py           # Minimal example
├── theme.json          # Color palette
├── components/
│   ├── rounded_frame.py
│   └── rounded_button.py
└── assets/fonts/       # Host Grotesk fonts
```

## ⚙️ Customization

**Colors** - Edit `theme.json`:
```json
"primary": "#your-color"
```

**Radius** - Per corner control:
```python
radius=(20, 20, 10, 10)  # TL, TR, BR, BL
```

**Hover** - Change intensity in `rounded_button.py`:
```python
factor=0.9  # 0.9 = 10% darker, 0.8 = 20% darker
```

## 💡 Examples

**Info Card:**
```python
card = RoundedFrame(parent, radius=15, bootstyle="dark.TFrame")
ttk.Label(card, text="Title", font=("Host Grotesk", 12, "bold")).pack(pady=10)
ttk.Separator(card).pack(fill=tk.X, padx=10)
ttk.Label(card, text="Content").pack(pady=10)
```

**Button Grid:**
```python
for i, (text, style) in enumerate([("Save", "success"), ("Delete", "danger")]):
    RoundedButton(parent, text=text, bootstyle=f"{style}.TButton").grid(row=0, column=i, padx=5)
```

## � Fonts

Host Grotesk fonts are in `assets/fonts/`. Install system-wide for best results:
- **Windows:** Right-click → Install
- **macOS:** Open in Font Book
- **Linux:** Copy to `~/.local/share/fonts/`

Falls back to system fonts if unavailable.

## � Requirements

- Python 3.8+
- ttkbootstrap 1.10.0+
- tkinter (included with Python)

## 📄 License

MIT License - Free for any use, commercial or personal.

## 🙏 Credits

Inspired by the Ghost selfbot UI design.

---

**Built for the Python community** • Star if you find it useful!
