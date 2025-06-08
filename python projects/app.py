from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    band_name = ""
    if request.method == "POST":
        city = request.form.get("city")
        pet = request.form.get("pet")
        band_name = city + pet
    return render_template("index.html", band_name=band_name)

# Only needed for local dev
if __name__ == "__main__":
    app.run(debug=True)
