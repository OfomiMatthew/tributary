from flask import Flask

app = Flask(__name__)
@app.route('/record',methods=['POST'])
def record_engine_temperature():
    pass
    return {"success":True},200 
@app.route('/collect',methods=['POST'])
def collect_engine_temperature():
    return {"success":True},200