#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request

app = Flask(__name__)

@app.route('/validacion', methods = ['POST'])
def validacion():
    return request.json

if __name__ == '__main__':
    app.run(host='localhost')


# In[ ]:




