from flask import Flask
from flask import json, jsonify, request, session, redirect, url_for
from subprocess import check_output

app = Flask(__name__)
app.secret_key='helloooooo'

@app.route('/')
def base():
    return "you are not logged in <br><a href = '/login'></b>"+ "click here to login</b></a>"


@app.route("/login", methods= ['POST','GET'])
def getCreds():
    if request.method == 'POST':
        session['access_key'] = request.form["access_key"]
        session['secret_key']= request.form["secret_key"]
        return redirect(url_for('index'))
    return '''
    <form action = "" method = 'post'>
        <p>accessKey: <input type = text name = access_key /></p>
        <p>secretKey: <input type = text name = secret_key /></p>
        <p><input type = submit value = Login /></p>
    </form>
    '''


@app.route("/run", methods=['POST','GET'])
def createTerraform():
    if ('access_key' in session) and (request.method == 'POST'):
        accessKeyString="access_key="+str(session['access_key'])
        secretKeyString="secret_key="+str(session['secret_key'])
        nameString = "name="+str(request.form["name"])
        ownerString = "owner=" +str(request.form["owner"])
        purposeString = "purpose=" + str(request.form["purpose"])
        output = check_output(["terraform","apply","-input=false","-auto-approve","-var",nameString,"-var",ownerString,"-var",purposeString,"-var",accessKeyString,"-var",secretKeyString,"terraform1"]).decode("utf-8")
        return jsonify({"output":"check amazon!","returnstring":output})
    elif ('access_key' in session) and (request.method == 'GET'):
        return '''
        <form action = "" method = 'post'>
            <p>enter the name of the vpc:  <input type = text name = name /></p>
            <p>enter your email: <input type = text name = owner /></p>
            <p>enter the purpose of this deployment: <input type = text name = purpose /></p>
            <p><input type = submit value = BUILD /></p>
         </form>
        '''
    else:
        return jsonify({'returnString':'YOU ARE NOT LOGGED IN'})


@app.route("/destroy", methods=['POST','GET'])
def destroyTerraform():
    if 'access_key' in session and (request.method == 'POST'):
        accessKeyString="access_key="+str(session['access_key'])
        secretKeyString="secret_key="+str(session['secret_key'])
        output = check_output(["terraform","destroy","-input=false","-var",accessKeyString,"-var",secretKeyString,"-auto-approve","/app/terraform1"]).decode("utf-8")
        return jsonify({"output":"Everything is gone!","returnstring":output})
    elif 'access_key' in session and (request.method == 'GET'):
        return '''
        <form action = "" method = 'post'>
        <p><input type = submit value = DESTROYYY /></p>
        '''
    else:
        return jsonify({'returnString':'YOU ARE NOT LOGGED IN'})


@app.route("/index")
def index():
    if 'access_key' in session:
        return "<b><a href='/run'>click to build a vpc with three subnets</a></b> or <b><a href='/destroy'>destroy the vpc</a></b>"
    return "You are not logged in"


if __name__ == '__main__':
    app.run( host='0.0.0.0' )
