import dbfunc
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route('/')
def server_stats():
    return render_template("server_stats.html")


@app.route('/playerstats/')
def playerstats():
    return render_template("player_stats.html")


@app.route('/monthly_stats')
def monthly_stats():
    month = request.args.get('month')
    uid = request.args.get('uid')
    return render_template("monthly_stats.html")


@app.route('/api/server_stats/overall_stats/')
def overall_stats():
    return jsonify(dbfunc.overall_stats())


@app.route('/api/server_stats/trader_stats/')
def trader_stats():
    return jsonify(dbfunc.trader_stats())


@app.route('/api/server_stats/clan_stats/')
def clan_stats():
    return jsonify(dbfunc.clan_stats())


@app.route('/api/server_stats/money_stats/')
def money_Stats():
    return jsonify(dbfunc.money_stats())


@app.route('/api/server_stats/used_weapons/')
def used_weapons():
    return jsonify(dbfunc.used_weapons())


@app.route('/api/server_stats/top_distance/')
def top_distance():
    return jsonify(dbfunc.top_distance())


@app.route('/api/server_stats/player_leaderboard/')
def player_leaderboard():
    return jsonify(dbfunc.player_leaderboard())


if __name__ == '__main__':
    app.run(debug=True)