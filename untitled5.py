# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JHickkvjU7NjUb2c_aiOBCEQpql29N2d
"""

from gtts import gTTS

text = "My name is Maftuna"

language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)