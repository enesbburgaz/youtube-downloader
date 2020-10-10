from flask import Flask,render_template,request,send_file
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

link = None
yt = None
@app.route("/search", methods = ["GET","POST"])
def videoInfo():
    global link, yt
    link = request.form.get("link")
    try:
        yt = YouTube(link)
        """
        videoViews = yt.views
        videoLen = yt.length
        videoDes = yt.description
        videoRating = yt.rating
        videoAudio = yt.streams.filter(only_audio=True)
        videoVideo = yt.streams.filter(only_video=True)
        videoQuality = yt.streams.filter(progressive=True)
        videoHighest = yt.streams.get_highest_resolution()
        """
        data =[{
            'title': yt.title,
            'description': yt.description,
        }]
        return render_template("index.html", data = data)
    except:
        return render_template("index.html", result = "Video şifreli. Lütfen başka bir video indirmeyi deneyiniz...")

@app.route("/download/<string:id>", methods = ["GET", "POST"])
def download(id):
    try:
        ys = yt.streams.get_by_itag('{0}'.format(id))
        dwn = ys.download()
        return send_file(dwn, as_attachment=True)
    except:
        pass

if __name__ == "__main__":
    app.run(debug = True)