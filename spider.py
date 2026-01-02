"""
spider.py
---------
Crawls a single website, extracts links between pages,
and stores page/link relationships in an SQLite database.

This script is intentionally limited to one domain
to ensure ethical crawling.
"""
import sqlite3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Pages(
                  id INTEGER PRIMARY KEY,
                  url TEXT UNIQUE,
                  html TEXT,
                  error INTEGER,
                  old_rank REAL,
                  new_rank REAL
                                  );
CREATE TABLE IF NOT EXISTS Links(
                  from_id INTEGER,
                  to_id INTEGER,
                  UNIQUE(from_id, to_id));
CREATE TABLE IF NOT EXISTS Webs(
                  url TEXT UNIQUE);
''')
#asking user for how many pages to crawling
#I am setting it to default 1 if user not enter a number value

pages = input("How many pages to crawl: ")
if pages.isdigit():
    pages = int(pages)
else:
    pages = 1

#collecting allowed websites and storing it into lists
#because database storing it as tuples
cur.execute("SELECT url from Webs")
webs = list()
for row in cur:
    webs.append(row[0])
for i in range(pages):
    cur.execute('''
    SELECT id, url FROM Pages
    WHERE html IS NULL AND error IS NULL
    ORDER BY RANDOM() LIMIT 1 
    ''')
    row = cur.fetchone()

    if row is None:
        start_url = input("Enter Starting URL:")
        if len(start_url) < 1:
            break
        cur.execute(
        'INSERT OR IGNORE INTO Webs(url) VALUES(?) ',
        (start_url,)
        )
        cur.execute('INSERT OR IGNORE INTO Pages(url,html,old_rank,new_rank) '
        'VALUES(?,NULL,1.0,1.0)',
        (start_url,)
        )
        conn.commit()
        continue

    from_id = row[0]
    url = row[1]
    print(f"Retrieving: {url}")

    cur.execute(
    'DELETE FROM Links WHERE from_id=?',
    (from_id,)
            )
    try:
        document = urllib.request.urlopen(url, context = ctx)
        html = document.read()
        if document.getcode() != 200:
            cur.execute(
                'UPDATE Pages SET error=? WHERE url =?',
                (document.getcode(),url)
                )
            conn.commit()
            continue

        if 'text/html' not in document.getheader('Content-Type'):
            cur.execute(
                'UPDATE Pages SET error=-1 WHERE url =? ',
                     (url,)
                        )
            conn.commit()
            continue

    except:
        cur.execute(
            'UPDATE Pages SET error=-1 WHERE url=?',
                (url,)
                )
        conn.commit()
        continue       
    cur.execute('UPDATE Pages SET html=? WHERE url=?',(html,url) )
    conn.commit()

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        href = tag.get('href',None)
        if href is None:
            continue
        
        href = urllib.parse.urljoin(url, href)
        href = href.split('#')[0]
        
        if href.endswith ('.png') or href.endswith('.pdf') or href.endswith('.jpeg') or href.endswith('.jpg') or href.endswith('.gif'):
            continue
        if href.endswith('/'):
            href = href[:-1]
        if len(webs) > 0:
            found = False
            for web in webs: 
                if href.startswith(web):
                    found = True
                    break
            if not found:
                    continue
        cur.execute(
            'INSERT OR IGNORE INTO Pages(url, html, old_rank, new_rank) VALUES(?,NULL,1.0,1.0)',
            (href, )
                )
        cur.execute(
            'SELECT id FROM Pages WHERE url=? LIMIT 1',
            (href, )
                )
        row = cur.fetchone()
        to_id = row[0]
        cur.execute(
            'INSERT OR IGNORE INTO Links (from_id, to_id) VALUES (?, ?)',
            (from_id, to_id )
                )
    conn.commit()


print('Crawling complete')
