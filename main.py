import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6LrYR4FGn93aDJ0q9JDQw7guatdKiOPwLm7T0Zt0UDaHw")

model = genai.GenerativeModel("gemini-2.5-flash")

print("🤖 My AI Agent")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(user)

    print("GOKUL:", response.text)