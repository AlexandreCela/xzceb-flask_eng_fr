from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/englishToFrench')
def translate():
    """
    Translates English text to French.
    """
    english_text = request.args.get('textToTranslate')
    french_text = englishToFrench(english_text)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = frenchToEnglish(textToTranslate)
    # Write your code here
    return english_text

@app.route("/")
def renderIndexPage():
     """
    Renders the index.html file.
    """
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
