from flask import Flask, render_template, request, redirect
import db_controller as db

app = Flask(__name__)
app.secret_key = 'flosic'

@app.route("/")

@app.route("/home")
def home():
    return render_template('main/flowerindex.html',flower_list = db.read_flower_tolist())

@app.route("/addflower/", methods=['GET', 'POST'])
def addflower():   
    if request.method == 'POST':
        db.add_flower(request.form['name'], request.form['word'] , request.form['etc'], request.form['modelnum'])
    return redirect('/home/')

@app.route("/deleteflower/<int:id>", methods=['GET', 'POST'])
def deleteflower(id):
    if request.method == 'POST':
        db.delete_flower(id)     
    return redirect('/home/')


@app.route("/songindex/")
def songindex():   
    return render_template('main/songindex.html', song_list = db.read_song_tolist())

@app.route("/addsong", methods=['GET', 'POST'])
def addsong():   
    if request.method == 'POST':
        song_list = db.recieve_csv_tolist()
    if song_list is not None:
        db.add_songlist(song_list)
    else :
        print("song_list is None")
        
    return redirect('/songindex/')

@app.route("/deletesong/<int:id>", methods=['GET', 'POST'])
def deletesong(id):
    if request.method == 'POST':
        db.delete_song(id) 
    
    return redirect('/songindex/')


@app.route("/resetaisong")
def resetaisong():
    db.reset_ai("song")
    return redirect('/songindex/')

@app.route("/resetaiflower")
def resetaiflower():
    db.reset_ai("flower")
    return redirect('/home/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

