#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request

app = Flask(__name__)

@app.route('/validacion')
def validacion():
    return "Hola mundo"

if __name__ == '__main__':
    app.run(host='localhost')


# In[ ]:




