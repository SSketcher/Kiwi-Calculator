import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

#Seting window fixed dimensions
Window.size = (320, 450)

#Loading kivy language file
Builder.load_file('calc.kv')

class StandardCalc(Widget):

    # String of currently calculating equation
    current_equation = ''
    # String of currently open of math operation or functions
    current_operation = ''


    # Method parsing the text on the calculator
    def __parser(self):
        try:
            if self.current_equation[-1] == '=':
                self.current_operation = f'{self.__equals(self.current_equation)}'
        except:
            pass

        signs = ['-', '(']

        for sign in signs:
            if self.current_operation == '-':
                self.current_operation = ''
            elif sign in self.current_operation:
                self.current_operation = f'({self.current_operation})'
            else:
                pass

        if self.current_equation == '' and self.current_operation == '':
            self.ids.calc_input.text = ''
        elif self.current_operation == '':
            self.ids.calc_input.text = f'{self.__equals(self.current_equation)}'
        else:
            self.ids.calc_input.text = f'{self.__equals(self.current_operation)}'
        self.ids.calc_equation.text = f'{self.current_equation}{self.current_operation}'

    # Method computing given equation
    def __equals(self, equation):
        signs = ['+', '-', '*', '/', '=']
        if equation[-1] in signs:
            equation = equation[:-1]       
            
        try:
            return f'{eval(equation)}'
        except:
            return f'Error'

    # Method clearing calc input and calc equation 
    def clear_all(self):
        self.current_equation = ''
        self.current_operation = ''

        self.__parser()

    # Method clearing calc input
    def clear(self):       
        if '=' in self.current_equation:
            self.current_equation = ''
            self.current_operation = ''
        else:
            self.current_operation = ''

        self.__parser()

    #Method for eraseing last element in the calc input
    def erase(self):
        if '/' in self.current_operation or '(' in self.current_operation or '**' in self.current_operation:
            self.current_operation = ''
        elif '=' in self.current_equation:
            self.current_equation = ''
            self.current_operation = ''
        else:
            self.current_operation = self.current_operation[:-1]

        self.__parser()

    # Method for math signes
    def math_operation(self, sign):
        signs = ['+', '-', '*', '/']

        try:
            if self.current_equation[-1] == '=':
                self.current_equation = ''
            elif self.current_equation[-1] in signs and self.current_operation == '':
                self.current_equation = f'{self.current_equation[:-1]}{sign}'
        except:
            pass

        if self.current_operation == '0' or self.current_operation == 'Error' or self.current_operation == '':
            pass
        elif self.current_equation == '':
            self.current_equation = f'{self.current_operation}{sign}'
            self.current_operation = ''
        else:
            self.current_equation = f'{self.current_equation}{self.current_operation}{sign}'
            self.current_operation = ''

        self.__parser()

    # Method adding decimal point in current number
    def decimal_point(self):
        if self.current_operation == 'Error' or self.current_operation == '':
            self.current_operation = f'0.' 
        elif '.' in self.current_operation:
            pass
        else:
            self.current_operation = f'{self.current_operation}.'

        self.__parser()

    # Method for numeric buttons
    def numeric_keypad(self, button):
        try:
            if self.current_equation[-1] == '=':
                self.current_equation = ''
                self.current_operation = f'{button}'
        except:
            pass

        if self.current_operation == '0' or self.current_operation == 'Error':
            self.current_operation = f'{button}'
        else:
            self.current_operation = f'{self.current_operation}{button}'

        self.__parser()
    
    # Method for changing sign of current operation
    def change_sign(self):
        if self.current_operation == '' or self.current_operation == 'Error' or self.current_operation == '0':
            pass
        elif '-' in self.current_operation:
            self.current_operation = f'{self.current_operation[1:]}'
        else:
            self.current_operation = f'-{self.current_operation}'

        self.__parser()

    # Method for applying math operation on current operation
    def mathfunc(self, func):      
        if self.current_operation == '0' or self.current_operation == 'Error' or self.current_operation == '':
            pass
        else:
            if func == 1:
                self.current_operation = f'({self.current_operation})/100'
            elif func == 2:
                self.current_operation = f'1/({self.current_operation})'
            elif func == 3:
                self.current_operation = f'({self.current_operation})**2'
            elif func == 4:
                self.current_operation = f'({self.current_operation})**(1/2)'

        self.__parser()
    


class KiwiCalculator(App):
    def build(self):
        return StandardCalc()

if __name__ == '__main__':
    KiwiCalculator().run()