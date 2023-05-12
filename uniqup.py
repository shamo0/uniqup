import sys
import argparse
from urllib.parse import urlparse, urlencode, parse_qs

def modify_urls(input_file, output_file):
    # Initialize list to hold modified URLs
    modified_urls = []

    # Read in URLs from input file
    with open(input_file, 'r') as f:
        urls = f.read().splitlines()

    # Iterate through each URL and modify its parameters
    for url in urls:
        url_parts = urlparse(url)
        query_dict = parse_qs(url_parts.query)
        param_list = []

        # Create list of new parameter values
        for i, key in enumerate(query_dict.keys()):
            param_list.append('param{}'.format(i+1))
            query_dict[key] = 'param{}'.format(i+1)

        # Rebuild modified URL with new parameter values
        new_query = urlencode(query_dict)
        modified_url = '{}?{}'.format(url_parts.geturl().split('?')[0], new_query)
        modified_urls.append(modified_url)

    # Sort and write unique modified URLs to output file
    with open(output_file, 'w') as f:
        for url in sorted(set(modified_urls)):
            f.write('{}\n'.format(url))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Modify URLs in a file')
    parser.add_argument('-i', '--input', metavar='input_file', type=str, help='Input file name', required=True)
    parser.add_argument('-o', '--output', metavar='output_file', type=str, help='Output file name', required=True)
    args = parser.parse_args()

    modify_urls(args.input, args.output)

