from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os
import requests
from fastapi.responses import StreamingResponse
from io import BytesIO

router = APIRouter()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class VoiceRequest(BaseModel):
    question: str
    language: str


class VoiceResponse(BaseModel):
    answer: str


@router.post("/ask", response_model=VoiceResponse)
async def ask_ai(data: VoiceRequest):

    prompt = f"""
    You are CropSense AI, an intelligent agriculture assistant.

    Rules:
    - Answer ONLY agriculture-related questions.
    - Help with crop recommendations, soil health, irrigation,
      fertilizer, weather, pests, and diseases.
    - Reply in {data.language}.
    - Keep answers short (2-5 sentences).
    - Use simple language that farmers can understand.
    - If the question is unrelated to farming, politely say
      you only answer agriculture questions.
      - Give practical agriculture advice.
      - If the question asks for fertilizer, crop recommendation, or disease treatment:
        ask for missing details like crop stage, soil type, location, and symptoms.
      - Never give dangerous chemical recommendations without context.
      - Keep answers simple for farmers.
      - For crop diseases or plant problems, explain possible causes, symptoms to check, and basic steps to solve the issue.

    Farmer's Question:
    {data.question}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are CropSense AI, an agriculture assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=300
    )

    return VoiceResponse(
        answer=response.choices[0].message.content
    )
@router.post("/speak")
async def speak(text: dict):

    api_key = os.getenv("ELEVENLABS_API_KEY")

    voice_id = "EXAVITQu4vr4xnSDxMaL"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text["text"],
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return {"error": response.text}

    return StreamingResponse(
        BytesIO(response.content),
        media_type="audio/mpeg"
    )