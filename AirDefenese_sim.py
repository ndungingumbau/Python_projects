import random
import math
import time

# Constants
AIRSPACE_SIZE = 100  # The area size of airspace (100x100 units)
DEFENSE_BASE = (50, 50)  # Defense base location

class AerialThreat:
    def __init__(self, id):
        self.id = id
        self.position = (random.randint(0, AIRSPACE_SIZE), random.randint(0, AIRSPACE_SIZE))
        self.is_neutralized = False

    def distance_to_base(self):
        x1, y1 = self.position
        x2, y2 = DEFENSE_BASE
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def __repr__(self):
        return f"Threat {self.id} at {self.position}, Distance to base: {self.distance_to_base():.2f}, Neutralized: {self.is_neutralized}"

class DefenseSystem:
    def __init__(self):
        self.threats = []
    
    def scan_for_threats(self, num_threats):
        """Detects a given number of aerial threats."""
        self.threats = [AerialThreat(i+1) for i in range(num_threats)]
        print("Scanning for threats...")
        time.sleep(1)
        print(f"{num_threats} threats detected:")
        for threat in self.threats:
            print(threat)

    def identify_nearest_threat(self):
        """Finds the nearest threat to the defense base."""
        active_threats = [threat for threat in self.threats if not threat.is_neutralized]
        if not active_threats:
            print("No active threats remaining.")
            return None
        nearest_threat = min(active_threats, key=lambda t: t.distance_to_base())
        print(f"Nearest threat identified: {nearest_threat}")
        return nearest_threat

    def neutralize_threat(self, threat):
        """Neutralizes a given threat."""
        if threat:
            print(f"Neutralizing threat {threat.id} at {threat.position}...")
            time.sleep(1)  # Simulate time to neutralize
            threat.is_neutralized = True
            print(f"Threat {threat.id} neutralized.")

    def defend_airspace(self):
        """Main process of scanning, targeting, and neutralizing threats."""
        while True:
            nearest_threat = self.identify_nearest_threat()
            if nearest_threat is None:
                print("All threats neutralized. Airspace secure.")
                break
            self.neutralize_threat(nearest_threat)
            time.sleep(1)

# Simulation
def simulate_air_defense():
    defense_system = DefenseSystem()
    num_threats = random.randint(3, 8)  # Random number of threats between 3 and 8
    defense_system.scan_for_threats(num_threats)
    defense_system.defend_airspace()

if __name__ == "__main__":
    simulate_air_defense()
