import tkinter as tk
import random
import math
import sys
import os

sys.path.insert(0, os.path.abspath('Spirograph'))
sys.path.insert(0, os.path.abspath('Snake'))
sys.path.insert(0, os.path.abspath('Avoid_cars_game'))
sys.path.insert(0, os.path.abspath('US_states_game'))
sys.path.insert(0, os.path.abspath('Hirst'))
from spirograph import create_spirograph
from snake_game import snake_game
from states_game import states_game
from avoid_cars import avoid_cars_game
from hirst_painting import hirst_painting
import turtle

class SpinningWheel:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Color Wheel")

        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.options = ["Spirograph", "Snake", "Guess U.S. States", "Car Racing", "Hirst Painting"]
        self.colors = ["red", "green", "blue", "yellow", "purple"]
        self.angle = 0
        self.spinning = False
        self.spin_speed = 5  # Starting speed
        self.acceleration = 4.0  # Acceleration factor
        self.spin_duration = 3000  # Total duration of spin in ms
        self.draw_wheel()

        self.spin_button = tk.Button(root, text="Spin the Wheel", command=self.start_spin, height=1, width=10)
        self.spin_button.pack(pady=10)
        self.pointer = self.create_pointer()  # Create the pointer

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack()

    def create_pointer(self):
        # Create a triangular pointer at the center of the wheel
        x1, y1 = 200, 180  # Point of the triangle
        x2, y2 = 190, 200  # Bottom left
        x3, y3 = 210, 200  # Bottom right
        return self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='black', outline='black')

    def draw_wheel(self):
        self.canvas.delete("wheel")
        for i, (color, option) in enumerate(zip(self.colors, self.options)):
            start_angle = i * (360 / len(self.options)) + self.angle
            end_angle = (i + 1) * (360 / len(self.options)) + self.angle
            self.canvas.create_arc(50, 50, 350, 350, start=start_angle, extent=(360 / len(self.options)), fill=color, outline="black", tags="wheel")
            self.create_pointer()  # Create the pointer
            
        for i, (color, option) in enumerate(zip(self.colors, self.options)):
            # Draw option text on the wheel
            start_angle = i * (360 / len(self.options)) + self.angle
            end_angle = (i + 1) * (360 / len(self.options)) + self.angle
            mid_angle = (start_angle + end_angle) / 2
            x = 200 + 100 * (math.sin(math.radians(20+mid_angle)))  # Adjusted radius for better placement
            y = 200 + 100 * (math.cos(math.radians(20+mid_angle)))
            self.canvas.create_text(x, y, text=option, font=("Arial", 14), fill="black", tags="wheel")

    def start_spin(self):
        if not self.spinning:
            os.system('clear')
            self.spinning = True
            self.angle = random.randint(0, 360)  # Start angle for the spin
            self.spin_speed = 10  # Reset speed for each spin
            self.spin_wheel(0)  # Start the spin

    def spin_wheel(self, elapsed):
        if elapsed < self.spin_duration:
            # Increment the angle for the spinning effect
            self.angle += self.spin_speed 
            self.angle = self.angle % 360
            self.draw_wheel()
            elapsed += 30  # Update elapsed time
            max_speed = 360  # Maximum speed in degrees per second
            acceleration_time = self.spin_duration / 2  # Time to accelerate to max speed
        
        
            if elapsed < acceleration_time:
                # Acceleration phase
                self.spin_speed= (max_speed / acceleration_time) * elapsed  # Linear acceleration
            elif elapsed < acceleration_time + 1:
                # Constant speed phase
                self.spin_speed = max_speed
            elif elapsed < self.spin_duration:
                # Deceleration phase
                self.spin_speed = max_speed * (1 - ((acceleration_time + 1) ** 2) / ((self.spin_duration - (acceleration_time + 1)) ** 2))
                #max_speed * (1 - (elapsed - (acceleration_time + 1)) / (self.spin_duration - (acceleration_time + 1)))
            else:
                # After total_time
                self.spin_speed = 0
             
            self.root.after(30, lambda: self.spin_wheel(elapsed))
        
        else:
            self.spinning = False
            self.finalize_spin()
        
        '''
            # Accelerate and then slow down
            if elapsed < self.spin_duration // 5:
                self.spin_speed += self.acceleration  # Speed up
            elif elapsed < 2*self.spin_duration // 5:
                self.spin_speed = max(0, self.spin_speed - self.acceleration)  # Slow down
            else:
                self.spin_speed = max(0, self.spin_speed - 3*self.acceleration)  # Slow down
        '''

        
    def ask_question(self, func, q_input):
        # Create the main window
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        

        # Show the popup dialog with a question
        response = tk.messagebox.askquestion("Question", q_input)
        
        # Handle the response
        if response == 'yes':
            func()
            root.destroy()
        else:
            root.destroy()
        
  
    
    def finalize_spin(self):
        selected_index = int(1-(self.angle -90) // 72) % 5 
        self.result_label.config(text=f"Selected: {self.options[selected_index-1]}")
        turtle.bye()
        if selected_index == 1:
            self.ask_question(create_spirograph, "Do you want to see a beautiful spirograph?")
        elif selected_index == 2:
            self.ask_question(snake_game, "Do you want to play a game of snake?")
        elif selected_index == 3:
            self.ask_question(states_game, "Do you want to try naming all the states in the U.S.?") 
        elif selected_index == 4:
            self.ask_question(avoid_cars_game, "Do you want to help a turtle cross a busy street?")
        else:
           self.ask_question(hirst_painting, "Do you want to enjoy a digitally created Hirst painting?")


        
if __name__ == "__main__":
    root = tk.Tk()
    
    # Set the size of the window (width x height)
    root.geometry("400x450")
    
    # Optionally, set a minimum size
    root.minsize(300, 200)
    
    # Optionally, set a maximum size
    root.maxsize(2000, 1000)
    

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)
    y = (screen_height // 2) - (300 // 2)
    root.geometry(f"+{x}+{y}")
    
    wheel = SpinningWheel(root)
    
    root.mainloop()
    
    
