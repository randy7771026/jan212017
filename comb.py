import json
global mintime, maxtime, ndata, count
ndata = []
mintime = 0
maxtime = 0
count = 0

print 'started'

def my_addf(jd,mintime, maxtime, ndata, count):
        global mintime, maxtime, ndata, count
        for i in range(len (jd)):
            if jd[i]['attributes']['Time_Begun'] < mintime:
                mintime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
            if jd[i]['attributes']['Time_Begun'] > maxtime:
                maxtime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
            count = count + 1
        
        print "i", i, "mintime", mintime, "maxtime", maxtime, "count", count
        return mintime, maxtime, ndata,count

def my_add(jd,mintime, maxtime, ndata, count):
        global mintime, maxtime, ndata, count
        for i in range(len (jd)):
            
            if jd[i]['attributes']['Time_Begun'] > maxtime:
                maxtime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
                count = count + 1
        
        print "i", i, "mintime", mintime, "maxtime", maxtime, "count", count
        return mintime, maxtime, ndata,count

with open("db.json") as db:
    json_data = []
    json_data = json.load(db)
    mintime = json_data[0]['attributes']['Time_Begun']
    maxtime = json_data[0]['attributes']['Time_Begun']
    ndata.append(json_data[0])
    my_addf(json_data, mintime, maxtime, ndata, count)

print 'b'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("d.json") as d:
    json_data = []    
    json_data = json.load(d)
    my_add(json_data, mintime, maxtime, ndata,count)

print 'd'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("dl.json") as dl:
    json_data = []    
    json_data = json.load(dl)
    my_add(json_data, mintime, maxtime, ndata, count)

print 'l'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("do.json") as do:
    json_data = []    
    json_data = json.load(do)
    my_add(json_data, mintime, maxtime, ndata, count)

print 'o'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open("dn.json") as dn:
    json_data = []    
    json_data = json.load(dn)
    my_add(json_data, mintime, maxtime, ndata, count)

print 'n'
print "mintime", mintime, "maxtime", maxtime, "count", count

with open('all05.json', 'w') as outfile:
     json.dump(json_data, outfile, sort_keys = True, indent = 4,
     ensure_ascii=False)

print mintime, maxtime, count
    
