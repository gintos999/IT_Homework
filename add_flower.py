import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type = str, required = True)
    parser.add_argument('--country', type = str, required = True)
    parser.add_argument('--petal-colour', type = str, required = True)
    parser.add_argument('--steam-length', type = int, required = True)
    parser.add_argument ('--with-thorns', action = 'store_true', required = False)
    parser.add_argument('--companion-plants', nargs='+', type = str, required = False)

    args = parser.parse_args()

    # params = ["name", "country", "petal-colour", "stem-length"]
    
    info = {
        "name" : args.name,
        "country" : args.country,
        "petal-colour" : args.petal_colour,
        "steam-length" : args.steam_length,
        "with-thorns" : "False"
    }
    
    if args.with_thorns:
        info["with-thorns"] = str(args.with_thorns)

    if args.companion_plants:
        info["companion-plants"] = args.companion_plants

with open("journal.txt", 'a') as file:
    file.write(json.dumps(info) + '\n')