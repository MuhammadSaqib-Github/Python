def decryptMessage(strng):
    thisdict = {
    '[':'1',
    '_':'2',
    ')':'3',
    '}':'4',
    ']':'5',
    '{':'6'
}
    decryptM = ""
    for element in strng:
        for k,v in thisdict.items():
            
            if element == k:
                decryptM+=v              
        
    return(decryptM)
strng = "_[[)}}]"
print("Input String: ",strng)
print("Decrypted String Is: " ,decryptMessage(strng))