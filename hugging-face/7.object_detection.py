from transformers.utils import logging
from transformers import pipeline
from helper import load_image_from_url, render_results_in_image
from PIL import Image
logging.set_verbosity_error()

od_pipe = pipeline(task="object-detection", 
                   model="facebook/detr-resnet-50")

raw_image = Image.open('family.jpg')
raw_image.resize((569, 491))

pipeline_output = od_pipe(raw_image)
processed_image = render_results_in_image(
    raw_image, 
    pipeline_output)

processed_image.save('family_processed.jpg')
