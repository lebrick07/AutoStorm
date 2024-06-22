# from flask import Blueprint, render_template, request, jsonify, current_app
# import openai

# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

# @main.route('/api/generate', methods=['POST'])
# def generate():
#     data = request.json
#     prompt = data.get('prompt')
#     openai.api_key = current_app.config['OPENAI_API_KEY']
#     response = openai.Completion.create(
#         engine="davinci-codex",
#         prompt=prompt,
#         max_tokens=100
#     )
#     return jsonify(response=response.choices[0].text)
from flask import Blueprint, render_template, request, jsonify, current_app
import openai

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    openai.api_key = current_app.config['OPENAI_API_KEY']
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Use the appropriate model name
            prompt=prompt,
            max_tokens=100
        )
        return jsonify(response=response.choices[0].text)
    except Exception as e:
        return jsonify(error=str(e)), 500
