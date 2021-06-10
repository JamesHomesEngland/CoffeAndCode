import itertools, re, time

leftadd = ["PIXON TRADING CENTRE","APARTMENT 3","NULL","PIXON LANE","","TAVISTOCK"]#,"PL19 8DH"
rightadd = ["","PIXON TRADING CENTRE","PIXON LANE","","FLAT 3"]#"PL19 8DH",

"""stuff = [1, 2, 3]
for L in range(0, len(stuff)+1):
    for subset in itertools.permutations(stuff, L):
            print(subset)
"""
def insertFlat(inlist):
    for i in inlist:
        print(inlist)
        str_i = str(i)
        if "FLAT" in str_i:
            aprt = i.replace("FLAT","APARTMENT")
            inlist.append(aprt)
            break
        if "APARTMENT" in str_i:
            flat = i.replace("APARTMENT","FLAT")
            inlist.append(flat)
            break

    print(inlist)

def cleanList(inlist):
    tlist = []
    for i in inlist:
        if i != '':
            if i != "NULL":# or i is not "NULL":
                tlist.append(i)
    return tlist

def cleanToString(inlist):
    outstr = ""
    for i in inlist:
        string = re.sub('[^ A-Za-z0-9]+', '', i)
        string = string.lower()
        string = string.replace(" ", "")
        outstr = outstr+ string
    return outstr

leftadd = insertFlat(leftadd)
leftadd = cleanList(leftadd)
print(leftadd)
rightadd = cleanList(rightadd)
print(rightadd)


rightstr = cleanToString(rightadd)
print(rightstr)
cnt = 0
srt = time.time()
for L in range(0, len(leftadd)+1):
    for subset in itertools.permutations(leftadd, L):
        cnt +=1
        print(cnt,cleanToString(list(subset)))
        if cleanToString(list(subset)) == rightstr:
            print(cleanToString(list(subset)))
            print(cnt,list(subset))
            print("WE DID IT")
            break
    else:
        continue
    break
print(time.time()-srt)

