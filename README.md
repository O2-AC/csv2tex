# csv2tex

This application converts a `.csv` file into `tex` code, ready for you to 
copy into your `tex` document. 

To use it directly from command line make sure that the repository is in your 
$PATH. I recommend creating a symbolic link to `$HOME/bin/csv2tex` and
add the `$HOME/bin` directory to your `$PATH` variable.

## Usage:
```
csv2tex [options] <file.csv>
```

For now you can ignore columns from the `.csv` file by using the 
`-i <column title>` switch. And separating the different columns
by a comma.
Additionally you can enable the `-b` switch to add `\bigstrut`
add the end of each entry to increase the space between the rows.

## Example
```
file.csv

Entry,var1,var2,var3
1,60,70,80
2,6,7,8
3,0.6,0.7,0.8
```
```
$ csv2tex file.csv
\begin{tabular}{lccc}
\hline
Entry&var1&var2&var3\\
\hline
1&60&70&80\\
2&6&7&8\\
3&0.6&0.7&0.8\\
3&0.6&0.7&0.8
\hline
\end{tabular}
```
With ignoring the column `var2`:
```
$ csv2tex -ivar2 file.csv
\begin{tabular}{lcc}
\hline
Entry&var1&var3\\
\hline
1&60&80\\
2&6&8\\
3&0.6&0.8\\
3&0.6&0.8
\hline
\end{tabular}
```

(c) Ole Osterthun
