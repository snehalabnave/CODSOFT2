#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
def myCalculator(source, side):
    calcFrame = Frame(source, borderwidth=2, bd=2, bg="black")
    calcFrame.pack(side=side, expand=YES, fill=BOTH)
    return calcFrame

def button(source, side, text, command=None):
    calcButton = Button(source, text=text, command=command)
    calcButton.pack(side=side, expand=YES, fill=BOTH)
    return calcButton
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'helvetica 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right'
              , bd=30, bg="beige").pack(side=TOP,
                                              expand=YES, fill=BOTH)
        for clearButton in (["C"]):
            erase = myCalculator(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))
    
        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = myCalculator(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda
                    storeObj=display, q=iEquals: storeObj
                       .set(storeObj.get() + q))
        EqualButton = myCalculator(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                            storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))
    def calc(self, display):
        try:
            display.set(eval(display.get()))  
        except:
            display.set("ERROR")

if __name__ == '__main__':
    app().mainloop()


# In[ ]:





# In[ ]:




