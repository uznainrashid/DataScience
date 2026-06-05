from google import genai

# 1. Client Initialize karein aur apni Free Gemini API key yahan dalein
client = genai.Client(
    api_key="..............."
)

try:
    print("Gemini se connect ho raha hai...")
    # 2. Gemini 3.5 Flash model use kar rahe hain (Free and Flash Fast)
    response = client.chats.create(
        model='gemini-3.5-flash',
        config={ "system_instruction": "Your works is only find a error in code." }
    )
    response1 = response.send_message("kya kr rahy hoon?")
    print(response1.text)
except Exception as e:
    print(f"\nKoi error aaya hai: {e}")