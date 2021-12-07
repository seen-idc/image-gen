from flask import Flask, request, send_file
import gen

app = Flask(__name__)

@app.route('/discord/welcome')
def discord_welcome():
    name = request.args.get('name')
    tag = request.args.get('tag')
    avatar = request.args.get('avatar')

    return send_file(gen.generate_welcome(name, tag, avatar), mimetype='image/png')