import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-p','--param1',help='x variable', required=True)
parser.add_argument('-q','--param2',help='y variable', required=True)
parser.add_argument('-r','--param3',help='z variable', required=True)

args=parser.parse_args('-p one -q two -r three'.split())
print(args)
args_dict = vars(args)    
print(args_dict)
