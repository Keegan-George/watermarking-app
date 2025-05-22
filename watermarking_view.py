from tkinter import *
from config import *


class WatermarkingView:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title(TITLE)
        self.root.config(padx=PADDING, pady=PADDING)

        # canvas area
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
            text="Upload an image to start",
            anchor=CENTER,
        )

        # upload image button
        self.upload_image_button = Button(
            text="Upload Image", command=self.upload_image
        )
        self.upload_image_button.grid(row=1, column=0)

        # watermark label
        self.watermark_label = Label(text="Watermark text:")
        self.watermark_label.grid(row=2, column=0)

        # watermark input field
        self.watermark_input = Entry(width=55)
        self.watermark_input.grid(row=2, column=1)

        # apply watermark button
        self.apply_watermark_button = Button(
            text="Apply Watermark", command=self.apply_watermark
        )
        self.apply_watermark_button.grid(row=2, column=2)

        # save image button
        self.save_button = Button(text="Save Image", command=self.save_image)
        self.save_button.grid(row=2, column=3)
