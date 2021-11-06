import sys
import cv2 as cv
import numpy as np
import imageio
import os
from PIL import Image

class Flipbook:
    def __init__(self,location="output.mp4",width=720, height = 720,fps=40):
        self.fps = fps #valid for mp4 only
        self.location = location
        self.image_size = (width,height)
        self.reel = []

    def __str__(self):
        return str([self.location, self.image_size])

    def resize(self,img):
        s = max(img.shape[0:2])
        f = np.zeros((s, s, 3), np.uint8) # Creating a dark square with NUMPY
        ax, ay = (s - img.shape[1]) // 2, (s - img.shape[0]) // 2 # Getting the centering position
        f[ay:img.shape[0] + ay, ax:ax + img.shape[1]] = img # Pasting the 'image' in a centering position
        f = cv.resize(f, self.image_size)
        return f

    def add_transition(self,img,smoothness):
        if(self.reel): #if images already exist in the reel, then add a transition between the new image and the last image of the reel
            img1 = self.reel[-1]
            img2 = cv.imread(img)
            for j in np.linspace(0,1,smoothness): #add smoothness number of frames in the transition
                output = cv.addWeighted(self.resize(img2),j,self.resize(img1),1-j,0)
                self.reel.append(output)
        else:
            img = cv.imread(img) #if no images exist, then just add the image
            self.reel.append(img)

    def join(self, other): #join one reel object to another
        for img in other.reel:
            self.reel.append(img)

    def release(self):
        typ = self.location[-3:]
        if(typ == "mp4"):
            out = cv.VideoWriter(self.location, cv.VideoWriter_fourcc(*'MP4V'), self.fps, self.image_size)
            for img in self.reel:
                out.write(img)
            out.release()
        elif(typ == "gif"):
            with imageio.get_writer(self.location, mode='I') as writer:
                for img in self.reel:
                    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                    writer.append_data(img)
        elif(typ == "pdf"):
            images = [Image.fromarray(cv.cvtColor(array, cv.COLOR_BGR2RGB)) for array in self.reel]
            images[0].save(self.location,"PDF",resolution=100.0,save_all=True,append_images=images[1:])
        else:
            print("Unidentified output type. Please use MP4, GIF or PDF.")

def add(tokens): #function for adding images to a reel
    smoothness = 100
    dest = ""
    typ = "constant"
    for i in range(2,len(tokens)):
        if(tokens[i] == 'smoothness'):
            smoothness = int(tokens[i+1])
        if(tokens[i] == 'to'):
            dest = tokens[i+1]
        if(tokens[i] == 'type'):
            typ = tokens[i+1]
    if(dest == ""):
        raise Exception("Enter variable name after 'to'.")
    if(tokens[0] == 'folder'):
        path = os.path.abspath(tokens[1])
        items = sorted(os.listdir(path))
        curr = 0
        for file in items:
            file_path = os.path.join(path,file)
            if(typ == "constant"):
                variables[dest].add_transition(file_path,smoothness)
            else:
                variables[dest].add_transition(file_path,curr)
            curr += smoothness//(len(items))

    elif(tokens[0] == 'file'):
        file_path = os.path.abspath(tokens[1])
        variables[dest].add_transition(file_path,smoothness)
    elif(tokens[0] == 'reel'):
        reel2 = variables[tokens[1]]
        variables[dest].join(reel2)
    else:
        raise Exception("Invalid command: ", tokens[0])

variables = {}

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        commands = f.read().split("\n")
    commands = [c for c in commands if len(c)>0 and c[0] != '#'] #use newline as a separator for commands and ignore the ones starting with #
    for command in commands:
        tokens = command.split()
        if(tokens[0] == 'set'): #used to set data members (fps, width, height)
            try:
                var = variables[tokens[1]]
                setattr(var, tokens[2],int(tokens[3]))
            except:
                raise Exception("Error at: ", command)
        elif(tokens[0] == 'add'):
            add(tokens[1:])
        elif(tokens[0] == 'release'): # used to release a reel object to hard disk
            if(tokens[2] != 'as'):
                raise Exception("Invalid command: ", command)
            var = variables[tokens[1]]
            var.location = tokens[3]
            var.release()
        elif(tokens[0] == 'new'): #used to declare a new flipbook or an integer also
            if(tokens[1] == 'flipbook'):
                variables[tokens[2]] = Flipbook()
            elif(tokens[1] == 'int'):
                variables[tokens[2]] = 0
                if(len(tokens) > 3):
                    variables[tokens[2]] += int(tokens[3])
            else:
                raise Exception("Invalid datatype: ",tokens[1])
        elif(tokens[0] == 'print'): #printing integer or details of the flipbook
            for i in range(1,len(tokens)):
                try:
                    print(variables[tokens[i]])
                except:
                    raise Exception("Undefined variable: ", tokens[i])
        else:
            raise Exception("Invalid command: ", command)
        

        
