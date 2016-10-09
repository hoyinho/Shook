from flask import Flask, render_template,session,redirect,request
import os
import utils
import time
import json
import datetime
import betsQuery

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if "loggedIn" in session and session["loggedIn"]:
        return render_template("index.html")
    else:
        return render_template("signup.html")
@app.route("/logoff")
def logoff():
    session["loggedIn"] = False
    session["username"] = ""
    return redirect("/")

@app.route("/create")
def create():
    username = request.args.get("username")
    password = request.args.get("password")
    if betsQuery.isUser(username):
        return json.dumps("False")
    else:
        betsQuery.newAccount(username, password)
        return json.dumps("True")
    
@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if betsQuery.correctAccount(username, password):
        session["loggedIn"] = True
        session["username"] = username
        return json.dumps("True")
    else:
        return json.dumps("False")
    
@app.route("/<link>")
def acceptBet(link):
    print len(link)
    print link
    if "loggedIn" in session and session["loggedIn"] and link != "favicon.ico":
        link = str(link)
        ID = betsQuery.getIdWithLink(link)
        bet = betsQuery.getBet(ID)
        prize = betsQuery.getPrize(ID)
        status = betsQuery.getStatus(ID)
        user1 = betsQuery.getUsername(betsQuery.getUser1(ID))
        user2 = betsQuery.getUser2(ID)
        closed = betsQuery.getClosed(ID)
        if status == "true":
            print user2
            user2 = betsQuery.getUsername(user2)
        return render_template("wilson.html", bet = bet, prize = prize, status = status, user1=user1, user2 = user2, closed = closed)
    else:
        return redirect("/")

@app.route("/accepted")
def accepted():
    link = request.args.get("link")
    ID = betsQuery.getIdWithLink(link)
    betsQuery.updateStatus(ID)
    user2 = betsQuery.getIdWithUsername(session["username"])
    betsQuery.updateUser2(user2, ID)
    print betsQuery.getUser2(ID)
    print betsQuery.getStatus(ID)
    print "testing"
    return json.dumps(0)

@app.route("/makeBet")
def makeBet():
    user1 = betsQuery.getIdWithUsername(session["username"])
    bet = request.args.get('bet')
    prize = request.args.get('prize')
    link = betsQuery.newLink()
    date = datetime.date.today()
    betsQuery.newBet(user1,-1, link,bet,prize,date, "false")
    return json.dumps(link)

@app.route("/win")
def win():
    whoWin = request.args.get("whoWin")
    link = request.args.get("link")
    ID = betsQuery.getIdWithLink(link)
    user1 = betsQuery.getUser1(ID)
    user2 = betsQuery.getUser2(ID)
    betsQuery.updateClosed(ID)
    if (whoWin == "1"):
        betsQuery.updateWins(user1, ID)
        betsQuery.updateLoss(user2, ID)
    else:
        betsQuery.updateWins(user2, ID)
        betsQuery.updateLoss(user1, ID)
    return json.dumps(0)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/bet")
def bet():
    if "loggedIn" in session and session["loggedIn"]:
        ID =betsQuery. getIdWithUsername(session["username"])
        wins = betsQuery.getWon(ID)
        losses = betsQuery.getLost(ID)
        wins = map(int, wins.split(" "))
        losses = map(int, losses.split(" "))
        wonBets = [[betsQuery.getBet(x),betsQuery.getPrize(x),betsQuery.getDate(x)] for x in wins]
        lostBets = [[betsQuery.getBet(x),betsQuery.getPrize(x),betsQuery.getDate(x)] for x in losses]
        return render_template("bet.html",wonBets = wonBets,lostBets = lostBets, username = session["username"])
    else:
        return redirect("/")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.debug = True
    app.secret_key = "random ke here"
    app.run(host='0.0.0.0', port=8000)
