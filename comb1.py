import json

ndata = []
mintime = 0
maxtime = 0
count = 0
jim = 0
jane = 0
jj =0

print 'started'

def my_addf(jd):
        global mintime, maxtime, ndata, count, jim, jane, jj
        for i in range(len (jd)):
            if jd[i]['attributes']['Time_Begun'] <= mintime:
                tmintime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
                jane = jane + 1
            if jd[i]['attributes']['Time_Begun'] > maxtime:
                tmaxtime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
                jim = jim + 1
            count = count + 1
        mintime = tmintime
        maxtime = tmaxtime
        jj = jim + jane
        print "jane", jane, "jim", jim, "jj", jj
        print "i", i, "mintime", mintime, "maxtime", maxtime, "count", count
        

def my_add(jd):
        global mintime, maxtime, ndata, count
        for i in range(len (jd)):
            
            if jd[i]['attributes']['Time_Begun'] > maxtime:
                tmaxtime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
                count = count + 1
        maxtime = tmaxtime
        print "i", i, "mintime", mintime, "maxtime", maxtime, "count", count
        

with open("db.json") as db:
    json_data = []
    json_data = json.load(db)
    mintime = json_data[0]['attributes']['Time_Begun']
    maxtime = json_data[0]['attributes']['Time_Begun']
 #   ndata.append(json_data[0])
    my_addf(json_data)

print 'b'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("d.json") as d:
    json_data = []    
    json_data = json.load(d)
    my_add(json_data)

print 'd'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("dl.json") as dl:
    json_data = []    
    json_data = json.load(dl)
    my_add(json_data)

print 'l'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("do.json") as do:
    json_data = []    
    json_data = json.load(do)
    my_add(json_data)

print 'o'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("dn.json") as dn:
    json_data = []    
    json_data = json.load(dn)
    my_add(json_data)

print 'n'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open('all01.json', 'w') as outfile:
     json.dump(ndata, outfile, sort_keys = True, indent = 4,
     ensure_ascii=False)

print mintime, maxtime, count
    
