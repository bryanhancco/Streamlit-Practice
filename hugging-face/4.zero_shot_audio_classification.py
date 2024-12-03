from datasets import load_dataset
from transformers import pipeline
from datasets import Audio

dataset = load_dataset("ashraq/esc50",
                       split="train[0:10]")
audio_sample = dataset[0]

zero_shot_classifier = pipeline(
    task="zero-shot-audio-classification",
    model="laion/clap-htsat-unfused")

dataset = dataset.cast_column(
    "audio",
     Audio(sampling_rate=48_000))
audio_sample = dataset[0]

candidate_labels = ["Sound of a child crying",
                    "Sound of vacuum cleaner",
                    "Sound of a bird singing",
                    "Sound of an airplane"]
classification = zero_shot_classifier(audio_sample["audio"]["array"],
                     candidate_labels=candidate_labels)
print(classification)