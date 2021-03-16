from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists

# playlists = [
#     {'title' : 'Tennis videos', 'description' : 'All videos about tennis'},
#     {'title' : 'Flask series', 'description' : 'All flask series videos and tutorials'}
# ]

@app.route('/')
def playlists_index():
    return render_template('playlists_index.html', playlists=playlists.find())

if __name__ == '__main__':
    app.run(debug=True)