# dot2cypher

## Introduction
Tool to convert dot file to a graph created from cypher 

https://en.wikipedia.org/wiki/DOT_(graph_description_language)




## Prerequisits
Before using dot2cypher install the following libraries.
```
pip install pydot
pip install getopts
```

To generate a dot-formatted network you can use pipdeptree.
```
pip install graphviz
pip install pipdeptree
```


## Usage

Generate a dot file and png file.
```
pipdeptree --packages ipykernel --graph-output dot > ipykernel-dependecies.dot
pipdeptree --packages ipykernel --graph-output png > ipykernel-dependecies.png
```

Example usuage dot2chpher.
```
python dot2cypher.py -i ipykernel-dependecies.png -o ipykernel-dependecies.cy
```

## References

https://pypi.org/project/getopts/

https://pypi.org/project/pipdeptree/

https://manpages.ubuntu.com/manpages/xenial/man1/debtree.1.html
