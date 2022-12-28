#!/usr/bin/python3


import logging
from collections import defaultdict
import curses
from parsimonious import Grammar, NodeVisitor, ParseError, VisitationError
import re

# input parsing by Dazbo at https://aoc.just2good.co.uk/2015/7


logging.basicConfig(
        filename='07.log', 
        level=logging.DEBUG, 
        format='%(asctime)s:%(levelname)s:\t%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



INPUTFILE="07-input.txt"
COLWIDTH=20  
DELAY=300 # 300ms delay to see how signals are calculated
#DELAY=0 # or no delay to get the answer sooner

grammar = Grammar(r"""
    expr = input? (op input)? feeds wire
    input = (number / wire) ws+
    op = ("AND" / "OR" / "LSHIFT" / "RSHIFT" / "NOT") ws+
    number = ~r"\d+"
    feeds = "-> "
    wire = ~r"[a-z]{1,2}"
    ws = ~r"\s"
""")


class BitwiseLogicVisitor(NodeVisitor):
    def parse(self, string_to_parse, wiredict):
        logger.debug("Parsing %s", string_to_parse)   

        self._wires_dict = wiredict
        self._inputs = []             # store int input values, left of the '->'. E.g. [7102, 65023]
        self._op = ""                 # E.g. AND
        self._target_wire = ""        # E.g. n
        self._processing_input = True # Set to False after we process the '->'
        self._output = {}             # Initialise empty wire:value dict
        super().parse(string_to_parse)  
        if "AND" in self._op:
            res = self._inputs[0] & self._inputs[1]
        elif "OR" in self._op:
            res = self._inputs[0] | self._inputs[1]
        elif "LSHIFT" in self._op:
            res = self._inputs[0] << self._inputs[1]
        elif "RSHIFT" in self._op:
            res = self._inputs[0] >> self._inputs[1]
        elif "NOT" in self._op:
            # The ~ operator in Python may return a signed -ve value.
            # We don't want this, so we & with a 16 bit mask of all 1s to convert to +ve representation
            res = ~self._inputs[0] & 0xFFFF
        else:
            # Where there is no op. E.g. '19138 -> b'
            res = sum(self._inputs)
        self._output[self._target_wire] = res
        logger.debug("Inputs were: %s, op was: %s, result: %s", self._inputs, self._op, self._output)   
        return self._output

    def visit_expr(self, node, visited_children):
        pass

    def visit_feeds(self, node, visited_children):
        self._processing_input = False

    def visit_op(self, node, visited_children):
        self._op = node.text.strip()       
        return self._op

    def visit_number(self, node, visited_children):
        number = int(node.text)
        self._inputs.append(number)
        return number

    def visit_wire(self, node, visited_children):
        wire = node.text.strip()
        if (self._processing_input):
            # if we have an input wire, then try to extract its numeric value
            self._inputs.append(self._wires_dict[wire])
        else:  # otherwise, this is an output wire
            self._target_wire = wire

    def generic_visit(self, node, visited_children):
        return visited_children or node




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
            outstring=wire+": "+str(wires[wire])
            outformat=curses.color_pair(1) # higlight the wires that have the signal
        except KeyError:
            outstring=wire+": "+value

            
        stdscr.addstr(outy, outx, outstring, outformat)
        #stdscr.addstr(outstring, outformat)
        outx+=COLWIDTH
        if (outx>=curses.COLS-COLWIDTH):
            outx=0
            outy+=1
    # print summary below
    outstring="Iteration: "+str(iteration)
    try:
        a_val=str(wires['a'])
        ending="     PRESS ANY KEY TO CONTINUE"
    except KeyError:
        a_val=instructions['a']
        ending=""
    outstring+="  current state of a: "+a_val+ending
    stdscr.addstr(outy+3, 5, outstring, curses.color_pair(1) )
    stdscr.refresh()


def process_instructions(instructions, blc_visitor, stdscr, wireinstr):
    wire_values = {}
    iteration=0
    while instructions:
        logger.debug(wire_values)
        iteration+=1
        for i, line in enumerate(instructions):
            try:
                wire_values.update(blc_visitor.parse(line, wire_values))
                # if we're here, the instruction parsed successfully, so remove it from the stack permanently
                popped = instructions.pop(i)
                logger.debug("Processed: %s", popped)

            except ParseError as e:
                logger.debug(e)
                continue
            except VisitationError as e:
                logger.debug(e)
                continue

        # We're ready to process the list again. 
        display_wires(stdscr, wire_values, iteration, wireinstr)
        curses.napms(DELAY) # delay so we can see how the values are changing
        #break # for now 1 iteration only
    return wire_values


def main(stdscr):
    # read input file
    with open(INPUTFILE) as inputfile:
        data=inputfile.read().splitlines()

    # dictionary of instructions, only needed for visualization
    wireinstr=defaultdict()
    for line in data:
        instr,wire=line.split(" -> ")
        instr=instr.strip()
        wire=wire.strip()
        wireinstr[wire]=instr

    # some more initialization
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    blc_visitor = BitwiseLogicVisitor()
    blc_visitor.grammar = grammar


    # part 1
    results = process_instructions(data.copy(), blc_visitor, stdscr, wireinstr)  # main loop goes here
    part1result=results['a']
    stdscr.getch()
    
    # part 2
    wire_b_instr = list(filter(re.compile(r"-> b$").search, data)) # return only rows that match
    wire_b_instr_index = data.index(wire_b_instr[0])  # the position of this instruction in the list
    data[wire_b_instr_index] = f"{part1result} -> b"  # replace the instruction with this new one
    results = process_instructions(data.copy(), blc_visitor, stdscr, wireinstr)  # main loop goes here
    part2result=results['a']
    stdscr.getch()

    return part1result,part2result


# wrapper to simplify init/cleanup of curses
part1result,part2result=curses.wrapper(main)

# print results again to the normal output
print("Part 1: Value of input a is ", part1result)
print("Part 2: Value of input a is ", part2result)
