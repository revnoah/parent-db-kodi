#!/usr/bin/python3

import pymysql
import os
import subprocess

class Database:
    PAGESIZE = 20
    DB_SOURCE_HOST = os.getenv("DB_SOURCE_HOST")
    DB_SOURCE_USER = os.getenv("DB_SOURCE_USER")
    DB_SOURCE_PASS = os.getenv("DB_SOURCE_PASS")
    DB_SOURCE_VIDEOS = os.getenv("DB_SOURCE_VIDEOS")
    DB_SOURCE_MUSIC = os.getenv("DB_SOURCE_MUSIC")
    DB_DEST_HOST = os.getenv("DB_DEST_HOST")
    DB_DEST_USER = os.getenv("DB_DEST_USER")
    DB_DEST_PASS = os.getenv("DB_DEST_PASS")
    DB_DEST_VIDEOS = os.getenv("DB_DEST_VIDEOS")
    DB_DEST_MUSIC = os.getenv("DB_DEST_MUSIC")

    def __init__(self):
        self.con = pymysql.connect(self.DB_SOURCE_HOST, self.DB_SOURCE_USER, self.DB_SOURCE_PASS, self.DB_SOURCE_VIDEOS, 
            cursorclass=pymysql.cursors. DictCursor)
        self.cur = self.con.cursor()

    def dbDump(dbName, dbUser = DB_SOURCE_USER, dbPass = DB_SOURCE_PASS):
        dbparams = [dbUser, dbPass, dbName]
        statement = 'mysqldump -u {0} -p{1} {2} > {2}.sql'
        subprocess.call(statement.format(*dbparams), shell=True)

    def dbImport(dbName, dbSource, dbUser = DB_DEST_USER, dbPass = DB_DEST_PASS):
        dbparams = [dbUser, dbPass, dbName, dbSource]
        statement = 'mysql -u {0} -p{1} {2} < {3}'
        subprocess.call(statement.format(*dbparams), shell=True)

    def list_employees(self):
        self.cur.execute("SELECT c00 FROM tvshows LIMIT 50")
        result = self.cur.fetchall()
        return result

    def dbMovies(self):
        sql = """ SELECT m.idMovie AS id, 
            m.c00 AS title, 
            m.c01 AS `desc` , 
            m.c03 AS tagline, 
            m.c08 AS thumb, 
            m.c12 AS rating, 
            m.c14 AS genre, 
            c15 AS director, 
            a.url 
            FROM movie AS m 
            INNER JOIN art AS a ON a.media_id = m.idMovie 
            WHERE a.media_type='movie' AND a.type='poster' 
            ORDER BY c00 LIMIT 50 """
        self.cur.execute(sql)
        # Fetch a single row using fetchone() method.
    #    records = cursor.fetchmany(PAGESIZE)
        records = self.cur.fetchall()
        movies = []
        for row in records:
            urlPosition = row["thumb"].find('preview="') + 9
            if urlPosition > 0:
                row["thumb"] = row["thumb"][urlPosition:]
                quotePosition = row["thumb"].find('"')
                row["thumb"] = row["thumb"][0:quotePosition]
            else:
                row["thumb"] = row["thumb"][7:-7]
            movies.append(row)

        return movies

    # dbDump(DB_SOURCE_VIDEOS)
    # dbDump(DB_SOURCE_MUSIC)

    # dbImport(DB_DEST_VIDEOS, '{}.sql'.format(DB_SOURCE_VIDEOS))
    # dbImport(DB_DEST_MUSIC, '{}.sql'.format(DB_SOURCE_MUSIC))
