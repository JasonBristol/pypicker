pypicker
========

A command line random picker for python.

```
usage: pypicker.py [-h] [-i PATH] [-g INTEGER] [-o PATH] [-j DELIMITER] [-v]
                   [-u] [--version]
                   [SAMPLE SIZE] [SAMPLE GROUP [SAMPLE GROUP ...]]
                   
Randomly pick items from a list
 
positional arguments:
  SAMPLE SIZE    number of items to pick (default: 1)
  SAMPLE GROUP   list of items to choose from.
  
optional arguments:
  -h, --help     show this help message and exit
  -i PATH        input file of items to choose from
  -g INTEGER     number of result groups to generate (default: 1)
  -o PATH        output file to write results to
  -j DELIMITER   join results using specified delimiter
  -v, --verbose  verbose output
  -u, --unique   force uniqueness across result groups
  --version      show program's version number and exit
  
Created by Jason Bristol <json.bristol@gmail.com>
```

## Randomly pick 2 items from a list

`$ python pypicker.py 2 a b c d`

>c<br/>
a<br/>

## Randomly pick an item from a file

`$ python pypicker.py -i test_input.txt`
>Yolanda Holland

## Randomly pick 4 groups of 4 from a list

`$ python pypicker.py 4 -i test_input.txt -g 4 -v`

>Picking 4 item(s) out of 29:<br/>
Faith Boone<br/>
Hilda Mullins<br/>
Lewis Potter<br/>
Leona Evans<br/>

>Picking 4 item(s) out of 29:<br/>
Francisco Williams<br/>
Yolanda Holland<br/>
Ellis Jennings<br/>
Danielle Gill<br/>

>Picking 4 item(s) out of 29:<br/>
Jessica Mitchell<br/>
Renee Willis<br/>
Betty Lane<br/>
Yolanda Holland<br/>

>Picking 4 item(s) out of 29:<br/>
Hilda Mullins<br/>
Jessica Mitchell<br/>
Boyd Hunter<br/>
Wilson Marshall<br/>

## Randomly pick 4 unique groups of 4 from a list

`$ python pypicker.py 4 -i test_input.txt -g -v -u`

>Picking 4 item(s) out of 25:<br/>
Danielle Gill<br/>
Boyd Hunter<br/>
Amos Warner<br/>
Leona Evans<br/>

>Picking 4 item(s) out of 21:<br/>
Ellis Jennings<br/>
Francisco Williams<br/>
Renee Willis<br/>
Herbert Ball<br/>

>Picking 4 item(s) out of 17:<br/>
Mindy Lopez<br/>
Faith Boone<br/>
Hilda Mullins<br/>
Lucille Clayton<br/>

>Picking 4 item(s) out of 13:<br/>
Yolanda Holland<br/>
Trevor Goodman<br/>
Lewis Potter<br/>
Betty Lane<br/>

## Write output to a file

`$ python pypicker.py 4 -i test_input.txt -o test_ouptut.txt`

*test_output.txt*

>Faith Boone<br/>
Leona Evans<br/>
Boyd Hunter<br/>
Phillip Bailey

## Join the results and seperate by a delimeter

`$ python pypicker.py 4 -i test_input.txt -j ', '`

>Shirley Joseph, Brandon Rice, Ellis Jennings, Anita Larson
