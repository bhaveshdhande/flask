from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
  return 'Hello from Flask!'
@app.route('/1')
def index():
  return render_template('index.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
