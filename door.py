from flask import Flask, render_template

app = Flask(__name__)

# 블로그 글 데이터 (예시)
blog_posts = [
    {"title": "첫 번째 포스트", "content": "안녕하세요, 첫 번째 블로그 포스트입니다!"},
    {"title": "두 번째 포스트", "content": "두 번째 글을 쓰는 중입니다."},
    # 추가적인 글은 필요에 따라 계속해서 추가할 수 있습니다.
]

@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
