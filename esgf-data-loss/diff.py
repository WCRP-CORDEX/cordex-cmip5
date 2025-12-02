import argparse

def get_datasets(filepath):
    datasets = set()
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # ignore empty lines
                dataset = line.split(maxsplit=1)[0]
                datasets.add(dataset)
    return datasets

def main():
    parser = argparse.ArgumentParser(description='Compute set difference of first datasets from two files.')
    parser.add_argument('file1', help='First input file')
    parser.add_argument('file2', help='Second input file')
    args = parser.parse_args()

    datasets1 = get_datasets(args.file1)
    datasets2 = get_datasets(args.file2)

    difference = datasets1 - datasets2

    for dataset in sorted(difference):
        print(dataset)

if __name__ == '__main__':
    main()

