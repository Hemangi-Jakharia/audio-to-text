# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:33:46 2022

@author: Hemangi
"""

# A python package for music and audio analysis.
# https://librosa.org/doc/latest/index.html
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# load model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# use below link to download other mode
# https://github.com/pytorch/fairseq/tree/master/examples/wav2vec#wav2vec-20

# The base model pretrained and fine-tuned on 960 hours of Librispeech on 16kHz sampled speech audio.
# When using the model make sure that your speech input is also sampled at 16Khz.

# load any audio file of your choice
collection_of_text = []
for i in range(2):

    speech, rate = librosa.load(f"sales_call_telephone_marketers.wav", sr=16000)

    input_values = tokenizer(speech, return_tensors='pt').input_values
    # Store logits (non-normalized predictions)
    with torch.no_grad():
        logits = model(input_values).logits

    # Store predicted id's
    predicted_ids = torch.argmax(logits, dim=-1)
    # decode the audio to generate text
    # Passing the prediction to the tokenzer decode to get the transcription
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    # transcriptions = tokenizer.decode(predicted_ids[0])
    # print(transcription)
    collection_of_text.append(transcription)

# print(collection_of_text)
final_complete_speech = ""

# convert batch of text into one complete sentence
for i in collection_of_text:
    final_complete_speech += i

print(final_complete_speech)

# use this code to install Spacy
# pip install -U pip setuptools wheel
# pip install -U spacy
import en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_lg")
doc = nlp(final_complete_speech.lower())
for i in doc.i:
    print(i.text, i.label)