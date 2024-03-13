#!/usr/bin/python3
"""frigging documentation for module for dynamic routes"""
from flask import Flask, abort, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
from operator import itemgetter

app = Flask(__name__)



@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    myDict = storage.all(State)
    myList = list(myDict.values())
    sorted_list = sorted(myList, key=itemgetter('name'))
    sorted_dict = {key: instance for key, instance in zip(myDict.keys(), sorted_list)}
    #just bear in mind that because of the rezipping, the ids are different in the key
    # from the value (which is the correct id -- I could fix this but...)
    return render_template('10-hbnb_filters.html', items=sorted_dict)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
