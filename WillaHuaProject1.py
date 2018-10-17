import os
import filecmp
from dateutil.relativedelta import *
from datetime import datetime

# link to Project 1 repository on GitHub.
# https://github.com/wiiilla/SI206-Project1

def getData(file):

    inFile = open(file,"r")
    line = inFile.readline()
    keys = line.rstrip().split(",")
    dictList = []
    line = inFile.readline()

    while line:

        values = line.rstrip().split(",")
        dict = {}
        for i in range(5):
            dict[keys[i]] = values[i]

        dictList.append(dict)

        line = inFile.readline()

    inFile.close()

    return dictList



def mySort(data,col):
    sortedList = sorted (data, key = lambda items: items[col])
    return sortedList[0]["First"]+" "+ sortedList[0]["Last"]



def classSizes(data):
    count = {}
    for d in data:
        if d["Class"] in count:
            count[d["Class"]] += 1
        else:
            count[d["Class"]] = 1

    return sorted (count.items(), key = lambda tuple: tuple[1], reverse = True )



def findMonth(a):
    count = {}
    for d in a:
        month = d["DOB"].split('/')[0]
        if month in count:
            count[month] += 1
        else:
            count[month] = 1
    sortedList = sorted ( count.items(), key = lambda x: x[1], reverse = True)
    return int(sortedList[0][0])



def mySortPrint(a,col,fileName):
    outfile = open("results.csv","w")
    sortedList = sorted (a, key = lambda items: items[col])
    for i in sortedList:
        outfile.write(i["First"]+","+ i["Last"] + "," + i["Email"] +"\n")

    outfile.close()
    pass



# Extra Credit: Find the average age (rounded) of the Students
def findAge(a):
    # this function accumulated the age of students by days instead of by years, for a higher precision.
    total = 0
    n = len(a)
    for d in a:
        datedob = datetime.strptime(d["DOB"], "%m/%d/%Y").date()
        today = datetime.today().date()
        ageInDays = (today - datedob).days
        # ageInYears = int(ageInDays / 365)
        total += ageInDays
    return int (total / n / 365)





################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
