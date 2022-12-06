# from flask import Flask, jsonify, render_template
from ts6 import *
from fastapi import FastAPI
from typing import Union
s = starter("dan")
base = s

app = FastAPI()

baselist2 = []
count = 0
for i,k in base.items():
    sl = {}
    sl["name"] = i
    sl["time"] = k
    baselist2.append(sl)
    count+=1


for i in range(len(baselist2)):
    baselist2[i]["id"]= i+1 
# это создает id для каждого гонщика. id = его место в таблице

# def reverse(x):
#     items = list(x.items())
#     y = {k: v for k, v in reversed(items)}
#     return y

# @app.route("/")
# def nach():
#     return "Это ответ на 7 таск (начальная страница)"
        
# @app.route("/report")
# def table():
#     return render_template("table.html",tables=s)

# @app.route("/report/drivers")
# def drivers():
#     return render_template("drivers.html",tables=s)

# @app.route('/report/drivers/driver_id=<string:about>')
# def about(about:str):
#     return render_template("dn.html",dn=about,tables=s)

# @app.route("/report/drivers/order=desc")
# def order():
#     return render_template("table_ord.html",tables=reverse(s))


    
@app.get("/spec/format=json/{id}")
def get_list(id):
    if id == "all":
        return baselist2
    else:
        return baselist2[int(id)-1]

@app.post("/spec/format=json")
def update_list(name:str,value:str, id: Union[int,None]=None):
    new_one = {name:value, "id":id}
    baselist2.append(new_one)
    return baselist2

@app.delete('/spec/format=json/{baselist_id}')
def delete_spec(baselist_id):
    ind, _ = next((x for x in enumerate(baselist2) if x[1]["id"] == int(baselist_id)), (None, None))
    baselist2.pop(ind)
    return baselist2