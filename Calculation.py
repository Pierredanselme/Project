def transcription(Ts):         #Program that convert DNA into RNA for the disease B
    RNA = ''
    trans = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}

    for base in Ts:
        if base in trans:
            RNA += trans[base]
        else:
            RNA += base

    return RNA

def check_disease_A(DNA):      #Program that compare your DNA with the special sequence of the disease A to see if you have it
    
    D_A = 'AATTCC'
    if D_A in DNA.upper():
        return 'I am sorry but you have the disease A'
    else:
        return 'You do not have the disease A, good news'

def check_disease_B(RNA):     #Program that compare your DNA with the special sequence of the disease B to see if you have it
    D_B = 'UUA'
    if D_B in RNA.upper():
        return 'I am sorry but you have the disease B'
    else:
        return 'You do not have the disease B, very good news'

def menu():                   #Program that display the menu
    print("Welcome to our lab, please choose an option:")
    print("1. Check for disease A")
    print("2. Check for disease B")
    print("3. Check the file")
    print("4. Leave")

def save_results(patient_name, result):    #Program that register your name and the result of your tests
    file = open("results.txt", "a")
    file.write("Patient: " + patient_name + "\n")
    file.write("Result: " + result + "\n\n")
    file.close()

def open_results_file():                   # Program taht show all the patient's results
    
    file = open("results.txt", "r")
    contents = file.read()
    file.close()
    print(contents)
    
 
def main():                               # This is the menu that will link all the programs
    while True:
        menu()
        choice = input("Enter your choice please : ")

        if choice == '1':
            DNA = input("Enter your DNA sequence for the special part of the 6th chromosome (only 6 letters) : ")
            result = check_disease_A(DNA)
            print(result)
            patient_name = input("Enter your name: ")
            save_results(patient_name, result)
        elif choice == '2':
            DNA = input("Enter your DNA sequence for the special part of the 5th chromosome (only 3 letters): ")
            RNA = transcription(DNA)
            result = check_disease_B(RNA)
            print(result)
            patient_name = input("Enter your name for the registration: ")
            save_results(patient_name, result)
        elif choice == '3':
            open_results_file()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


main()
