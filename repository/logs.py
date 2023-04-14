import json
import pyodbc
from datetime import datetime
from fastapi.responses import ORJSONResponse
from models.InsertLogs import LogBody

server = 'activitylogserver.database.windows.net'
database = 'activitylogdb'
username = 'activitylog'
password = 'Pass@123'   
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

def insert_logs(logBody: LogBody, logger):
    user = logBody.User
    log = logBody.Log 
    start_time = datetime.fromisoformat(logBody.start_time)
    end_time = datetime.fromisoformat(logBody.end_time)
    try:
        cursor = cnxn.cursor()
        insert_statement = 'INSERT INTO [dbo].[Logs] ([User], [Timestamp], [Log], [start_time], [end_time]) VALUES (\''+user+'\',\''+datetime.now().strftime("%m-%d-%Y %H:%M:%S")+'\',\''+log+'\',\''+start_time.strftime("%m-%d-%Y %H:%M:%S")+'\',\''+end_time.strftime("%m-%d-%Y %H:%M:%S")+'\')'
        logger.info("The insert statement: "+insert_statement)
        cursor.execute(insert_statement)
        cnxn.commit()
        logger.info("Insertion successful for the request body: "+logBody.toJSON())
        return {"Status":True, "Message": "Insertion Successful", "RequestBody": logBody.toJSON()}
    except Exception as e:
        logger.error("Error in inserting: "+e)
        return {"Status":False, "Message": "Error in inserting: " + str(e), "RequestBody": logBody.toJSON()}

    