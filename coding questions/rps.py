m=input("")

def rps(m):
    if m=="rock":
        return "paper"
    elif m=="paper":
        return "scissors"
    elif m=="scissors":
        return "rock"
    else:
        return "invalid move"

print("winning move:",rps(m))