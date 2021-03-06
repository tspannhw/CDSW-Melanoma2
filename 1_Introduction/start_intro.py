import os
import subprocess
import wait

def runApp(): 
   print("Starting Flask App")
   python = "/usr/local/bin/python"  
   url = ("http://" + os.environ["CDSW_ENGINE_ID"] +
           ".consoles." + os.environ["CDSW_DOMAIN"])
   FNULL = open(os.devnull, 'w')
   proc = subprocess.Popen([python, "./app.py"], stdout=FNULL, stderr=FNULL)
   wait.tcp.open(int(os.environ["CDSW_APP_PORT"]))
   return proc.pid  

  
  
runApp()  