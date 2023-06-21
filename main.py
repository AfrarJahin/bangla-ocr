import gradio as gr
import easyocr


def decode_image_to_string(input_image):
    # Perform OCR on the input image
    reader = easyocr.Reader(['bn'])
    result = reader.readtext(input_image)

    # Extract and concatenate the detected text
    extracted_text = ' '.join([res[1] for res in result])

    return extracted_text


# Gradio interface
inputs = gr.inputs.Image()
outputs = gr.outputs.Textbox()
title = "Image to Bangla Text Decoder"
description = "Upload an image and get the decoded text in Bangla."

gr.Interface(decode_image_to_string, inputs, outputs, title=title, description=description).launch()
