class Auditorium:
    """this class is about details of auditorium
        it has name,eventslist,date,time,totalseats attributes
        and infoAuditorium,addevents,bookevents methods"""
    def __init__(self,name,totalseats):
        self.name=name
        self.eventslist=list()

        self.totalseats=totalseats
    def infoAuditorium(self):
        return f"Auditorium name:{self.name},total seats:{self.totalseats}"

    def addEvents(self,event):
        self.eventslist.append(event)
    def booksEvents(self,):
        for event in self.eventslist:
             return event


