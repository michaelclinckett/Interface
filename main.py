#______IMPORT________#
import tkinter as tk
from tkinter import messagebox
import math
from colorama import Fore
from data import _Ones, _Tens, _placeholders

#______DEFINE_______#
error =("not supporting yet")
#___________________CONVERTING FUNCTION_____________________________#
def main():
  lb_output.config(state="normal")
  lb_output.delete('1.0', "end")
  
  validation()

def validation():
  global display
  str = lb_input.get()
  msg = ''
  try:
    if str[0] == ".":
      str = "0"+str
  except IndexError:
    display = ""
    msg = "Please put in something"
    
  try:                #try if input number
    float(str)
    if float(str) >= 0:      #Try if numeber bigger or equal 0
      convert(str)
    else:  
      display = ""
      msg = "Please enter a positive number to convert"
      
    
  except ValueError:
    display = ""
    msg = "Please put in a VALID number"
 
  if msg != '':
    messagebox.showinfo('message', msg)

#==Convert numeral to english words============================================#
def convert(raw_num):
  global display
  num1 = ""
  num2 = ""
  display = ''
  try:
    if "." in raw_num:
      split_num = raw_num.split(".")
      num1, num2 = split_num 
      num1 = int(num1)
      num2 = num2[0:3]
      num2 = int(num2)/(10**len(num2))
      #print(num2)
      num2 = round(num2, 2)
      #print(num2)
      num2 = num2*100
      #print(split_num)
    
      if num2 == 100:
        num1 = num1 + 1
        num2 = ""
    else:
      num1 = int(raw_num) 
  except ValueError:
    messagebox.showinfo('message', "Please put in a valid input")


  if len(str(num1)) > 126:
    messagebox.showinfo('message', "Sorry, this number is larger than our dictionary")
    
  else:
  
    if num2 == "":
      if num1 < 100:    #checking to use 2_digit or 3_digit convert
        two_output = two_d_convert(num1)
        if two_output == "one":        
          display = (two_output.capitalize(), "dollar")
          display_calc_dollar(display)
        else:
          display = " ".join((two_output.capitalize(), "dollars"))
          display_calc_dollar(display)
      elif num1 < 1000:
      
        display = " ".join((three_d_convert(num1).capitalize(), "dollars"))
        display_calc_dollar(display)
      else:      #larger than 1000 input
        output_str = more_convert(num1).capitalize(), "dollars"
        display = ("".join(output_str))
        display_calc_dollar(display)
        
  
  
    else:                      #decimal number loop

      if num1 == 0:
        display = (" ".join(cents_convert(num2)).capitalize())
        display_calc_dollar(display)
      elif num1 < 100:
        two_output = two_d_convert(num1)
        if two_output == "one":        
          raw_display = (((two_output).capitalize()),"dollar and", " ".join(cents_convert(num2)))
          display = " ".join(raw_display)
          display_calc_dollar(display)
        else:
          raw_display = ((two_output).capitalize()),"dollars and", " ".join(cents_convert(num2))
          display = " ".join(raw_display)
          display_calc_dollar(display)

      elif num1 < 1000:
      
        raw_display = (three_d_convert(num1).capitalize()),"dollars","and", " ".join(cents_convert(num2))
        display = " ".join(raw_display)
        display_calc_dollar(display)
      
    
      else:
        cents_output = "".join(((more_convert(num1).capitalize()),"dollars"))
        raw_display = (cents_output,"and", " ".join(cents_convert(num2)))
        display = " ".join(raw_display)
        display_calc_dollar(display)
      
  

  
#==Two digit handling =========================================================#

def two_d_convert(num):
  if num < 20:                      #validate if number fit requirement for   dictionary 1

    return (_Ones[num])    #This should able to convert number with in 1-19
        
  else:
      tens, ones = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_in_words = _Tens[tens]  #From dictionary find tens

      if ones != 0:
        one_in_words = _Ones[ones]  #From dictionary find ones
        return " ".join((ten_in_words, one_in_words))  #prints the dollar amount
        
      else:
        return (ten_in_words)
  


#==Convert decimal to cents ===================================================#    

def cents_convert(cent):
  if cent < 20:                      #validate if number fit requirement for   dictionary 1
      if cent == 1:
        return (_Ones[cent], "cent")    #Print one dollar
      else: 
        return (_Ones[cent], "cents")    #This should able to convert number with in 1-19
  elif cent < 100:
      ten_cents, single_cents = [(cent//(10**i))%10 for i in range(math.ceil(math.log(cent, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_cents_in_words = _Tens[ten_cents]  #From dictionary find tens

      if single_cents != 0:
        single_cents_in_words = _Ones[single_cents]  #From dictionary find single_cents
    
        return (ten_cents_in_words, single_cents_in_words, "cents")  #prints the dollar amount
      else:
        return (ten_cents_in_words, "cents")
  else:    #number greater than 100
      return (Fore.RED +"There is an error"+Fore.WHITE)


#==Three digits handling ======================================================#
def three_d_convert(num):
  raw_hundred = int(num/100)                  #first number in three digit
  raw_number = num - (raw_hundred*100)        #the last two digit
  if raw_hundred != 0:
    if raw_number != 0:
    
      hundred = " ".join((_Ones[raw_hundred], "hundred"))
      return " ".join((hundred,"and", two_d_convert(raw_number)))
    else:
      hundred = " ".join((_Ones[raw_hundred], "hundred"))
      return hundred
  else:
    return (two_d_convert(raw_number))

    

#==Handling more than 4 digits number =========================================#
def more_convert(num):
  two_digit = ""
  string = ""
  loop_time = 0
  while num >= 100:
    last_three_numbers = int(str(num)[-3:])                #Pull out the last three digits from input                          
    num = num//1000                                        #Truncate the last three digits
    
    if loop_time != 0:      
      last_three_digits = three_d_convert(last_three_numbers)+" "+_placeholders[loop_time]+" "
    else:
      last_three_digits = three_d_convert(last_three_numbers)+" "
    if last_three_numbers == 0:
      loop_time += 1
    else:
      string = last_three_digits + string
      loop_time += 1

  else:    
    if num == 0:
      return (string.capitalize())
    else:
      two_digit = two_d_convert(num)+" "+_placeholders[loop_time]+" "
      outcome = two_digit + string
      return(outcome.capitalize())




#______FUNCTION FOR TKINTER_______#

def display_calc_dollar(display):
    lb_output.config(state='normal')
    #age calculated is insert into the text box after clearing th eprevious info in the textbox.
    lb_output.delete('1.0', tk.END)
    lb_output.insert(tk.END, display)
    lb_output.config(state='disabled')


def export():


  text_file = open("output.txt", "w")
  
  try:
    n = text_file.write(str(display))
    if str(display) == '':
      messagebox.showinfo('ERROR', "No text is available to export")
    else:
      
      text_file.close()
  except NameError:
    messagebox.showinfo('ERROR', "No text is available to export")
  



#________MAIN_________#

window = tk.Tk()
window.geometry("600x350")
window.config(bg="#ed9c40")
window.resizable(width=False, height=False)
window.title("Number to Dollars converter")
 
#_______LABEL________#
lb_title = tk.Label(window, text="Number to dollars converter", font=("Arial", 20), fg="white", bg="#ed9c40")

lb_input_lb = tk.Label(window, text="Please type in a numeral number here to convert to english words:", font=("Arial", 12), fg="white", bg="#ed9c40")

lb_limit = tk.Label(window, text="*The limit of convertion is 10^126 for this program", font=("Arial", 8), fg="red", bg="#ed9c40")

lb_input = tk.Entry(window, width=47)

lb_output = tk.Text(window, state='disabled', font=("Arial", 8), fg="grey", bg="white", width=60, height=5)

btn_calculate_dollar = tk.Button(window,
                              text="Convert",
                              font=("Arial", 13),
                              command=main)

btn_exit = tk.Button(window,
                     text="Exit Application",
                     font=("Arial", 13),
                     command=exit)

lb_export = tk.Button(window,
                     text="Download",
                     font=("Arial", 13),
                     command=export)

#_______PLACING________#

lb_title.place(x=100, y=20)                        #Title placing

lb_input_lb.place(x=30, y=60)                      #Lable of input placing

lb_limit.place(x=150, y=90)                        #Place note for limit

lb_input.place(x=70, y=110)                        #input box placing

btn_calculate_dollar.place(x=230, y= 150)          #button "Convert" placing

lb_output.place(x=70, y= 210)                      #Output showing box placing

btn_exit.place(x=400, y=300)                       #Exit button placing

lb_export.place(x=225, y=300)

