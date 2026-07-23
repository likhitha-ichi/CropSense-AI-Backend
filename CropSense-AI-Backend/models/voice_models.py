from pydantic import BaseModel, Field


class VoiceQueryRequest(BaseModel):
    query: str = Field(..., min_length=1, description="The farmer's text question")
    language: str = Field("en", description="BCP-47 language code (e.g. 'en', 'hi', 'te')")

    model_config = {
        "json_schema_extra": {
            "example": {
                "query": "Which crop should I grow this season given low rainfall?",
                "language": "en",
            }
        }
    }


class VoiceQueryResponse(BaseModel):
    query: str
    intent: str = Field(..., description="Detected intent category")
    response: str
    language: str
    message: str = ""
