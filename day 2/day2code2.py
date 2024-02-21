no_of_glasess=int(input("Enter a number"))
total_cost=no_of_glasess*50
sugarcane=total_cost*(20/100)
salt_mint = total_cost*(20/100)
shop_rent=total_cost*(30/100)
profit = total_cost - (sugarcane+salt_mint+shop_rent)
print(int(profit))
