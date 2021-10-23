# -*- coding: utf-8 -*-
"""text-summarizer.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1jhmuUgWFqoClLMjSQB3wacCFEiW4JJ7v
"""

from transformers import pipeline

#downloading the model
model = pipeline("summarization", model="facebook/bart-large-cnn")



#buiding gradio function
def func(Text):
  return model(Text)

import gradio as gr

descriptions="This is an AI Text Summarizer. The AI system summarizes text, while still keeping the core points. Just paste the text you want to summarized in the text box and watch AI work!! BUILT BY EDEM GOLD"

app = gr.Interface(fn=func, inputs="textbox", outputs="textbox", title="Text Summarizer", description=descriptions)

app.launch()

