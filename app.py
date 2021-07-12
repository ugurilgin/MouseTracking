import os
from flask import Flask
from flask import request ,jsonify
from flask import flash
from flask import render_template,redirect,url_for
from flask_mysqldb import  MySQL
from flask_cors import CORS
from flask_mysqldb import  MySQL
from Host import Host
app=Flask(__name__,template_folder='templates')
CORS(app)
app.secret_key=os.urandom(24)
############## < MySQL Settings > ##############
myHost=Host()
app.config['MYSQL_HOST'] = myHost.hostName #"localhost"
app.config['MYSQL_USER'] = myHost.hostUser#"root"
app.config['MYSQL_PASSWORD'] = myHost.hostPassword#""
app.config['MYSQL_DB'] = myHost.hostDB#"brainsoup"
mysql=MySQL(app)
############## </MySQL Settings > ############## 
@app.route('/',methods=['GET','POST'])
def index():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        content=request.json
        for item in content:
            x=item["x"]
            y=item["y"]
            click=item["click"]
            
            cursor.execute("INSERT INTO move (x,y,click) VALUES( %(x)s,%(y)s,%(click)s)",{'x': x,'y':y,'click':click})  
            mysql.connection.commit()
       
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')