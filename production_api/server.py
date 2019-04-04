from sanic import Sanic
from sanic.response import json
import code

app = Sanic()

@app.route("/", methods=["GET", "POST"])
async def listener(request):
    code.interact(local=locals())
    return json({"hello": "there"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
