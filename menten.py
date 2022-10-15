import argparse
import json

def speed_calculation(S, E0, KM, k):
    v = k * S * E0 / (KM + S)
    return (v)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', type = float, required = True)
    parser.add_argument('-E0', type = float, required = True)
    parser.add_argument('-KM', type = float, required = True)
    parser.add_argument('-k', type = float, required = True)
    parser.add_argument ('--save-file', type = str, required = False)

    args = parser.parse_args()
    
    v = speed_calculation(args.S, args.E0, args.KM, args.k)

    dict = {
        "v": v,
        "S": args.S,
        "E0": args.E0,
        "KM": args.KM,
        "k": args.k
    }

if args.save_file:
    with open(args.save_file, 'w') as file:
        file.write(json.dumps(dict, indent = 4))