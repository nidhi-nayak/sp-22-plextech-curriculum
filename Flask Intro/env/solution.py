from flask import Flask, request 

app = Flask(__name__)

@app.route('/hello')
def index():
    name = request.args.get('name')
    if name: 
        return "Hello " + name
    else: 
        return "Hello World"

@app.route('/reflect')
def reflect(): 
    data = request.data
    return 'Hello' + str(data) 

@app.route('/reflect/plex')
def reflect_plex(): 
    plex_data = request.json
    out = {}
    for key in plex_data: 
        out['plex_'+key] = plex_data[key]
    new = {}
    for key in out: 
        if type(out[key]) == str : 
            new[key] = 'plex_' + str(out[key])
        else: 
            new[key] = out[key]
    return new

@app.route('/reflect/plex/form')
def form_route(): 
    data = request.form
    out = {} 
    for key in data: 
        out['plex_'+key] = data[key]
    new = {}
    for key in out:  
        new[key] = 'plex_' + str(out[key])
    return new

@app.route('/hello-json')
def dictionary(): 
    return {"text": "Hello World from Dictionary"}

@app.route('/hello-html')
def html():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route('/hello-html-error')
def dummy():
    return "test"

@app.route('/hello/<name>')
def whatevername(name):
   return 'Hello ' + str(name)

@app.route('/hello/<name>/<thing>/<money>')
def sentence(name,thing,money):
    return 'Hello ' + str(name) + ', your ' + str(thing) + ' is ' + str(10-int(money))

app.run(host='0.0.0.0', port=81, debug=True)
