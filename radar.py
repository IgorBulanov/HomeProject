'''
Created on 1 мая 2018 г.

@author: Igor
'''
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np

import tkinter as tk
from tkinter import ttk

import radar.mainApp as app

if __name__ == '__main__':
    global theApp
    theApp = app.Application()
    theApp.run()
