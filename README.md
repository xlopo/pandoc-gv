# Usage

    pandoc -tjson README.md |./pandoc-gv.py |pandoc -fjson -oREADME.pdf -H header.txt

Where the contents of "header.txt" is

    \usepackage{graphicx}

# Examples

* Make sure you include graphicx in your head!

* Defaults to "dot" layout engine

~~~~
```  {#gv}
digraph g {
	A->B;
	A->C;
	C->D;
}
```
~~~~

*Produces*

![Example 1](https://github.com/lopo/oandoc-gv/raw/master/examples/solarized-yinyang.png)

# "Inline" Code Block

* That is to say, a code section where the text or commands preceding or following does not have at least 2 newlines

* Note that the parameters have to be passed at the end in this case

~~~~
Graph over here -> 
``` 
digraph g {
	A->B;
	A->C;
	C->D;
}
``` {#gv} $O(n) \text{ include Code section }$
~~~~

\textbf{Produces}

``` 
digraph g {
	A->B;
	A->C;
	C->D;
}
``` {#gv} $O(n) \text{ include Code section }$

# Regular code block (uninterpreted by Graphviz)

* The {.dot} parameter section is required for this to work

```
digraph g {
	A->B;
	A->C;
	C->D;
}
```

# Changing the Layout

* Given an optional second "."-command gets interpreted as the layout engine

~~~~
``` {#gv .neato}
digraph g {
	A->B;
	A->C;
	B->A;
	C->D;
}
```
~~~~

\textbf{Produces}

``` {#gv .neato}
digraph g {
	A->B;
	A->C;
	B->A;
	C->D;
}
```


~~~~
``` {#gv .circo}
digraph g {
	A->B;
	A->C;
	C->D;
	C->F;
	C->G;
}
```
~~~~

\textbf{Produces}

``` {#gv .circo}
digraph g {
	A->B;
	A->C;
	C->D;
	C->F;
	C->G;
}
```
