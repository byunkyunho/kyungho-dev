from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # 디버그 모드로 실행하여 수정 사항이 바로 반영되도록 함
    app.run(debug=True, port=5000, host="0.0.0.0")