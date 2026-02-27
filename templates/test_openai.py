from google import genai

# paste your Gemini API key
client = genai.Client(api_key="AIzaSyBbDAQlEk4D3yu3tzHJSFi3lkaQujy0tpk")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Say hello in one sentence"
)

print(response.text)
