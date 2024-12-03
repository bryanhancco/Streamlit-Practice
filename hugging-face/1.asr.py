from transformers import pipeline
from transformers import TextGenerationPipeline 

chatbot = pipeline(
    task="text-generation",
    model="facebook/blenderbot-400M-distill"
)
user_message = """
What are some fun activities I can do in the winter?
"""

conversation = chatbot(user_message, do_sample=False)
print(conversation )