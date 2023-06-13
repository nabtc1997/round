def round_to(num, digits=3):
    try:
        if num == 0: return 0
        scale = int(math.floor(math.log10(abs(num - int(num))))) + digits
        if scale < digits: scale = digits
        return round(num, scale)
    except: return num
