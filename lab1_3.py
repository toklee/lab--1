def draw(step):
    print(' ' * int(step * 20),"\x1b[48;5;123m","\x1b[m")
def graf():
    height = 20
    step = 1
    for t in range(height,0,-1):
        draw(step)
        step = t/20
if __name__=="__main__":
    graf()