# Excercise 02: Identify a Color from RGB Values.
# This program asks the user to enter Red, Green, and Blue values.
# Each RGB value must be an integer between 0 and 255.
# The program then identifies some predefined colors using if, elif, and else.


# Start a try block to check whether the user enters valid integer values.
try:

    # Ask the user to enter the Red component and convert the entered value to an integer.
    red = int(input("Enter Red: "))

    # Ask the user to enter the Green component and convert the entered value to an integer.
    green = int(input("Enter Green: "))

    # Ask the user to enter the Blue component and convert the entered value to an integer.
    blue = int(input("Enter Blue: "))


    # Check whether all three RGB values are within the valid range of 0 to 255.
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:

        # Check whether the RGB values represent Black.
        if red == 0 and green == 0 and blue == 0:

            # Store the identified color name in the variable 'colour'.
            colour = "Black"


        # Check whether the RGB values represent White.
        elif red == 255 and green == 255 and blue == 255:

            # Store the identified color name in the variable 'colour'.
            colour = "White"


        # Check whether the RGB values represent Red.
        elif red == 255 and green == 0 and blue == 0:

            # Store the identified color name in the variable 'colour'.
            colour = "Red"


        # Check whether the RGB values represent Green.
        elif red == 0 and green == 255 and blue == 0:

            # Store the identified color name in the variable 'colour'.
            colour = "Green"


        # Check whether the RGB values represent Blue.
        elif red == 0 and green == 0 and blue == 255:

            # Store the identified color name in the variable 'colour'.
            colour = "Blue"


        # Check whether the RGB values represent Yellow.
        elif red == 255 and green == 255 and blue == 0:

            # Store the identified color name in the variable 'colour'.
            colour = "Yellow"


        # Execute this block when the RGB values do not match any predefined color above.
        else:

            # Store "Mixed Colour" because the RGB combination is valid but not predefined.
            colour = "Mixed Colour"


        # Print the identified color after checking all RGB combinations.
        print(f"Colour: {colour}")


    # Execute this block when one or more RGB values are outside the range 0 to 255.
    else:

        # Display an error message for an RGB value outside the valid range.
        print("Error: RGB values must be between 0 and 255.")


# Catch a ValueError if the user enters something that cannot be converted to an integer.
except ValueError:

    # Display an error message when the entered value is not an integer.
    print("Error: RGB values must be integers.")