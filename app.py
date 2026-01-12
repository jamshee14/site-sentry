from flask import Flask, request,jsonify,render_template,redirect
import requests
import time
from datetime import datetime
import csv
app=Flask(__name__)
@app.route("/",methods=["GET"])
def check_website():
    site=request.args.get('url',"https://www.google.com")
    try:
        start_time=time.time()
        response=requests.get(site,timeout=5)
        latency=(time.time()-start_time)*1000
        result={
            "body":site,
            "Status":"online",
            "latency":f"{latency:.2f} ms",
            "response_code":response.status_code
        }
    except Exception as e:
        result={
            "body":site,
            "Status":"offline",
            "error":str(e)
        }
    timestamp=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open('network_log.csv','a',newline='')as file:
        writer=csv.writer(file)
        writer.writerow([timestamp,result['body'],result['Status'],result.get('latency',' ms ')])
    return redirect('/history')
@app.route('/history',methods=['GET'])
def get_history():
    logs=[]
    try:
        with open('network_log.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                logs.append({
                    "time":row[0],
                    "site":row[1],
                    "status":row[2],
                    "latency":row[3]
                })
        return render_template('dashboard.html',logs=logs)
    except FileNotFoundError:
        logs=[]
if __name__=="__main__":
    app.run(debug=True,port=5000)
