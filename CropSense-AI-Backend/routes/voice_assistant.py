from fastapi import APIRouter, UploadFile, File, HTTPException
from models.voice_models import VoiceQueryRequest, VoiceQueryResponse


router = APIRouter()


@router.post("/query", response_model=VoiceQueryResponse, summary="Answer a text-based agriculture query")
def text_query(request: VoiceQueryRequest):
    """
    Process a text query about agriculture and return a spoken/written response.

    The voice assistant answers questions about crops, weather, soil, pests,
    and irrigation using the CropSense knowledge base.
    """
    # TODO: Integrate with an NLP model or LLM (e.g. OpenAI, Gemini, local LLaMA).
    # Route the parsed intent to the relevant backend service for a grounded answer.

    return VoiceQueryResponse(
        query=request.query,
        intent="general_agriculture",
        response=(
            "I'm your CropSense AI assistant. I can help you with crop recommendations, "
            "weather forecasts, soil health analysis, smart irrigation, and pest detection. "
            "Full NLP integration is coming soon!"
        ),
        language=request.language,
        message="Placeholder response – NLP model not yet connected.",
    )


@router.post("/transcribe", summary="Transcribe an audio file to text")
async def transcribe_audio(file: UploadFile = File(..., description="Audio file (WAV/MP3/OGG)")):
    """
    Transcribe a farmer's voice query from an audio recording.

    Accepted formats: WAV, MP3, OGG.
    Returns the transcribed text which can then be passed to /api/voice/query.
    """
    allowed_types = {"audio/wav", "audio/mpeg", "audio/ogg", "audio/x-wav"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported audio format '{file.content_type}'. Use WAV, MP3, or OGG.",
        )

    contents = await file.read()
    file_size_kb = len(contents) / 1024

    # TODO: Integrate with a speech-to-text service (e.g. Whisper, Google STT).
    # import whisper
    # model = whisper.load_model("base")
    # result = model.transcribe(audio_path)

    return {
        "transcription": "Placeholder – audio transcription not yet implemented.",
        "file_name": file.filename,
        "file_size_kb": round(file_size_kb, 2),
        "language_detected": "en",
    }


@router.get("/languages", summary="List supported languages")
def list_languages():
    """Return the languages supported by the voice assistant."""
    return {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "hi", "name": "Hindi"},
            {"code": "te", "name": "Telugu"},
            {"code": "ta", "name": "Tamil"},
            {"code": "kn", "name": "Kannada"},
            {"code": "mr", "name": "Marathi"},
            {"code": "gu", "name": "Gujarati"},
            {"code": "pa", "name": "Punjabi"},
        ]
    }
