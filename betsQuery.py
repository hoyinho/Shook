import sqlite3

dbName = "bets.db"

def getUser1(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT user1 FROM allBets WHERE id = " + str(id) + ";"
    user1 = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return user1

"""Return user2 with id"""
def getUser2(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT user2 FROM allBets WHERE id = " + str(id) + ";"
    user2 = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return user2
"""return link with id"""
def getLink(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT link FROM allBets WHERE id = " + str(id) + ";"
    link = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return link
"""return bet with id"""
def getBet(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT bet FROM allBets WHERE id = " + str(id) + ";"
    bet = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return bet
"""return prize with id"""
def getPrize(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    q = "SELECT prize FROM allBets WHERE id = " + str(id) + ";"
    id = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    return id
"""return id with link"""
def getIdWithLink(link):
    
    
