price=105.50
qty=36
amount=price*qty
if amount>10000:
    print ("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount


# Type your code here #
# Next condition for 5% discount
elif amount>5000:
    print ("5% discount applicable")
    discount=amount*5/100
    amount=amount-discount

# Next condition for 2% discount
elif amount>2000:
    print ("2% discount applicable")
    discount=amount*2/100
    amount=amount-discount
    
# Next condition for 1% discount
elif amount>1000:
    print ("1% discount applicable")
    discount=amount*1/100
    amount=amount-discount
#else print 'no discount applicable'

else:
    print("Sorry, No discount applicable.")

print ("amount payable:",amount)
