import sqlite3

def connect():
    conn = sqlite3.connect("hotel.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hotel (id INTEGER PRIMARY KEY, name TEXT, Address TEXT, phone_number INTEGER, no_of_days INTEGER, room_type text,total INTEGER)")
    conn.commit()
    conn.close()

def insert(name,address,phone_number,no_of_days,room_type,total):
    from back import calculation
    conn=sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO hotel VALUES (NULL, ?,?,?,?,?,?)",(name,address,phone_number,no_of_days,room_type,calculation(no_of_days,room_type)))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotel")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name = '',address = '',phone_number = '',room_type = '',no_of_days = '',total = ''):
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotel WHERE name=? or address = ? or phone_number = ? or room_type=? or no_of_days = ? or total = ?",(name,address,phone_number,room_type,no_of_days,total))
    rows = cur.fetchall()
    conn.close();
    return rows

def delete(id):
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM hotel where id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,name,address,phone_number,room_type,no_of_days,total):
    from back import calculation
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("UPDATE hotel SET name=?,address=?,phone_number=?,room_type=?,no_of_days=?,total=? where id=?",(name,address,phone_number,room_type,no_of_days,calculation(no_of_days,room_type),id))
    conn.commit()
    conn.close()

def calculation(no_of_days,room_type):
    if(room_type==("normal" or "NORMAL")):
        total = int(no_of_days)*1500
        return total
    
    elif room_type==("KING" or "king"):
        total = int(no_of_days)*1800
        return total

    elif room_type==("delux" or "DELUX"):
        total = int(no_of_days)*2000
        return total

connect()