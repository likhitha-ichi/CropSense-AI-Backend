from fastapi import APIRouter
from pydantic import BaseModel
import google.generativeai as genai
import os

router = APIRouter()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
for m in genai.list_models():
    print(m.name)
model = genai.GenerativeModel("gemini-2.0-flash")


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
    - Support crop prediction, weather, irrigation, soil health, fertilizer, pests and diseases.
    - Reply in {data.language}.
    - Keep answers short (2-5 sentences).
    - Use simple language a farmer can understand.
    - If the question is unrelated to farming, politely say you only answer agriculture questions.

    Farmer's Question:
    {data.question}
    """

    response = model.generate_content(prompt)

    return VoiceResponse(
        answer=response.text
    )