def check(val):
    if val == 0:
        raise ValueError("Zero not allowed")
    elif val < 0:
        raise ValueError ("Negative number is not allowed!")
    
    try:
        t = val**0.5
        print (t)
    except ValueError as e:
        print ("Squareroot not possible")
    except Exception as e:
        print (e)


check("a")