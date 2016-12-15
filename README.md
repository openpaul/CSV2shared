# CSV to .shared conversion
Imagine you want to use Mothur (https://www.mothur.org/) on a Abundance table, but only have it as a CSV.
Somehow I did not find a conversion in Mothurs Documentation.

This script can do exactly that: It takes a CSV OTU or any abundance table and converts it into a simple .shared file of Mothur.

It requires python 2.7 and could be easily ported to Python 3.

## Call the script

Just call the scrip via 

```
python CSV2shared.py input.csv output.shared
```

Adjust the field delimiter if needed.

## Disclaimer
I wrote this and used it once. It might not work for you, but I though I'd rather share this then just let it go to waste.

Feel free to file an issue or better a pull request if you encounter a mistake or error.
