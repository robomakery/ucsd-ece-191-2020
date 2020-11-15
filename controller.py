import pygame
import time

pygame.init()
pygame.joystick.init()

done = False

started = False

#Runs when Controller is connected
while not done:
    pygame.event.get()
    joystick_count = pygame.joystick.get_count()

#no joystick found
    if joystick_count < 1:
        print('No Joystick')
        pygame.quit()

#checking for joystick
    if not started:
        print('%s joystick(s) found:' % joystick_count)
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            name = joystick.get_name()
            joystick_id = joystick.get_id()
            print('Name: %s, ID: %s' % (name, joystick_id))
        started = True
        time.sleep(4)

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(joystick.get_name())
    x = joystick.get_axis(0)
    y = joystick.get_axis(1)
    print('%s, %s' % (x, y))