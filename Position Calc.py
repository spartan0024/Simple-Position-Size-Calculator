n1=float(input('Account Balance: '))
n2=float(input('Entry Price    : '))
n3=float(input('Stop Loss      : '))
n4=float(input('Target Price   : '))
n5=float(input('Risk %         : '))
n6=Quantity=abs((n1/100)*n5)/(n2-n3)
print('Quantity       :',n6)
n7=Risk_Ratio=abs(((n4-n2)*((n1/100)*n5)/(n2-n3))/((n3-n2)*n6))
print('Risk Ratio     :',n7)
n8=Leverage=20
print('Leverage       :',n8)
n9=Margin=(n6*n2)/n8
print('Margin         :',n9)
n10=float(input('Manual RR      : '))
n11=TP=abs((n2-n3)*n10+n2)
print('TP   :',n11)
print('SL   :',n3)
