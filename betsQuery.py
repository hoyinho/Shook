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

"""return link with id"""
def getLink(id):
    
"""return bet with id"""
def getBet(id):
    
"""return prize with id"""
def getPrize(id):
    
"""return id with link"""
def getIdWithLink(link):
    
    
