def transcription(Ts):                                     # secondary program that transcribe DNA in RNA, it will be used for the disease B
    
    RNA = ''
    trans = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    for base in trans:
        RNA += trans[base] 

    return RNA

def main(): # check if you have some disease link to skin's texture
    DNA = input('Give me your special DNA for this part: ')  # You need to give the special sequence of DNA that code for the the texture of the skin (to see if it is correct of it has a mutation)
    B = transcription(DNA)
    D_A = 'AATTCC'                                           # specific sequence of the disease A (impact DNA)
    D_B = 'UUA'                                              # specific sequence of the disease B (impact RNA)
    conclusions = []
    for i in DNA:
        if i not in 'ATCG':     #DNA only have 4 letters 
            conclusions.append('We ask for the DNA only')
            break  

    if D_A in DNA:
        conclusions.append('You have the disease A')
    else:
        conclusions.append('You do not have the disease A')

    if D_B in B:
        conclusions.append('You have the disease B')
    else:
        conclusions.append('You do not have the disease B')

    print(conclusions)

main()
