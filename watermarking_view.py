from config import *
from tkinter import *
from PIL import ImageTk


class WatermarkingView:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title(TITLE)
        self.root.config(padx=PADDING, pady=PADDING)
        self.display_img = None

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
        self.upload_image_button = Button(text="Upload Image")
        self.upload_image_button.grid(row=1, column=0)

        # watermark label
        self.watermark_label = Label(text="Watermark text:")
        self.watermark_label.grid(row=2, column=0)

        # watermark input field
        self.watermark_input = Entry(width=55)
        self.watermark_input.grid(row=2, column=1)

        # apply watermark button
        self.apply_watermark_button = Button(text="Apply Watermark")
        self.apply_watermark_button.grid(row=2, column=2)

        # save image button
        self.save_image_button = Button(text="Save Image")
        self.save_image_button.grid(row=2, column=3)

    def get_watermark_text(self) -> str:
        """
        Returns the text currently entered in the input field.
        """
        return self.watermark_input.get()

    def display_image(self, image: Image):
        """
        Display image in the UI.
        """
        # resize image to canvas dimensions
        resized_image = image.resize((CANVAS_WIDTH, CANVAS_HEIGHT))

        # initialize PhotoImage object
        self.display_img = ImageTk.PhotoImage(image=resized_image)

        # display image centered on canvas
        self.canvas.create_image(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.display_img
        )
