import sys
from tkinter import Menu
import ttkbootstrap as ttk


class RoundedMenu(Menu):
    """
    A custom menu widget with Ghost theme styling.
    
    This component extends tkinter.Menu to match the Ghost theme
    with proper color palette and styling for menu bars and popup menus.
    
    Args:
        parent: The parent widget
        tearoff: Whether the menu can be torn off (default: 0)
        **kwargs: Additional Menu configuration options
    """
    def __init__(self, parent, tearoff=0, **kwargs):
        self.parent = parent
        self.root = parent.winfo_toplevel()
        
        # Try to get style colors, fallback to defaults if not available
        try:
            self.style = self.root.style
            self.bg_color = self.style.colors.get("secondary")
            self.fg_color = self.style.colors.get("fg")
            self.active_bg = self.style.colors.get("primary")
            self.active_fg = self.style.colors.get("selectfg")
            self.disabled_fg = self.style.colors.get("light")
        except:
            # Fallback colors if style is not available
            self.bg_color = "#222324"
            self.fg_color = "#ffffff"
            self.active_bg = "#433dfb"
            self.active_fg = "#ffffff"
            self.disabled_fg = "#ADB5BD"
        
        # Set default font
        if "font" not in kwargs:
            kwargs["font"] = ("Host Grotesk", 10) if sys.platform != "darwin" else ("Host Grotesk",)
        
        # Initialize Menu with Ghost theme colors
        super().__init__(
            parent,
            tearoff=tearoff,
            bg=self.bg_color,
            fg=self.fg_color,
            activebackground=self.active_bg,
            activeforeground=self.active_fg,
            activeborderwidth=0,
            borderwidth=0,
            relief="flat",
            disabledforeground=self.disabled_fg,
            **kwargs
        )
    
    def add_command(self, **kwargs):
        """Add a command item to the menu with Ghost theme styling"""
        # Set default accelerator color if not provided
        if "accelerator" in kwargs and "foreground" not in kwargs:
            kwargs["foreground"] = self.fg_color
        super().add_command(**kwargs)
    
    def add_cascade(self, **kwargs):
        """Add a cascade (submenu) to the menu"""
        # If a menu is provided, ensure it's also styled
        if "menu" in kwargs:
            submenu = kwargs["menu"]
            if isinstance(submenu, Menu):
                submenu.configure(
                    bg=self.bg_color,
                    fg=self.fg_color,
                    activebackground=self.active_bg,
                    activeforeground=self.active_fg,
                    activeborderwidth=0,
                    borderwidth=0,
                    relief="flat",
                    disabledforeground=self.disabled_fg
                )
        super().add_cascade(**kwargs)
    
    def add_checkbutton(self, **kwargs):
        """Add a checkbutton item to the menu"""
        if "selectcolor" not in kwargs:
            kwargs["selectcolor"] = self.active_bg
        super().add_checkbutton(**kwargs)
    
    def add_radiobutton(self, **kwargs):
        """Add a radiobutton item to the menu"""
        if "selectcolor" not in kwargs:
            kwargs["selectcolor"] = self.active_bg
        super().add_radiobutton(**kwargs)


def create_menubar(root):
    """
    Helper function to create a themed menubar for a window.
    
    Args:
        root: The root window or toplevel widget
    
    Returns:
        A RoundedMenu configured as a menubar
    """
    menubar = RoundedMenu(root)
    root.config(menu=menubar)
    return menubar


def create_popup_menu(parent):
    """
    Helper function to create a themed popup/context menu.
    
    Args:
        parent: The parent widget
    
    Returns:
        A RoundedMenu configured as a popup menu
    """
    return RoundedMenu(parent, tearoff=0)