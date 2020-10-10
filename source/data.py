#
#  data.py
#  Unbound Bible Python Edition
#

class Verse:
    book    = 0
    chapter = 0
    number  = 0
    count   = 0

myBibleArray = [0, \
     10, 20, 30, 40, 50, 60, 70, 80, 90,100,110,120,130,140,150,160,190,220,230,240, \
    250,260,290,300,310,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470, \
    480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670, \
    680,690,700,710,720,730,000,000,000,000,000,000,000,000,000,000,165,468,170,180, \
    462,464,466,467,270,280,315,320]

def unbound2mybible(id: int) -> int:
    try:
        return myBibleArray[id]
    except:
        return id

def mybible2unbound(id: int) -> int:
    try:
        r = myBibleArray.index(id)
    except:
        return id

def isNewTestament(n: int) -> bool:
     return n >= 40 and n < 77

