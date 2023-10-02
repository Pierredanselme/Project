def transcription(Ts):                                     # secondary program that transcribe DNA in RNA, it will be used for the disease B
    
    RNA = ''
    trans = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    for base in trans:
        RNA += trans[base] 

    return RNA

def main():
    DNA = input('Give me your special DNA for this part: ')  # You need to give the special sequence of DNA that code for the the texture of the skin (to see if it is correct of it has a mutation)
    B = transcription(DNA)
    D_A = 'AATTCC'                                           # specific sequence of the disease A (impact DNA)
    D_B = 'UUA'                                              # specific sequence of the disease B (impact RNA)

    for i in DNA:        # Check if it is only DNA
        if i not in 'ATCG':
            return 'We ask for the DNA only'

    if D_A in DNA:      # check if the patient has the disease A
        print('You have the disease A')
    else:
        print('You do not have the disease A')

    if D_B in B:
        print('You have the disease B')

    else:
        print('You do not have the disease B')

main()
 



