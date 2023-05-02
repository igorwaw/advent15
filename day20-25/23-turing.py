#!/usr/bin/python3

class Computer:
    register: dict = {}
    pointer: int
    instructions: list

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.instructions = f.read().splitlines()
        self.reset()

    def reset(self) -> None:
        self.register["a"]=0
        self.register["b"]=0
        self.pointer=0


    def __repr__(self) -> str:
        return f"Registers: {self.register} pointer {self.pointer} current instruction {self.instructions[self.pointer]}"


    def run(self, debug=False) -> None:
        while self.pointer<len(self.instructions):
            if (debug): print(self)
            cmd = self.instructions[self.pointer][:3]
            arg = self.instructions[self.pointer][4:]
            self.pointer+=1  # will have to decrease by 1 for jumps
            match cmd:
                case "hlf": 
                    self.register[arg]=self.register[arg]//2
                case "tpl": 
                    self.register[arg]*=3
                case "inc": 
                    self.register[arg]+=1
                case "jmp": 
                    self.pointer+=int(arg)-1
                case "jie": 
                    register,offset=arg.split(",")
                    self.pointer += int(offset) -1 if self.register[register]%2==0 else 0
                case "jio": 
                    register,offset=arg.split(",")
                    self.pointer += int(offset) -1 if self.register[register]==1 else 0
                case _: raise ValueError
        


computer=Computer("23-input.txt")
computer.run()
print("Part 1, register B: ",computer.register["b"])
computer.reset()
computer.register["a"]=1
computer.run()
print("Part 1, register B: ",computer.register["b"])