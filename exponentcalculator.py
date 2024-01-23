# Calculate the Exponent

# Function
def base_and_exponent(base, exp):
    result = 1
    # Loop
    for p in range(exp):
        result *=base
# Print
    print(base, "raised to the power of", exp, "is:", result)
# Given