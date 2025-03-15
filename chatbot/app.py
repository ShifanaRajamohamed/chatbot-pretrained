from flask import Flask, render_template,request,jsonify 
import random 
app=Flask(__name__)
responses={"hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm fine, thank you!", "I'm doing well!", "I'm just a bot, but I'm good!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "Interesting! Tell me more."]
}


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
     user_message=request.json["message"].lower()
     response=responses.get(user_message,random.choice(responses["default"]))
     return jsonify({"response":response})
if __name__=="__main__":
    app.run(debug=True)