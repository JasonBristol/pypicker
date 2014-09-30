pypicker
========

A command line random picker for python.

```
usage: pypicker.py [-h] [-ng NG] [-o O] [-j J] [-v] [-u] N I

Randomly pick n items from a list

positional arguments:
  N           number of items to pick (default 1)
  I           input file of items to choose from

optional arguments:
  -h, --help  show this help message and exit
  -ng NG      number of result groups to generate (default 1)
  -o O        output file to write results to
  -j J        join results using specified delimeter
  -v          verbose output
  -u          force uniqueness across result groups

Created by Jason Bristol <Gethsemane369@gmail.com>
```
========

**Randomly pick an item from a list**

```$ python pypicker.py 1 test_input.txt```
>Yolanda Holland

========

**Randomly pick 4 items from a list**

```$ python pypicker.py 4 test_input.txt```

>Trevor Goodman<br/>
Francisco Williams<br/>
Jessica Mitchell<br/>
Herbert Ball

========

**Randomly pick 4 groups of 4 from a list**

```$ python pypicker.py 4 test_input.txt -ng 4 -v```

>Picking 4 individuals out of 29:<br/>
Faith Boone<br/>
Hilda Mullins<br/>
Lewis Potter<br/>
Leona Evans<br/>

>Picking 4 individuals out of 29:<br/>
Francisco Williams<br/>
Yolanda Holland<br/>
Ellis Jennings<br/>
Danielle Gill<br/>

>Picking 4 individuals out of 29:<br/>
Jessica Mitchell<br/>
Renee Willis<br/>
Betty Lane<br/>
Yolanda Holland<br/>

>Picking 4 individuals out of 29:<br/>
Hilda Mullins<br/>
Jessica Mitchell<br/>
Boyd Hunter<br/>
Wilson Marshall<br/>

========

**Randomly pick 4 unique groups of 4 from a list**

```$ python pypicker.py 4 test_input.txt -ng -v -u```

>Picking 4 individuals out of 25:<br/>
Danielle Gill<br/>
Boyd Hunter<br/>
Amos Warner<br/>
Leona Evans<br/>

>Picking 4 individuals out of 21:<br/>
Ellis Jennings<br/>
Francisco Williams<br/>
Renee Willis<br/>
Herbert Ball<br/>

>Picking 4 individuals out of 17:<br/>
Mindy Lopez<br/>
Faith Boone<br/>
Hilda Mullins<br/>
Lucille Clayton<br/>

>Picking 4 individuals out of 13:<br/>
Yolanda Holland<br/>
Trevor Goodman<br/>
Lewis Potter<br/>
Betty Lane<br/>

========

**Write output to a file**

```$ python pypicker.py 4 test_input.txt -o test_ouptut.txt```

*test_output.txt*

>Faith Boone<br/>
Leona Evans<br/>
Boyd Hunter<br/>
Phillip Bailey

========

**Join the results and seperate by a delimeter**

```$ python pypicker.py 4 test_input.txt -j ','```

>Shirley Joseph, Brandon Rice, Ellis Jennings, Anita Larson

========
