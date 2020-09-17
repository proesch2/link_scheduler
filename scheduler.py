import sqlite3
import pandas as pd
from datetime import datetime as dt
import webbrowser
import time
from link import Link


# adds link to text db in memory
def insert_link(link):
    with conn:
        c.execute("INSERT INTO links VALUES (?, ?, ?, ?, ?)",
                  (link.name, link.http, link.day, link.hour, link.min))


# opens web link to given site hyperlink
def access_site(site):
    name = site[0]
    http = site[1]
    print('Opening link to ' + name)
    webbrowser.open_new(http)


# create DB on memory
conn = sqlite3.connect(':memory:')

# create cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE links (
            name TEXT,
            http TEXT,
            day INTEGER,
            hour INTEGER,
            min INTEGER
            )""")

print('Reading schedule...')
schedule = pd.read_csv('Schedule.csv')

print(len(schedule), ' items on schedule:\n')
for i, row in schedule.iterrows():
    site = Link(row['name'], row['http'], row['day'], row['hour'], row['min'])
    print(site.__str__())
    insert_link(site)

print('\nLinks are displayed, but will open automatically at listed time.\n')

# get time to open link
early = int(input('How early will you access links? (whole minutes)\t'))

if early == 0:
    print('Links will open on time.')
elif early == 1:
    print('Links will open ', early, ' minute early.')
else:
    print('Links will open ', early, ' minutes early.')

# infite loop for this program to perform forever
print('\n<Press CTRL + C to end>\n')
while True:
    with conn:
        # get current time to check schedule
        now = dt.now()
        if now.second == 0:
            now = now.replace(minute=(now.minute + early))
            c.execute("SELECT name, http FROM links WHERE day = ? AND hour = ? AND min = ?",
                      (now.weekday(), now.strftime('%H'), now.strftime('%M')))
            for site in c.fetchall():
                access_site(site)

            # sleep for a second to prevent continuously opening for a second
            time.sleep(1)
