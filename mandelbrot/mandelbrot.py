import socket
import struct
import math
import time

class MinecraftRCON:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect(('localhost', 25575))
        packet = struct.pack('<ii', 1, 3) + b'python\x00\x00'
        self.sock.send(struct.pack('<i', len(packet)) + packet)
        self.sock.recv(4096)

    def command(self, cmd):
        packet = struct.pack('<ii', 1, 2) + cmd.encode() + b'\x00\x00'
        self.sock.send(struct.pack('<i', len(packet)) + packet)
        return self.sock.recv(4096)

def mandelbrot(c, max_iter):
    """Calculate if point escapes the Mandelbrot set"""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n  # Escaped after n iterations
        z = z*z + c
    return max_iter  # Never escaped

def get_block_color(iter_count, max_iter):
    """Choose block color based on escape speed"""
    if iter_count == max_iter:
        return "black_wool"  # Never escaped

    colors = [
        "white_wool", "orange_wool", "magenta_wool", "light_blue_wool",
        "yellow_wool", "lime_wool", "pink_wool", "gray_wool",
        "light_gray_wool", "cyan_wool", "purple_wool", "blue_wool",
        "brown_wool", "green_wool", "red_wool"
    ]  # no black here: black_wool is reserved for points inside the set
    return colors[iter_count % len(colors)]

mc = MinecraftRCON()

print(" MANDELBROT FRACTAL GENERATOR")
print("======================================")
print()

center_x, center_y, center_z = 0, 70, 0
print(f"Drawing at: X={center_x}, Y={center_y}, Z={center_z}")
print("Patterns are NOT removed; later patterns draw over earlier ones")
print()

patterns = [
    # (width, height, max_iter, scale, center_re, center_im, block_type, description)
    # center_re/center_im is the point of the complex plane drawn at the middle of the
    # picture. The set spans about -2 to 0.47 on the real axis, so -0.75 centers it.
    (200, 200, 30, 0.015, -0.75, 0.0, "wool", "GIANT Mandelbrot - Full View"),
    (300, 300, 40, 0.010, -0.75, 0.0, "wool", "MASSIVE View - Huge Area"),
    (400, 400, 50, 0.007, -0.75, 0.0, "wool", "COLOSSAL - Epic Scale"),
    (150, 150, 150, 0.001, -0.7436, 0.1318, "wool", "Detailed Zoom - Seahorse Valley"),
]

for pattern_idx, (width, height, max_iter, scale, center_re, center_im, block_type, description) in enumerate(patterns):
    print()
    print(f" PATTERN {pattern_idx + 1}: {description}")
    print(f" Size: {width}x{height} ({width*height} total blocks)")
    print(f" Iterations: {max_iter}, Scale: {scale}, Center: {center_re} + {center_im}i")
    print(f" Minecraft Area: {width} x {height} blocks")
    print(f" Block: {block_type}")

    # Mark center
    mc.command(f"setblock {center_x} {center_y} {center_z} diamond_block")
    mc.command(f"say Drawing: {description}")

    print(f" Generating {width}x{height} Mandelbrot...")
    print(" This may take several minutes for the largest patterns...")

    start_x = center_x - width // 2
    start_z = center_z - height // 2

    blocks_placed = 0
    start_time = time.time()

    # Generate Mandelbrot pattern
    for x in range(width):
        for z in range(height):
            # Convert to complex coordinates
            real = (x - width/2) * scale + center_re
            imag = (z - height/2) * scale + center_im
            c = complex(real, imag)

            # Calculate Mandelbrot
            iter_count = mandelbrot(c, max_iter)

            # Get block color
            if block_type == "wool":
                full_block_type = get_block_color(iter_count, max_iter)
            else:
                full_block_type = block_type

            # World coordinates - Y is fixed at 70
            world_x = start_x + x
            world_z = start_z + z

            mc.command(f"setblock {world_x} {center_y} {world_z} {full_block_type}")
            blocks_placed += 1

            # Progress updates
            if blocks_placed % 250 == 0:
                elapsed = time.time() - start_time
                percent = (blocks_placed / (width * height)) * 100
                print(f" Progress: {blocks_placed}/{width*height} ({percent:.1f}%) - {elapsed:.1f}s")
                time.sleep(0.05)

    total_time = time.time() - start_time
    print(f" Pattern {pattern_idx + 1} complete!")
    print(f" Time: {total_time:.1f}s, Blocks: {blocks_placed}")
    print(f" Area covered: {width} x {height} blocks")

    if pattern_idx < len(patterns) - 1:
        print()
        print(f" Next pattern will be {patterns[pattern_idx + 1][0]}x{patterns[pattern_idx + 1][1]} blocks")
        input(" Press Enter to draw the next one...")
    else:
        mc.command("say done.")

print()
print(" PROGRAM DONE ")
print(f" Mandelbrot fractal remains at (0, {center_y}, 0)")
print(f" The last pattern spans {patterns[-1][0]} x {patterns[-1][1]} blocks")
