from config import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from watermarking_view import WatermarkingView
from watermarking_model import WatermarkingModel


class WatermarkingController:
    def __init__(self, model: WatermarkingModel, view: WatermarkingView):
        self.model = model
        self.view = view
        self.view.upload_image_button.config(command=self.open_image)
        self.view.apply_watermark_button.config(command=self.apply_watermark)
        self.view.save_image_button.config(command=self.save_image)

    def open_image(self):
        """
        Open an image on your local.
        """
        self.model.filepath = filedialog.askopenfilename()
        self.model.pil_img = Image.open(self.model.filepath).convert("RGBA")
        self.view.display_image(self.model.pil_img)

    def save_image(self):
        """
        Save watermarked image.
        """
        if self.model.output_img:
            self.model.output_img.save(OUTPUT_FILENAME)

    def apply_watermark(self):
        """
        Apply watermark text to image.
        """
        if self.model.pil_img:
            # create fully transparent watermark image same size as the original
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
            watermark_text = self.view.get_watermark_text()
            _, _, watermark_width, watermark_height = draw.textbbox(
                xy=(0, 0), text=watermark_text, font=font
            )

            # determine coordinates to center the watermark
            watermark_position = (
                (img_width - watermark_width) // 2,
                (img_height - watermark_height) // 2,
            )

            # draw watermark text
            draw.text(
                xy=watermark_position,
                text=watermark_text,
                fill=FONT_COLOUR,
                font=font,
            )

            # combine original image with watermark text img
            self.model.output_img = Image.alpha_composite(
                self.model.pil_img, watermark_img
            )

            # display the new image
            self.view.display_image(self.model.output_img)
