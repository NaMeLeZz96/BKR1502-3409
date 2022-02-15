#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        NPTAR = request.form.get("NPTAR")
        TLTAR = request.form.get("TLTAR")
        WCTAR = request.form.get("WCTAR")
        print(NPTAR,TLTAR,WCTAR)
        model = load_model("BKRNN")
        pred = model.predict([float(NPTAR), float(TLTAR), float(WCTAR)])
        print(pred)
        s = "The predicted bankruptcy score is: " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




