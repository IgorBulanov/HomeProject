'''
Created on 11 мая 2018 г.

@author: Igor
'''
import tkinter as tk
from tkinter import ttk

class ScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kw):
        self.parent = parent
        tk.Frame.__init__(self, parent, *args, **kw)
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False)
        self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=False)

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                                relief = 'groove',
                                yscrollcommand=self.vscrollbar.set,
                                xscrollcommand=self.hscrollbar.set)
        self.canvas.configure(yscrollincrement='6', xscrollincrement='6')
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #
        self.vscrollbar.config(command=self.canvas.yview)
        self.hscrollbar.config(command=self.canvas.xview)
        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas)  #.canvas
        self.canvas.create_window(0, 0, window=self.interior, anchor=tk.NW) #

        self.vscrollbar.lift(self.interior)
        self.hscrollbar.lift(self.interior)

        self.interior.bind('<Configure>', self._configure_interior)
        self.interior.bind('<Enter>', self._bound_to_mousewheel)
        self.interior.bind('<Leave>', self._unbound_to_mousewheel)

    def _bound_to_mousewheel(self, event):
        #        self.canvas.bind("<MouseWheel>", self._on_mousewheel_vertical)
        self.canvas.bind_all('<Button-4>', lambda event: self._on_mousewheel_vertical(event))
        self.canvas.bind_all('<Button-5>', lambda event: self._on_mousewheel_vertical(event))
        self.canvas.bind_all('<Control-Button-4>', lambda event: self._on_mousewheel_horizontal(event))
        self.canvas.bind_all('<Control-Button-5>', lambda event: self._on_mousewheel_horizontal(event))

    def _unbound_to_mousewheel(self, event):
        #        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")
        self.canvas.unbind_all("<Control-Button-4>")
        self.canvas.unbind_all("<Control-Button-5>")

    def _on_mousewheel_vertical(self, event):
        direction = 0
        if event.num == 5 or event.delta == -120:
            direction = 1
        if event.num == 4 or event.delta == 120:
            direction = -1
        self.canvas.yview_scroll(direction, tk.UNITS)
    #        event.widget.yview_scroll(direction, tk.UNITS)

    def _on_mousewheel_horizontal(self, event):
        direction = 0
        if event.num == 5 or event.delta == -120:
            direction = 1
        if event.num == 4 or event.delta == 120:
            direction = -1
        self.canvas.xview_scroll(direction, tk.UNITS)
    #        event.widget.xview_scroll(direction, tk.UNITS)

    def _configure_interior(self, event):
        #self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        #print(self.canvas.bbox(tk.ALL))    #for debug only;
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas width to fit the inner frame
            self.canvas.config(width = self.interior.winfo_reqwidth())
        if self.interior.winfo_reqheight() != self.canvas.winfo_height():
            # update the canvas width to fit the inner frame
            self.canvas.config(height = self.interior.winfo_reqheight())

