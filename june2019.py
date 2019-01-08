global weeks,days,daynames,routenames

weeks = 4
days = 5
daynames = ("Mon", "Tue", "Wed", "Thu", "Fri")
routenames = ("A","B","C","D","E","F")

def enterTime(bus):

    print("Enter punctuality value for bus ",bus,": ",sep='',end='')

    valid = False

    while valid is False:

        temp = input()

        try:

            temp = int(temp)
            valid = True
            
        except:

            print("Value must be an integer")

    return temp

def countLate(route):

    counter = 0
    
    for i in route:
        if i < 0:
            counter += 1

    return counter
    
def sumLate(route):

    total = 0

    for i in route:
        if i < 0:
            total += i

    return total

def meanTime(route):

    return(sum(route)/len(route))

def routeAnalysis(name, route):

    print("Route",name)
    
    count = countLate(route)
    meanall = meanTime(route)
    
    if count == 0:
        meanlate = 0
    else:
        meanlate = sumLate(route)/count
           
    print("Number late:     ",count)
    print("Mean punctuality:",meanall)
    print("Mean late:       ",meanlate)

def dayAnalysis(A,B,C,D,E,F):

    valid = False

    while valid is False:

        temp = input("Enter day to analyse (eg Mon2)")

        try:

           weeknum = int(temp[-1])
           day = temp[:3]
           if weeknum in [0,1,2,3] and day in daynames:
               valid = True

        except:

           print("Invalid day. Please enter in the format Mon2.")

    daynum = daynames.index(day)
    index = (days * weeknum) + daynum

    print(weeknum,day,index)    

    count = 0

    count += singleday("A",A,index)
    count += singleday("B",B,index)
    count += singleday("C",C,index)
    count += singleday("D",D,index)
    count += singleday("E",E,index)
    count += singleday("F",F,index)

    print(count,"buses were late on this day.")
    
def singleday(name,route,index):

    print("Route",name)
    print("=======")
    print()

    punctuality = route[index]

    if punctuality < 0:
        print("Bus was",abs(punctuality),"minutes late")
        return 1
    else:
        print("Bus was not late")
        return 0
    

def main():

    A = [0]*(weeks*days)
    B = [0]*(weeks*days)
    C = [0]*(weeks*days)
    D = [0]*(weeks*days)
    E = [0]*(weeks*days)
    F = [0]*(weeks*days)

##    for weeknum in range(weeks):
##
##        print("Week ",weeknum +1)
##        
##        for day in range(days):
##
##            print()
##            print(daynames[day])
##                  
##            index = (weeknum * weeks) + day
##
##            A[index] = enterTime("A")
##            B[index] = enterTime("B")
##            C[index] = enterTime("C")
##            D[index] = enterTime("D")
##            E[index] = enterTime("E")
##            F[index] = enterTime("F")

    A = [0, 0, 0, 2, 2, 4, 0, 3, 4, -2, -5, 0, 0, 3, 4, -1, 8, 1, 1, -2]
    B = [0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0]
    C = [2, 0, -1, -1, -2, -2, -3, -1, 0, 0, -2, 0, 1, 1, 1, 1, -1, -1, 2, -2]
    D = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    E = [-1, -1, -1, -1, -2, -4, -10, -2, 0, 0, 0, 0, 1, 2, -3, 1, 1, 3, -1, 0, 0]
    F = [0, -5, -5, -5, -4, -3, -5, 0, 0, 0, 0, -2, -3, 1, 1, 1, 0, 0, -2, -5]

    print("Route Analysis")
    print("==============")
    print()

    routeAnalysis("A",A)
    routeAnalysis("B",B)
    routeAnalysis("C",C)
    routeAnalysis("D",D)
    routeAnalysis("E",E)
    routeAnalysis("F",F)

    group = [A,B,C,D,E,F]
    for route in group:
        routeAnalysis("Temp",route)
        
    numlates = []

    numlates.append(countLate(A))
    numlates.append(countLate(B))
    numlates.append(countLate(C))
    numlates.append(countLate(D))
    numlates.append(countLate(E))
    numlates.append(countLate(F))

    mostLates = max(numlates)
    position = numlates.index(mostLates)
    worstroute = chr(65+position)

    print("Worst route is Route",worstroute)

    # Day Analysis

    dayAnalysis(A,B,C,D,E,F)
           
main()

