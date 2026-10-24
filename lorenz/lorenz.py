from rcon.source import Client
import numpy as np
import time

class LorenzAttractor:
    def __init__(self, host='localhost', port=25575, password='password'):
        self.rcon = Client(host, port)
        self.rcon.__enter__()
        try:
            self.rcon.login(password)
        except Exception as e:
            print(f"Login failed: {e}")
            self.rcon.__exit__(None, None, None)
            raise
        print("Connected to Minecraft server")

        self.center_x = 0
        self.center_y = 70
        self.center_z = 0

    def close(self):
        if self.rcon:
            self.rcon.__exit__(None, None, None)

    def execute(self, command):
        try:
            response = self.rcon.run(command)
            if isinstance(response, bytes):
                response = response.decode('utf-8')
            return response
        except Exception as e:
            print(f"RCON error: {e}")
            return None

    def lorenz(self, state, sigma=10.0, rho=28.0, beta=8.0/3.0):
        x, y, z = state
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        return np.array([dx, dy, dz])

    def integrate(self, initial_state, steps, dt=0.005):
        points = []
        state = np.array(initial_state, dtype=float)
        for _ in range(steps):
            points.append(tuple(state))
            k1 = self.lorenz(state)
            k2 = self.lorenz(state + 0.5 * dt * k1)
            k3 = self.lorenz(state + 0.5 * dt * k2)
            k4 = self.lorenz(state + dt * k3)
            state += dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0
        return points

    def draw_attractor(self,
                       initial=(0.1, 0.1, 0.1),
                       steps=60000,
                       dt=0.005,
                       scale=3.5,
                       skip=2):
        print(f"Integrating Lorenz system for {steps} steps (dt={dt})...")
        points = self.integrate(initial, steps, dt)

        print("Placing blocks in Minecraft...")
        color_map = [
            'red_wool', 'orange_wool', 'yellow_wool', 'lime_wool',
            'green_wool', 'cyan_wool', 'light_blue_wool', 'blue_wool',
            'purple_wool', 'magenta_wool', 'pink_wool'
        ]

        placed = 0
        for i, (x, y, z) in enumerate(points):
            if i % skip != 0:
                continue

            mc_x = self.center_x + int(x * scale)
            mc_y = self.center_y + int(y * scale)
            mc_z = self.center_z + int(z * scale)

            t_norm = i / steps
            color_index = int(t_norm * len(color_map))
            color_index = max(0, min(color_index, len(color_map)-1))
            block = color_map[color_index]

            self.execute(f"setblock {mc_x} {mc_y} {mc_z} {block}")
            placed += 1
            if placed % 500 == 0:
                time.sleep(0.05)

        print(f"Placed {placed} blocks. Done!")

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 25575
    PASSWORD = "MySecret123"   # CHANGE THIS

    lorenz = LorenzAttractor(HOST, PORT, PASSWORD)
    lorenz.draw_attractor(
        initial=(0.1, 0.1, 0.1),
        steps=60000,
        dt=0.005,
        scale=3.5,
        skip=2
    )
    lorenz.close()
    print("Lorenz attractor complete. Fly around y=70 to see the butterfly.")
