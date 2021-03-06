import string
import random
import sqlite3

dbName = "bets.db"

"""Return user1 with id"""
def getUser1(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT user1 FROM allBets WHERE id = " + str(id) + ";"
    user1 = int(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return user1

def updateUser2(user2, id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "UPDATE allBets SET user2 = " + str(user2) + " where id = '" + str(id) + "';"
    c.execute(q)
    conn.commit()
    conn.close()

"""Return user2 with id"""
def getUser2(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT user2 FROM allBets WHERE id = " + str(id) + ";"
    user2 = int(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return user2
"""return link with id"""
def getLink(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT link FROM allBets WHERE id = " + str(id) + ";"
    link = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return link
"""return bet with id"""
def getBet(ID):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT bet FROM allBets WHERE id = " + str(ID) + ";"
    bet = c.execute(q).fetchall()
    print bet[0]
    bet = str(bet[0][0])
    conn.commit()
    conn.close()
    return bet
"""return prize with id"""
def getPrize(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT prize FROM allBets WHERE id = " + str(id) + ";"
    prize = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return prize
"""return id with link"""
def getIdWithLink(link):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT id FROM allBets WHERE link = '" + link + "';"
    ID = c.execute(q).fetchall()[0][0]
    conn.commit()
    conn.close()
    return ID
"""insert new line"""
def newBet( user1, user2, link, bet, prize, date,status):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "INSERT INTO allBets values(?, ?, ?, ?, ?, ?,?,?,?);"
    c.execute(q, (str(getNewID()), user1, user2, link, bet, prize, date,status,"false" ))
    conn.commit()
    conn.close()
    
def getDate(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT date FROM allBets WHERE id = " + str(id) + ";"
    date = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return date

def getWon(uid):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT won FROM accounts WHERE uid = " + str(uid) + ";"
    win = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return win

def getLost(uid):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT lost FROM accounts WHERE uid = " + str(uid) + ";"
    lost = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return lost

"""Checking validity of user"""
def isUser(username):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT uid FROM accounts WHERE username = '" + username + "';"
    result = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return len(result) == 1

def correctAccount(username, password):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    result = []
    if (isUser(username)):
        q = "SELECT uid FROM accounts WHERE username = '" + username + "' and password = '" + password + "';"
        result = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return len(result) == 1

def getNewUID():
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT uid FROM accounts"
    result = c.execute(q).fetchall()
    newID = len(result)
    conn.commit()
    conn.close()
    return newID

def newAccount(username,password):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "INSERT INTO accounts VALUES(?,?,?,?,?);"
    c.execute(q, (str(getNewUID()), username, password, "", ""))
    conn.commit()
    conn.close()

def getIdWithUsername(username):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT uid FROM accounts WHERE username = '" + username + "';"
    uid = int(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return uid
    
def getUsername(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT username FROM accounts WHERE uid = " +str(id)+  ";"
    username =c.execute(q).fetchall()
    print username
    print id
    username = str(username[0][0])
    conn.commit()
    conn.close()
    return username

def getNewID():
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT id FROM allBets"
    result = c.execute(q).fetchall()
    newID = len(result)
    conn.commit()
    conn.close()
    return newID

def generateLink(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def newLink():
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    link = generateLink()
    q = "SELECT id FROM allBets WHERE link= '" + link + "';"
    result = c.execute(q).fetchall()
    while (len(result) == 1):
        link = generateLink()
        q = "SELECT id FROM allBets WHERE link= '" + link + "';"
        result = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return link

def getStatus(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT status FROM allBets WHERE id= " + str(id) + ";"
    status = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return status

def updateStatus(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "UPDATE allBets SET status = 'true' where id=" + str(id) + ";"
    c.execute(q)
    conn.commit()
    conn.close()

def updateClosed(ID):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "UPDATE allBets SET closed = 'true' where id = " + str(ID) + ";"
    c.execute(q)
    conn.commit()
    conn.close()
    
def getClosed(ID):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT closed FROM allBets where id = " + str(ID) + ";"
    closed = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return closed

def updateWins(uid, id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    won = getWon(uid) + " " + str(id)
    print won + " testing"
    q = "UPDATE accounts SET won = '" + won + "' WHERE uid = " + str(uid)+  ";"
    c.execute(q)
    conn.commit()
    conn.close()

def updateLoss(uid, id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    lost = getLost(uid) + " " + str(id)
    q = "UPDATE accounts SET lost = '" + lost + "' WHERE uid = " + str(uid) + ";"
    c.execute(q)
    conn.commit()
    conn.close()
