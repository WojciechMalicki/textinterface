# SimpleProgressBar
<font color = #33ffbb>This simple module allows you to create a progress bar in a terminal in text mode. The bar consists of curly braces: {}, in which the numerical value of the progress is enclosed, and the bar is made of square brackets [] and two types of signs expressing the progress and the amount of remaining space. </font> 
#### The progress bar is an o bject with three properties, each of them having default values:
- **width** - an integer, specifies the number of characters between square brackets. The default is 20.
- **char** - string, a single character representing a progress step. The default value is '#'.
- **spc** - string, a single character representing any other place. The default is '-'.
#### The strap has two methods:
- **.next(progress)** - increases the numerical percentage value in curly braces and the number of the progress element, the 'progress' parameter is set to <0, 1>, the default is 0.
- **.end()** - sets the value in curly braces and the graphical representation to 100%. It's a good idea to invoke it after the loop is finished to set it to the maximum value.

---

### Import:
`import simpleprogressbar`
or:
`from simpleprogressbar import progressBar`

Create an object with default values with the first method of import:
`my_bar = simpleprogressbar.progressBar()`

Create an object with default values with the second method of import:
`my_bar = progressBar()`

> {10%}[##------------------]

Create an object with its own properties:
`my_bar = progressBar(width = 10, char = '>', spc = '.')`

> {10%}[>---------]

---

### Example
```python
    from simpleprogressbar import progressBar
    from time import sleep

    my_bar = progressBar(width = 50, char = ':', spc = '.')

    end = 100
    for i in range(end):
        sleep(0.1)
        my_bar.next(i / end)
    
    my_bar.end()
    
