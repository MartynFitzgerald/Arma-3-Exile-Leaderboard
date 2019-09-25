import mysql.connector
import math

# MYSQL CONFIG VARIABLES
host = "localhost"
db = "exile_chernarus_isles_x64"
user = "root"
passwd = ""


def getConnection():
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=passwd,
        database=db,
        use_unicode=True,
        charset="utf8"
    )
    return cnx


def overall_stats():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT COUNT(*), SUM(kills), SUM(deaths), AVG(kills), (SELECT AVG(distance) from player_stats) "
                    "from account;")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'USERS': str(row[0]),
                             'KILLS': str(row[1]),
                             'DEATHS': str(row[2]),
                             'KD': str(row[3]),
                             'DISTANCE': math.ceil(row[4])})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data


def trader_stats():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT COUNT(playerid), SUM(poptabs), AVG(poptabs), "
                    "(SELECT item_sold FROM trader_log GROUP BY item_sold ORDER BY count(*) DESC LIMIT 1), "
                    "(SELECT account.name FROM trader_log INNER JOIN account ON trader_log.playerid = account.uid GROUP BY trader_log.playerid ORDER BY count(*) DESC LIMIT 1) "
                    "FROM trader_log")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'TRADES': str(row[0]),
                             'TOTAL_MONEY_SPENT': str(row[1]),
                             'AVG_MONEY_SPENT':  math.ceil(row[2]),
                             'TOP_ITEM_SOLD': row[3],
                             'TOP_PLAYER': row[4]})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data


def clan_stats():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT clan.name, (SELECT COUNT(name) FROM clan), (SELECT COUNT(clan_id) FROM account) "
                    "FROM account "
                    "INNER JOIN clan ON account.clan_id = clan.id "
                    "WHERE clan_id != 'Null' "
                    "GROUP BY clan_id "
                    "ORDER BY count(*) DESC LIMIT 1;")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'TOP_CLAN': row[0],
                             'AVG_CLAN_MEMBERS': math.ceil(row[1]),
                             'TOTAL_CLANS': row[2]})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data


def money_stats():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT SUM(player.money), SUM(account.locker), (SELECT SUM(money) FROM container) "
                    "FROM player "
                    "RIGHT JOIN account ON player.account_uid = account.uid;")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'PLAYERS':  str(row[0]),
                             'LOCKERS':  str(row[1]),
                             'CONTAINERS':  str(row[2])})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data


def used_weapons():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT weaponused, count(*) "
                    "FROM player_stats "
                    "GROUP BY weaponused "
                    "ORDER BY count(*) DESC LIMIT 10;")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'WEAPONS': row[0],
                             'KILLS': row[1]})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data


def top_distance():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT a.name, aa.name, ps.weaponused, ps.distance "
                    "from player_stats ps "
                    "inner join account a on a.uid = ps.killer "
                    "inner join account aa on aa.uid = ps.victim "
                    "WHERE (weaponused!='Explosive' "
                    "AND weaponused!='RoadKill' "
                    "AND distance < 50000) "
                    "order by distance desc limit 10;")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'KILLER': row[0],
                             'VICTIM': row[1],
                             'WEAPON': row[2],
                             'DISTANCE': row[3]})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data


def player_leaderboard():
    cnx = getConnection()
    """ Connecting to MySQL database """
    if cnx.is_connected():
        data = []
        cur = cnx.cursor()
        cur.execute("SELECT uid, name, kills, deaths, IFNULL(((SELECT SUM(distance) "
                    "FROM player_stats "
                    "WHERE killer=uid) / kills), 0), "
                    "IFNULL((kills / deaths), kills), last_connect_at "
                    "FROM account "
                    "WHERE kills > 0 "
                    "ORDER BY name DESC")
        row = cur.fetchone()

        if row is not None:
            while row is not None:
                data.append({'UID': row[0],
                             'NAME': row[1],
                             'KILLS': row[2],
                             'DEATHS': row[3],
                             'AVERAGE_DISTANCE': math.ceil(row[4]),
                             'KD': math.ceil(row[5]),
                             'LAST_ONLINE': str(row[6])})
                row = cur.fetchone()
        cur.close()
    cnx.close()
    return data

