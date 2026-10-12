Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# ==========================================
# STEP 1: GRADE SYSTEM WITH INPUT VALIDATION
# ==========================================

# try-except ensures the program doesn't crash if the user accidentally types letters
try:
    # Captures text input and immediately converts it to a whole number (integer)
    tamil = int(input('tamil mark: '))

    # Step 1a: Checks if the mark is between 90 and 100 inclusive
    if 90 <= tamil <= 100:
        print("grade O")
        
    # Step 1b: If not matching above, checks if the mark is between 80 and 89 inclusive
    elif 80 <= tamil <= 89:
        print("grade a")
        
    # Step 1c: Checks if the mark is between 70 and 79 inclusive
    elif 70 <= tamil <= 79:
        print("grade b")
        
    # Step 1d: Checks if the mark is between 60 and 69 inclusive
    elif 60 <= tamil <= 69:
        print("grade c")
        
    # Step 1e: Checks if the mark is between 50 and 59 inclusive
    elif 50 <= tamil <= 59:
        print("grade d")
        
    # Step 1f: Checks if the mark is between 0 and 49 inclusive (Fixed logic to include 0)
    elif 0 <= tamil <= 49:
        print("fail")
        
    # Step 1g: Triggers if the number is out of bounds (e.g., -10 or 105)
    else:
        print('enter valid mark')

# Handles cases where input cannot be turned into a number (e.g., entering "abc")
except ValueError:
    print('enter valid mark (integers only)')


... # Visual separator line in the terminal
... print("-" * 20)  
... 
... 
... # ==========================================
... # STEP 2: ELIGIBILITY SYSTEM
... # ==========================================
... 
... try:
...     # Prompts for age and weight inputs and converts them to integers
...     age = int(input('enter age: '))
...     weight = int(input('enter weight: '))
... 
...     # Step 2a: Evaluates both conditions simultaneously using 'and' logic.
...     # BOTH must be true (Age must be strictly above 15 AND weight must be strictly above 50)
...     if age > 15 and weight > 50:
...         print('eligible')
...         
...     # Step 2b: If either age is 15 or less, OR weight is 50 or less, this fallback runs
...     else:
...         print('not eligible')
... 
... # Prevents terminal crashes if inputs for age or weight are non-numeric strings
... except ValueError:
...     print('enter valid numbers for age and weight')
