#author Phil Roesch roeschp@wit.edu
#supporting class Link to organize data

import calendar

class Link() :
    # name - string name of link
    # http -  http link to site
    # day - day to open link [0-6] [Monday-Sunday]
    # time - time (H:M) to open link
    def __init__(self, name, http, day, hour, min):
        self.name = name
        self.http = http
        self.day = day
        self.hour = hour
        self.min = min

    def __str__(self):
        return self.name + ' at ' + str(self.hour).zfill(2) + ':' + str(self.min).zfill(2) + ' on ' + calendar.day_name[self.day] + ' (' + self.http + ')'
