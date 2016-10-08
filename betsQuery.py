import sqlite3

dbName = "bets.db"

def getUser1(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT user1 FROM allBets WHERE id = " + str(id) + ";"
    user1 = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return user1

"""Return user2 with id"""
def getUser2(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT user2 FROM allBets WHERE id = " + str(id) + ";"
    user2 = str(c.execute(q).fetchall()[0][0])
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
def getBet(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT bet FROM allBets WHERE id = " + str(id) + ";"
    bet = str(c.execute(q).fetchall()[0][0])
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
    id = int(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return id
"""insert new line"""
def newBet(id, user1, user2, link, bet, prize):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "INSERT INTO allBets values(?, ?, ?, ?, ?, ?);"
    c.execute(q, (str(id), user1, user2, link, bet, prize))
    conn.commit()
    conn.close()
def getDate(id);
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT date FROM allBets WHERE id = " + str(id) + ";"
    date = str(c.execute(q).fetchall()[0][0])
    conn.commit()
    conn.close()
    return date
def getWin(uid)
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT win FROM accounts WHERE uid = " + str(uid) + ";"
    win = str(c.excute(q)fetchall()[0][0])
    conn.commit()
    conn.close()
    return win
def getLost(uid)
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT lost FROM accounts WHERE uid = " + str(uid) + ";"
    lost = str(c.excute(q)fetchall()[0][0])
    conn.commit()
    conn.close()
    return lost


    
    
