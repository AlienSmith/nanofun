import sys, httpx, asyncio

async def transcribe(file_path):
    async with httpx.AsyncClient(timeout=60.0) as client:
        with open(file_path, "rb") as f:
            files = {"file": (file_path, f, "audio/mpeg")}
            resp = await client.post("http://localhost:9000/v1/audio/transcriptions", 
                                     files=files, data={"model": "whisper-1"})
        print(resp.json().get("text", ""))

if __name__ == "__main__":
    asyncio.run(transcribe(sys.argv[1]))