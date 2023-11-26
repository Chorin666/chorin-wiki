from flask import Flask, render_template, request
import markdown
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        markdown_text = convert_to_markdown(user_input)
        save_to_file(markdown_text)
        return render_template('result.html', markdown_text=markdown_text)
    return render_template('index.html')

def convert_to_markdown(text):
    return markdown.markdown(text)

def save_to_file(text):
    with open('docs/index.html', 'w', encoding='utf-8') as file:
        file.write(f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Published Page</title></head><body>{text}</body></html>')

if __name__ == '__main__':
    os.makedirs('docs', exist_ok=True)
    app.run(debug=True)
