#A simple app to clock in to work, to easily recall those times later when entering times
import rumps
import os
from datetime import datetime as dt

class keeperApp(rumps.App):
    def __init__(self):
        super(keeperApp, self).__init__("Time Keeping")
        self.menu = ["Add", "Show Times", "Clear Time"]
        self.times = []
        
    @rumps.clicked("Add")
    def addTime(self, _):
        now = dt.now()
        self.times.append(now.strftime('%H:%M'))
        rumps.alert(f"{now.strftime('%H:%M')} was added")

    @rumps.clicked("Clear Time")
    def clearTimes(self, _):
        self.times.clear()
        rumps.alert("Times were cleared")

    @rumps.clicked("Show Times")
    def showTimes(self, _):
        message = ""
        for times in self.times:
            message += f"{times}\n"
        rumps.alert(message)

if __name__ == '__main__':
    keeperApp().run()