
import requests, zipfile, os


import subprocess
try:
    print('''Access this local server from any device nearby.''')
    subprocess.run(['python app.py'], check = True)
except subprocess.CalledProcessError:
    URL = 'https://github.com/ziminl/reel-download/blob/main/server.zip'

    r = requests.get(URL, allow_redirects=True)
    open('server.zip', 'wb').write(r.content)

    with zipfile.ZipFile('server.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
        print('''Access this local server from any device nearby.''')
       
    
    
    subprocess.run(['python app.py'], check = True)
