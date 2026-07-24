from fastapi import APIRouter
from pydantic import BaseModel
from google import genai
import os

router = APIRouter()

client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )


class VoiceRequest(BaseModel):
        question: str
        language: str


class VoiceResponse(BaseModel):
        answer: str


@router.post("/ask", response_model=VoiceResponse)
async def ask_ai(data: VoiceRequest):

        prompt = f"""
        You are CropSense AI, an agriculture assistant.

        Rules:
        - Answer only farming-related questions.
        - Help with crops, soil, irrigation, fertilizer, pests and diseases.
        - Reply in {data.language}.
        - Keep answers short and simple for farmers.

        Farmer question:
        {data.question}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return VoiceResponse(
            answer=response.text
        )