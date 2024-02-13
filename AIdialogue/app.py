from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# ASR 파이프라인 초기화
asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")

# TTS 파이프라인 초기화
tts_pipeline = pipeline("text-to-speech", model="suno/bark")

# Fill-Mask 파이프라인 초기화
fill_mask_pipeline = pipeline("fill-mask", model="FacebookAI/xlm-roberta-large")

# 번역 파이프라인 초기화
translation_pipeline = pipeline("translation", model="facebook/mbart-large-50-many-to-many-mmt")

# 텍스트 생성 파이프라인 초기화
text_generation_pipeline = pipeline("text-generation", model="HuggingFaceM4/VLM_WebSight_finetuned", trust_remote_code=True)

@app.route('/asr', methods=['POST'])
def automatic_speech_recognition():
    audio_file = request.files['audio']
    # ASR 처리
    result = asr_pipeline(audio_file)
    return jsonify(result)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    # TTS 처리
    result = tts_pipeline(text)
    return jsonify(result)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    # 번역 처리
    result = translation_pipeline(text)
    return jsonify(result)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    text = request.form['text']
    # 텍스트 생성 처리
    result = text_generation_pipeline(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
