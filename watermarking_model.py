class WatermarkingModel:
    def __init__(self):
        self.filepath = None
        self.tk_img = None  # required to prevent image being garbage collection after the function completes
        self.pil_img = None
        self.output = None
