a="Zihan Sun"           #define a string
print("adshdb\ajdndj")  #\a is the alert character
print("djandj\tssjajn") #\t is the tab character
print("adshdb\vjdndj")  #\v is the vertical tab character
print("ABC\bDEF")       #\b is the backspace character
print("abc\ndef")       #\n is the new line character
print("abc\rdef")       #\r is the carriage return character
print("ABC\fDEF")       #\f is the form feed character, statrting a new page
print("ABC\\DEF")
print("ABC\'DEF")      #\\ is the backslash character, \' is the single quote character
print("ABC\"DEF")      #\" is the double quote character
print("ABC\0DEF")     #\0 is the null character
print("ABC\060DEF")  #\ooo is the octal value, transalated to zero
      
if "sjaj":
    print ("If is running")
if "":
    print("If is not running")
x=-100
if x>0:
    print("positive")
elif x==0:
    print("zero")
elif x<0:
    print("negative")

expr1="zihan"
match expr1:
    case "zihan":
        print("First name")
    case 123:
        print("this is a number 123")
    case "test":
        print ("this will not be printed")
    case _:
        print("default case")
    