from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os

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