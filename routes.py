from flask import Flask, render_template
import json
import facebook

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/facebook")
def fb():
    token = "EAADcgFoskxIBAGkU2Q9ofBOKAN3K9gImnA8oBZCi44uP83QpdRxXiRuGPDU8f958UKTJsDXTwvk2KeVuPcnRjyZCZAjTUWSTu0V7W7Ucw4YriZBlWgLAMvb4z51yRnGFZA0f9mc7MhTXrAV5cZCd4uqlbyQXfAvPELrBhHjHJoRvRSvZBle72StUEwZA1kZADqB1MRPUYYZAlKccfEPGQ7OZCMiN4azmG2xZCAZCiUP1FWgZAiagZDZD"
    graph = facebook.GraphAPI(access_token=token)

    fields = ["email, posts"]
    profile = graph.get_object("me", fields = fields)
    return json.dumps(profile,indent=4)

@app.route("/about")
def about():
   return render_template("about.html")

if (__name__ == "__main__"):
    app.run(debug=True, host="192.168.1.12", port = 5000)
    #facebook()