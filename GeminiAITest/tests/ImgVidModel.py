import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

api_key="GeminiAPIKEY"
if not api_key:
    # It's better to log this error and provide a user-friendly message
    # rather than crashing the server in production.
    # For now, we'll raise for clarity during development.
    raise ValueError("GOOGLE_API_KEY environment variable not set.")
genai.configure(api_key=api_key)

# Initialize the generative text model
text_model = genai.GenerativeModel("gemini-2.5-flash")

# Dictionary to hold chat sessions (for multi-user support, this would be per-user)
# For this example, we'll keep a simple global chat for the text model
global_text_chat = text_model.start_chat(history=[])

# --- Placeholder for a hypothetical Image Generation Service ---
# In a real application, you would replace this with actual API calls
# to services like DALL-E, Stability AI, or a custom model.
def generate_image_with_api(prompt):
    print(f"DEBUG: Calling image generation service with prompt: '{prompt}'")
    # Simulate an API call delay
    import time
    time.sleep(3)
    # Simulate a successful response with a placeholder image URL
    # Replace this with your actual image generation API integration
    # For example:
    #   response = requests.post("https://some-image-gen-api.com/generate", json={"prompt": prompt, "size": "512x512"})
    #   response.raise_for_status()
    #   data = response.json()
    #   image_url = data['images'][0]['url']

    # Using Unsplash source for dynamic, random images for demonstration
    # This will give a different image each time based on keywords from the prompt
    search_query = prompt.replace(" ", "%20") # URL encode the prompt
    return f"https://source.unsplash.com/random/500x500/?{search_query}"
    # return "https://via.placeholder.com/500x500.png?text=Generated+Image" # Generic placeholder

# --- Flask Routes ---

@app.route('/')
def index():
    return render_template('indexx.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = global_text_chat.send_message(user_message)
        return jsonify({"response": response.text, "type": "text"}) # Add type for frontend
    except Exception as e:
        print(f"Error in text chat: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/generate_image', methods=['POST'])
def generate_image_route():
    image_prompt = request.json.get('prompt')
    if not image_prompt:
        return jsonify({"error": "No image prompt provided"}), 400

    try:
        # Call the hypothetical image generation service
        image_url = generate_image_with_api(image_prompt)
        return jsonify({"image_url": image_url, "type": "image"})
    except Exception as e:
        print(f"Error in image generation: {e}")
        return jsonify({"error": f"Failed to generate image: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)