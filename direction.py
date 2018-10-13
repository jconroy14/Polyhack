from enum import Enum
class direction(Enum):
    North = 1;
    South = -1;
    East = 2;
    West = -2;
    Northeast = 3;
    Northwest = 4;
    Southeast = -4;
    Southwest = -3;
    Up = 9;

dir_input_mappings = [
    {("north","n"):direction.North},\
    {("south","s"):direction.South},\
    {("west","w"):direction.West},\
    {("east","e"):direction.East},\
    {("northwest","nw"):direction.Northwest},\
    {("northeast","ne"):direction.Northeast},\
    {("southwest","sw"):direction.Southwest},\
    {("southeast","se"):direction.Southeast},\
    {("up","u"):direction.Up}\
]
