import re
st = input("are you agree : ")
#^->eta check korbe string er surute.^y(es)?->string er surute yache kina ba y er sathe es o thakte pare.
if re.search("^y(es)?",st,re.IGNORECASE):
    print("agreed")
if re.search("^n(o)?",st,re.IGNORECASE):
    print("disagreed")
