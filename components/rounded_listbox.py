import sys
from tkinter import Listbox, StringVar, END, Frame
import ttkbootstrap as ttk


class RoundedListbox(Frame):
    """
    A custom listbox widget with Ghost theme styling and scrollbar.
    
    This component wraps a tkinter.Listbox with a scrollbar to match the Ghost theme
    with proper color palette and border styling.
    
    Args:
        parent: The parent widget
        values: List of initial values for the listbox
        height: Number of visible rows
        selectmode: Selection mode ('single', 'browse', 'multiple', 'extended')
        font: Font tuple (family, size, weight)
    """
    def __init__(self, parent, values=None, height=6, selectmode="browse", **kwargs):
        self.parent = parent
        self.root = parent.winfo_toplevel()
        self.style = self.root.style
        self.custom_values = values or []
        
        # Get Ghost theme colors
        self.bg_color = self.style.colors.get("inputbg")
        self.fg_color = self.style.colors.get("inputfg")
        self.select_bg = self.style.colors.get("primary")
        self.select_fg = self.style.colors.get("selectfg")
        self.border_color = self.style.colors.get("selectbg")
        self.border_color_focus = self.style.colors.get("primary")
        
        # Remove custom kwargs
        kwargs.pop("bootstyle", None)
        kwargs.pop("radius", None)
        custom_font = kwargs.pop("font", None)
        
        # Initialize the Frame container
        super().__init__(parent, bg=self.border_color, highlightthickness=0)
        
        # Create inner container for border effect
        self.inner_frame = Frame(self, bg=self.border_color, highlightthickness=2,
                                highlightbackground=self.border_color, highlightcolor=self.border_color_focus)
        self.inner_frame.pack(fill="both", expand=True)
        
        # Set default font
        if custom_font is None:
            custom_font = ("Host Grotesk", 10) if sys.platform != "darwin" else ("Host Grotesk",)
        
        # Create the Listbox
        self.listbox = Listbox(
            self.inner_frame,
            bg=self.bg_color,
            fg=self.fg_color,
            selectbackground=self.select_bg,
            selectforeground=self.select_fg,
            highlightthickness=0,
            relief="flat",
            borderwidth=0,
            activestyle="none",
            height=height,
            selectmode=selectmode,
            font=custom_font,
            **kwargs
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        
        # Create styled scrollbar
        self.scrollbar = ttk.Scrollbar(self.inner_frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        
        # Configure listbox to use scrollbar
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        
        # Insert initial values
        if self.custom_values:
            for value in self.custom_values:
                self.listbox.insert(END, value)
        
        # Bind events for hover and focus effects
        self.listbox.bind("<Enter>", self._on_enter)
        self.listbox.bind("<Leave>", self._on_leave)
        self.listbox.bind("<FocusIn>", self._on_focus_in)
        self.listbox.bind("<FocusOut>", self._on_focus_out)
        
        # Prevent mouse wheel from propagating to parent
        self.listbox.bind("<MouseWheel>", self._on_mousewheel)
        self.listbox.bind("<Button-4>", self._on_mousewheel)
        self.listbox.bind("<Button-5>", self._on_mousewheel)
        
        # Track if mouse is over the widget
        self.is_hovering = False

    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling - prevent propagation to parent"""
        if sys.platform == "win32":
            self.listbox.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif sys.platform == "darwin":
            self.listbox.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.listbox.yview_scroll(-1, "units")
            elif event.num == 5:
                self.listbox.yview_scroll(1, "units")
        return "break"  # Prevent event from propagating to parent

    def _on_enter(self, event=None):
        """Handle mouse enter - change border to purple"""
        self.is_hovering = True
        self.inner_frame.configure(highlightbackground=self.border_color_focus)
        
    def _on_leave(self, event=None):
        """Handle mouse leave - reset border if not focused"""
        self.is_hovering = False
        # Only reset if not focused
        if self.focus_get() != self.listbox:
            self.inner_frame.configure(highlightbackground=self.border_color)
    
    def _on_focus_in(self, event=None):
        """Handle focus in - purple border"""
        self.inner_frame.configure(highlightbackground=self.border_color_focus)
    
    def _on_focus_out(self, event=None):
        """Handle focus out - gray border if not hovering"""
        if not self.is_hovering:
            self.inner_frame.configure(highlightbackground=self.border_color)

    def set_values(self, values):
        """Replace all items in the listbox"""
        self.listbox.delete(0, END)
        for value in values:
            self.listbox.insert(END, value)
    
    def get_selected(self):
        """Get the currently selected item(s)"""
        selection = self.listbox.curselection()
        if not selection:
            return None
        if len(selection) == 1:
            return self.listbox.get(selection[0])
        return [self.listbox.get(i) for i in selection]
    
    def get_selected_index(self):
        """Get the index of the currently selected item(s)"""
        selection = self.listbox.curselection()
        if not selection:
            return None
        if len(selection) == 1:
            return selection[0]
        return list(selection)
    
    # Delegate common Listbox methods to the internal listbox
    def insert(self, index, *elements):
        """Insert elements at the given index"""
        return self.listbox.insert(index, *elements)
    
    def delete(self, first, last=None):
        """Delete elements from first to last index"""
        return self.listbox.delete(first, last)
    
    def get(self, first, last=None):
        """Get elements from first to last index"""
        return self.listbox.get(first, last)
    
    def curselection(self):
        """Return tuple of selected indices"""
        return self.listbox.curselection()
    
    def selection_set(self, first, last=None):
        """Set selection to items between first and last"""
        return self.listbox.selection_set(first, last)
    
    def selection_clear(self, first, last=None):
        """Clear selection between first and last"""
        return self.listbox.selection_clear(first, last)
    
    def size(self):
        """Return the number of items in the listbox"""
        return self.listbox.size()