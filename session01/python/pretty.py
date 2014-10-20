### "Arrow"

arrow = "->"

def arrowify(**args):
    for key, value in args.items():
        print str(key)+arrow+str(value)
