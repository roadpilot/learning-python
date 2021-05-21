#!/usr/bin/env python3

# continue - bypasses the rest of the loop and loops again
# break - breaks out completely from the loop
# else - executes when loop finishes normally

secret = "swordfish"
pw = ''
auth = False
count = 0
max_count = 5

while pw != secret:
    count +=1
    if count > max_count: break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else "Calling the FBI...")