import numpy as np

#colours:
    #0 -> white
    #1 -> yellow
    #2 -> green
    #3 -> blue
    #4 -> orange
    #5 -> red

class Cube:
    def __init__(self):
        self.state = np.array([
            [0,0,0,0],  #bottom
            [1,1,1,1],  #top
            [2,2,2,2],  #front
            [3,3,3,3],  #back
            [4,4,4,4],  #right
            [5,5,5,5]   #left
        ])
        #[bottom_left, bottom_right, top_right, top_left]
    
    def print_cube(self):
        print("Bottom:", self.state[0])
        print("Top:", self.state[1])
        print("Front:", self.state[2])
        print("Back:", self.state[3])
        print("Right:", self.state[4])
        print("Left", self.state[5])
        print("\n\n")
    
    def display_flat(self):
        color_map = {0: 'W', 1: 'Y', 2: 'G', 3: 'B', 4: 'O', 5: 'R'}
        
        top = self.state[1]
        bottom = self.state[0]
        front = self.state[2]
        back = self.state[3]
        right = self.state[4]
        left = self.state[5]
        
        # Display in cross pattern
        print("        ", color_map[top[3]], color_map[top[2]])
        print("        ", color_map[top[0]], color_map[top[1]])
        print()
        print(color_map[left[3]], color_map[left[2]], " ", 
              color_map[front[3]], color_map[front[2]], " ",
              color_map[right[3]], color_map[right[2]], " ",
              color_map[back[3]], color_map[back[2]])
        print(color_map[left[0]], color_map[left[1]], " ", 
              color_map[front[0]], color_map[front[1]], " ",
              color_map[right[0]], color_map[right[1]], " ",
              color_map[back[0]], color_map[back[1]])
        print()
        print("        ", color_map[bottom[3]], color_map[bottom[2]])
        print("        ", color_map[bottom[0]], color_map[bottom[1]])
        print("\n")
    
    def U(self):
        #top face rotate clockwise
        temp = self.state[1][0]
        for i in range(3):
            self.state[1][i] = self.state[1][i+1]
        self.state[1][3] = temp

        temp2 = self.state[2][2]
        temp3 = self.state[2][3]

        #front
        self.state[2][2] = self.state[4][2]
        self.state[2][3] = self.state[4][3]

        #right
        self.state[4][2] = self.state[3][2]
        self.state[4][3] = self.state[3][3]

        #back
        self.state[3][2] = self.state[5][2]
        self.state[3][3] = self.state[5][3]

        #left
        self.state[5][2] = temp2
        self.state[5][3] = temp3

    def U_prime(self):
        for i in range(3):
            self.U()

    def U2(self):
        for i in range(2):
            self.U()

    def D(self):
        #bottom face rotate clockwise
        temp = self.state[0][0]
        for i in range(3):
            self.state[0][i] = self.state[0][i+1]
        self.state[0][3] = temp

        temp2 = self.state[2][0]
        temp3 = self.state[2][1]

        #front
        self.state[2][0] = self.state[4][0]
        self.state[2][1] = self.state[4][1]

        #right
        self.state[4][0] = self.state[3][0]
        self.state[4][1] = self.state[3][1]

        #back
        self.state[3][0] = self.state[5][0]
        self.state[3][1] = self.state[5][1]

        #left
        self.state[5][0] = temp2
        self.state[5][1] = temp3

    def D_prime(self):
        for i in range(3):
            self.D()

    def D2(self):
        for i in range(2):
            self.D()
    
    def F(self):
        #front face rotate clockwise
        temp = self.state[2][0]
        for i in range(3):
            self.state[2][i] = self.state[2][i+1]
        self.state[2][3] = temp

        temp2 = self.state[1][0]
        temp3 = self.state[1][1]

        #top
        self.state[1][0] = self.state[5][1]
        self.state[1][1] = self.state[5][2]

        #left
        self.state[5][1] = self.state[0][2]
        self.state[5][2] = self.state[0][3]

        #bottom
        self.state[0][2] = self.state[4][3]
        self.state[0][3] = self.state[4][0]

        #left
        self.state[4][3] = temp2
        self.state[4][0] = temp3
    
    def F_prime(self):
        for i in range(3):
            self.F()
    
    def F2(self):
        for i in range(2):
            self.F()

    def B(self):
        #back face rotate clockwise
        temp = self.state[3][0]
        for i in range(3):
            self.state[3][i] = self.state[3][i+1]
        self.state[3][3] = temp

        temp2 = self.state[1][2]
        temp3 = self.state[1][3]

        #top
        self.state[1][2] = self.state[4][1]
        self.state[1][3] = self.state[4][2]

        #right
        self.state[4][1] = self.state[0][0]
        self.state[4][2] = self.state[0][1]

        #bottom
        self.state[0][0] = self.state[5][3]
        self.state[0][1] = self.state[5][0]

        #left
        self.state[5][3] = temp2
        self.state[5][0] = temp3

    def B_prime(self):
        for i in range(3):
            self.B()
    
    def B2(self):
        for i in range(2):
            self.B()

    def R(self):
        #right face rotate clockwise
        temp = self.state[4][0]
        for i in range(3):
            self.state[4][i] = self.state[4][i+1]
        self.state[4][3] = temp

        temp2 = self.state[1][1]
        temp3 = self.state[1][2]

        #top
        self.state[1][1] = self.state[2][1]
        self.state[1][2] = self.state[2][2]

        #front
        self.state[2][1] = self.state[0][1]
        self.state[2][2] = self.state[0][2]

        #bottom
        self.state[0][1] = self.state[3][3]
        self.state[0][2] = self.state[3][0]

        #left
        self.state[3][3] = temp2
        self.state[3][0] = temp3
    
    def R_prime(self):
        for i in range(3):
            self.R()
    
    def R2(self):
        for i in range(2):
            self.R()
    
    def L(self):
        #left face rotate clockwise
        temp = self.state[5][0]
        for i in range(3):
            self.state[5][i] = self.state[5][i+1]
        self.state[5][3] = temp

        temp2 = self.state[1][3]
        temp3 = self.state[1][0]

        #top
        self.state[1][3] = self.state[3][1]
        self.state[1][0] = self.state[3][2]

        #back
        self.state[3][1] = self.state[0][3]
        self.state[3][2] = self.state[0][0]

        #bottom
        self.state[0][3] = self.state[2][3]
        self.state[0][0] = self.state[2][0]

        #front
        self.state[2][3] = temp2
        self.state[2][0] = temp3

    def L_prime(self):
        for i in range(3):
            self.L()

    def L2(self):
        for i in range(2):
            self.L()
        
#main program
cube = Cube()
cube.display_flat()

while(True):
    move = input("Input your next move: ")
    
    if move == "X":
        break

    match move:
        case "U":
            cube.U()
        case "U\'":
            cube.U_prime()
        case "U2":
            cube.U2()
        case "D":
            cube.D()
        case "D\'":
            cube.D_prime()
        case "D2":
            cube.D2()
        case "F":
            cube.F()
        case "F\'":
            cube.F_prime()
        case "F2":
            cube.F2()
        case "B":
            cube.B()
        case "B\'":
            cube.B_prime()
        case "B2":
            cube.B2()
        case "R":
            cube.R()
        case "R\'":
            cube.R_prime()
        case "R2":
            cube.R2()
        case "L":
            cube.L()
        case "L\'":
            cube.L_prime()
        case "L2":
            cube.L2()
        case _:
            print("Invalid Move.")
    
    cube.display_flat()