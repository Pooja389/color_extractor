from flask import Flask , redirect,url_for,render_template,request,flash
from werkzeug.utils import secure_filename
import os
import colorgram
app = Flask(__name__)
app.secret_key = "pooja"

UPLOAD_FOLDER = 'color/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")


def get_top_colors(image_path):
    colors = colorgram.extract(image_path,10)
    top_colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]
    return top_colors

@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        flash("No file part")
        return redirect(url_for("home"))
    
    file = request.files["image"]
    

    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("home"))
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)  
        
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        print(f"File saved at: {filepath}")
        flash("Image uploaded successfully")


        top_colors = get_top_colors(filepath)
        return render_template("index.html", image_url=url_for('static', filename=f'uploads/{filename}'), top_colors=top_colors)


if __name__ == "__main__":
    app.run(debug=True)