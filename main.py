"""
Application that adds a simple text watermark to an image of your choosing.
"""

from tkinter import Tk
from watermarking_view import WatermarkingView
from watermarking_model import WatermarkingModel
from watermarking_controller import WatermarkingController

window = Tk()
model = WatermarkingModel()
view = WatermarkingView(window)
controller = WatermarkingController(model, view)


window.mainloop()
