from pynput.mouse import Button,Listener, Controller
import time

mouse = Controller()

#m=0
while True:
    mouse.click(Button.left)
    time.sleep(.5)

#def click(x,y,button,pressed):
    #print(x,y,button,pressed)
#listener monitorar o mouse
#listener = Listener(on_click=click,on_move=move,on_scroll=scroll)
#listener = Listener(on_click=click)
#listener.start()
#listener.join()
#listener.stop()
#mouse.release(Button.right)

#print(mouse.position)
#mouse.position = (15,756)
#mouse.move(150,0)
# 1 click
# mouse.click(Button.left)

# 2 click
# mouse.click(Button.left,2)

#mantem pressionado
#mouse.press(Button.left)

#solta botao
#mouse.release(Button.left)
#mouse.scroll(0,-100)



