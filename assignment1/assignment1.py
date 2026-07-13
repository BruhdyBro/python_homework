def hello():
    return("Hello!")


def greet(name):
    return("Hello, " + name + "!")


def calc(a, b, operation="multiply"):
    if (operation == "multiply"):
        try:
            return a*b
        except (TypeError):
            return "You can't multiply those values!"
    elif (operation == "add"):
        return a+b
    elif (operation == "divide"):
        try:
            return a/b
        except (ZeroDivisionError):
            return "You can't divide by 0!"
    elif (operation == "subtract"):
        return a-b
    elif (operation == "modulo"):
        return a%b
    elif (operation == "int_divide"):
        return a//b
    elif (operation == "power"):
        return pow(a,b)
    return "Unknown operation"


def data_type_conversion (val, datatype):
    try:
        if (datatype == "int"):
            try:
                return int(val)
            except (Exception):
                return "You can't convert " + val + " into a int."
            
        elif (datatype == "float"):
            try:
                return float(val)
            except (Exception):
                return "You can't convert " + val + " into a float."
            
        elif (datatype == "str"):
            return str(val)
    except:
        return f"You can't conver {val} into  a {datatype}."
        

def grade(*args):
    try:
        average = sum(args)/len(args) 
    except(Exception):
        return "Invalid data was provided."
    
    if (average >= 90):
        return "A"
    elif(average >= 80):
        return "B"
    elif(average >= 70):
        return "C"
    elif(average >= 60):
        return "D"
    else:
        return "F"
    

def repeat(string, count):

    newString = ""
    for i in range(count):
        newString += string

    return newString


def student_scores(posParam, **kwargs):
    if (posParam == "mean"):
        sum = 0
        for value in kwargs.values():
            sum += value
        return sum/len(kwargs)
    
    elif (posParam == "best"):
        firstName = next(iter(kwargs))
        best = kwargs.get(firstName)
        bestName = "Tom"
        for key, value in kwargs.items():
            if (value > best):
                best = value
                bestName = key
        return bestName
    

def titleize(input):
    words = input.split()
    for i, word in enumerate(words):

        if (i == 0):
            words[i] = word.capitalize()
        
        elif (i == len(words)-1):
            words[i] = word.capitalize()
        
        elif (word == "a" or
            word == "on" or
            word == "an" or
            word == "the" or
            word == "of" or
            word == "and" or
            word == "is" or
            word == "in"):
                continue
        else:
            words[i] = word.capitalize()
    return " ".join(words)


def hangman(secret, guess):
    hiddenWord = ["_"] * len(secret)

    for i, char in enumerate(secret):
        if (char in guess):
            hiddenWord[i] = char
    return "".join(hiddenWord)


def pig_latin(input):
    words = input.split()
    codeword = [""] * len(words)
    for j, word in enumerate(words):
        individual = ""

        if (word[0] == "a" or
            word[0] == "e" or
            word[0] == "i" or
            word[0] == "o" or
            word[0] == "u"):
            individual = word + "ay"

        else:
            count = 0
            while count < (len(word)):
                if ( (word[count] == "q") and (count != len(word) - 1) and (word[count+1] == "u") ):
                    count += 2

                elif (word[count] != "a" and
                    word[count] != "e" and
                    word[count] != "i" and
                    word[count] != "o" and
                    word[count] != "u"):
                        count += 1

                else:
                    break
            individual = word[count:len(word)] + word[0:count] + "ay"
        
        codeword[j] += individual
    
    return " ".join(codeword)       