def unix_match(filename: str, pattern: str) -> bool:
    a = filename
    b = pattern
    import re
    rr = True
    bb = re.findall('(\[.*?\])', b)
    mm = re.sub('(\[.*?\])','$',b)

    x= []
    for i in mm:
        if i != '$':
    		x.append(i)
    qita = ''.join(x)
    tiqu = []
    if len(a) != len(mm):
    	rr = False
    else:
    	for i in range(0, len(mm)):
    		if mm[i] == '$':
    			tiqu.append(a[i])
    	for i in range(0, len(tiqu)):
    		if qita[i] not in a:
    			rr = False
    			break
    		elif '!' in bb[i] and tiqu[i] in bb[i]:
    			rr = False
    			break
    		elif '!' not in bb[i] and tiqu[i] not in bb[i]:
    			rr = False
    			break
    if bb == [] and b != a:
    	rr = False
    if a == b:
    	rr = True
    return rr



if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
