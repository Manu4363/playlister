from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists

# playlists = [
#     {'title' : 'Tennis videos', 'description' : 'All videos about tennis'},
#     {'title' : 'Flask series', 'description' : 'All flask series videos and tutorials'}
# ]

# Function to build the URL with the video ids
def video_url_creator(id_lst):
    videos = []
    for vid_id in id_lst:
        # We know that embedded YouTube videos always have this format
        video = 'https://youtube.com/embed/' + vid_id
        videos.append(video)
    return videos

@app.route('/')
def playlists_index():
    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """ SUBLIT A NEW PLAYLIST """
    # Grab the video IDs and make a list out of them
    video_ids = request.form.get('video_ids').split()
    # call our helper function to create the list of links
    videos = video_url_creator(video_ids)
    playlist = {
        'title' : request.form.get('title'),
        'description' : request.form.get('description'),
        'videos' : videos,
        'video_ids': video_ids
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_show'))

@app.route('/playlists/new')
def playlists_new():
    return render_template('playlists_new.html')


@app.route('/playlists/<playlist_id>')
def playlists_show(playlist_id):
    """ SHOW A SINGLE PLAYLIST """
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_show.html', playlist=playlist)


if __name__ == '__main__':
    app.run(debug=True)