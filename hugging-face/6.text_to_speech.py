from transformers import pipeline
import soundfile as sf

narrator = pipeline("text-to-speech",
                    model="kakao-enterprise/vits-ljs")

text = """
Researchers at the Allen Institute for AI, \
HuggingFace, Microsoft, the University of Washington, \
Carnegie Mellon University, and the Hebrew University of \
Jerusalem developed a tool that measures atmospheric \
carbon emitted by cloud servers while training machine \
learning models. After a model’s size, the biggest variables \
were the server’s location and time of day it was active.
"""

narrated_text = narrator(text)

audio_data = narrated_text["audio"][0]
sf.write('narrated_audio.wav', audio_data, narrated_text["sampling_rate"])