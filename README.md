# graphwar_function_grapher  
this is a graphwar function previewing tool to effectively avoid mistakes is games  
![graphwarsc1](https://user-images.githubusercontent.com/81552194/181109164-fc588080-fc81-4005-ba6f-e4c6e3ab15a0.png)
## Dependencies  
Win32  
matplotlib  
numpy  
sympy  
## Usage
1.open graphwar and play  
2.when you calculated a function and wanted a preview  
3.copy the function  
4.run main.py  
5.hit update  
6.hit paste  
7.click yourself, and you get a preview of the function!  
8.repeat 5~7 the next time you need preview

## Important!  
#### if your function won't show up you might have made the following mistakes
4x is invalid syntax as 4\*x should be used  
e^x is invalid as exp(x) should be used  
x^2.5 is invalid as x^2 should be used  

#### The following functions are tested to be supported:  
(3)/(1+exp(-55\*(x+4)))  
3/(1+(-4\*(x+3))^2)  
0.5\*(abs(x+4)-abs(x-5))  
3\*sin(2\*x)/(1+exp(-3\*(x+1)))  

if you find any more bugs tell me at issues
