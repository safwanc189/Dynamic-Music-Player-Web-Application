from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tracks = [
        {"name": "Let Her Go", "file": "track1.mp3", "image": "track1.jpeg"},
        {"name": "Choolo", "file": "track2.mp3", "image": "track2.jpeg"},
        {"name": "7 Years", "file": "track3.mp3", "image": "track3.jpeg"},
        {"name": "fukumean", "file": "track4.mp3", "image": "track4.jpg"},
        {"name": "Father Stretch", "file": "track5.mp3", "image": "track5.jpeg"},
    ]
    return render_template('index.html', tracks=tracks)

if __name__ == '__main__':
    app.run(debug=True)
