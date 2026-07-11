import google.generativeai as genai

genai.configure(api_key="GET AN API KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

print("🤖 My AI Agent")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(user)

    print("GOKUL:", response.text)
