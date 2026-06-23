"""9.Write a program to calculate a discount:
  Purchase > 5000 → 20%
  Purchase > 2000 → 10%
  Otherwise → No discount
  using nested if statements."""
purchase = float(input("Enter the purchase amount: "))
if purchase > 2000:
    if purchase > 5000:
        discount = purchase * 0.20
        print("You get a 20% discount of amount:", discount)
        print("Total bill :", purchase - discount)
    else:
        discount = purchase * 0.10
        print("You get a 10% discount of amount:", discount)
        print("Total bill :", purchase - discount)
else:
    print("No discount. Total bill:", purchase)
   