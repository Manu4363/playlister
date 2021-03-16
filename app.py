from flask import Flask, render_template

app = Flask(__name__)

playlists = [
    {'title' : 'Tennis videos', 'description' : 'All videos about tennis'},
    {'title' : 'Flask series', 'description' : 'All flask series videos and tutorials'}
]

@app.route('/')
def playlists_index():
    return render_template('playlists_index.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)