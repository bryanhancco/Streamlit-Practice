from transformers import pipeline 
import torch


### Translation pipeline

translator = pipeline(
    task="translation_EN_to_FR",
    model="google-t5/t5-base",
    torch_dtype=torch.bfloat16) 

text = """\
My puppy is adorable, \
Your kitten is cute.
Her panda is friendly.
His llama is thoughtful. \
We all have nice pets!"""

text_translated = translator(text)

print(text_translated)

### Free memory
import gc
del translator
gc.collect()

### Summarizing pipeline

summarizer = pipeline(task="summarization",
                      model="facebook/bart-large-cnn",
                      torch_dtype=torch.bfloat16)

text = """Paris is the capital and most populous city of France, with
          an estimated population of 2,175,601 residents as of 2018,
          in an area of more than 105 square kilometres (41 square
          miles). The City of Paris is the centre and seat of
          government of the region and province of Île-de-France, or
          Paris Region, which has an estimated population of
          12,174,880, or about 18 percent of the population of France
          as of 2017."""
          
summary = summarizer(text,
                     min_length=10,
                     max_length=100)

print(summary)