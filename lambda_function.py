import requests
import json
import time
def site_check():
    site="https://google.com"
    try:
        start_time=time.time()
        response=requests.get(site,timeout=5)
        print(response.status_code)
        latency=(time.time()-start_time)*1000
        data={
            "site":site,
            "status":"online",
            "latency":f"{latency:.2f} ms"
        }
    except Exception as e:
        data={
            "site":site,
            "status":"offline",
            "error":str(e)
        }
    return {
        'status code':300,
        'body':json.dumps(data)
    }
if __name__=="__main__":
    print(site_check())