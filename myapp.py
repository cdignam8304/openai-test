
# Get Google Bard cookie
with open('bardkey.txt', "r") as f:
    bard_cookie = f.readline()
# print(bard_cookie)


import bardapi
import os


# set your input text
input_text = "Write a poem about a cat with no more than 10 lines."

# set your __Secure-1PSID value to key
# Send an API request and get a response.
response = bardapi.core.Bard(token=bard_cookie).get_answer(input_text)
print(response)

