"""
Simple Usage Example - Ghost Theme Template
============================================

This file demonstrates the basic usage of the Ghost theme components
in a minimal application.
"""

import ttkbootstrap as ttk
from ttkbootstrap.utility import enable_high_dpi_awareness
from components import RoundedFrame, RoundedButton


def on_button_click(event=None):
    """Example callback function"""
    print("Button was clicked!")
    

def create_simple_app():
    """Create a simple application using Ghost theme components"""
    
    # Enable high DPI
    enable_high_dpi_awareness()
    
    # Create root window
    root = ttk.tk.Tk()
    root.title("Ghost Theme - Simple Example")
    root.geometry("500x400")
    
    # Apply Ghost theme
    root.style = ttk.Style()
    root.style.load_user_themes("theme.json")
    root.style.theme_use("ghost")
    
    # Configure font
    root.style.configure("TLabel", font=("Host Grotesk",))
    
    # Main container
    container = ttk.Frame(root)
    container.pack(fill=ttk.BOTH, expand=True, padx=30, pady=30)
    
    # Header card
    header = RoundedFrame(container, radius=15, bootstyle="secondary.TFrame")
    header.pack(fill=ttk.X, pady=(0, 15))
    
    title = ttk.Label(
        header,
        text="Welcome to Ghost Theme!",
        font=("Host Grotesk", 16, "bold")
    )
    title.configure(background=root.style.colors.get("secondary"))
    title.pack(pady=20, padx=20)
    
    # Content card
    content = RoundedFrame(container, radius=15, bootstyle="dark.TFrame")
    content.pack(fill=ttk.BOTH, expand=True, pady=(0, 15))
    
    content_title = ttk.Label(
        content,
        text="Quick Start",
        font=("Host Grotesk", 12, "bold")
    )
    content_title.configure(background=root.style.colors.get("dark"))
    content_title.pack(pady=(15, 10), padx=15, anchor=ttk.W)
    
    ttk.Separator(content, orient="horizontal").pack(fill=ttk.X, padx=15, pady=(0, 10))
    
    instructions = [
        "1. Import components from the components module",
        "2. Use RoundedFrame for containers",
        "3. Use RoundedButton for interactive elements",
        "4. Customize colors in theme.json",
        "5. Build something amazing!",
    ]
    
    for instruction in instructions:
        label = ttk.Label(
            content,
            text=instruction,
            font=("Host Grotesk", 10)
        )
        label.configure(background=root.style.colors.get("dark"))
        label.pack(pady=2, padx=15, anchor=ttk.W)
    
    ttk.Label(content, text="").pack(pady=5)  # Spacer
    
    # Buttons
    button_frame = ttk.Frame(container)
    button_frame.pack(fill=ttk.X)
    
    primary_btn = RoundedButton(
        button_frame,
        text="Primary Action",
        bootstyle="primary.TButton",
        command=on_button_click,
        radius=8,
        padx=20,
        pady=10
    )
    primary_btn.pack(side=ttk.LEFT, expand=True, fill=ttk.X, padx=(0, 5))
    
    success_btn = RoundedButton(
        button_frame,
        text="Success Action",
        bootstyle="success.TButton",
        command=on_button_click,
        radius=8,
        padx=20,
        pady=10
    )
    success_btn.pack(side=ttk.LEFT, expand=True, fill=ttk.X, padx=(5, 0))
    
    # Run the application
    root.mainloop()


if __name__ == "__main__":
    create_simple_app()
