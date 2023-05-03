#!/usr/bin/env python3

class MyString:
    
    def __init__(self, value = " "):
        if type(value) == str:
          self.value = value

    def is_sentence(self):
       return self.value[-1] == "."
    
    def is_question(self):
       return self.value[-1] == "?"
    
    def is_exclamation(self):
       return self.value[-1] == "!"
    
    def count_sentences(self):
       new = self.value.replace("?",".")
       new = new.replace("!",".")
       new = new.split(".")
       count = 0
       for string in new:
          print(string)
          if string != "":
             count += 1
          else:
             print("The value must be a string.")
       return count