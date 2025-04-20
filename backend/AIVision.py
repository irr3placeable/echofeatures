import base64
from openai import OpenAI

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


image_path = "foodtest.jpg"
 
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Please analyze the contents of the image and list the ingredients, foods, and quantities (e.g., cups, ounces, milliliters). Dont add any additional text other 'than the foods infront of you include' before the ingredients",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0])

import textwrap

def print_wrapped(text, width=80):
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)

print_wrapped(str(response.choices[0].message))