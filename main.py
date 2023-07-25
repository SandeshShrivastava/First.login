from flask import Flask,render_template
app = Flask(__name__,template_folder='static')

@app.route('/')
def port_folio():
    return render_template(  'index.html'  )
app.run(debug=True)