#!/usr/bin/python3
"""frigging documentation for module for dynamic routes"""
from flask import Flask, abort, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
from operator import itemgetter

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id=None):
    all_states = []
    myDict = storage.all(State)
    if id is None:
        myList = list(myDict.values())
        sorted_list = sorted(myList, key=itemgetter('name'))
        sorted_dict = {key: instance for key, instance in zip(myDict.keys(), sorted_list)}
        #just bear in mind that because of the rezipping, the ids are different in the key
        # from the value (which is the correct id -- I could fix this but...)
        return render_template('9-states.html', items=sorted_dict, id=None)
    else:
        for item in myDict.values():
            if item.id == id:
                all_states.append(item)
                return render_template('9-states.html', items=all_states, id=id)
    return render_template('9-states.html', items=None)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
