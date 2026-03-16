# Initialize counters for each ice cream flavor
vainilla = 0
chocolate = 0
fresa = 0

# Loop that runs 5 times to ask the user for ice cream choices
for i in range(0,5,1):
    
    # Ask the user which flavor they want and convert the input to an integer
    helado = int(input("que saber de helado deseas 1.vainilla,2.chocolate,3.fresa:"))
    
    # Check if the user selected vanilla
    if helado == 1:
        vainilla += 1  # Increase the vanilla counter
    
    # Check if the user selected chocolate
    elif helado == 2:
        chocolate += 1  # Increase the chocolate counter
    
    # Check if the user selected strawberry
    elif helado == 3:
        fresa += 1  # Increase the strawberry counter
    
    # If the user enters an invalid number
    else:
        # Display an error message asking for a valid option
        print("sabor invalido favor de elegir un numero 1.vainilla,2.chocolate,3.fresa:")

# After the loop ends, display the number of orders for each flavor
print("numero de pedido por sabor:")

# Print the total count for each flavor
print("vainilla:", vainilla)
print("chocolate:", chocolate)
print("fresa:", fresa)