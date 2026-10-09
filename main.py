#main is defined with no arguments 
#def name_of_function();
#indent for code that belongs to function
#return  --> this is optional. If we dont write return, it will automatically return None


#def main():
    #class_size= 7
    #print("hello class of " + str(class_size)+ "!")
    #single apostrophes
    #print('hello world')
    #triple quotes 
   # print("""hello world""")

    #printing with fStrings
    #print(f"hello class of {class_size}!")
    #use brackets when working with fStrings
    #_name="nina"
   # _rent=8000
    #print(f"Hello my name is {_name} and I pay {_rent/30} in rent per day")
 
    
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

def name_of_function():
    #sample function to show structure 
    print("good example!")



def function_with_args(name):
    print(f"Hello, thank you for your focus {name}")


    #we pass arugemnts to out function
def greeting(name):
    return f"Hello,{name}"

def make_a_fraction(x,y=1):
    return f"{x} / {y}"

def put_under_one(y, x=1):
     return f"{x}/{y}"

def put_under_one_alt(x): 
     return f"1/{x}"

def demo(name, age):
   print(name, age) 

def show_employee(En, salary):
     print("name=", En, " salary=", salary)

def employee(Jessica,salary1):
    print("name2=", Jessica, " salary=", salary1)

     
     
     

#Lists - a data collection option that is ORDERED and MUTABLE 
    #WE declaren list using []
def main(): 
        
        
        
    name = "kyanni" 
    other_name="KG"
    function_with_args(name)
    function_with_args(other_name)
    
    number = "5.0" 
    print(type(int(float(number))))
    print(type(number))
    print(f"Our output is{number}")
    name_of_function()

    #We can store return output into variables for later
    my_greeting = greeting("Ms.Dinko")
    print(my_greeting)

    print(make_a_fraction(15,4))
    make_a_fraction(15,4)

    #print (make_a_fraction(15,4))
    print(make_a_fraction(15))
    demo("Kelly", 25)

    show_employee("Ben", 12000)
    show_employee("jessica", 9000)
  #declaring an empty list that we can add later 
    my_list = []
    my_other_list = list()

    #declaring list with items already in it 
    my_classes = ["Math","Post-AP", "English"]

    print(len(my_classes))
    #we can index using the name of the list followed by [x]
    #our last element in our list is always len(list) -1   
    print(my_classes[2])
    print(my_classes[len(my_classes)-1])
    print(my_classes[-1])

    print(my_classes[-2])
    #using a 0 index always gives us our first element
  

    # we can update and replace an items of our list with indeces 
    my_classes[1] = "AP Comp Sci"
    print(my_classes)

    my_classes[1] +=" A" 
    print(my_classes)

    print(len(my_classes) >=4 )

    my_list = []
    my_other_list = list()
    my_classes = ["math", "computer science", "english"]
    print (len(my_classes))
    print(my_classes[2])
    print(my_classes[len(my_classes)-1])
    print(my_classes[-1])
    my_classes[1] = "ap"
    print(my_classes)
    my_classes[1] += " comp sci"
    print(my_classes)
    print(my_classes.index("math"))
    print("math" in my_classes)
    my_classes.append("journalism")
    my_classes.insert(2, "biology")
    print(my_classes.pop())
    print(my_classes.sort())
    print(my_classes)

    #reverse the list in place ysung .reverse()
    my_classes.reverse()
    print(my_classes)

    print(len(my_classes))

    colors_a =["blue", "turquoise", "baby blue", "red"]
    colors_b =["burgunday", "orange", "blue", "brown"]

   #colors_a = colors_a + colors_b
    colors_a.extend(colors_b)
    print(colors_a)

    print("orange" in colors_a)
    print("pink" in colors_a)

    print(colors_a.index("orange"))
    #print(colors_a.index("pink"))

    #get the frequency or count of an item in a listName.count(item)

    count=colors_a.count("blue")
    print(f"There are {count} blues!")

    #task is updating a list item from turquois to green
    colors_a[colors_a.index("turquoise")]="green"
    print(colors_a)

    
    #.sorted() edits current list 
    #sorted(list)makes a new copy




if __name__ == "__main__":
     main()