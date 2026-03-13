"""
This module contains the implementation of the `sort` function, 
which classifies packages based on their dimensions and mass. 
"""

MAX_DIMENSION = 150
MAX_VOLUME = 1_000_000
MAX_MASS = 20


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Classifies a package based on its dimensions and mass.
    Args:        
        width (float): The width of the package.
        height (float): The height of the package.
        length (float): The length of the package.
        mass (float): The mass of the package  
    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED" based on the classification
    Raises:
        ValueError: If any of the input dimensions or mass are zero or negative.
    """
    bulky = False 
    heavy = False

    # Validate input: input cannot be 0 or negative
    if width <= 0:
        raise ValueError("Width must be greater than 0")
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    if mass <= 0:
        raise ValueError("Mass must be greater than 0")        

    # If any of the dimensions are greater or equal to MAX_DIMENSION, the package is bulky
    if width >= MAX_DIMENSION or height >= MAX_DIMENSION or length >= MAX_DIMENSION:
        bulky = True

    # If the volume of the package is greater or equal to the MAX_VOLUME, the package is bulky
    if width * height * length >= MAX_VOLUME:
        bulky = True
    
    # If the mass of the package is greater or equal to MAX_MASS, the package is heavy
    if mass >= MAX_MASS:
        heavy = True
    
    # Determine the classification based on the bulky and heavy flags
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"    
    else:
        return "STANDARD"


def test_sort():
    """         
    In production, and with more time, and a standard environment, I would have used Pytest.

    Note: I had issues using Replit (saving/sharing) and CopePen doesn't support Python.   
    """
    test_data = [
        (150, 1, 1, 1, "SPECIAL"),
        (1, 150, 1, 1, "SPECIAL"),
        (1, 1, 150, 1, "SPECIAL"),
        (100, 100, 100, 1, "SPECIAL"),
        (90, 90, 90, 10, "STANDARD"),
        (100, 100, 100, 20, "REJECTED"),
        (0,1,1,1, "ValueError"),
        (1,0,1,1, "ValueError"),
        (1,1,0,1, "ValueError"),
        (1,1,1,0, "ValueError"),
        (-1,1,1,1, "ValueError"),
        (1,-1,1,1, "ValueError"),
        (1,1,-1,1, "ValueError"),
        (1,1,1,-1, "ValueError"),
    ]

    for width, height, length, mass, expected in test_data:
        try:
            result = sort(width, height, length, mass)
            print(f"Input: ({width}, {height}, {length}, {mass}) -> Output: {result} (Expected: {expected})")
        except ValueError:
            print(f"Input: ({width}, {height}, {length}, {mass}) -> Output: ValueError (Expected: {expected})")
   

if __name__ == "__main__":
    # Run the test function for sort.
    test_sort() 
