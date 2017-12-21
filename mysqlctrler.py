#-*- coding:utf-8 -*-
import MySQLdb

class MysqlCtrler:
	def __init__(self,db,host="10.0.109.75",user="sec_opr",passwd="Sec_opr@456",port=3307):	
		self.config={'db':db,
					'host':host,
					'user':user,
					'passwd':passwd,
					'port':port,
					'charset':'utf8',
					'unix_socket':'/tmp/mysql.sock'
					}					
		self.conn = MySQLdb.connect(**self.config)
		self.cursor = self.conn.cursor()

	#data = [(x,y,z),(a,b,c)]格式,columns=(column1,column2,column3)
	def insert(self,table,columns,data):
		values = []
		for x in xrange(len(data[0])):
			values.append("%s")
		sqli = "insert into "+table+"("+",".join(columns)+") values("+",".join(values)+")"
		self.cursor.executemany(sqli,data)	
		self.conn.commit()

    #qcolumn = (a,b,c)格式
	def query(self,table,qcolumn,wcolumn = 1,wvalue= 1):
		sqlq ="select "+",".join(qcolumn)+" from %s where %s='%s'" % (table,wcolumn,wvalue)
		self.cursor.execute(sqlq)
		data = self.cursor.fetchall()
		return data

	def delete(self,table,column,value):
		sqld = "delete from %s where %s='%s'" % (table,column,value)
		self.cursor.execute(sqld)
		self.conn.commit()
    
    #data =[(column1,value1,wcolumn1,wvalue1)]
	def update(self,table,data):
		values =[]
		for x in xrange(len(data)):
			values.append((data[x][1],data[x][3]))
		sqlu = "update "+table+" set "+data[0][0]+"=%s where "+data[0][2]+"=%s"
		self.cursor.executemany(sqlu,values)
		self.conn.commit()

	def execsql(self,sql):
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		return data
		#self.conn.commit()

	def __del__(self):
		self.cursor.close()
		self.conn.close()