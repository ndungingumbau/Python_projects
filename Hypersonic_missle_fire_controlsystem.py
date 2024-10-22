import math
import time

# Constants
GRAVITY = 9.81  # m/s^2, gravitational constant
SPEED_OF_SOUND = 343  # m/s
HYPERSONIC_MULTIPLIER = 5  # Hypersonic speed starts at 5x the speed of sound
MISSILE_SPEED = SPEED_OF_SOUND * HYPERSONIC_MULTIPLIER  # Hypersonic missile speed in m/s

class Target:
    def __init__(self, x, y, speed, heading):
        self.x = x  # Current x position (m)
        self.y = y  # Current y position (m)
        self.speed = speed  # Speed in m/s
        self.heading = heading  # Heading in degrees (angle of movement)
    
    def move(self, time_interval):
        # Update target position based on current speed and heading
        self.x += self.speed * time_interval * math.cos(math.radians(self.heading))
        self.y += self.speed * time_interval * math.sin(math.radians(self.heading))
    
    def get_position(self):
        return self.x, self.y

class Missile:
    def __init__(self, launch_x, launch_y, launch_angle):
        self.launch_x = launch_x
        self.launch_y = launch_y
        self.launch_angle = launch_angle  # Angle in degrees
        self.speed = MISSILE_SPEED
        self.time_in_air = 0
    
    def get_position(self, time_interval):
        # Calculate missile's current position after being launched
        self.time_in_air += time_interval
        x = self.launch_x + self.speed * self.time_in_air * math.cos(math.radians(self.launch_angle))
        y = self.launch_y + self.speed * self.time_in_air * math.sin(math.radians(self.launch_angle)) - 0.5 * GRAVITY * (self.time_in_air ** 2)
        return x, y

class FireControlSystem:
    def __init__(self, target, missile):
        self.target = target
        self.missile = missile
    
    def launch_missile(self):
        print("Launching missile...")
        for t in range(0, 100):  # Simulate 100 seconds of flight
            time.sleep(1)
            missile_pos = self.missile.get_position(1)
            target_pos = self.target.get_position()
            print(f"Time: {t+1}s | Missile Position: {missile_pos} | Target Position: {target_pos}")
            if self.hit_target(missile_pos, target_pos):
                print("Target hit!")
                break
    
    def hit_target(self, missile_pos, target_pos):
        # Check if missile is close enough to target to be considered a hit
        distance = math.sqrt((missile_pos[0] - target_pos[0]) ** 2 + (missile_pos[1] - target_pos[1]) ** 2)
        return distance < 50  # Consider a hit if within 50 meters

# Example usage
target = Target(x=5000, y=0, speed=200, heading=90)  # A target moving at 200 m/s to the east
missile = Missile(launch_x=0, launch_y=0, launch_angle=45)  # Missile launched at 45 degrees

fire_control = FireControlSystem(target, missile)
fire_control.launch_missile()
