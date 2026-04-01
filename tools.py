import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP for Nanobot
mcp = FastMCP("AudioForge")

WHISPER_URL = "http://localhost:9000/v1/audio/transcriptions"
KOKORO_URL = "http://localhost:8880/v1/audio/speech"

@mcp.tool()
async def listen_to_audio(file_path: str) -> str:
    """Transcribes an audio file into text using Whisper."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        with open(file_path, "rb") as f:
            files = {"file": (file_path, f, "audio/mpeg")}
            resp = await client.post(WHISPER_URL, files=files, data={"model": "whisper-1"})
        
        text = resp.json().get("text", "Error: No transcription found.")
        return f"Transcription: {text}"

@mcp.tool()
async def speak_text(text: str, voice: str = "af_heart") -> str:
    """Converts text to an mp3 file using Kokoro TTS."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(KOKORO_URL, json={"input": text, "voice": voice})
        
        if resp.status_code == 200:
            with open("output.mp3", "wb") as f:
                f.write(resp.content)
            return "Speech generated and saved to output.mp3"
        return f"Error: Failed to generate speech (Status {resp.status_code})"

if __name__ == "__main__":
    mcp.run()