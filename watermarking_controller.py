from config import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from watermarking_view import WatermarkingView
from watermarking_model import WatermarkingModel


class WatermarkingController:
    def __init__(self, model: WatermarkingModel, view: WatermarkingView):
        self.view = view
        self.model = model
        self.view.upload_image_button.config(command=self.upload_image)
        self.view.apply_watermark_button.config(command=self.apply_watermark)
        self.view.save_image_button.config(command=self.save_image)

    def upload_image(self):
        self.model.filepath = filedialog.askopenfilename()
        self.model.pil_img = Image.open(self.model.filepath).convert("RGBA")
        self.display_image_in_canvas(self.model.pil_img)

    def display_image_in_canvas(self, image: Image):
        resized_image = image.resize((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.model.tk_img = ImageTk.PhotoImage(image=resized_image)
        self.view.canvas.create_image(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.model.tk_img
        )

    def save_image(self):
        if self.model.output:
            self.model.output.save(f"added_watermark.png")

    def apply_watermark(self):
        if self.model.pil_img:
            # create fully transparent watermark image
            watermark_img = Image.new(
                "RGBA", self.model.pil_img.size, (255, 255, 255, 0)
            )

            # create draw context for the watermark image
            draw = ImageDraw.Draw(watermark_img)

            # set watermark font size as a percentage of the image size
            img_width, img_height = watermark_img.size
            font = ImageFont.truetype(
                font=FONT, size=int(FONT_SIZE_PERCENTAGE * img_height)
            )

            # get size of a bounding box around the watermark text
            watermark_text = self.view.watermark_input.get()
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

            self.model.output = Image.alpha_composite(self.model.pil_img, watermark_img)

            self.display_image_in_canvas(self.model.output)
