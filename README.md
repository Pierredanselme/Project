# Identification of a disease

# Context :

All Human have DNA that can mutate into different things and also create diseases. Some of the disease are genetic and can be identify in the DNA of the desired person. 
However, if we can identify a specific sequence of a specific disease and then add it on the program; we can compare the sequence with the DNA of a person, to see if this person have the disease. In our case the disease that impact the texture of the skin.
In addition, diseases can be transcribed into RNA and then protein, so we can also search for specific sequence in the RNA of the person.
For the diseas A, it impact the specific sequence of the 6 th chromosome and for the B it affects the 4th chromosome so you need to put this special sequence in the program)

I think it is a good way to use all the notions that we study and to add more like dictionary etc.. It is also link to my courses in the Tec like biology.

For information the transcription transform A-> U,   T -> A,   C -> G,  and  G -> C (We will use a dictionnary)

               Where A,T,C,G are nucleotids (parts of the DNA)


#Algorithm :

  INTPUT

    - The choice of what test you want to have
    
    - The DNA sequence of the person (the sequence that code for the texture of the skin that can have 2 diseases)

    - Your name if you want to register 
    
    - (A dictionary that convert DNA into RNA and the sequences of the diseases) already in the program


  PROCESS

    - Choose an option for the test that you want 
    
    - With the option that the user enter, open the program that can do this option 

        For the disease A and B : 
                                    - Ask the user for their special sequences 
                                    - Return the result (you have / don't have the disease)

        For the registration:
                                    - Open a file 
                                    - Ask for the name of the user 
                                    - Write the patient's result with his name in a file
                                    - Close the file

        For the program the show the file :
                                                - Open the file 
                                                - Read it in the console
                                                - Close the file



TEST PLAN :

# Test plan 
   
    # If I ask for the test of the disease A and my DNA is AAGTct --> You do not have the disease A, good news
    # Then he will ask me for my name --> Pierre A
    
    # If I ask for the test of the disease B and my DNA is AAT --> I am sorry but you have the disease B
    # Then he will ask me for my name --> Pierre B
    
    #If I ask him to print the list --> Patient: Pierre A
                                       #Result: You do not have the disease A, good news
                                       
                                       #Patient: Pierre B
                                       #Result: I am sorry but you have the disease B

    
  OUTPUT
  
    - The result of your test ( you have / you have not the disease ) if you put 1 or 2
    
    - The file with all the patient if you put 3
