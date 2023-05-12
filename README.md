# Uniqup

A Python script that takes in a file of URLs, modifies their parameters, and writes unique modified URLs to an output file.

## Description

Uniqup is a Python script that reads in a file of URLs, modifies their parameters, and writes unique modified URLs to an output file. This script can be used with tools like `gau` and `gauplus` to ensure that only unique URLs are kept. The modified URLs are created by replacing the values of each query parameter with a new value in the format `paramN`, where `N` is an integer starting from 1. The modified URLs are then sorted and duplicates are removed to produce the final output file.
<br><br>
![screen1](https://github.com/shamo0/uniqup/assets/48299520/745cb160-927c-40dd-b0bb-fe4fa5f74657)
<br><br>
If you get URLs such as these from wayback or gau, you can run this python script on the url file to get rid of the repeated parameters with different values.
<br><br>
![screen2](https://github.com/shamo0/uniqup/assets/48299520/74ec8424-f840-422a-96d1-eb0ac20ed0df)
<br><br>
You will be left with these types of URLS with unique parameters eventually saving you time on testing your injection payloads :)

## Usage

### Installation

1. Clone the repository:
 
```git clone https://github.com/shamo0/uniqup.git```


### Usage Instructions

To run the script, use the following command:
```python3 uniqup.py -i <input_file> -o <output_file>```




