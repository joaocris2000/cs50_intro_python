#dá as calories do fruto inserido

def main():
    fruit=input("Whats the fruit? ").strip().lower()
    consult(fruit)
    
def consult(valor):
    libre={
        "apple":"130",
        "avocado":"50",
        "banana":"110",
        "cantaloupe":"50",
        "grape fruit":"60",
        "grapes":"90"}
        #haviam mais...
    if valor in libre:
           print(f"calories: {libre[valor]}")
    else:
            print("fruit not recozinable")
      
main()


