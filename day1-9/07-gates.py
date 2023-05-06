#!/usr/bin/python3


from collections import defaultdict
import curses
import re




INPUTFILE="07-input.txt"
COLWIDTH=20  
DELAY=300 # 300ms delay to see how signals are calculated
#DELAY=0 # or no delay to get the answer sooner




def display_wires(stdscr, wires, iteration, instructions):
    """ prints the state of all logic gates in multiple columns using curses """
    stdscr.clear()
    outx=0
    outy=0
    for wire,value in instructions.items():
        # try to get the signal value for the wire
        # if we don't have it, print instruction for the wire
        outformat=curses.A_NORMAL
        try:
            outstring = f"{wire}: {str(wires[wire])}"
            outformat=curses.color_pair(1) # higlight the wires that have the signal
        except KeyError:
            outstring = f"{wire}: {value}"


        stdscr.addstr(outy, outx, outstring, outformat)
        #stdscr.addstr(outstring, outformat)
        outx+=COLWIDTH
        if (outx>=curses.COLS-COLWIDTH):
            outx=0
            outy+=1
    # print summary below
    outstring = f"Iteration: {str(iteration)}"
    try:
        a_val=str(wires['a'])
        ending="     PRESS ANY KEY TO CONTINUE"
    except KeyError:
        a_val=instructions['a']
        ending=""
    outstring += f"  current state of a: {a_val}{ending}"
    stdscr.addstr(outy+3, 5, outstring, curses.color_pair(1) )
    stdscr.refresh()

def execute(line : str, wire_values: dict) -> bool:
    # returns true if instruction executed, false otherwise
    instr,targetwire=line.split(" -> ")
    #print(f"{targetwire}: instruction {instr}")

    splitinstr=instr.split()
    if len(splitinstr)==1: # either number or another gate
        return process_assingment(instr, wire_values, targetwire)
    elif len(splitinstr)==2: # 1-argument command, must be NOT
        return process_not(splitinstr[1], wire_values, targetwire)
    else: # 2-argument command - separate functions for readability
        if splitinstr[1]=="AND":
            return process_and(splitinstr[0], splitinstr[2], wire_values, targetwire)
        elif splitinstr[1]=="OR":
            return process_or(splitinstr[0], splitinstr[2], wire_values, targetwire)
        elif splitinstr[1]=="LSHIFT":
            return process_lshift(splitinstr[0], int(splitinstr[2]), wire_values, targetwire)
        elif splitinstr[1]=="RSHIFT":
            return process_rshift(splitinstr[0], int(splitinstr[2]), wire_values, targetwire)
        else:
            raise ValueError(f"wrong command {splitinstr[1]}")


def process_not(sourcewire: str, wire_values: dict, targetwire: str) -> bool:
    if sourcewire in wire_values:
        # The ~ operator in Python may return a signed -ve value.
        # We don't want this, so we & with a 16 bit mask of all 1s to convert to +ve representation
        wire_values[targetwire] = ~wire_values[sourcewire] & 0xFFFF
        return True
    else:
        return False


def process_assingment(instr: str, wire_values: dict, targetwire: str) -> bool:
    try: # simplest case first: 123 -> x
        val=int(instr)
        wire_values[targetwire]=val
        return True
    except ValueError: # not a number - another gate then
        if instr in wire_values:
            wire_values[targetwire]=wire_values[instr]
            return True
        else:
            return False


def process_lshift(sourcewire: str, arg2: int, wire_values: dict, targetwire: str) -> bool:
    if sourcewire not in wire_values:
        return False
    wire_values[targetwire] = wire_values[sourcewire] << arg2
    return True

def process_rshift(sourcewire: str, arg2: int, wire_values: dict, targetwire: str) -> bool:
    if sourcewire not in wire_values:
        return False
    wire_values[targetwire] = wire_values[sourcewire] >> arg2
    return True


def process_and(arg1: str, arg2: str, wire_values: dict, targetwire: str) -> bool:
    if arg2 not in wire_values:
        return False
    try: # special case - 1st argument is a value not wire
        value=int(arg1)
        wire_values[targetwire] = value & wire_values[arg2]
        return True
    except ValueError:
        # normal case - it's a wire
        if arg1 not in wire_values:
            return False
        wire_values[targetwire] = wire_values[arg1] & wire_values[arg2]
        return True

def process_or(arg1: str, arg2: str, wire_values: dict, targetwire: str) -> bool:
    if arg2 not in wire_values:
        return False
    try: # special case - 1st argument is a value not wire
        value=int(arg1)
        wire_values[targetwire] = value | wire_values[arg2]
        return True
    except ValueError:
        # normal case - it's a wire
        if arg1 not in wire_values:
            return False
        wire_values[targetwire] = wire_values[arg1] | wire_values[arg2]
        return True



def process_instructions(data, stdscr, wireinstr):
    wire_values = {}
    iteration=0
    while data:
        iteration+=1
        for line in data[:]:
            if execute(line, wire_values):
                # if the instruction worked, remove it from the queue
                #print(f"removing: {line}")
                data.remove(line)
        #print(f"Iteration {iteration} instructions left {len(instructions)}")
        display_wires(stdscr, wire_values, iteration, wireinstr)
        curses.napms(DELAY) # delay so we can see how the values are changing
        #break # for now 1 iteration only
    return wire_values


def main(stdscr):
    # read input file
    with open(INPUTFILE) as inputfile:
        data=inputfile.read().splitlines()

    # dictionary of instructions, only needed for visualization
    wireinstr=defaultdict(str)
    for line in data:
        instr,wire=line.split(" -> ")
        instr=instr.strip()
        wire=wire.strip()
        wireinstr[wire]=instr

    # some more initialization
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    


    # part 1
    results = process_instructions(data.copy(), stdscr, wireinstr)  # main loop goes here
    part1result=results['a']
    stdscr.getch()
    
    # part 2
    wire_b_instr = list(filter(re.compile(r"-> b$").search, data)) # return only rows that match
    wire_b_instr_index = data.index(wire_b_instr[0])  # the position of this instruction in the list
    data[wire_b_instr_index] = f"{part1result} -> b"  # replace the instruction with this new one
    results = process_instructions(data.copy(), stdscr, wireinstr)  # main loop goes here
    part2result=results['a']
    stdscr.getch()

    return part1result,part2result


# wrapper to simplify init/cleanup of curses
part1result,part2result=curses.wrapper(main)

# print results again to the normal output
print("Part 1: Value of input a is ", part1result)
print("Part 2: Value of input a is ", part2result)
