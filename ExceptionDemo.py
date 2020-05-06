"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nThere was a divide by zero error. Exiting\n")
        exit
    except:
        print("\nUnknown exception\n")
        exit

main()    