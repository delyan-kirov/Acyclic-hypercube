def update_essence_file(input_file: str, output_file: str, new_p: str, new_f: str):
    """Update the values of p and f in an ESSENCE file.

    Args:
        input_file (str): The name of the input file containing the original ESSENCE code.
        output_file (str): The name of the output file to save the updated ESSENCE code to.
        new_p (str): The new value for p.
        new_f (str): The new value for f.
    """
    # Read the contents of the input file
    with open(input_file, "r") as file:
        contents = file.read()

    # Replace the values of p and f with the user input values
    contents = contents.replace("p >= 2", f"p >= {new_p}")
    contents = contents.replace("f >= 1", f"f >= {new_f}")

    # Write the updated contents to the output file
    with open(output_file, "w") as file:
        file.write(contents)

# Example usage
input_file = "boolean.essence"
output_file = "essenceC.essence"
new_p = input("Enter a new value for p: ")
new_f = input("Enter a new value for f: ")
update_essence_file(input_file, output_file, new_p, new_f)