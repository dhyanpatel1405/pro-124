
from typing import List
from unicodedata import name
from flask import Flask,jsonify,request

app=Flask(__name__)
List=[
{
    "id" :1,
    "name" :"dhyan",
    "contact" :"9825599201",
    "done" :False
},

{
    "id" :1,
    "name" :"𝚄𝙽𝙺𝙽𝙾𝚆𝙽",
    "contact" :"9876543210",
    "done" :False
},


{
    "id" :2,
    "name" :"dhyey",
    "contact" :"9099051534",
    "done" :False

}



]
@app.route("/get-data")
def get_my_data():
    return jsonify({
        "data" :List
    })




if __name__=='__main__':
    app.run()