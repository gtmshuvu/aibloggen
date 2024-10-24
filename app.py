from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = 'AIzaSyC0_Xbc9ZyQ6koIfD3NVvXwofU0_G3JwPo'
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'

def generate_blog_content(prompt, max_tokens=500):
    headers = {'Content-Type': 'application/json'}
    data = {'prompt': prompt, 'max_tokens': max_tokens}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result.get('choices', [{}])[0].get('text', 'No content generated.')
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json.get('prompt')
    generated_content = generate_blog_content(content)
    return jsonify({"generated_content": generated_content})

if __name__ == '__main__':
    app.run(debug=True)
