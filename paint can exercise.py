wall_height=input("What is the height of the wall?")
wall_width=input("What is the width of the wall?")
total_wall_area=int(wall_height)*int(wall_width)
total_paint_area=total_wall_area*2
a_tin_of_paint_area=10
paint_needed=total_paint_area/int(a_tin_of_paint_area)
paint_needed=round(paint_needed)
print(f"The number of paint cans needed = {paint_needed}.")
