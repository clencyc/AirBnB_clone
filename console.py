#!/usr/bin/python3

import cmd
# print(dir(cmd.Cmd))
class Mycommand(cmd.Cmd):#this is inheritance
    
    prompt = "(airbnb$$) >"

    def do_quit(self, arg):
        """This quits or exits the program"""
        return True
    
    # aliasing
    do_exit = do_quit
    
Mycommand().cmdloop()