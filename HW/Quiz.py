def quiz():
    import time
    marks = 0
    QA1 = ("" or "")
    QA2 = ("" or "")
    QA3 = ("" or "")
    QA4 = ("" or "")
    QA5 = ("" or "")
    QA6 = ("D" or "d")
    QA7 = ("B" or "b")
    QA8 = ("" or "")
    QA9 = ("" or "")
    QA10 = ("" or "")
    c_ans = [QA1, QA2, QA3, QA4, QA5, QA6, QA7, QA8, QA9, QA10]
    
    print("This is a Quiz about computers")
    time.sleep(2)
    
    print("\nQ1. What is the function of a CPU in a computer? ")
    print("A. To store files and documents")
    print("B. To process and execute instructions")
    print("C. To display images on the screen")
    print("D. To connect to the internet")
    ans1 = input("Your Answer: ")
    
    print("\nQ2. What does RAM stand for, and what is its role in a computer?")
    print("A. Random Access Memory; stores temporary data for quick access")
    print("B. Read Access Memory; stores files permanently")
    print("C. Randomly Available Memory; speeds up downloads")
    print("D. Readable Access Memory; stores pictures and videos")
    ans2 = input("Your Answer: ")
    
    print("\nQ3")
    ans3 = input("Your Answer: ")
    
    print("\nQ4")
    ans4 = input("Your Answer: ")
    
    print("\nQ5")
    ans5 = input("Your Answer: ")
    
    print("\nQ6. How many Bits are in a byte?")
    print("A. 4")
    print("B. 32")
    print("C. 1024")
    print("D. 8")
    ans6 = input("Your Answer: ")
    print("\nQ7. What is a Virus?")
    print("A. An Anti-Malware software")
    print("B. A program designed to steal or damage data")
    print("C. A computer component")
    print("D. A software that can help with spelling and Grammar")
    ans7 = input("Your Answer: ")
    
    print("\nQ8")
    ans8 = input("Your Answer: ")
    
    print("\nQ9")
    ans9 = input("Your Answer: ")
    
    print("\nQ10")
    ans10 = input("Your Answer: ")
    
    ans = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10]
    for i in range(10):
        if ans[i] == c_ans[i]:
            marks += 1
        else:
            print(f"Q{i+1} was incorrect")
        
        
quiz()