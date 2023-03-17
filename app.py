import random
from transformers import pipeline
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def generate_text():
    text = request.args.get('text', '')
    if not text:
        return 'No text provided.'
    model = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B', max_length=50, num_return_sequences=3, temperature=0.7)
    responses = model(text)
    sarcastic_responses = [f"Sure, because that's a great idea." for response in responses]
    response = random.choice(sarcastic_responses)
    response = 'Leon S. Kennedy: ' + response
    return response

if __name__ == '__main__':
    app.run()
