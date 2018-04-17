from functools32 import lru_cache

global lifespan

@lru_cache()
def mature(month) :
    if month == 1:
        return 0
    else:
        return totals(month-1) - deaths(month)

@lru_cache()
def new_born(month) :
    if month == 1 :
        return 1
    elif month >= 2 :
        return mature(month-1)

@lru_cache()
def deaths(month) :
    if month <= lifespan :
        return 0
    else :
        return new_born(month-lifespan)

@lru_cache()
def totals(month) :
    return mature(month) + new_born(month)


if __name__ == '__main__' :
    global lifespan
    lifespan = 18
    i = totals(88)
    print i
