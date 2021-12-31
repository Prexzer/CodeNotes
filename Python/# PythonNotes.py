# Python notes

# can use ; to write multiple lines in the same line
# example: command 1; command 2 (REMEMBER COMMANDS RUN IN ORDER)

# Exponentiation is ** 
#       ex: 4 ** 3 = 4^3 which is 64
 
# type function returns the type of variable passed in
# type (variable)

# strings can be declared using '' or ""
# IMPORTANT -> when printing strings and numbers must convert using str()

# convert variables to other types using float(), int(), bool(), str()

# if condition:
#       expression
# elif condition:
#       expression
# else condition:
#       expression

# while condition:
#       expression

# for var in sequence:
#       expression

# ex:
#       for height in array:
#           print(height)                            <-- prints each element

# for index, var in enumarate(sequence):
#       print(str(index) + ". " + str(squence))      <-- this allows us to keep track of an index

# for c in "string":                                 <-- can also loop through a string

# for x in range(10):                                <-- loops 10 times

# range(3,6)                                         <-- creates a range of 3 ~ 5

# TUPLES
# ========

# var = ("hi", 3, 2.3)                               <-- made with parenthesis (act similar to lists) **IMMUTABLE
# a, b, c  = var                                     <-- unpacking tuples

# var[0]                                             <-- accessing individual truple elements

# tuples are faster as they use less space than a list

# LISTS
# ==========

# arr[] = [5, "hi", 20.1, true]
# arr[-1] returns true

# arr[start:end]
# inclusive:exclusive
# arr[1:4] returns 5, "hi", 20.1

# arr[:5]
# returns elements 1 through 4

# arr[5:]
# returns elements 5 onward

# del(var[2]) <-- deletes third element in the list
#             <-- remember that all elements after element is deleted moves down 1 index (CAREFUL WHEN DELETING MULTIPLE THINGS)

# var + [22, "world"] <-- adds elements to the back of the list
# var.append()

# IMPORTANT
# listy = var       <-- listy now contains the reference to var (Var is a list)
#                   <-- doing listy[1] = 0, while also cause var[1] to become 0

# Using these two methods will allow us to create a copy of the list
# listy = list(x)
# listy = var[:]

# List comprehension
# ------------------

# """the template"""
# [(output expression) for (iterator variable) in (iterable)]
# {var: (var expression) for var in range(x)}                                  <-- dict version

# listy
# newlisty = [var + 1 for var in listy]                                        <-- creates a list from listy where all values are 1 greater
# newlisty = [(var1, var2) for var1 in range(10) for var2 in range(20)]        <-- tuple version
# newlisty = [[innerVar for innerVar in range(x)] for outerVar in range(y)]    <-- inner specifies the number of columns, outer the number of rows

# ex:   doctor = ['april', 'mary', 'nick']
#       listy = [doc[0] for doc in doctor]                                     <-- returns a list ['a','m','n']

# [var if (expression) else (express) for var in range(x)]                     <-- changes the output based on conditions
# [var for var in range(x) if x % 2 == 0]                                      <-- will only create outputs when the condition passes

# **IMPORTANT-- replacing the [] with () creates a generator
# (var for var in range(x))                                                    <-- creates a generator object
#  ----> allows you to iter over this list later when needed instead all at once (USEFUL FOR LARGE CHUNKS)

# list(generatorVar)                                                           <-- transform your generator into a list
# for x in generatorVar:                                                       <-- iterate through

# Generator functions
# ---------------------

# instead of 'return' use 'yield'
# yield does not work the same way as return, yield will store values until the function is done (aka you can have yield in loops)


# FUNCTIONS
# ===========

# max()                          <-- returns max
# round(int, decimalPlaces)      <-- rounds numbers to specified decimal places (Leave second part blank to get nearest INT)
# len()                          <-- returns length of list

# To get help for a function use the two following methods
# ?functionName
# help(functionName)  

# function(var[, var2])         <-- implies that var is required and var2 is optional

# sorted()                      <-- uses timsort (merge sort combined with insertion)

# listy.index("cat")            <-- returns index of cat
#      .count(2)                <-- counts the number of times 2 shows up

# USER MADE FUNCTIONS
# =====================

# def functionName(argument):
#       """ THIS IS A COMMENT USED FOR DESCRIBING FUNCTION """

# Search for variable names in the order: Local scope(inside fuction) -> enclosing local(when nested functions) -> global scope -> built-in modules 
#                                         -->(called LEGB RULE)
# This means you can pull variables from outside the function if needed BUT THEY WILL NOT BE UPDATED WHEN THE FUNCTION IS DONE

# global variableName                   <-- allows us to edit a global function inside a function

# nonlocal variableName                 <-- allows us to edit the variable in the outer function in a nested function

# def functionName(name, number = 1)    <-- default values can be set, if the function is called with only one arg then number is set to 1 by default

# def functionName(*args):              <-- using *args allows for any number of arguments to be passed (*args becomes a tuple containing the elements)

# def functionName(**kwargs)            <-- the args are passed in as a dict
#           ex: functionName(name = "bob", job = "teacher")     **kwargs becomes {name:'bob', job:'teacher'}

# LAMBDA FUNCTIONS
# ================

# variable = lambda x, y: x**y                       <-- example of a quick lambda function
#       ex: variable(2,3)                            <-- returns 8
# 
# Useful for Anonymous functions
# 
# map(func, seq)                                     <-- this function takes in a function and a sequence (this returns a map use list(map()) to make it into a list)
#       ex: map((lambda var: var **3), list)         <-- applies the variable function to all list elements

# filter()
# reduce()  <-- from functools import reduce

# ERROR HANDLING
# ==============

# try:
#       code....
# except:                                           <-- used as a general catch all for errors
#       code....

# raise ValueError()                                <-- allows you to create your own message for a value error

# alternative except
# ------------------
# except TypeError:                                 <-- will only go in here when there is a TypeError

# ITERABLES
# ===========

# examples: lists, strings, dict, file connections
# has an object with iter()

# var = iter(iterable)                              <-- var will hold the current iteration of the iterable
# next(iterable)                                    <-- moves the iterable to the next iteration and returns it

# print(*iterable)                                  <-- using the * will push out the rest of the iterable

# Example
# --------
# file = open('file.txt')
# it = iter(file)
# print(next(it))                                   <-- prints the first line of the file

# it = range(number)
# print(*it)
# ---------

# enumerate(iterable, startingIndex)                <-- creates a enumerate object that contains orignal list plus a count for each item (this is an iterable)

# list(enumerate())                                 <-- use this to print the enumarate object

# zip()                                             <-- takes in multiple lists and turns them into one list. Each index is a tuple containing the original elements.
# doing things like (*zippedList) will unzip the list after
# ^ SAME FOR ENUMERATE
#
# newVar1, newVar2 = zip(*zipList)                  <-- can use this to unzip lists and store them into variables

# for chunckin pd.read_csv('data.csv', chunksize = 1000)    <-- allows us to read in files that are too large


# PACKAGES
# ==========

# import numpy
# numpy.array()                   <-- if you import use like this

# import numpy as np              **INDUSTRY STANDARD  
# np.array()                      <-- if you import use like this

# from numpy import array
# array()                         <-- if you import use like this

# Combination of the above
# from numpy import array as arr
# arr()

# NUMPY
# ======

# numpy arrays can only have 1 data set
# array / (array * 2) is a valid numpy command(will iterate through and divide each element)

# array[array > 20]              <-- returns array with all values greater than 20
# array > 20                     <-- returns a true and false array filled with corresponding bool values for each element

# .shape                         <-- returns the shape of a 2d array in the form of (rows, columns)

# np.inf                         <-- represents infinity

# to work with multiple elements
# array[:, 1]                    <-- will print second column of all rows

# np.mean()                      <-- prints the mean of an array
# np.median()
# np.std()
# np.corrcoef(arr1,arr2)

# np.logical_and()              <-- if you use multiple arrays they must all be the same size
# np.logical_or()
# np.logical_not()

# for i in np.nditer(array)     <-- two go through every element in a 2D numpy array

# np.random.seed()              <-- seed input if needed
# np.random.rand()              <-- prints random number (floats by default)
# np.random.randint(0,n)        <-- generates int from [0, n)       (inclusive, exclusive)

# np.transpose()

# MATPLOTLIB
# ===========

#  import matplotlib.pyplot

# plt.plot(arr1, arr2)                    <-- plots arrays as points  ex: arr1 is x and arr 2 is y
# plt.scatter()                           <-- does not draw a line
# plt.hist()                              <-- use help(plt.hist) to see arguments
#                                         EX: s =           (this is size)
#                                             bins =        (default 10, can specify a number if you want, or pass in a series of numbers)
#                                             c =           (this is color)
#                                             alpha =       (opacity)
#                                             histtype =    (ex: 'step' <-- creates bar graph that aren't solid just lines)
#                                             yerr =        (use with .std() will create an error margin on your graph)

# plt.show()
# plt.clf                                 <-- cleans the plot

# plt.xlabel()
# plt.xscale()  ex: "log"                 <-- scales the x axis
# plt.title()
# plt.xtick()                             <-- parameteres: rotation = , (pass in degress to rotate)
# plt.yticks([],
#            [])                          <-- names each tick with the new name from the second corresponding array index

# plt.style.use()                         <-- changes the entire look of the graph, can use "ggplot"/"default"/'bmh'/'seaborn-colorblind' (more styles at matplotlib.org/gallery/style_sheets/style_sheets_reference.html)
#                                         <-- this goes before calling plt.subplots

# fig, ax = plt.subplots(n, m)            <-- plt.subplots() creats a figure object and an axis object (if you pass in n and m numbers will create n*m with n rows and m columns)
#                                         <-- figure is the container that holds everything we see on the page
#                                         <-- ax is the part of the page that holds the data

# ax.plot()                               <-- pass in data 
#                                         <-- can use marker = 'v', linestyle = 'none'/'--', color = 'b'/'r', label =""

# ax.bar()                                <-- bar graph
#                                         <-- calling this again with new data and passing "bottom = previousDataVariable" creates a stacked bar graph (to keep stacking do bottom = previous+previous2)
                                
# ax.hist()                               <-- histogram            

# ax.legend                               <-- prints a key with labels passed into plots/bars

# ax[0][0].plot()                         <-- if you create a n*m array of graphs

# ax.set_xlabel()
# ax.set_title()
# ax.tick_params()                        <-- allows us to change the ticks, ex: pass in 'y', colors = 'blue' to make ticks for y axis blue
# ax.set_xticklabel()                     <-- accepts only sequences, rotation = 90(rotates labels)

# ax2 = ax.twinx()
# ax2.plot()
# ax2.set_ylabel                                                         <--  These lines allow us to plot two series with the same x but different y (creates y axis on the right)

# ax.annotate('string', xy=[x,y], xytext=[x2,y2], arrowprops ={})         <-- makes annotation at certain point xy=[] and places the text at xytext =[]
#                                                                         <-- arrowprops creates an arrow from text to point(empty dict passed in makes default arrow)
#                                                                         <-- matplotlib.org/users/annotations.html for options, ex: {'arrowstyle':'->', 'color':'gray'}

# ax.errorbar(x,y, yerr)                                                  <-- add verticle markers to indicate error margin

# ax.boxplot([x,y])      

# ax.scatter()

# fig.savefig("filename.filetype")                                        <-- saves the graph to the file with name passed in
#                                                                         <-- quality parameter determines how compressed you make it (100 no compression ~ 1 fully)
#                                                                         <-- file types jpg/svg/png
#                                                                         <-- dpi = (dots per inch) creates a higher quality image the higher the number
# fig.set_size_inches([5,3])

# SEABORN
# ========

# import seaborn as sns
# import matplotlib.pyplot as plt                                         <-- seaborn is built on top of matplotlib so we have to import both

# sns.scatterplot(x=list1, y=list2)                                      extra parameters:
#                                                                           hue = '' or [] (pass in a column name from DataFrame to color code the data) (pass in a list if not using pandas)
#                                                                           hue_order = [] (pass a list with the order you want the hues to be displayed in)
#                                                                           palette = {} (pass in a dict where keys are the list elements from the hues and the values are the colors you want in hex or 'blue')

# sns.relplot()                                                          <-- the most used type of plot, also allows you to create subplots within the same figure using row, col
#                                                                            kind = 'scatterplot' or  'line' or others
#                                                                            row = , will order them in a row based on input specified. ex: 'day' will order it in rows monday -> friday
#                                                                            col =, same thing as row except up and down
#                                                                            *** using both row and column will create a matrix with the two inputs (ex: row = 'smoker', column = 'day' creates 2x5)
#                                                                            col_wrap = n, will cause a new row to be made after n number of graphs have been placed (ex: = 2 will make the third chart on a new row)
#                                                                            col_order = [], pass in a list with the order you want the columns in
#                                                                            size = 
#                                                                            style = 
#                                                                            alpha =  (this is transparency ranging from 0 ~ 1)
#                                                                            markers = True/False (adds different style dots to points)
#                                                                            dashes = True/False (makes the lines dashed or not)
#                                                                            ci = 'sd'/None/Check API for more     (confidence interval)

# sns.catplot()                                                         <-- used for catergorial plots(bar graphs, etc) same parameters as relplot()
#                                                                           kind = 'count'/'bar'/'box'/'point'/etc
#                                                                           whis = number or [] (changes the whisker for the box, number does IQR * NUMBER, list does [lowerPercentile, upperPercentile]) (default whis is IQR * 1.5)
#                                                                           sym = '' (used to eliminate outliers in box plot by passing empty string)

#                                                                           (Used in point plots)
#                                                                           join = False/True (toggle the lines between points between x variables)
#                                                                           estimator = np.median (median is usally better as it doesnt include outliers)
#                                                                           capsize = (adds lines to end of ci, pass in a number to specify the size of the line caps)
#                                                                           point plots are similar to bar plots (point is usally better to compare 2 sets of data rather than stacking two of the same bar under the same x)

# sns.set_style()                                                       <-- "white"(default)/'whitegrid'/'tick'/'dark'/'darkgrid'/etc

# sns.set_palette()                                                     <-- diverging palettes: 'RdBu'/'PRGn', reverse the palette by adding _r to the string -> 'RdBu_r'/'PRGn_r'
#                                                                           sequential palettes: 'Greys'/'Blues'/'PuRd'/'GnBu' (these are good for sequential data)
#                                                                           you can also pass in a custom list  of color names or hex codes of colors --> []

# sns.set_context()                                                     <-- scaling options to change the size of the plot. 'paper'/'notebook'/'talk'/'poster'

# fGrid = sns.relplot()/sns.catplot()                                   <-- FacetGrid (can have multiple subplots)
# axPlot = sns.scatterplot()/sns.countplot()/etc.                       <-- AxesSubplot (only one plot)

# fGrid.fig.suptitle()                                                  <-- adds title to plot (can also pass in y parameter to fix height)
# fGrid.set()                                                           <-- parameters: xlabel = "", ylabel = ""
# fGrid.set_titles("This is {col_name}")                                <-- adds individual titles for each subplot ({col_name} in the string updates for each subplot)


# (if multiple x-values are put on the line plot, seaborn automatically takes the mean and creates a confidence interval)

# sns.countplot(x = 'columnName', data= dataFrameName)                   <-- pulls that data from the specified column (DATA MUST BE TIDY)
# sns.countplot(x = list)                                                <-- returns a bargraph with the amount of times a unique entry occurs

# or sns.countplot(y = list)

# sns.swarmplot(x =, y = , data =)                                       <-- similar to bar graph but values keep all their information

# plt.show()                                                             <-- still use plt.show() to display the graph

# DICTIONARY
# ===========

# var = [key:value, key:value, key:value]
# var[key] returns value

# var[key] =                              <-- adds key and value, if reused on same key updates value
# del(var[key])
# var.keys()                              <-- returns a list with all the keys

# inserting duplicate keys will only update the existing value stored

# keys must be immutable (NO LISTS/ARRAYS)

# key in var                             <-- returns true or false if the key is in the dict

# for key, value in dict.items()         <-- looping through dictionaries (Dicts are unordered)


# Panda
# =======

# DataFrames (call these bric)
# bric                                   <-- a table data set
# bric = pd.DataFrame()                  <-- converts a dict to a bric
#       >>>>> The keys become the column labels and the values become row values (default row names are 0,1, 2, etc)
#       >>>>> bric.index = names         <-- uses the array list to name the rows column

# csv = comma-seperated values

# brics = pd.read_csv("path/file.csv")   <-- to read in the data

# brics columns should always contain only 1 type.
# different columns can have different types

# brics.shape
# brics.values                           <-- returns it as a 2D numpy array
# brics.columns                          <-- returns  column names
# brics.index                            <-- returns row names/index

# brics.describe()                       <-- returns statistics for each column
# brics.info()                           <-- shows info on each column, such as data type and number of missing values (cannot be used on columns)

# brics.sort_values()                    <-- pass column name to sort entire dataframe by that column(ascending order by default), ascending = False (descending order)
#                                        <-- (values = []) pass in a list of column names to sort accordingly in case of ties, ascending = [] can specify which column you want ascending/descending
# brics.sort_index()                     <--- sort by row instead (level = for a list instead), not really good industry practice

# brics["columnName"].isin([])          <-- pass in a list to filter for rows that contain values contained in the list (returns corressponding list with true and false values)

# brics['columnName'].mean()            <-- .median(), .mode(), .min(), .max(), .var(), .std(), .sum(), .quantile() (ADD AXIS TO SPECIFY WHICH DIRECTION , AXIS = 'COLUMNS', default is index)

# brics['columnName'].cumsum()          <-- .cummax(), .cummin(), .cumprod()        (cumulative functions, return the running cumulative at each part of the list, rather than a single value)

# brics['columnName'].agg()             <-- you can pass in functions that require columns. (ex: def pct30(column): return column.quantile(0.3), then you call .agg(pct30)) (can also pass in a list of functions)

# brics.drop_duplicates(subset = 'columnName') <-- returns a dataFrama with removed duplicates based on the column passed in (can pass in just one column or a list of columns)

# brics['columnName'].value_counts()    <-- returns a panda series with the number of times an element is seen (sort=True to return sorted by most seen, normalize = True to return it in % out of total)

# brics.group('columnName1')['columnName2'].agg([sum, min, max])      <-- allows you to group column information based on column1(these become the rows) and column2 the corressponding values, (CAN ALSO PASS A LIST INTO 'Colname1')
#                                                                     <-- returns a panda series object

# brics.pivot_table(values= 'columnName', index = 'rowEntries', columns='', fill_value = 0 aggfunc=, Margins = True) 
#                                           <-- value is name of column to summarize, index the column to group by, fillvalue fills NaN, columns is for multiple columns(multiple indexes)
#                                           <-- margins will sum the entire row and place at the end

# brics.set_index('columnName' or [])       <-- allows us to make on of the columns as an index, passing in a list produces multi-level index(hierarchial index)
# brics.reset_index()                       <-- resets current index back to default(does not delete the column that was there), drop = True to drop

# ACCESSING THE DATA
# ------------------

# brics['column']                       <-- this print out the entire selected column (as well as the row labels for the column)
#                                       <-- issue with this is that it also prints "name: 'column', dtype: object" at the end
#                                       <--- this a pandas.core.series.Series

# bric[['column']]                      <-- solves previous issue (this is a pandas.core.frame.DataFrame)
# bric[['column1', 'column2']]          <-- prints multiple columns

# bric[1:4]                             <-- selects what rows you want to print

# LOC IS LABEL BASED
# ILOC IS INDEX BASED

# bric.loc[['row']]                     <-- selects the specified row name
# bric.loc[['row', 'row2']]

# bric.loc[['row','row2], ['column5', 'column6']]  <-- only prints the overlap over the rows and columns

# bric.iloc[[1]]                        <-- prints all row values (and column names)
# bric.iloc[[1,2], [2,3]]               <-- rows 1 and 2, columns 3, 4 overlap

# select only columns do [:, 'column'] or [:, 1]    (slicing)
#                                                   (to slice inner index level pass a tuple (outerName, innerName):(outerName, innerName))

# for label, row in brics.iterrows():
#       print(label + ": " + bric['column'])        <-- will print the entire column with the labels

# the .iterrows()                                   <-- this always produces a Series, not always the best thing to do

# brics['column'].apply(len)                        <-- doing this is better than iterating through every column element and applying len with a for loop as that approach creates a series
# --> for methods try .apply(str.upper)

# brics.head(n)                                     <--returns n items starting from the top, default n = 5 if not specified

# brics['column'].unique()                          <-- returns a list with all the unique elements in that column

# data_array = brics.values                         <-- transforms dataframe into numpy array

# brics[(condition1) & (condition2)]                <-- how to filter by multiple conditions    

# brics['column'].dt.component                      <-- returns a list with all the corresponding component specified for each row (replace .component with .month, .year, .day)

# Missing Data
# -------------

# brics.isna()                                      <-- returns entire dataframe but filled with True/False in the corresponding slots if it is N/A or not
# brics.isna().any()                                <-- returns if a column contains N/A
# brics.isna().sum()                                <-- returns number of N/A in each column
# brics.dropna()                                    <-- drops all entries that have missing values
# brics.fillna(0)                                   <-- replaces N/A with value passed in

# Joining Data
# -------------

# Inner join returns only rows that appear in the same column

# newFrame = brics.merge(dataFrame2, on='columnName')       <-- Inner joins two tables together using .merge() pass in the second dataframe and the column they share in column 
#                                                           <-- suffixes =('_1,_2') when columns share the same column names it will attach _x, _y by default but we can specify using suffix

# One-to-many -> will return a larger dataset when multiple entries map to one 

#


# FILE HANDLING
# ==============

# Flat files are .csv,.txt(files that contain delimiters)

# with open('fileName', 'r') as file:                    <-- opens and closes file (Best version)
#       code....

# file = open('fileName', mode = 'w')                    <-- the C programming version
# file.write('hi')
# file.close()  

# file.read()                                            <-- reads entire file can be used in print statements
# file.readline()

# file = np.loadtext(filename, delimiter = ',' or '\t')  <-- other parameters: (np.loadtext cannot handle multiple)
#                                                            skiprows = []  (skips the specified number of rows)
#                                                            usecols = [] (use to specify exactly what columns you want [0,2] will only load first and third column)
#                                                            dtype = (will tell what type of data is passed in, useful for strings)

# np.genfromtxt()                                         <-- other parameters: (creates structed array-made for multiple data types) (each element of this array is a ?tuple? containing a row from the file) 
#                                                             names= True (tells reader there is a header)
#                                                             dtype = (must tell its none when using multiple)

# np.recfromcsv()                                         <-- same as genfromtxt but dtype by default is none and delimiter is ',' by default

# pd.read_csv()                                           <-- other parameters:
#                                                             sep = (panda version of delimiter)
#                                                             comment = '#  (tells the reader that everything after this char '#' is a comment)
#                                                             na_values = [] (pass in a list of strings that it will recognize as N/A when scanning)

# excelFile = pd.ExcelFile(file)
# excelFile.parse('Sheet1') or (0)                        <-- parses entire excel sheets, pass in the sheet name as a string or index as a float
# excelFile.sheet_names                                   <-- pulls sheet names

# xls = pd.read_excel(url, sheet_name = None)             <-- reads in excel from a url, sheet name set to none to import entire dataset
# xls.keys()                                              <-- name of the sheets

# Pickled files
# -------------

# import pickle
# with open('file.pkl', 'rb') as file :                  <-- 'rb' read binary, indicting its not meant to be read by humans
#       data = pickle.load(file)

# ^ used for datatypes that cant be saved as flat files(such as lists and dict)

# import os
# currdir = os.getcwd()                                 <-- gets current working dir
# os.listdir(currdir)                                   <-- lists the current dir

# from sas7bdat import SAS7BDAT                         <-- importing SAS files
# with SAS7BDAT('filePath') as file:
#       df_sas = file.to_data_frame()

# data = pd.read_stata('')                              <-- stata files

# import h5py
# data = h5py.File(filename, 'r')                       <-- for HDF5

# h5py files are structued in meta, quality, strain (these are contained in data.keys())
# data['meta'] to access the information in that group  

# import scipy.io                                       <-- import a .mat file
# mat = scipy.io.loadmat(fileName)

# Relation model
# --------------

# Each row(record) in a table represents an instance of an entity type
# each column in a table represents an attribute or feature of an instance
# each table contains a primary key column, what has a unique entry for each row
# there are relations between tables

# PostgreSQL, SQLite, mySQL

# SQLite 
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///dataBaseName')      <-- include sqlite:/// as it is a connection string
# connec = engine.connect()                             <--  connects to the data base
# rs = connec.execute('SELECT * FROM tableName')        <-- loads all the data from the table into rs
#       or connec.execute('SELECT * FROM tableName' WHERE conditionExpression) <-- allows us to import only records that pass the condition
#       or connec.execute('SELECT * FROM tableName ORDER BY columnName')       <-- sorts the table by ascending order of the specified column 
#                           'INNER JOIN Customers on Orders.CustomerID = Customer.CustomerID' <-- allows us to create a table that will join information together based on shared column key
#       format for inner join: SELECT (columns) FROM table1 INNERJOIN table2 on table1.column = table2.column

# # df = pd.DataFrame(rs.fetchall())                      
# df.columns = rs.keys()                                <-- sets column names
# con.close         

# with engine.connect() as connec:
#       rs = connec.execute('SELECT column1, column2, column3 FROM Orders') <-- will import only these columns
#       df = pd.DataFrame(rs.fetchmany(size=))                            <-- can specify how many rows to import using size=

# EVEN EASIER WAY********
# df = pd.read_sql_query("SELECT * FROM tableName", engine)

# tableNames = engine.table_names()                     <-- returns list with names of tables

# SELECT * FROM tableNames                              <-- returns all columns and rows of the table

# URL
# =====

# from urllib.request import urlretrieve, Request, urlopen

# urlretrieve(url, fileName)                            <-- opens url and saves content into a specified file(creates one if there isnt)
#                                                       <-- we can also just pass the url into pd.read_csv() to convert without a local file

# request = Request(url)
# response = urlopen(request)
# html = response.read()
# response.close()                                      <-- manual way of fetching responses from a url

# import requests
# r = requests.get(url)
# htmlText = r.text                                     <-- using requests package, easier to perform GET requests

# r.json()                                              <-- the requests package also has a json decoder(turns it into dict)

# urlopen()

# Beautiful Soup
# ---------------

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(htmlText)
# print(soup.prettify())                                <-- turns the html into a nice structered form

# soup.title                                            <-- returns the title under the title tags for the html page          
# soup.get_text()                                       <-- returns text

# for link in soup.find_all('a')                        <-- .find_all() gets all tags associated with that you passed in (all <a> tags in the example)
#       print(link.get('href'))                         <-- .get() pulls only the parameters passed in from the tag (href='' from the <a> tag in this case)

# JSON
# -----

# import json

# with open('snakes.json', 'r') as json_file:
#       json_data = json.load(json_file)                <-- python imports the json as a dict

# DATA CLEANING
# ==============

# brics['column'].str.strip()                                  <-- returns a pandas column with specificied part of the string removed
# brics['column'].astype()                                     <-- converts and returns column values as new type ex: 'int', 'category'(useful for numbers that represent categories)
# brics['coumn'].dtype                                         <-- returns the data type of the values in the column

# brics.drop(brics[brics['column'] > 5].index, inplace = true) <-- drops all values that fail to meet condition
# brics.loc[brics['column'] > n, 'column'] = n                 <-- sets a cap

# duplicates = brics.duplicated()                              <-- returns list of boolean values, true where duplicates are
#                                                              <-- subset= (columns to parse)
#                                                              <-- keep= 'first'/'last'/False <-- keeps only first/only last/ all
#                                                              <-- inplace: (drops directly from dataFrame no need to reassign)
# brics = brics.drop_duplicates()                              <-- drops complete duplicates

# diff = set(brics['column']).difference(brics2['column'])     <-- returns a set of inconsistent elements
# diff_row = brics['column'].isin(diff)                        <-- returns bool list of that contains true/false if diff is in that row
# brics[~diff_row]                                             <-- the '~' not allows us to return just the consistent rows

# brics['column'].str.strip()                                  <-- removes spaces from strings

# brics['newColumn'] = pd.qcut(brics['column'], q = number, labels = [])    <-- q specifies the number of bins it will place values in, label is a list of names to name the bins
# brics['newColumn'] = pd.cut(brics['column'], bins = [], labels = [])      <-- bins takes in a list of range to cut at ex: [0, 20, 40, 100] will create 0~20, 20~40, 40~100)
# 
# difference between qcut and cut is (qcut will cut it into even numbers into each bin) (cut makes the cutoffs more spreadout to represent the whole range of numbers)  

# brics['column'] = brics['column'].replace(dictionary)        <-- takes in a dictionary to map values with their new corressponding value (useful for collapsing categories)
# brics['column'].replace([], np.nan, inplace = true)          <-- replaces a list of values with NaN, inplace = True(we don't have to reassign does it in place)

# brics['column'] = brics['column'].str.replace("unwanted string", "wanted string")
#                                                              <-- r'\D+' is a regular expression that says anything that is not a digit

# brics['column'].str.len()                                    <-- returns list with len of each string in that column

# pd.to_datetime(brics['column'])                              <-- converts string to datetime object
#                                                                  :infer_datetime_format = True (used when different date formats happen)
#                                                                  :errors = 'coerce' (returns NA for where conversions fail)

# brics['column'].dt.strftime('%d-%m-%Y')                      <-- another way to convert
# brics[['column1', 'column2', 'column3']].sum(axis = 1)       <-- will sum the values in these columns for each row and return a list with the computed value

# 3 Types of missing data:
#                       Missing Completely at Random           (No systematic relationship between missing values and other/own values)
#                       Missing at Random                      (systematic relationship between missing values and other/own OBSERVED values)
#                       Missing not at Random                  (systematic relationship between missing values and other/own UNOBSERVED values)

# msno.matrix(brics)                                           <-- will create a graph to show where missing values are located

# Minimum edit distance algos:
#                      Damerau-Levenshtein  (insertion, substitution, deletion, transposition)     
#                      Levenshtein          (insertion, substitution, deletion)                     (fuzzywuzzy package)
#                      Hamming              (substitution) 
#                      Jaro Distance        (transposition) 

# from fuzzywuzzy import process
# process.extract(string, brics['column'], limit = n)         <-- returns a list of tuples in the form (stringMatched, similarityScore, indexInThisList)
#                                                             <-- limits specifies how many strings you want to return, EX: = 2, will return the two strings with the highest similarityScore

# import recordlinkage

# indexer recordlinkage.Index()                               <-- creates index object
# indexer.block()                                             <-- pass in the column you want
# pairs = indexer.index(brics1, bric2)

# compare_cl = recordlinkage.Compare()

# these two functions add the comparsions to the compare object
# ---
# compare_cl.exact('bric1columnName','bric2columnName', label=)                 <-- used to compare for exact matches(strings/ints/floats etc)
# compare_cl.string('bric1columnName','bric2columnName', threshold=, label=)    <-- used when you want to compare strings that are not exact but similar (set the threshhold you want)

# matches = compare_cl.compute(pairs, brics1, brics2)                           <-- will return a dataframe with 0 and 1s for matches

# matches[matches.sum(axis = 1) => n]                                           <-- will only display if the number of columns matching is >= n

# pd.get_dummies()                                                              <-- returns a dataframe with strings into "dummy variables" aka int

# from sklearn.preprocessing import Imputer
# from sklearn.pipeline import Pipeline

# imp = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# steps = [('imputation', imp), ('logistic_regression', logreg)]
# pipeline = PipeLine(steps)                                                     <-- pipeline allows us to drop missing values and compute our ML model at the same time
# pipeline.fit()/.predict()

# normalizing data
# ------------------
# results in values centered around 0 and std of 1

# Standardization: subtract mean, divide by variance
# or
# subtract by the minimum and divide by the range (will result in values -1 to 1)

# from sklearn.preprocessing import scale
# X_scaled = scale(X)


# Statistical Thinking
# =====================

# ECDF graph (a graph that shows how many points fall under a certain percentile)

#def ecdf(data):
    #"""Compute ECDF for a one-dimensional array of measurements."""
    ## Number of data points: n
    #n = len(data)

    # x-data for the ECDF: x
    #x = np.sort(data)

    # y-data for the ECDF: y
    #y = np.arange(1, n+1) / n

    #return x, y

# this is a quick function to get the x and y values for our function

# np.percentile(brics['column'], [25, 50, 75])              <-- returns values at the percentiles values passed in as a list

# np.var()                                                  <-- returns variance (sum of xbar - x_i )^2
# np.std()                                                  <-- returns standard dev value  (sqrt of the variance)

# covariance is the distance from the mean of the x, and mean of the y
# np.cov()                                                  <-- returns a covariance matrix

# Pearson correlation (covariance / (std of x * std of y)) aka (variablitity due to codependence/ independant variability)
# ranges from [-1, 1] (complete negative corr to complete positive corr)

# Probability mass funciton (PMF) --> the set of probabilities of discrete outcomes

# SUPERVISED LEARNING - W/ SCIKIT LEARN
# =======================================

# from sklearn.neighbors import KNeighborsClassifier

# knn = KNeighborsClassifier(n_neighbors = n)
# knn.fit(data, target)                                     <-- trains the data (only dataframes/numpyarr, no misisng data, only numbers (no strings))
# knn.predict()                                             <-- predicts a new point

# from sklearn.model_selection import train_test_split      <-- used to split into training and testing sets

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 21, stratify = y)

# from sklearn.linear_model import LinearRegression

# reg = LinearRegression()
# reg.fit()
# reg.prediction()

# from sklearn.model_selection import cross_val_score

# cv_results = cross_val_score(LinReg, X, y, cv = 5)        <-- cv is the number of cross validations
# %timeit cross_val_score                                   <-- shows how long it takes (more CVs = more time)

# Ridge will let us punish our model from overfitting (using large coefficients)
# adjust the alpha (too low alpha will lead to overfitting, too high will lead to underfitting)

# from sklearn.model_selection import Ridge
# variables = train_test_split()
# ridge = Ridge(alpha = 0.1, normalize = True)
# ridge.fit()
# ridge.predict()
# ridge.score(x, y)

# Lasso shrinks less import coefficients to 0

# from sklearn.linear_model import Lasso
# lasso = Lasso(alpha = 0.1)
# lasso_coef = lasso.fit(X, y).coef_

# THIS IS GOOD FOR GRAPHS SHOWING WHICH FEATURES ARE THE MOST IMPORTANT

# confusion matrix
# ----------------

# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix

# print(confusion_matrix(y_test, y_pred))                  <-- prints the matrix
# print(classification_report(y_test, y_pred))             <-- prints a report with precision/recall/f1 score/support
#-----------------------------

# logistic regression

# from sklearn.linear_model import LogisticRegression
# same idea as linear

# from sklearn.metrics import roc_curve
# y_pred_prob = logreg.predict_proba(X_test)[:,1]
# fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# ROC PLOT

# plt.plot([0,1], [0,1], 'k--')
# plt.plot(fpr, tpr, label ='Logistic Regression')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Logistic Regrssion ROC Curve')

# Area under ROC curve

# from sklearn.metrics import roc_auc_score
# roc_auc_score(y_test, y_pred_prob)

# or using cross validation
# cross_val_score(reg, X, y, cv = 5, scoring = 'roc_auc')

# Hyper parameter tuning

# from sklearn.model_selection import GridSearchCV

# param_grid = {'n_neighbors': np.arange(1, 50)}
# knn = KNeighborsClassifer()
# knn_cv = GridSearch(knn, param_grid, cv =5)
# knn_cv.fit(X, y)
# knn_cv.best_params_

# RandomizedSearchCV()                                   <-- instead of grid search we can use this on really large CV


