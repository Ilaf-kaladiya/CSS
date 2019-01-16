def encrypt(text,s): 
    result = "" 
  
    for i in range(len(text)): 
        char = text[i] 
  
        
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  
text = input("Enter Text:\n")
text = text.replace(" ","")
s = int(input("Enter shifts:\n"))
e_text =encrypt(text,s)

print ("Text  : " + text )
print ("Shift : " + str(s))
print ("Cipher: " + e_text) 

key=input("Enter textual key:\n")

chars=list(key)
s_chars=sorted(chars)

order=[]

for i in chars:
    if i==-1:
        continue
    ind=s_chars.index(i)
    del s_chars[ind]
    s_chars.insert(ind,-1)
    order.append(ind+1)
lkey=len(key)
lpt=len(e_text)

rows,remain =divmod(lpt,lkey)
extra=lkey-remain

if remain>0:
    rows+=1
    for i in range(extra):
        
        pt=pt+"!"

mat_pt = []

for i in range(1,rows+1):
    if i==1:
        start=0
        end=lkey
    else:
        start=end
        end=i*lkey
    temp=[]
    temp=list(e_text[start:end])
    mat_pt.append(temp)
lmat_pt = len(mat_pt)

ct=[]

for k in range(1,lkey+1):
    
    ### get current column number
    j=order.index(k)
    temp=[]
    
    for i in range(lmat_pt):
        temp.append(mat_pt[i][j])
    ct.append(temp)

CIPHER = ""
for i in ct:
    for j in i:
        CIPHER=CIPHER+j
Single=CIPHER

print("Product Cipher: " +Single)


