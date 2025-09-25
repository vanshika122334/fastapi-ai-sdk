"""
Simple chat example using FastAPI AI SDK.

Run with:
    uvicorn examples.simple_chat:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_ai_sdk import AIStreamBuilder, ai_endpoint

app = FastAPI(title="Simple Chat Example")

# Add CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/chat")
@ai_endpoint()
async def chat(message: str):
    """
    Simple chat endpoint that echoes the message back.

    Args:
        message: The user's message

    Returns:
        AI SDK compatible streaming response
    """
    builder = AIStreamBuilder()

    # Add different types of content
    builder.text(f"You said: {message}\n\n")
    builder.text("Let me respond with some streaming text...")

    return builder


@app.post("/api/chat-with-chunks")
@ai_endpoint()
async def chat_with_chunks(message: str):
    """
    Chat endpoint that streams response in chunks.

    Args:
        message: The user's message

    Returns:
        Chunked streaming response
    """
    builder = AIStreamBuilder()

    response = f"""
    Thank you for your message: "{message}"

    This is a longer response that will be streamed to you in chunks.
    Each chunk will appear gradually, creating a typewriter effect.

    This is useful for creating more engaging user experiences,
    especially when dealing with longer AI-generated responses.
    """

    # Stream in 20-character chunks
    builder.text(response.strip(), chunk_size=20)

    return builder


@app.get("/")
async def root():
    """Root endpoint with usage instructions."""
    return {
        "message": "Simple Chat API",
        "endpoints": [
            {
                "path": "/api/chat",
                "method": "POST",
                "description": "Simple chat endpoint",
                "params": {"message": "string"},
            },
            {
                "path": "/api/chat-with-chunks",
                "method": "POST",
                "description": "Chat with chunked response",
                "params": {"message": "string"},
            },
        ],
        "example_curl": 'curl -X POST "http://localhost:8000/api/chat" -d "message=Hello"',
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
