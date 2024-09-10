# import os
import sqlite3

class Statics:

    nowList : list[str] = []
    __conn : sqlite3.Connection
    __curr : sqlite3.Cursor

    @staticmethod
    def setlist(res : list[str]) -> None:
        Statics.nowList = res
        Statics.__conn = sqlite3.connect('data.db')
        Statics.__curr = Statics.__conn.cursor()

    @staticmethod
    def getone() -> bytes:
        if Statics.nowList.__len__() == 0: return b''
        Statics.__curr.execute('select * from resources where name=?', (Statics.nowList[0],))
        Statics.nowList.__delitem__(0)
        data : bytes = Statics.__curr.fetchone()[1]
        if Statics.nowList.__len__() == 0:
            Statics.__curr.close()
            Statics.__conn.close()
        return data

    @staticmethod
    def close() -> None:
        Statics.__curr.close()
        Statics.__conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    sqlc = 'update resources set bin=? where name=?'#'insert into resources(name, bin) values(?, ?)'
    bl = b''
    # wa = b''
    # bo = b''
    with open('bo2.png', 'rb') as f:
        bl = f.read()
        f.close()
    # with open('wat.png', 'rb') as f:
    #     wa = f.read()
    #     f.close()
    # with open('bo.png', 'rb') as f:
    #     bo = f.read()
    #     f.close()
    cur.execute(sqlc, (bl, 'plate'))
    conn.commit()
    # cur.execute(sqlc, ('whitet', wa))
    # conn.commit()
    # cur.execute(sqlc, ('plate', bo))
    # conn.commit()
    cur.close()
    conn.close()
    # Statics.setlist(['white'])
    # print(Statics.getone())