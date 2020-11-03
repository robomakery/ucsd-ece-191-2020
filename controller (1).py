#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame==2.0.0.dev20


# In[1]:


import time
import pygame
from pygame.locals import *

class InputEvent:
    def __init__(self, key, down):
        self.key = key
        self.down = down
        self.up = not down

class InputManager:
    def __init__(self):

        self.init_joystick()

        # XBox button layout designations.
        self.buttons = ['up', 'down', 'left', 'right', 'start']
        
        # If there needs to be a keyboard fallback configuration, fill those out
        # here in this mapping. could copy the same system for the joystick configuration 
        self.key_map = {
            K_UP : 'up',
            K_DOWN : 'down',
            K_LEFT : 'left',
            K_RIGHT : 'right',
            K_RETURN : 'start',
        }
        
        # This will tell us which logical buttons are pressed, whether it's
        # via the keyboard or joystick
        self.keys_pressed = {}
        for button in self.buttons:
            self.keys_pressed[button] = False
        
        # A list of joystick configurations
        self.joystick_config = {}
       
        # When escape is pressed or the user closes the window via its
        # chrome, this flag is set to True. 
        self.quit_attempt = False
    
    # button is a string of the designation in the list above
    def is_pressed(self, button):
        return self.keys_pressed[button]
    
    # This will pump the pygame events. If this is not called every frame,
    # then the PyGame window will start to lock up. 
    def get_events(self):
        events = []
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.quit_attempt = True
            
            # This is where the keyboard events are checked
            if event.type == KEYDOWN or event.type == KEYUP:
                key_pushed_down = event.type == KEYDOWN
                button = self.key_map.get(event.key)
                if button != None:
                    events.append(InputEvent(button, key_pushed_down))
                    self.keys_pressed[button] = key_pushed_down
        
        # checks configured button
        for button in self.buttons:
            
            # determine what something like "Y" actually means in terms of the joystick
            config = self.joystick_config.get(button)
            if config != None:
                
                # button is configured to an axis direction
                if config[0] == 'is_axis':
                    status = self.joystick.get_axis(config[1])
                    if config[2] == 1:
                        pushed = status > 0.5
                    else:
                        pushed = status < -0.5
                    if pushed != self.keys_pressed[button]:
                        events.append(InputEvent(button, pushed))
                        self.keys_pressed[button] = pushed
                
        return events        
    
    # Any button that is currently pressed on the game pad will be toggled
    # to the button designation passed in as the 'button' parameter.
    def configure_button(self, button):
        
        js = self.joystick
        
        # check axes for activity
        for axis_index in range(js.get_numaxes()):
            axis_status = js.get_axis(axis_index)
            if axis_status < -.5 and not self.is_axis_used(axis_index, -1):
                self.joystick_config[button] = ('is_axis', axis_index, -1)
                return True
            elif axis_status > .5 and not self.is_axis_used(axis_index, 1):
                self.joystick_config[button] = ('is_axis', axis_index, 1)
                return True
                
        return False
    
    # determines if a particular axis are already 
    # configured to a particular button designation
    
    def is_axis_used(self, axis_index, direction):
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None and config[0] == 'is_axis':
                if config[1] == axis_index and config[2] == direction:
                    return True
        return False
    
    # The joystick needs to be plugged in before this method is called (see main() method)
    def init_joystick(self):
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        self.joystick = joystick
        self.joystick_name = joystick.get_name()


# In[ ]:




