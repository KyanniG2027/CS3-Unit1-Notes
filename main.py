#main is defined with no arguments 
#def name_of_function();
#indent for code that belongs to function

def main():
    class_size= 7
    print("hello class of " + str(class_size)+ "!")
    #single apostrophes
    print('hello world')
    #triple quotes 
    print("""hello world""")

    #printing with fStrings
    print(f"hello class of {class_size}!")
    #use brackets when working with fStrings
    _name="nina"
    _rent=8000
    print(f"Hello my name is {_name} and I pay {_rent/30} in rent per day")

if __name__ == "__main__":
    main()
        
    
        #NOTES
  
    #Java int x=5; Phython x=5
    #Java is strictly typed while phython is dynamic 
    #Java moreThanOneWord VS PHYTHON underscore more_than_one_word

     # Python comments 
     #not allowed: 
     # -to start with numbers 
     # special char
     #Keywords: and, if, True, False 
     #careful: int, list, string (can be overwritten) 
        #int+int=int or int/int=float or int + float = float
     #NUMBERS in phython int x=500 
     #floats: x=500.1
     #Complex x=30j
     #x=75 float(75)
     #print("your grade us:")
        #print(int(grade))
    def main():
        number = "5.0" 
        print(type(int(float(number))))
        print(type(number))
        print(f"Our output is{number}")
        name_of_function()

    def name_of_function():
        #sample function to show structure 
        print("good example!")

    def function_with_args(name):
        print(f"Hello, thank you for your focus {name}")

    def main():
        name = "kyanni" 
        other_name="KG"
        function_with_args(name)
        function_with_args(other_name)
    