# Strings

Overview of *Strings* and their usage.

Strings can be **delimited** by single or double *quotation marks* (but the quotes have to match):

```python
single_quoted_string = 'data science'
double_quoted_string = "data science"
```

Python uses **backslashes** to encode *special* characters. For example:

```python
tab_string = "\t"   # represents the tab character
len(tab_string)     # is 1
```

If you want backslashes as backslashes (which you might in Windows directory names or in regular expressions), you can create *raw* strings using `r""`:

```python
not_tab_string = r"\t"      # represents the characters '\' and 't'
len(not_tab_string)         # is 2
```

You can create *multiline* strings using three double quotes:

```sh
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
```

A new feature in Python 3.6 is the **f-string**, which provides a simple way to substitute values into strings. For example, if we had the first name and last name given separately:

```python
first_name = "Joel"
last_name = "Grus"
```

we might want to combine them into a full name. There are multiple ways to construct such a **full_name** string:

```sh
full_name1 = first_name + " " + last_name               # string addition
full_name2 = "{0} {1}".format(first_name,last_name)     # string.format
```

but the **f-string** way is much less unwieldy:

```python
full_name3 = f"{first_name} {last_name}"
```

and is to be preferred.
