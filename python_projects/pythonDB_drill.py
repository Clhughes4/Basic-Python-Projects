
import sqlite3


conn = sqlite3.connect('drill.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Info( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        DataType TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('drill.db')


with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            print(file)
            cur.execute('INSERT INTO tbl_Info(DataType) VALUES (?)', \
                    (file,))
    conn.commit()
conn.close()










