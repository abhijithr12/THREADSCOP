from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, nullable=True)  


if os.path.exists("community.db"):
    os.remove("community.db")

with app.app_context():
    db.create_all()


@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    posts_data = [{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "date_posted": post.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": post.user_id
    } for post in posts]
    return jsonify(posts_data)


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    if not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content are required"}), 400
    
    new_post = Post(
        title=data["title"],
        content=data["content"],
        user_id=data.get("user_id")  
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
