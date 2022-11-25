# International Standard Book Numbers Validator

## Space Complexity Analysis
~~~
Space complexity = O(n) 

The worst case will take place if the new ISBN-13 number is the last number you can increament "new_isbn_13" with before it becomes a 14 digits number.
~~~

${\text{ let } O(n) = f(x) \text{ and } {O(n^2)} = g(x)}$

${\text{ Since n ∝ space, } g(x) \text{ is the tightest } f(x) \text{ upper-bound:}}$

${\text{ iff, } f(n) \le g(x) \text{ where }, n \ge n_0 \text{ and } n_0 > 0}$ 


```python
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
```





 

 
