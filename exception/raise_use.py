# _ * _ coding:utf-8 _ * _

class MuffledCalculator:
    muffled=True
    
    def calc(self,expr):
        try:
            #eval只能提供字符串作为参数，如'10/2',会自动转换为整型
            return eval(expr)
        except ZeroDivisionError:
            
            if self.muffled:
                print "Division by zero is illegal"
            else:
                raise

        
