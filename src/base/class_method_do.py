class Student:
   
    def methodA(self):
        pass
    
    #类中方法的相互调用
    def methodB(self):
        self.methodA()