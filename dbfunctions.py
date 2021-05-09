
def getLogin(self,bd,  userdb, passworddb, host, port, database,username, password):
      try:
          conn = bd.connect(user = '',
                              password = '',
                              host= host ,
                              port= port,
                              database= database )
          cursor = conn.cursor()
          query = "SELECT * FROM user_client WHERE username = \'"+username+"\' AND password = \' " + password + "\'"
          cursor.execute(query)
          record = cursor.fetchall()
          print(record)
          if (record.length() != 0):
            return self.openHomeAdmin
          else:
            return 'ERR '

      except (Exception) as error :
          print ("ERROR", error)
          return print('Algo salio mal...')
      finally:
          #closing database connection.
              if(conn):
                  cursor.close()
                  conn.close()
                  #print("PostgreSQL connection is closed")
