
def isbn_number_validator(isbn_number):
    
    # ISBN numbers variables
    isbn_10 = 10
    isbn_13 = 13

    if (len(isbn_number) == isbn_13):
        # Multiplies ISBN values with 3 and 1 alternately, 
        # and calculates the sum of the products.
        product_sum_13 = sum([int(isbn_number[i])  * (3 if i % 2 else 1) for i in range(isbn_13)])

        # Checks if the 'product_sum' is divisible by 10
        if product_sum_13 % 10 == 0:
            return True
        else:
            return False 

    if len(isbn_number) == isbn_10:
        product_sum_10 = 0

        for i in range(isbn_10):
                # Multiplies each ISBN value with a range of 10 - 1 integers,
                # in descending order.
                product_sum_10 += int(isbn_number[i]) * (10-i)    

        # Multiplies ISBN values with 3 and 1 alternately, 
        # and calculates the sum of the products when 'product_sum' is divisible by 11
        if product_sum_10 % 11 == 0:
            new_isbn_13 = "978"+isbn_number
            product_sum_isbn_10 = sum([int(new_isbn_13[i])  * (3 if i % 2 else 1) for i in range(isbn_13)])

            # Incremeants 'product_sum_isbn_10' and 'counter' by 1
            # when 10 is not divis
            counter = 0

            # Incremeants 'product_sum_isbn_10' and 'counter' by 1
            # when 10 is not divisible by 10
            while product_sum_isbn_10 % 10 != 0:
                product_sum_isbn_10 += 1
                counter += 1

            print(f"New ISBN-13 = {(counter) + int(new_isbn_13) }")
            return True 
        
        return False
         
def main():    

    isbn_number = "9780316066525"

    # Prints results and raise TypeError exception when 
    # 'isbn_number' entered is not a string.
    try:   
        if isbn_number_validator(isbn_number):
            print("Valid")
        else:
            print("Invalid ISBN number")
    except TypeError:
            print("Invalid value entered, please enter a string of integers.")
    
main()    
    
        
    
    