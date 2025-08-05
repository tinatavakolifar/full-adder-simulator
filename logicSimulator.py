print ('This is a full adder circuit simulator. by entering input your output will be given.')
input('Please enter the state of input A, B and C-in with \'y\' or \'n\'. Hit enter to continue.\n')
 
inputList = []
prompts = ['Is input A active?: ', 'Is input B active?: ', 'Is carry-in active?: ']

for prompt in prompts:
    while True:
        answer = input(prompt).lower()
        if answer in ('y', 'n'):
            inputList.append(answer)
            break
        else:
            print ('Invalid input. Please answer with \'y\' or \'n\'')

A, B, C = inputList
A, B, C = [x == 'y' for x in (A, B, C)] # تبدیل بله و خیر به بولین

def xor(a, b): return a != b #تعریف کردن ایکس اور برای پایتون

class FullAdder: #کلاس محاسبه فول ادر
    count = 0
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def sum (self): #محاسبه سام
        return xor(xor(self.A, self.B), self.C)
    def carry (self): #محاسبه کری
        return (self.A and self.B) or (self.C and xor(self.A, self.B))

faWanted = FullAdder(A, B ,C)
print ('The sum of this circuit is %s and the Carry-out of the circuit is %s' % (faWanted.sum(), faWanted.carry()) )
print ('You can also access the full-adder truth table in a file named FAtruthTable.csv')

ttInput = 0b000 #برای وارد کردن ورودی ها در جدول درستی

with open('FAtruthTable.csv','w') as f:
    f.write('A,B,C-in,sum,C-out\n')
    for ttInput in range(8): #تمام طول دامنه ورودی
        C = ttInput & 1
        B = (ttInput >> 1) & 1
        A = (ttInput >> 2) & 1
        fa = FullAdder(bool(A), bool(B),bool(C))
        f.write('%d,%d,%d,%d,%d\n' % (A, B, C, int(fa.sum()), int(fa.carry())))
