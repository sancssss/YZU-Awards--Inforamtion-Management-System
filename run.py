# -*- coding: UTF-8 -*- 
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from app import app

app.run(debug = True, port = 5000)