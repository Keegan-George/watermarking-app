"""
Application that adds a simple text watermark to an image of your choosing.
"""

from tkinter import Tk
from watermarking_view import WatermarkingView

window = Tk()
view = WatermarkingView(window)
