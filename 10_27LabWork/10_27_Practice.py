s = "Program\nCode"          
print("Hello\tWorld")        # \t for tab
print("ABC\bXYZ")            # \b backspace
print("123\r456")        # \r carriage return
print("xxx\fyyy")        # \f form feed
print("MyList:\\")        # \\ backslash

if "Hello":
    print("This string runs")
if "":
    print("This will not run")

num =50
if num > 100:
    print("Greater than 100")
elif num == 50:
    print("Equal to 50")
else:
    print("Less than 100 and not 50")

value =42
match value:
    case 1:
        print("One")
    case 42:
        print("Correct Answer")
    case "Abc":
        print("ABC")
    case _:
        print("Default case")
