# ------------------------------------------------------
#        Name: (Jae Harrison)
#       Peers: (add any collaborators)
#  References: (How to Think Like a Computer Scientist (online), lecture slides)
# ------------------------------------------------------


def main():
    """
    This is a Docstring for the main function. This is the short description.

    Here, after a blank line, you can add a longer paragraph description.
    Docstrings are like long comments that we put right under the function definition.
    The Docstring goes from one set of "opening" three double-quotes to
    another set of "closing" three double-quotes. We also try to keep the lines short.
    The Docstring has 4 sections:
      - the short one-line description
      - the paragraph description
      - the Params section that indicates input parameters and return values
      - the "how to run" section called "Example Use".

    PARAMS:
        - None. If the function took an input int of "apples" called num, we would
                indicate it like this: - num: int with number of apples
    RETURNS:
        - None. If the function returned something (like the integer half of num),
                we would indicate it like this: int : integer half of num
    """

    # ========== Setup for HW. DO NOT MODIFY ======
    x=0
    y=0
    a=0
    b=0
    c=0
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    result5 = 0
    # End of Setup code ---------------------------



    # Part 1: Basic Operations
    # =============================================
    # Your code for part 1 under this line and before the print statements
  
    x = 27
    y = 1
    a = 1.5
    b = 7
    c = -1
    
    result1 = (3*x - 9*y)/((2*a)*(b - c))
    #There was definitely a learning curve in remembering the proper way to type equations in Python, I had to go back to the textbook a few times)
    
    print("Part 1: x =", x)
    print("Part 1: y =", y)
    print("Part 1: a =", a)
    print("Part 1: b =", b)
    print("Part 1: c =", c)
    print("Part 1: result =", result1)

    # End of Part 1 ----------------------
 

    # Part 2: Power
    # =============================================
    # Your code for part 2 under this line and before the print statements

    x = 5
    y = -3
    
    result2 = (x**2)*(y**4)
    #I'm curious if this same method work for complex equations in superscript?
    
    print("Part 2: x =", x)
    print("Part 2: y =", y)
    print("Part 2: result =", result2)

    # End of Part 2 ----------------------



    # Part 3: Integer divide
    # =============================================
    # Your code for part 3 under this line and before the print statements
    
    a = 100
    b = 13
    
    result3 = (a//b)
    #I initially had int(a/b) but I decided a//b was not only more concise but a helpful shortcut that I should take advantage of!
    
    print("Part 3: a =", a)
    print("Part 3: b =", b)
    print("Part 3: result =", result3)

    # End of Part 3 ----------------------


    # Part 4: Modulo
    # =============================================
    # Your code for part 4 under this line and before the print statements
    
    result4 = 100 % 13
    #I initially got this part wrong and didn't test it before I committed it, but it was a simple typo fix. 
    
    print("Part 4: result =", result4)

    # End of Part 4 ----------------------

if __name__ == "__main__":
    main()
