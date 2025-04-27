from flask import Flask, render_template_string, redirect, url_for
import random

app = Flask(__name__)

# 문제-답 리스트
quiz_data = [
    ("a.find('abc')", "문자열 a에 'abc'가 들어간 위치 반환"),
    ("a.startswith('abc')", "문자열 a는 'abc'로 시작하는 문자열 여부 반환"),
    ("a.endswith('abc')", "문자열 a는 'abc'로 끝나는 문자열 여부 반환"),
    ("a.strip()", "좌우 공백 없앰"),
    ("a.rstrip()", "오른쪽 공백 없앰"),
    ("a.lstrip()", "왼쪽 공백을 없앰"),
    ("a.isdigit()", "문자열이 숫자인지 여부 반환"),
    ("a.islower()", "문자열이 소문자인지 여부 반환")
]

# HTML 코드 직접 파이썬 안에 작성
html_template = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>랜덤 퀴즈</title>
</head>
<body>
    <h1>🧠 랜덤 퀴즈</h1>

    <h2>문제:</h2>
    <p><strong>{{ question }}</strong></p>

    <h2>정답:</h2>
    <p>{{ answer }}</p>

    <form action="{{ url_for('index') }}">
        <button type="submit">다음 문제 보기</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    question, answer = random.choice(quiz_data)
    return render_template_string(html_template, question=question, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
