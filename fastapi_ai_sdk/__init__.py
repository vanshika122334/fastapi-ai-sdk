"""
FastAPI AI SDK - A Pythonic helper library for Vercel AI SDK backend implementation.

This library provides a complete set of utilities for building FastAPI backends
that are compatible with the Vercel AI SDK frontend.
"""

from .models import (
    # Message lifecycle
    StartEvent,
    FinishEvent,
    # Text parts
    TextStartEvent,
    TextDeltaEvent,
    TextEndEvent,
    # Reasoning parts
    ReasoningStartEvent,
    ReasoningDeltaEvent,
    ReasoningEndEvent,
    # Source references
    SourceURLEvent,
    SourceDocumentEvent,
    # File reference
    FileEvent,
    # Structured data
    DataEvent,
    # Tool calls
    ToolInputStartEvent,
    ToolInputDeltaEvent,
    ToolInputAvailableEvent,
    ToolOutputAvailableEvent,
    # Steps
    StartStepEvent,
    FinishStepEvent,
    # Error
    ErrorEvent,
    # Base
    StreamEvent,
)
from .stream import AIStreamBuilder, AIStream
from .response import create_ai_stream_response
from .decorators import ai_endpoint, streaming_endpoint, tool_endpoint

__version__ = "0.1.0"

__all__ = [
    # Models
    "StartEvent",
    "FinishEvent",
    "TextStartEvent",
    "TextDeltaEvent",
    "TextEndEvent",
    "ReasoningStartEvent",
    "ReasoningDeltaEvent",
    "ReasoningEndEvent",
    "SourceURLEvent",
    "SourceDocumentEvent",
    "FileEvent",
    "DataEvent",
    "ToolInputStartEvent",
    "ToolInputDeltaEvent",
    "ToolInputAvailableEvent",
    "ToolOutputAvailableEvent",
    "StartStepEvent",
    "FinishStepEvent",
    "ErrorEvent",
    "StreamEvent",
    # Stream utilities
    "AIStreamBuilder",
    "AIStream",
    # Response helpers
    "create_ai_stream_response",
    # Decorators
    "ai_endpoint",
    "streaming_endpoint",
    "tool_endpoint",
]
