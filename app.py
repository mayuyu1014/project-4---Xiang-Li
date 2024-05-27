# Import the dependencies.
from flask import Flask, render_template, request, jsonify
from SD_generation import sd_generate

#################################################
# Flask Setup
#################################################
app = Flask(__name__, static_folder="static")
@app.route("/", methods=['GET', 'POST'])
def index():
    input=''
    details=''
    cues=''
    pics=''
    if request.method == 'POST':
        input = request.form.get('input')
        details = request.form.get('details')
        cues = request.form.get('cues')
        pics = sd_generate(input, details, cues)
        print("drawing")

    return render_template('index.html', input=input, details=details, cues=cues, pics=pics)

#################################################
# Run the app
#################################################
if __name__ == '__main__':
    app.run(debug=True)