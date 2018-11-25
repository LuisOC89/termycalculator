# termycalculator

## Calculator in terminal

Calculator created in order to participate in the 2nd edition of the contest [zContest](https://github.com/soft9000/zContest)

### Scope
1. You will be able to enter mathematical expressions like if you were using a calculator.
2. Operations are limited to sum, difference, multiplication, division and operations inside parenthesis.
3. Decimal numbers will have to be entered in fractional form. Ex: `1/2` instead of `0.5` .
4. It is ok if you leave blank spaces. The program will put the numbers together for you. 
Ex: `1  /  2` is going to be considered as `1/2`.

### Examples:
`Calculate this: 12+34/2+1+2*5-30`  
`Results: 10.0`  
  
`Calculate this: 1 2 + 4     4`  
`Results: 56`

`Calculate this: (((12+3/(4/5))-32)+5)`  
`Results: -11.25`

`Calculate this: 23+(1)+6+(87)-32/(9*5)`  
`Results: 116.29`

`Calculate this: 8-9+67*1/2-40+(54*1/2-3+(45-2))`
`Results: 59.5`

##### Division by zero  
`Calculate this: 12+32/(1-1)`  
`Results: Surprise? Check yourself`

### Start application
1. Download this project and unzip it in the folder of your preference.
2. Using [bash](https://git-scm.com/downloads) or other program of your preference (with python previously installed)
access the project's folder.
3. Enter on bash terminal: `python interface.py`.

### --see-steps option
This is an option to see all the steps the calculator goes through while processing a valid expression.
You can activate it by entering on bash terminal: `python interface.py --see-steps` instead of `python interface.py`.