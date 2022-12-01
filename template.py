import argparse
import unittest

class Test(unittest.TestCase):
    
    def test_puzzle1:
        pass
    def test_puzzle2:
        pass

def parse_input(path):
    return "Not Yet Implemented"
    
def puzzle1(path):
    return "Not yet Implemented"

def puzzle2(path):
    return "Not Yet Implemented"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="mode")
    
    run = subparser.add_parser('run')
    run.add_argument("--input",required=True,type=str)
    run.add_argument("--puzzle",required=True,type=int)
    
    
    args = parser.parse_args()
    if args.mode =='run':
        if args.puzzle == 1:
            print (puzzle1(args.input))
            
        elif args.puzzle==2:
            print (puzzle2(args.input))
    else:
        unittest.main()

    
