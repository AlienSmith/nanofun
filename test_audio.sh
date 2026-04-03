#nanobot agent -m "Run the full pipeline: 1. Transcribe /workspace/audio_in/test_voice.mp3. 2. Translate the output to English, add a funny quote to the end. 3. Pass the result to speak_text."
#nanobot agent -m "Transcribe /workspace/audio_in/test_voice.mp3. Then call speak_text with this schema: {'text': '[TRANSCRIPT] + funny remark'}. DO NOT skip the text parameter."
#nanobot agent -m "Do this in ONE go: Transcribe /workspace/audio_in/test_voice.mp3 AND immediately call speak_text with the output. Do not wait for my input between steps."
# nanobot agent -m "PIPELINE TASK: 
# 1. Transcribe /workspace/audio_in/test_voice.mp3.
# 2. Create a 'Final Message' by taking that transcription and appending a hilarious, sarcastic quote about AI or programmers.
# 3. Call speak_text with that 'Final Message'. 
# DO NOT wait for input. Execute the tools sequentially now."

# STRIKE 1: Get the raw transcript and save it to a variable
TRANSCRIPT=$(nanobot agent -m "Transcribe /workspace/audio_in/test_voice.mp3 and return ONLY the text.")

# STRIKE 2: Send that text back in a fresh session with the joke request
nanobot agent -m "Take this text: '$TRANSCRIPT'. Add a funny programmer quote to it and call the speak_text tool immediately."