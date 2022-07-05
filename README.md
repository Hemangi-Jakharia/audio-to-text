# audio-to-text
The steps are explained in the code.
Step 1
A python package for music and audio analysis - https://librosa.org/doc/latest/index.html
Step 2 - load model and tokenizer
# The base model pretrained and fine-tuned on 960 hours of Librispeech on 16kHz sampled speech audio.
# When using the model make sure that your speech input is also sampled at 16Khz.
Step 3 -  load any audio file
Step 4
a) Store logits (non-normalized predictions)
b) Store predicted id's
c)decode the audio to generate text
  Passing the prediction to the tokenzer decode to get the transcription
  convert batch of text into one complete sentence
  
Step 5 Spacy to identitfy intent and keywords
