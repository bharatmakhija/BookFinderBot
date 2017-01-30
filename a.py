from b import my_b_variable, my_b_function, MyBClass

def my_a_function(var):
     my_a_variable = my_b_function(var)
     return my_a_variable

if __name__ == '__main__':
     import sys
     command_line_arg = "bharat"
     print(my_a_function(command_line_arg))
