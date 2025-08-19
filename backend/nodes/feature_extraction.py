import json
import os
import openai
from dotenv import load_dotenv
from backend.state import CarState
from typing import Dict, Optional, cast

load_dotenv()

client = openai.AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint=str(os.getenv("AZURE_OPENAI_ENDPOINT")),
)

def extract_text(state:CarState) -> CarState:

    text = state['filtered_input']

    prompt =(
        "A customer wants to sell their car. He provided the following description: "+text + "\n\n"
        "As a car sales expert, to list the car, we need to extract the following information:\n"
        "car's color, brand, model, manufactured year, motor size in cc, any notices mentioned, price and currency, you can extract extra information if you think is important\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-AS177",
            messages=[
                {"role": "system", "content": "You are a car sales expert that extracts car information from text and returns it in raw JSON format only, without any formatting."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
        )
        content = response.choices[0].message.content
        print(f"OpenAI API response: {content}")

        if content is not None:
            extracted = json.loads(content)
        else:
            extracted = ""
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
    
    print(f"Extracted data: {extracted}")
    state["output"] = cast(Dict[str, Optional[str]], extracted)
    print("input node")
    return state