message_test = "Welcome in the 1337 world"
##SUBSTITUTION_TEST = [['e', '3']]
SUBSTITUTIONS = [['a', '4'], ['e', '3'], ['l', '1'], ['o', '0'], ['t', '7']]

#Functions section
def coder_message(message, substitutions):
    for s in substitutions:
        vcar = s[0]
        ncar = s[1]
        message = message.replace(vcar, ncar)
        print("Converted text: " + message)
    return message

#Test section in main
message = input("Write the sentence that I must encrypt")
converted_txt = coder_message(message, SUBSTITUTIONS)
print("You had entered : " + message)
print("Your sentence entered, converted gives: " + converted_txt)
