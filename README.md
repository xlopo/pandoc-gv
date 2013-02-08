# Usage

    pandoc -tjson README.md |./pandoc-gv.py |pandoc -fjson -oREADME.pdf -H header.txt

Where the contents of "header.txt" is

    \usepackage{graphicx}

# Examples

* Make sure you include graphicx in your head!

* Defaults to "dot" layout engine

    ```  {#gv}
    digraph g {
        A->B;
        A->C;
        C->D;
    }
    ```

**Produces**

![Example 1](https://github.com/xlopo/pandoc-gv/raw/master/examples/example_01.png)

# "Inline" Code Block

* That is to say, a code section where the text or commands preceding or following does not have at least 2 newlines

* Note that the parameters have to be passed at the end in this case

    Graph over here -> 
    ``` 
    digraph g {
        A->B;
        A->C;
        C->D;   
    }
    ``` {#gv} $O(n) \text{ include Code section }$

**Produces**

![Example 2](https://github.com/xlopo/pandoc-gv/raw/master/examples/example_02.png)


# Regular code block (uninterpreted by Graphviz)

* Without the "{.dot}" parameter section, the text gets rendered as a regular code block

    ```
    digraph g {
        A->B;
        A->C;
        C->D;
    }
    ```

# Changing the Layout

* An optional secondondary "."-command gets interpreted as the layout engine


    ``` {#gv .neato}
    digraph g {
        A->B;
        A->C;
        B->A;
        C->D;
    }
    ```

\textbf{Produces}

``` {#gv .neato}
digraph g {
    A->B;
    A->C;
    B->A;
    C->D;
}
```


    ``` {#gv .circo}
    digraph g {
        A->B;
        A->C;
        C->D;
        C->F;
        C->G;
    }
    ```

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
