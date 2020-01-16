import turtle as t
"""
t.pd()
for _ in range(5):
    t.fd(100)
    t.lt(72)
    t.fd(100)
    t.rt(144)
t.mainloop()

"""
t.pd()
t.speed(10)
t.pensize(20)
t.pencolor("red")
t.fillcolor("yellow")
t.begin_fill()
for _ in range(8):
    for _i in range(5):
        t.fd(150)
        t.rt(72)
    t.rt(45)
t.end_fill()
t.mainloop()
