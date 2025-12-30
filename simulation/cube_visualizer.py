from vpython import *
from cube2 import Cube

# Color mapping
COLOR_MAP = {
    0: vector(1, 1, 1),      # White
    1: vector(1, 1, 0),      # Yellow
    2: vector(0, 1, 0),      # Green
    3: vector(0, 0, 1),      # Blue
    4: vector(1, 0.5, 0),    # Orange
    5: vector(1, 0, 0)       # Red
}

class CubeVisualizer:
    def __init__(self, cube):
        self.cube = cube
        self.cubelets = []
        self.face_stickers = []
        
        scene.title = "2x2 Rubik's Cube Visualizer\n"
        scene.width = 1000
        scene.height = 800
        scene.background = color.gray(0.2)
        scene.range = 3
        scene.camera.pos = vector(3, 3, 3)
        scene.camera.axis = vector(-3, -3, -3)
        
        # Create the cube
        self.create_cube()
        
        scene.append_to_caption("\n\nRotate view: Right-click drag")
        scene.append_to_caption("\nZoom: Scroll wheel")
        scene.append_to_caption("\n\nEnter moves in the console (U, U', U2, D, D', D2, F, F', F2, B, B', B2, R, R', R2, L, L', L2)")
        scene.append_to_caption("\nType 'X' to exit")
        
    def create_cube(self):

        for cubelet in self.cubelets:
            for sticker in cubelet['stickers']:
                sticker['sticker'].visible = False
            cubelet['core'].visible = False
        
        self.cubelets = []
        self.face_stickers = []
        
        # Define positions for 8 cubelets of 2x2 cube
        positions = []
        for x in [-0.5, 0.5]:
            for y in [-0.5, 0.5]:
                for z in [-0.5, 0.5]:
                    positions.append(vector(x, y, z))
        
        # Create each cubelet
        gap = 0.05
        size = 1.0 - gap
        
        for pos in positions:
            # Black core cube
            core = box(pos=pos, size=vector(size, size, size), 
                      color=color.black, opacity=1)
            
            # Create stickers on visible faces
            stickers = []
            sticker_thickness = 0.02
            sticker_size = size * 0.95
            
            # Determine which faces are visible and add colored stickers
            # Right face (x = 0.5)
            if pos.x > 0:
                right_sticker = box(pos=pos + vector(size/2 + sticker_thickness/2, 0, 0),
                                   size=vector(sticker_thickness, sticker_size, sticker_size),
                                   color=color.white)
                stickers.append({'sticker': right_sticker, 'face': 'right', 'pos': pos})
            
            # Left face (x = -0.5)
            if pos.x < 0:
                left_sticker = box(pos=pos + vector(-size/2 - sticker_thickness/2, 0, 0),
                                  size=vector(sticker_thickness, sticker_size, sticker_size),
                                  color=color.white)
                stickers.append({'sticker': left_sticker, 'face': 'left', 'pos': pos})
            
            # Top face (y = 0.5)
            if pos.y > 0:
                top_sticker = box(pos=pos + vector(0, size/2 + sticker_thickness/2, 0),
                                 size=vector(sticker_size, sticker_thickness, sticker_size),
                                 color=color.white)
                stickers.append({'sticker': top_sticker, 'face': 'top', 'pos': pos})
            
            # Bottom face (y = -0.5)
            if pos.y < 0:
                bottom_sticker = box(pos=pos + vector(0, -size/2 - sticker_thickness/2, 0),
                                    size=vector(sticker_size, sticker_thickness, sticker_size),
                                    color=color.white)
                stickers.append({'sticker': bottom_sticker, 'face': 'bottom', 'pos': pos})
            
            # Front face (z = 0.5)
            if pos.z > 0:
                front_sticker = box(pos=pos + vector(0, 0, size/2 + sticker_thickness/2),
                                   size=vector(sticker_size, sticker_size, sticker_thickness),
                                   color=color.white)
                stickers.append({'sticker': front_sticker, 'face': 'front', 'pos': pos})
            
            # Back face (z = -0.5)
            if pos.z < 0:
                back_sticker = box(pos=pos + vector(0, 0, -size/2 - sticker_thickness/2),
                                  size=vector(sticker_size, sticker_size, sticker_thickness),
                                  color=color.white)
                stickers.append({'sticker': back_sticker, 'face': 'back', 'pos': pos})
            
            self.cubelets.append({
                'pos': pos,
                'core': core,
                'stickers': stickers
            })
            
            self.face_stickers.extend(stickers)
        
        # Update colors based on cube state
        self.update_colors()
    
    def update_colors(self):
        # State format: [bottom, top, front, back, right, left]
        # Each face: [bottom_left, bottom_right, top_right, top_left]
        
        state = self.cube.state
        
        for sticker_info in self.face_stickers:
            sticker = sticker_info['sticker']
            face = sticker_info['face']
            pos = sticker_info['pos']
            
            # Determine which position on the face this sticker represents
            color_idx = None
            
            if face == 'bottom':  # y = -0.5
                face_state = state[0]
                if pos.z < 0 and pos.x < 0:  # back-left
                    color_idx = face_state[0]
                elif pos.z < 0 and pos.x > 0:  # back-right
                    color_idx = face_state[1]
                elif pos.z > 0 and pos.x > 0:  # front-right
                    color_idx = face_state[2]
                elif pos.z > 0 and pos.x < 0:  # front-left
                    color_idx = face_state[3]
            
            elif face == 'top':  # y = 0.5
                face_state = state[1]
                if pos.z > 0 and pos.x < 0:  # front-left
                    color_idx = face_state[0]
                elif pos.z > 0 and pos.x > 0:  # front-right
                    color_idx = face_state[1]
                elif pos.z < 0 and pos.x > 0:  # back-right
                    color_idx = face_state[2]
                elif pos.z < 0 and pos.x < 0:  # back-left
                    color_idx = face_state[3]
            
            elif face == 'front':  # z = 0.5
                face_state = state[2]
                if pos.y < 0 and pos.x < 0:  # bottom-left
                    color_idx = face_state[0]
                elif pos.y < 0 and pos.x > 0:  # bottom-right
                    color_idx = face_state[1]
                elif pos.y > 0 and pos.x > 0:  # top-right
                    color_idx = face_state[2]
                elif pos.y > 0 and pos.x < 0:  # top-left
                    color_idx = face_state[3]
            
            elif face == 'back':  # z = -0.5
                face_state = state[3]
                if pos.y < 0 and pos.x > 0:  # bottom-right (from back view)
                    color_idx = face_state[0]
                elif pos.y < 0 and pos.x < 0:  # bottom-left (from back view)
                    color_idx = face_state[1]
                elif pos.y > 0 and pos.x < 0:  # top-left (from back view)
                    color_idx = face_state[2]
                elif pos.y > 0 and pos.x > 0:  # top-right (from back view)
                    color_idx = face_state[3]
            
            elif face == 'right':  # x = 0.5
                face_state = state[4]
                if pos.y < 0 and pos.z > 0:  # bottom-front
                    color_idx = face_state[0]
                elif pos.y < 0 and pos.z < 0:  # bottom-back
                    color_idx = face_state[1]
                elif pos.y > 0 and pos.z < 0:  # top-back
                    color_idx = face_state[2]
                elif pos.y > 0 and pos.z > 0:  # top-front
                    color_idx = face_state[3]
            
            elif face == 'left':  # x = -0.5
                face_state = state[5]
                if pos.y < 0 and pos.z < 0:  # bottom-back
                    color_idx = face_state[0]
                elif pos.y < 0 and pos.z > 0:  # bottom-front
                    color_idx = face_state[1]
                elif pos.y > 0 and pos.z > 0:  # top-front
                    color_idx = face_state[2]
                elif pos.y > 0 and pos.z < 0:  # top-back
                    color_idx = face_state[3]
            
            if color_idx is not None:
                sticker.color = COLOR_MAP[color_idx]
    
    def apply_move(self, move):
        """Apply a move to the cube and update visualization"""
        move_map = {
            "U": self.cube.U,
            "U'": self.cube.U_prime,
            "U2": self.cube.U2,
            "D": self.cube.D,
            "D'": self.cube.D_prime,
            "D2": self.cube.D2,
            "F": self.cube.F,
            "F'": self.cube.F_prime,
            "F2": self.cube.F2,
            "B": self.cube.B,
            "B'": self.cube.B_prime,
            "B2": self.cube.B2,
            "R": self.cube.R,
            "R'": self.cube.R_prime,
            "R2": self.cube.R2,
            "L": self.cube.L,
            "L'": self.cube.L_prime,
            "L2": self.cube.L2
        }
        
        if move in move_map:
            move_map[move]()
            self.update_colors()
            return True
        return False

# Main program
def main():
    cube = Cube()
    visualizer = CubeVisualizer(cube)
    
    print("\n=== 2x2 Rubik's Cube 3D Visualizer ===")
    print("Rotate the view with right-click drag")
    print("Zoom with scroll wheel\n")
    print("Available moves:")
    print("U, U', U2 - Top layer")
    print("D, D', D2 - Bottom layer")
    print("F, F', F2 - Front face")
    print("B, B', B2 - Back face")
    print("R, R', R2 - Right face")
    print("L, L', L2 - Left face")
    print("\nType 'X' to exit\n")
    
    # Also show the flat display
    #cube.display_flat()
    
    while True:
        move = input("Enter move: ")
        
        if move == "X":
            print("Exiting...")
            break
        
        if visualizer.apply_move(move):
            print(f"Applied {move}")
            #cube.display_flat()
        else:
            print("Invalid move. Try U, D, F, B, R, L (with ' or 2)")

if __name__ == "__main__":
    main()
