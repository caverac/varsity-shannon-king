# poor-man version of tokenization
import re


regex_for_matching_punctuation = "[^0-9a-z]"

message = "hi Shannon, this is me"
new_message = re.sub("[^0-9a-zA-Z]", " ", message)


results = new_message.split(" ")

for token in results:
    token_length = len(token)
    message_to_print = f"token is {token} and length is {token_length}"
    print(message_to_print)
