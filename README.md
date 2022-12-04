# dot2cypher
Tool to convert dot file to a graph created from cypher 

https://en.wikipedia.org/wiki/DOT_(graph_description_language)

https://manpages.ubuntu.com/manpages/xenial/man1/debtree.1.html


prerequisits

```
pip install pydot
pip install getopts
```


```pi
pipdeptree --packages ipykernel --graph-output dot > ipykernel-dependecies.dot
pipdeptree --packages ipykernel --graph-output png > ipykernel-dependecies.png
```
# References

https://pypi.org/project/getopts/

https://pypi.org/project/pipdeptree/
