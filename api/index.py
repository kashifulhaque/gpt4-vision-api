import base64
import requests

from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Header, File, UploadFile, HTTPException

app = FastAPI()

def validate_api_key(api_key: Optional[str] = Header(None)) -> None:
  if api_key is None:
    raise HTTPException(status_code = 400, detail = "OpenAI API key missing! 🙄")

@app.get("/api", description = "API Health check endpoint ❤️‍🩹")
def hello_world():
  return { "docs": "/api/docs" }

@app.post("/api/vision", description = "OpenAI's GPT-4 Vision API 👁️")
async def vision(question: str, image: UploadFile = File(...), api_key: Optional[str] = Header(None)):
  if len(question) == 0:
    raise HTTPException(status_code = 400, detail = "Empty question string! 🫙")
  
  validate_api_key(api_key)

  try:
    contents = await image.read()
    base64_image = base64.b64encode(contents).decode("utf-8")
    base64_image = f"data:image/jpeg;base64,{base64_image}"
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"Error processing image: {str(e)}")

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": question
          },
          {
            "type": "image_url",
            "image_url": {
              "url": base64_image
            }
          }
        ]
      }
    ],
    "max_tokens": 500
  }

  try:
    response = requests.post("https://api.openai.com/v1/chat/completions", headers = headers, json = payload)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    raise HTTPException(status_code = 500, detail = f"Error making request to OpenAI API: {str(e)}")

  data = {"gpt": response.json(), "question": question, "base64_image": base64_image}
  return JSONResponse(content = data, status_code = 200)
