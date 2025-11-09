"""
Ghost Theme Template Showcase
==============================

A beautiful, reusable tkinter template showcasing the Ghost selfbot's UI design.
Features hexagonal rounded boxes, smooth hover effects, and a modern dark theme.

This template is completely standalone and can be used in any tkinter project.

Components:
- RoundedFrame: Hexagonal/rounded container with customizable corner radii
- RoundedButton: Interactive button with hover effects
- Ghost Theme: Modern dark color palette

Author: Based on Ghost selfbot design
License: Free to use in any project
"""

import os
import sys
import ttkbootstrap as ttk
from ttkbootstrap.utility import enable_high_dpi_awareness
from ttkbootstrap.scrolled import ScrolledFrame
from components import RoundedFrame, RoundedButton, RoundedCombobox, RoundedListbox


class GhostTemplateShowcase:
    """Main showcase application demonstrating all Ghost theme components"""
    
    def __init__(self):
        self.size = (700, 650)
        
        # Enable high DPI for crisp rendering on modern displays
        enable_high_dpi_awareness()
        
        # Initialize root window
        self.root = ttk.tk.Tk()
        self.root.title("Ghost Theme Template - Showcase")
        self.root.geometry(f"{self.size[0]}x{self.size[1]}")
        self.root.minsize(self.size[0], 500)
        
        # Load and apply custom theme
        self.setup_theme()
        
        # Center window on screen
        self.center_window()
        
    def setup_theme(self):
        """Load and configure the Ghost theme"""
        self.root.style = ttk.Style()
        
        # Load custom Ghost theme
        theme_path = os.path.join(os.path.dirname(__file__), "theme.json")
        self.root.style.load_user_themes(theme_path)
        self.root.style.theme_use("ghost")
        
        # Configure widget styles with Host Grotesk font
        # Note: Install Host Grotesk font family for best results
        self.root.style.configure("TEntry", 
            background=self.root.style.colors.get("dark"), 
            fieldbackground=self.root.style.colors.get("secondary")
        )
        self.root.style.configure("TCheckbutton", background=self.root.style.colors.get("dark"))
        self.root.style.configure("TMenubutton", font=("Host Grotesk",))
        self.root.style.configure("TCheckbutton", font=("Host Grotesk",))
        self.root.style.configure("TEntry", font=("Host Grotesk",))
        self.root.style.configure("TLabel", font=("Host Grotesk",))
        self.root.style.configure("TButton", font=("Host Grotesk",))
        
        # Configure scrollbar to match Ghost theme
        self.root.style.configure("Vertical.TScrollbar",
            background=self.root.style.colors.get("primary"),
            troughcolor=self.root.style.colors.get("bg"),
            bordercolor=self.root.style.colors.get("bg"),
            arrowcolor=self.root.style.colors.get("fg")
        )
        
        self.root.style.map("Vertical.TScrollbar",
            background=[
                ('pressed', self.root.style.colors.get("info")),
                ('active', self.root.style.colors.get("primary")),
                ('!active', self.root.style.colors.get("secondary"))
            ]
        )
        
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (self.size[0] // 2)
        y = (screen_height // 2) - (self.size[1] // 2)
        
        self.root.geometry(f"{self.size[0]}x{self.size[1]}+{x}+{y}")
        
    def create_header_section(self, parent):
        """Create the header showcase section"""
        # Main header container with rounded corners
        header = RoundedFrame(parent, radius=15, bootstyle="secondary.TFrame")
        header.pack(fill=ttk.BOTH, expand=False, pady=(0, 10))
        
        # Title
        title = ttk.Label(
            header, 
            text="Ghost Theme Template", 
            font=("Host Grotesk", 18, "bold")
        )
        title.configure(background=self.root.style.colors.get("secondary"))
        title.pack(pady=(15, 5), padx=15)
        
        # Subtitle
        subtitle = ttk.Label(
            header, 
            text="A beautiful, reusable tkinter theme with hexagonal boxes", 
            font=("Host Grotesk", 10)
        )
        subtitle.configure(
            background=self.root.style.colors.get("secondary"), 
            foreground="lightgrey"
        )
        subtitle.pack(pady=(0, 15), padx=15)
        
    def create_color_palette_section(self, parent):
        """Display the color palette"""
        section_title = ttk.Label(
            parent, 
            text="Color Palette", 
            font=("Host Grotesk", 14, "bold")
        )
        section_title.pack(pady=(10, 10), anchor=ttk.W)
        
        # Color palette container
        palette_frame = ttk.Frame(parent)
        palette_frame.pack(fill=ttk.BOTH, expand=False, pady=(0, 10))
        
        colors = [
            ("Primary", "primary", "#433dfb"),
            ("Secondary", "secondary", "#222324"),
            ("Success", "success", "#0abf34"),
            ("Info", "info", "#2b6eff"),
            ("Warning", "warning", "#f39c12"),
            ("Danger", "danger", "#ff341f"),
            ("Dark", "dark", "#1a1c1c"),
            ("Background", "bg", "#121111"),
        ]
        
        for i, (name, style, hex_code) in enumerate(colors):
            color_box = RoundedFrame(
                palette_frame, 
                radius=10, 
                bootstyle=f"{style}.TFrame"
            )
            color_box.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky=ttk.NSEW)
            
            label = ttk.Label(
                color_box, 
                text=f"{name}\n{hex_code}", 
                font=("Host Grotesk", 8),
                anchor="center"
            )
            label.configure(background=self.root.style.colors.get(style))
            label.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
        
        # Configure grid weights for even distribution
        for i in range(4):
            palette_frame.grid_columnconfigure(i, weight=1)
            
    def create_components_section(self, parent):
        """Showcase different component variations"""
        section_title = ttk.Label(
            parent, 
            text="Components Showcase", 
            font=("Host Grotesk", 14, "bold")
        )
        section_title.pack(pady=(10, 10), anchor=ttk.W)
        
        # Container for component examples
        components_container = ttk.Frame(parent)
        components_container.pack(fill=ttk.BOTH, expand=False)
        components_container.grid_columnconfigure(0, weight=1)
        components_container.grid_columnconfigure(1, weight=1)
        
        # Info Card Example (Left)
        info_card = RoundedFrame(
            components_container, 
            radius=15, 
            bootstyle="dark.TFrame"
        )
        info_card.grid(row=0, column=0, sticky=ttk.NSEW, padx=(0, 5), pady=(0, 5))
        
        card_title = ttk.Label(
            info_card, 
            text="Info Card", 
            font=("Host Grotesk", 12, "bold")
        )
        card_title.configure(background=self.root.style.colors.get("dark"))
        card_title.pack(pady=(10, 5), padx=10, anchor=ttk.W)
        
        ttk.Separator(info_card, orient="horizontal").pack(fill=ttk.X, padx=10, pady=5)
        
        info_text = ttk.Label(
            info_card, 
            text="This is an example of a rounded\ninformation card with dark theme.", 
            font=("Host Grotesk", 9)
        )
        info_text.configure(background=self.root.style.colors.get("dark"))
        info_text.pack(pady=(5, 10), padx=10, anchor=ttk.W)
        
        # Stats Card Example (Right)
        stats_card = RoundedFrame(
            components_container, 
            radius=15, 
            bootstyle="dark.TFrame"
        )
        stats_card.grid(row=0, column=1, sticky=ttk.NSEW, padx=(5, 0), pady=(0, 5))
        
        stats_title = ttk.Label(
            stats_card, 
            text="Statistics", 
            font=("Host Grotesk", 12, "bold")
        )
        stats_title.configure(background=self.root.style.colors.get("dark"))
        stats_title.pack(pady=(10, 5), padx=10, anchor=ttk.W)
        
        ttk.Separator(stats_card, orient="horizontal").pack(fill=ttk.X, padx=10, pady=5)
        
        stat_items = [
            ("Total Items:", "142"),
            ("Active Users:", "1,337"),
            ("Uptime:", "99.9%"),
        ]
        
        for label, value in stat_items:
            stat_frame = ttk.Frame(stats_card)
            stat_frame.configure(style="dark.TFrame")
            stat_frame.pack(fill=ttk.X, padx=10, pady=2)
            
            stat_label = ttk.Label(
                stat_frame, 
                text=label, 
                font=("Host Grotesk", 9)
            )
            stat_label.configure(background=self.root.style.colors.get("dark"))
            stat_label.pack(side=ttk.LEFT)
            
            stat_value = ttk.Label(
                stat_frame, 
                text=value, 
                font=("Host Grotesk", 9, "bold")
            )
            stat_value.configure(background=self.root.style.colors.get("dark"))
            stat_value.pack(side=ttk.RIGHT)
        
        ttk.Label(stats_card, text="").pack(pady=5)  # Spacer
        
    def create_buttons_section(self, parent):
        """Showcase button variations"""
        section_title = ttk.Label(
            parent, 
            text="Interactive Buttons", 
            font=("Host Grotesk", 14, "bold")
        )
        section_title.pack(pady=(10, 10), anchor=ttk.W)
        
        # Buttons container
        buttons_frame = ttk.Frame(parent)
        buttons_frame.pack(fill=ttk.X, pady=(0, 10))
        
        # Different button styles
        button_configs = [
            ("Primary Action", "primary.TButton", self.on_button_click),
            ("Success", "success.TButton", self.on_button_click),
            ("Info", "info.TButton", self.on_button_click),
            ("Warning", "warning.TButton", self.on_button_click),
            ("Danger", "danger.TButton", self.on_button_click),
        ]
        
        for i, (text, style, command) in enumerate(button_configs):
            btn = RoundedButton(
                buttons_frame,
                radius=8,
                text=text,
                bootstyle=style,
                command=command,
                padx=15,
                pady=8
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky=ttk.EW)
        
        # Configure column weights
        for i in range(3):
            buttons_frame.grid_columnconfigure(i, weight=1)
            
    def create_input_section(self, parent):
        """Showcase form inputs"""
        section_title = ttk.Label(
            parent,
            text="Form Inputs",
            font=("Host Grotesk", 14, "bold")
        )
        section_title.pack(pady=(10, 10), anchor=ttk.W)
        
        # Input container
        input_container = RoundedFrame(
            parent,
            radius=15,
            bootstyle="secondary.TFrame"
        )
        input_container.pack(fill=ttk.X, pady=(0, 10))
        
        # Text entry
        entry_label = ttk.Label(
            input_container,
            text="Text Input:",
            font=("Host Grotesk", 10)
        )
        entry_label.configure(background=self.root.style.colors.get("secondary"))
        entry_label.pack(pady=(15, 5), padx=15, anchor=ttk.W)
        
        entry = ttk.Entry(input_container, font=("Host Grotesk", 10))
        entry.insert(0, "Enter text here...")
        entry.pack(fill=ttk.X, padx=15, pady=(0, 10))
        
        # Combobox
        combo_label = ttk.Label(
            input_container,
            text="Dropdown Selection:",
            font=("Host Grotesk", 10)
        )
        combo_label.configure(background=self.root.style.colors.get("secondary"))
        combo_label.pack(pady=(5, 5), padx=15, anchor=ttk.W)
        
        combobox = RoundedCombobox(
            input_container,
            values=["Python", "JavaScript", "TypeScript", "Rust", "Go", "C++", "Java"],
            width=30
        )
        combobox.pack(fill=ttk.X, padx=15, pady=(0, 10))
        
        # Listbox
        listbox_label = ttk.Label(
            input_container,
            text="Select Items:",
            font=("Host Grotesk", 10)
        )
        listbox_label.configure(background=self.root.style.colors.get("secondary"))
        listbox_label.pack(pady=(5, 5), padx=15, anchor=ttk.W)
        
        listbox = RoundedListbox(
            input_container,
            values=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7"],
            height=5,
            selectmode="browse"
        )
        listbox.pack(fill=ttk.BOTH, padx=15, pady=(0, 10))
        
        # Checkbutton
        check_var = ttk.BooleanVar(value=True)
        checkbutton = ttk.Checkbutton(
            input_container,
            text="Enable awesome feature",
            variable=check_var,
            bootstyle="primary"
        )
        checkbutton.pack(padx=15, pady=(0, 15), anchor=ttk.W)
        
    def create_footer(self, parent):
        """Create footer with usage information"""
        footer = RoundedFrame(parent, radius=10, bootstyle="dark.TFrame")
        footer.pack(fill=ttk.X, pady=(10, 0))
        
        footer_text = ttk.Label(
            footer,
            text="💡 Free to use in any project • Customize colors in theme.json",
            font=("Host Grotesk", 9),
            anchor="center"
        )
        footer_text.configure(
            background=self.root.style.colors.get("dark"),
            foreground="lightgrey"
        )
        footer_text.pack(pady=10, padx=15)
        
    def on_button_click(self, event=None):
        """Example button callback"""
        print("Button clicked!")
        
    def build_ui(self):
        """Build the complete showcase UI"""
        # Create scrollable container
        scrolled_container = ScrolledFrame(self.root, autohide=True)
        scrolled_container.pack(fill=ttk.BOTH, expand=True)
        
        # Main container with padding
        main_container = ttk.Frame(scrolled_container)
        main_container.pack(fill=ttk.BOTH, expand=True, padx=25, pady=25)
        
        # Build all sections
        self.create_header_section(main_container)
        self.create_color_palette_section(main_container)
        self.create_components_section(main_container)
        self.create_buttons_section(main_container)
        self.create_input_section(main_container)
        self.create_footer(main_container)
        
    def run(self):
        """Start the application"""
        self.build_ui()
        self.root.mainloop()


if __name__ == "__main__":
    app = GhostTemplateShowcase()
    app.run()
