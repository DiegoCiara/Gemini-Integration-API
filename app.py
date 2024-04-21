import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

api_key = os.getenv("API_KEY_GEMINI")

if not api_key:
    raise ValueError("API_KEY_GEMINI não encontrada. Verifique se a variável de ambiente está configurada corretamente.")

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

instructions_folder = "system_instructions"
if not os.path.exists(instructions_folder):
    os.makedirs(instructions_folder)

instruction_files = os.listdir(instructions_folder)

all_instructions = ""

for file_name in instruction_files:
    file_path = os.path.join(instructions_folder, file_name)
    if os.path.isfile(file_path): 
        with open(file_path, "r") as f:
            all_instructions += f.read() + "\n"

system_instruction = all_instructions.strip()


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)


@app.route("/gemini", methods=["POST"])
def gemini_response():
    history = request.json.get("history", [])
    user_input = request.json.get("user_input")
    convo = model.start_chat(history=history)
    convo.send_message(user_input)

    response = {"response": convo.last.text}
    return jsonify(response)

if __name__ == "__main__":
    app.run()