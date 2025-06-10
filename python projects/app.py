from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    band_name = ""
    if request.method == "POST":
        city = request.form.get("city")
        pet = request.form.get("pet")
        band_name = city + pet
    return render_template("index.html", band_name=band_name)

# Render requires this format
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
