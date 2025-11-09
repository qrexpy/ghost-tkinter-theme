import sys
import ttkbootstrap as ttk
from tkinter import StringVar


class RoundedCombobox(ttk.Combobox):
    """
    A custom combobox widget with Ghost theme styling and hover effects.
    
    This component extends ttk.Combobox to match the Ghost theme
    with proper transparency handling and smooth interactions.
    
    Args:
        parent: The parent widget
        values: List of values for the dropdown
        textvariable: StringVar to bind the selected value
        command: Callback function when value changes
        state: Widget state ('normal' or 'readonly')
        width: Width of the combobox
        font: Font tuple (family, size, weight)
    """
    def __init__(self, parent, values=None, textvariable=None, command=None, **kwargs):
        # Store custom parameters
        self.custom_command = command
        self.custom_values = values or []
        
        # Remove custom kwargs that aren't Combobox parameters
        kwargs.pop("bootstyle", None)
        kwargs.pop("radius", None)
        
        self.parent = parent
        self.root = parent.winfo_toplevel()
        self.style = self.root.style
        
        # Store the original background color
        self.original_bg = self.style.colors.get("inputbg")
        self.hover_bg = self._lighten_color(self.original_bg, 1.1)
        
        # Create textvariable if not provided
        if textvariable is None:
            self.textvariable = StringVar()
            if self.custom_values:
                self.textvariable.set(self.custom_values[0])
        else:
            self.textvariable = textvariable
        
        # Set default values
        if "state" not in kwargs:
            kwargs["state"] = "readonly"
        if "width" not in kwargs:
            kwargs["width"] = 20
        if "font" not in kwargs:
            kwargs["font"] = ("Host Grotesk", 10) if sys.platform != "darwin" else ("Host Grotesk",)
        
        # Configure custom style
        combobox_style = "Ghost.TCombobox"
        self._configure_combobox_style(combobox_style)
        kwargs["style"] = combobox_style
        
        # Initialize the Combobox
        super().__init__(
            parent,
            textvariable=self.textvariable,
            values=self.custom_values,
            **kwargs
        )
        
        # Bind command if provided
        if command:
            self.bind("<<ComboboxSelected>>", lambda e: command())
        
        # Bind hover effects
        self.bind("<Enter>", self._hover_enter)
        self.bind("<Leave>", self._hover_leave)

    def _configure_combobox_style(self, style_name):
        """Configure custom combobox style matching the Ghost theme"""
        # Configure the combobox style
        self.style.configure(
            style_name,
            fieldbackground=self.original_bg,
            background=self.original_bg,
            foreground=self.style.colors.get("inputfg"),
            bordercolor=self.style.colors.get("selectbg"),  # Gray border by default
            darkcolor=self.original_bg,
            lightcolor=self.original_bg,
            arrowcolor=self.style.colors.get("inputfg"),
            insertcolor=self.style.colors.get("inputfg"),
            selectbackground=self.original_bg,  # Match background to hide selection
            selectforeground=self.style.colors.get("inputfg"),  # Keep text color same
            borderwidth=2,
            relief="solid",
        )
        
        # Map states
        self.style.map(
            style_name,
            fieldbackground=[
                ("readonly", self.original_bg),
                ("disabled", self.style.colors.get("dark")),
                ("hover", self.hover_bg)
            ],
            background=[
                ("readonly", self.original_bg),
                ("disabled", self.style.colors.get("dark")),
                ("hover", self.hover_bg)
            ],
            foreground=[("disabled", self.style.colors.get("light"))],
            arrowcolor=[("disabled", self.style.colors.get("light"))],
            selectbackground=[
                ("readonly", self.original_bg),
                ("!readonly", self.original_bg),
                ("hover", self.hover_bg)
            ],
            selectforeground=[
                ("readonly", self.style.colors.get("inputfg")),
                ("!readonly", self.style.colors.get("inputfg"))
            ],
            bordercolor=[
                ("focus", self.style.colors.get("primary")),  # Purple when focused
                ("hover", self.style.colors.get("primary")),  # Purple when hovered
                ("!focus", self.style.colors.get("selectbg"))  # Gray when not focused
            ],
        )

    def _lighten_color(self, hex_color, factor=1.1):
        """Lighten color for hover effect"""
        if not hex_color.startswith("#"):
            return hex_color

        rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
        lightened_rgb = tuple(min(255, int(value * factor)) for value in rgb)
        return f"#{lightened_rgb[0]:02x}{lightened_rgb[1]:02x}{lightened_rgb[2]:02x}"

    def _hover_enter(self, event=None):
        """Apply hover effect"""
        self.style.configure(
            "Ghost.TCombobox",
            fieldbackground=self.hover_bg,
            background=self.hover_bg,
            selectbackground=self.hover_bg,
        )

    def _hover_leave(self, event=None):
        """Reset to original color"""
        self.style.configure(
            "Ghost.TCombobox",
            fieldbackground=self.original_bg,
            background=self.original_bg,
            selectbackground=self.original_bg,
        )

    def get(self):
        """Get the current value"""
        return self.textvariable.get()

    def set(self, value):
        """Set the current value"""
        self.textvariable.set(value)