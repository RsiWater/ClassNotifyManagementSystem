import sqlite3

class ExeDB:
    __conn = sqlite3

    def __init__(self):
        self.__conn = sqlite3.connect('GradeDB.db')

    def __del__(self):
        self.__conn.close()

    def get(self):
        the_data = self.__conn.execute('SELECT * FROM Student_Grade')
        data=[]
        for d in the_data:
            data.append(d)
        return data

    def addH(self,ID,grade):
        the_data = self.__conn.execute('SELECT h_grade FROM Student_Grade where ID="{}"'.format(ID))
        data = the_data.fetchone()
        data = data[0]
        data = data+grade
        self.__conn.execute('UPDATE Student_Grade SET h_grade={} WHERE ID="{}"'.format(data,ID))
        self.__conn.commit()

    def addRC(self,ID):
        the_data = self.__conn.execute('SELECT rc_grade FROM Student_Grade where ID="{}"'.format(ID))
        data = the_data.fetchone()
        data = data[0]
        data = data + 1
        self.__conn.execute('UPDATE Student_Grade SET rc_grade={} WHERE ID="{}"'.format(data,ID))
        self.__conn.commit()

    def modH(self,ID,grade):
        self.__conn.execute('UPDATE Student_Grade SET h_grade={} WHERE ID="{}"'.format(grade,ID))
        self.__conn.commit()

    def modRC(self,ID,grade):
        self.__conn.execute('UPDATE Student_Grade SET rc_grade={} WHERE ID="{}"'.format(grade,ID))
        self.__conn.commit()

    def insert(self,ID,rc_grade,h_grade): #rc_grade點名成績 h_grade作業成績
        try:
            self.__conn.execute('INSERT INTO Student_Grade (ID,rc_grade,h_grade) VALUES (?,?,?)',(ID,rc_grade,h_grade))
            self.__conn.commit()
        except:
            print('something wrong')
    
    def delete(self,ID):
        self.__conn.execute('DELETE FROM Student_Grade WHERE ID="{}"'.format(ID))
        self.__conn.commit()

if __name__=='__main__':
    db = ExeDB()
    print(db.get())
    #db.addRC('A1065502')
    #db.addH('A1065506',4)
    #db.modH('A1065506',1)
    #db.modRC('A1065506',2)
    #db.insert('abc123',100,95)
    #db.delete('abc123')