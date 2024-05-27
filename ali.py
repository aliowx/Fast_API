"""

in this project, we wanna decide to create AI for the Translation with Python and
it's important to pip install the FastAPI and understand how to use that also 
The Pydantic library is used for validation and data management.

uvicorn ali:app --reload in the Terminal 

"""


from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Create an instance of FastAPI
app = FastAPI()

# Define a Pydantic model for the input data
class InputText(BaseModel):
    """
    This class acts as a data model for API input
    """
    text:str

# Define an endpoint for sentiment analysis
@app.post("/translate/")
async def translate(input_text: InputText):
    source_text = input_text.text
    source_language = "en"  # Default to English
    target_language = "fr"  # Default to French

    translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-{}-{}".format(source_language, target_language))

    translated_text = translation_pipeline(source_text, max_length=200)[0]["translation_text"]

    return {"translated_text": translated_text}

#Simple function to recognize terms
@app.post("/detect-idiom/")
async def detect_idiom(input_text: InputText):
    source_text = input_text.text
    # Add your idiom detection logic here
    detected_idioms = []

    return {"detected_idioms": detected_idioms}