from flask import Flask, render_template, g, request, session, redirect, url_for
import sqlite3
app = Flask(__name__)

POKEMONDB = 'koshermon.db'

@app.route('/')
def index():
    db = sqlite3.connect(POKEMONDB)
    tables = get_all(db)
    db.close()
    return render_template('index.html',
    pokemon=tables['pokemon'])

@app.route('/mon/<params>')
def single_mon(params):
    db = sqlite3.connect(POKEMONDB)
    tables = get_one(params, db)
    db.close()
    return render_template('single.html',
    mon=tables['mon'])

def get_all(db):
    pokemon = []
    cur = db.execute('SELECT * FROM pokemon_cleaned')
    for row in cur:
        pokemon.append(list(row))
    return {'pokemon':pokemon}

def get_one(params, db):
    mon = []
    cur = db.execute("SELECT * FROM pokemon_cleaned WHERE id=%s" % params)
    for row in cur:
        mon.append(list(row))
    return {'mon':mon}
