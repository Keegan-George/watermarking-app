from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk, ImageFont
from styling import *


class Watermarking:
    def __init__(self):
        self.window = Tk()
        self.window.title("Watermarking Application")
        self.window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING)
        self.tk_img = None  # required to prevent image being garbage collection after the function completes
        self.pil_img = None
        self.output = None

        # ui widgets
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.upload_image_button = Button(
            text="Upload Image", command=self.upload_image
        )
        self.watermark_label = Label(text="Watermark text:")
        self.watermark_input = Entry(width=55)
        self.apply_watermark_button = Button(
            text="Apply Watermark", command=self.apply_watermark
        )
        self.save_button = Button(text="Save Image", command=self.save_image)
        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
            text="Upload an image to start",
            anchor=CENTER,
        )

        # widget grid positions
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.upload_image_button.grid(row=1, column=0)
        self.watermark_label.grid(row=2, column=0)
        self.watermark_input.grid(row=2, column=1)
        self.apply_watermark_button.grid(row=2, column=2)
        self.save_button.grid(row=2, column=3)

        self.window.mainloop()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        self.pil_img = Image.open(file_path).convert("RGBA")
        self.display_image_in_canvas(self.pil_img)

    def apply_watermark(self):
        if self.pil_img:
            # create fully transparent watermark image
            watermark_img = Image.new("RGBA", self.pil_img.size, (255, 255, 255, 0))

            # create draw context for the watermark image
            draw = ImageDraw.Draw(watermark_img)

            # set watermark font size as a percentage of the image size
            img_width, img_height = watermark_img.size
            font = ImageFont.truetype(
                font=FONT, size=int(FONT_SIZE_PERCENTAGE * img_height)
            )

            # get size of a bounding box around the watermark text
            watermark_text = self.watermark_input.get()
            _, _, watermark_width, watermark_height = draw.textbbox(
                xy=(0, 0), text=watermark_text, font=font
            )

            # determine coordinates to center the watermark
            watermark_position = (
                (img_width - watermark_width) // 2,
                (img_height - watermark_height) // 2,
            )

            draw.text(
                xy=watermark_position,
                text=watermark_text,
                fill=FONT_COLOUR,
                font=font,
            )

            self.output = Image.alpha_composite(self.pil_img, watermark_img)

            self.display_image_in_canvas(self.output)

    def save_image(self):
        if self.output:
            self.output.save(f"added_watermark.png")

    def display_image_in_canvas(self, image: Image):
        resized_image = image.resize((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.tk_img = ImageTk.PhotoImage(image=resized_image)
        self.canvas.create_image(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.tk_img
        )
