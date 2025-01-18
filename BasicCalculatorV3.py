class Calculator:

    def operator(self, choice, num1, num2):
        #Performs the selected arithmetic operation.
        match choice:
            case 1:
                return num1 + num2 #addition
            case 2:
                return num1 - num2 #subtraction
            case 3:
                return round((num1 * num2), 2) #multiplication, rounded to 2 dp
            case 4:
                return round((num1 / num2), 2) #division, rounded to 2 dp
            case _:
                print('Operation Failed.') #Handles invalid operation selection
    
    def displayMenu(self, num1, num2):
        #Displays a menu and handled user input of arithemtic operations.
        while True:    
            try:
                #Prompt use for airthmetic operation choice.
                choice = int(input('Select your operation:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\nInput: '))
                if choice < 1 or choice > 4: #Data validation check for choice value
                    print('Invalid input.')
                else:
                    ans = self.operator(choice, num1, num2) #Call operator method
                    print(f'\nYour answer is {ans}\n') #Display result
                    return False
            except ValueError:
                print('Invalid input. Please enter a number between 1-4.') #Handling ValueError for non-integer inputs. 

    def readNo(self, prompt):
        #Reads a numerical input from the user with error handling.
        try:
            num = float(input(prompt)) #Input converted to float
            return num
        except ValueError:
            print('Invalid input. Please enter a number.') #Handling ValueError for non-integer inputs.

    def finalMenu(self, num1, num2):
        #Displays the final menu allowing the user to restart, perform another calculation, or exit.
        quit = False
        while True:
            choice = input('Make your next selection\n1) Pick new numbers\n2) Pick a new arithmetic operation\n3) Quit\n')
            match choice:
                case '1':
                    print('Resarting process') #Restart with new numbers.
                    break
                case '2':
                    self.displayMenu(num1, num2) #Go back to arithmetic menu
                case '3':
                    print('Closing calculator.')
                    quit = True #Exit the program
                    break
                case _:
                    print('Invalid selection. Closing calculator.') #Handle invalid inputs
                    quit = True
                    break                   
        return quit
                
def main():
    #Main fuction to run the calculator
    calculator = Calculator()
    quit = False
    while quit == False:
        #Prompt user for two numbers. 
        num1 = int(calculator.readNo('Enter your first number: '))
        num2 = int(calculator.readNo('Enter your second number: '))
        calculator.displayMenu(num1, num2) #Display airthmetic operations
        quit = calculator.finalMenu(num1, num2) #Display final menu

if __name__ == "__main__":
    main()