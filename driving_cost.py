# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    gas_used = (miles_driven / miles_per_gallon)
    price = gas_used * dollars_per_gallon
    return price
    

def main():
    mpg = float(input())
    gas_price = float(input())
    
    miles10 = driving_cost(mpg, gas_price, 10)
    miles50 = driving_cost(mpg, gas_price, 50)
    miles400 = driving_cost(mpg, gas_price, 400)
    print(miles10, miles50, miles400)

main()