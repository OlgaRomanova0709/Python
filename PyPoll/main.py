import os
import csv
path=os.path.join('election_data.csv')
path2=os.path.join('election.csv')
cand={}
candList=list()
candtotal=list()
sumV=int()
per=float()
persList=list()
winnerpers=float()
with open (path,'r') as information:
    datas=csv.reader(information, delimiter=",")
    datas_header=next(datas)
    
    for x in datas:
        candtotal.append(x[2])
  
    for i in candtotal:
        if i not in cand:
            cand[i]=1
        else:
            cand[i]+=1    
    sumV=sum(cand.values())
with open(path2,"w",newline="") as textinform:
    dataOut=csv.writer(textinform)
    dataOut.writerow(["Election Results"])
    dataOut.writerow(["-----------------"])
    dataOut.writerow([f"Total Votes: {sumV}"])
    dataOut.writerow(["-----------------"])

    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {sumV}") 
    print("--------------------")
    for i in cand:
        per=round(((cand[i]/sumV)*100),2)
        persList.append(per)
        candList.append(i)
        print(f"{i}: {round(((cand[i]/sumV)*100),2)}% ({cand[i]}) ")
        dataOut.writerow([f"{i}: {round(((cand[i]/sumV)*100),2)}% ({cand[i]}) "])
    winnerpers=max(persList)
    roster=zip(candList,persList)    
    for i in roster:
        if i[1]==winnerpers:
            print("--------------------")
            print(f"Winner: {i[0]}")
            dataOut.writerow(["--------------------"])
            dataOut.writerow([f"Winner: {i[0]}"])







