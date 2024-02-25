from math import sqrt

triangle_side_1 = float(input("please enter triangle_side_1: "))
triangle_side_2 = float(input("please enter triangle_side_2: "))
triangle_side_3 = float(input("please enter triangle_side_3: "))

triangle_perimeter = triangle_side_1 + triangle_side_2 + triangle_side_3
half_triangle_perimeter = triangle_perimeter / 2

triangle_area = sqrt(half_triangle_perimeter
                     * (half_triangle_perimeter - triangle_side_1)
                     * (half_triangle_perimeter - triangle_side_2)
                     * (half_triangle_perimeter - triangle_side_3)
                     )

print(f"Triangle_perimeter  = {triangle_perimeter} ")
print(f"Triangle_area =   = {triangle_area} ")
