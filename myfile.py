from shapes import Triangle, Rectangle, Oval, Paper

rect1 = Rectangle()
rect1.set_height(100)
rect1.set_width(200)
rect1.set_color('orange')
rect1.draw()

rect2 = Rectangle()
rect2.set_x(100)
rect2.set_y(100)
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color('yellow')
rect2.draw()

oval = Oval()
oval.randomize()
oval.draw()

triangle = Triangle(5, 5, 100, 5, 100, 200)
triangle.set_color('green')
triangle.draw()

Paper.display()