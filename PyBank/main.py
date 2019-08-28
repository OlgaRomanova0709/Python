import os
import csv
SumPr=float()
avg=float()
x=float()
ProfLos=list()
maxProf=list()
maxPr=float()
minPr=float()
times=list()
roster=list()
path=os.path.join('budget_data.csv')
path2=os.path.join('budget.csv')
with open (path,'r') as information:
    datas=csv.reader(information, delimiter=",")
    datas_header=next(datas)
    for pos in datas:
        SumPr=SumPr+float(pos[1])
        ProfLos.append(pos[1])
        times.append(pos[0])
    times.pop(0)   
    print("Financial Analysis")
    print("===================================")
    print(f"Total Months: {str(len(ProfLos))}")
    print(f"Total: $ {str(SumPr)}")

with open (path2,"w",newline="") as finalinform: 
    datafinal=csv.writer(finalinform)
    datafinal.writerow(["Financial Analysis"])
    datafinal.writerow(["==================================="])
    datafinal.writerow([f"Total Months: {str(len(ProfLos))}"])
    datafinal.writerow([f"Total: $ {str(SumPr)}"])

    for i in range(1,len(ProfLos)): 
        x=float(ProfLos[i])-float(ProfLos[i-1])
        maxProf.append(x)
    roster=zip(times,maxProf)
    maxPr=max(maxProf)
    minPr=min(maxProf)
    avg=round((sum(maxProf)/len(maxProf)),2)
    print(f"Average Change: $ {avg}") 
    datafinal.writerow([f"Average Change: $ {avg}"]) 
    for i in roster:
        if i[1]==maxPr:
            print(f"Greatest Increase in Profits: {i[0]} ($ {maxPr} )")  
            datafinal.writerow([f"Greatest Increase in Profits: {i[0]} ($ {maxPr} )"])
        if i[1]==minPr:
            print(f"Greatest Decrease in Profits: {i[0]} ($ {minPr} )")
            datafinal.writerow([f"Greatest Increase in Profits: {i[0]} ($ {maxPr} )"])