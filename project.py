import argparse
import numpy as np
import math
import matplotlib.pyplot as plot

plot.style.use = '_mpl-gallery'

# Define args and parse into "args" variable
parser = argparse.ArgumentParser(
    prog="LaunchLab"
)
parser.add_argument('--speed', help='Speed (m/s) of projectile', type=float)
parser.add_argument('--angle', help='Launch angle (Degs) of projectile', type=float)
parser.add_argument('--initialheight', help='Initial launch height(m) of projectile', type=float)
parser.add_argument('--output', help="Specify the output (plot - creates a graph plotting trajectory, summary - prints flight time, max height and distance travelled)", type=str)
# parser.add_argument('--resistance', help='Resistance acting on projectile', type=float) ADD LATER MAYBE

args = parser.parse_args()

class Projectile:
    g = 9.81  # m/s^2

    def __init__(self, speed, angle, iheight):
        self.speed = speed
        self.angle = angle
        self.iheight = iheight
        self.angle_rad = math.radians(angle)
        self.vx = speed * math.cos(self.angle_rad)
        self.vy = speed * math.sin(self.angle_rad)

    def time_of_flight(self):
        # quadratic formula, taking the positive root
        return (self.vy + math.sqrt(self.vy**2 + 2 * self.g * self.iheight)) / self.g

    def max_height(self):
        return self.iheight + self.vy**2 / (2 * self.g)

    def range(self):
        return self.vx * self.time_of_flight()

    def trajectory(self, num_points=100):
        """Return arrays of x,y points along the flight path."""
        t = np.linspace(0, self.time_of_flight(), num_points)
        x = self.vx * t
        y = self.iheight + self.vy * t - 0.5 * self.g * t**2
        return x, y

    def summary(self):
        return (
            f"Time of flight: {self.time_of_flight():.2f}s\n"
            f"Max height: {self.max_height():.2f}m\n"
            f"Range: {self.range():.2f}m"
        )
    def plot(self):
        x, y = self.trajectory()

        fig, ax = plot.subplots()
        ax.plot(x, y, label="Trajectory", color="tab:blue")

        # mark launch point
        ax.scatter(0, self.iheight, color="green", zorder=5, label="Launch")

        # mark peak
        t_peak = self.vy / self.g
        x_peak = self.vx * t_peak
        ax.scatter(x_peak, self.max_height(), color="red", zorder=5, label="Max Height")

        # mark landing point
        ax.scatter(self.range(), 0, color="black", zorder=5, label="Landing")

        ax.set_xlabel("Distance (m)")
        ax.set_ylabel("Height (m)")
        ax.set_title(f"Projectile Trajectory ({self.speed} m/s @ {self.angle}°)")
        ax.set_ylim(bottom=0)
        ax.grid(True, alpha=0.3)
        ax.legend()

        plot.show()

projectile = Projectile(args.speed, args.angle, args.initialheight)
if not args.output:
    projectile.plot()
else:
    if args.output == "plot":
        projectile.plot()
    elif args.output == "summary":
        print(projectile.summary())
    else:
        parser.print_help()