/**
 * Example Next.js component for integrating with FastAPI AI SDK backend.
 *
 * Installation:
 * npm install ai @ai-sdk/react
 */

"use client";

import { useChat } from "@ai-sdk/react";
import { useState } from "react";

export default function ChatComponent() {
  const [useTools, setUseTools] = useState(true);
  const [includeReasoning, setIncludeReasoning] = useState(true);

  const {
    messages,
    input,
    handleInputChange,
    handleSubmit,
    isLoading,
    error,
    data,
  } = useChat({
    api: "http://localhost:8000/api/chat",
    // Optional: Send additional body parameters
    body: {
      use_tools: useTools,
      include_reasoning: includeReasoning,
    },
    // Optional: Handle streaming data
    onFinish: (message) => {
      console.log("Message finished:", message);
    },
  });

  return (
    <div className="max-w-4xl mx-auto p-4">
      <div className="mb-4 space-y-2">
        <h1 className="text-2xl font-bold">FastAPI AI SDK Chat Demo</h1>

        <div className="flex gap-4">
          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={useTools}
              onChange={(e) => setUseTools(e.target.checked)}
            />
            <span>Use Tools</span>
          </label>

          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={includeReasoning}
              onChange={(e) => setIncludeReasoning(e.target.checked)}
            />
            <span>Include Reasoning</span>
          </label>
        </div>
      </div>

      <div className="border rounded-lg p-4 h-96 overflow-y-auto mb-4 bg-gray-50">
        {messages.length === 0 && (
          <p className="text-gray-500">Start a conversation...</p>
        )}

        {messages.map((message) => (
          <div
            key={message.id}
            className={`mb-4 ${
              message.role === "user" ? "text-right" : "text-left"
            }`}
          >
            <div
              className={`inline-block p-3 rounded-lg ${
                message.role === "user"
                  ? "bg-blue-500 text-white"
                  : "bg-white border"
              }`}
            >
              {/* Handle different part types */}
              {message.experimental_attachments?.map((attachment, i) => (
                <div key={i} className="mb-2">
                  {attachment.contentType?.startsWith("image/") && (
                    <img
                      src={attachment.url}
                      alt="Attachment"
                      className="max-w-xs rounded"
                    />
                  )}
                </div>
              ))}

              {/* Render message content */}
              <div className="whitespace-pre-wrap">{message.content}</div>

              {/* Render tool calls if any */}
              {message.toolInvocations?.map((tool, i) => (
                <div key={i} className="mt-2 p-2 bg-gray-100 rounded text-sm">
                  <div className="font-semibold">Tool: {tool.toolName}</div>
                  <div className="text-xs text-gray-600">
                    Input: {JSON.stringify(tool.args, null, 2)}
                  </div>
                  {tool.result && (
                    <div className="text-xs text-gray-600 mt-1">
                      Result: {JSON.stringify(tool.result, null, 2)}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="text-center text-gray-500">
            <span className="animate-pulse">AI is thinking...</span>
          </div>
        )}

        {error && (
          <div className="text-red-500 text-center">Error: {error.message}</div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Type your message..."
          className="flex-1 p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={isLoading}
          className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50"
        >
          Send
        </button>
      </form>

      {/* Display structured data if available */}
      {data && (
        <div className="mt-4 p-4 bg-gray-100 rounded-lg">
          <h3 className="font-semibold mb-2">Structured Data:</h3>
          <pre className="text-xs overflow-x-auto">
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

// Example usage in a Next.js page:
/*
// app/page.tsx
import ChatComponent from '@/components/ChatComponent'

export default function Home() {
  return (
    <main className="min-h-screen py-8">
      <ChatComponent />
    </main>
  )
}
*/

// Example with custom message rendering:
export function CustomMessageComponent({ message }: { message: any }) {
  return (
    <div className="message">
      {/* Render text parts */}
      {message.annotations?.map((annotation: any, i: number) => {
        if (annotation.type === "text") {
          return <span key={i}>{annotation.text}</span>;
        }

        // Render reasoning parts (usually hidden or styled differently)
        if (annotation.type === "reasoning") {
          return (
            <details key={i} className="my-2">
              <summary className="cursor-pointer text-gray-600 text-sm">
                Show reasoning
              </summary>
              <div className="p-2 bg-gray-50 rounded text-sm">
                {annotation.text}
              </div>
            </details>
          );
        }

        // Render custom data
        if (annotation.type?.startsWith("data-")) {
          const dataType = annotation.type.replace("data-", "");
          return (
            <div key={i} className="my-2 p-2 bg-blue-50 rounded">
              <div className="font-semibold text-sm">{dataType}:</div>
              <pre className="text-xs">
                {JSON.stringify(annotation.data, null, 2)}
              </pre>
            </div>
          );
        }

        return null;
      })}
    </div>
  );
}
