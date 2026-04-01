import sys, httpx, asyncio

async def speak(text):
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post("http://localhost:8880/v1/audio/speech", 
                                 json={"input": text, "voice": "af_heart"})
        with open("output.mp3", "wb") as f:
            f.write(resp.content)
    print("output.mp3") # Tell the LLM where the file is

if __name__ == "__main__":
    asyncio.run(speak(sys.argv[1]))