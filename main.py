
import os
import google.generativeai as genai

# Ensure your API key is set in the environment variables
genai.configure(api_key=os.environ["zaSyAW5pgrcTIAIlVTm_YL9dIc1iNowU1ditjIg"])

# Create the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",  # Ensure this model name is correct
    generation_config=generation_config,
    system_instruction="Your role is to engage with students to help them learn languages like German, Korean, Spanish, and Russian, as well as assist with subjects like math, biology, geography, physics, English, and Afan Oromo. You can also converse in those languages.",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": ["hello"],
        },
        {
            "role": "model",
            "parts": ["Hello there! I'm excited to help you with your learning journey today. What would you like to work on? ..."],
        },
        {
            "role": "user",
            "parts": ["I want to learn Japanese\n"],
        },
        {
            "role": "model",
            "parts": ["Okay! While I don't have native fluency in Japanese..."],
        },
        {
            "role": "user",
            "parts": ["huh?"],
        },
        {
            "role": "model",
            "parts": ["You're right, I jumped right in! Sorry about that..."],
        },
    ]
)

# Replace "INSERT_INPUT_HERE" with actual user input
user_input = "What is the capital of Japan?"  # Example input
response = chat_session.send_message(user_input)

# Print the response
print(response.text)