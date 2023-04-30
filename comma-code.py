# create a function that takes a list
#   and returns the elements of said list in a string format
# if the list is empty, return an empty string
# if the length of the list is two or greater,
#   include "and" before the final element
#   e.g. "apples and oranges"
# if the length of the list is three or greater,
#   include a comma after every element except the last
#   e.g. "apples, oranges, and bananas"

# included a couple extra rules:
# do not mutate the original list
# do not make a copy of the list

def writeListAsString(givenList):
    listLength = len(givenList)
    
    if listLength == 0:
        return ""

    resultingString = str(givenList[0])

    # lists with one element cause r[0] to not meet the value constraint
    # i.e. r[i] > stop == False
    # therefore, the range is empty, and the for loop runs zero times
    for i in range(1, listLength):
        if listLength >= 3:
            resultingString += ","
        if listLength >= 2 and givenList[i] == givenList[-1]:
            resultingString += " and"
            
        resultingString += " " + str(givenList[i])

    return resultingString

if __name__ == "__main__":
    print(writeListAsString([]))
    print(writeListAsString(["apples"]))
    print(writeListAsString(["apples", "oranges"]))
    print(writeListAsString(["apples", "oranges", "bananas"]))
    print(writeListAsString([0, 1.0, "two", (3,), [4, 5]]))
