# Flight issues

## Setting up the environment

At least python 3.9 is required to run this project.

Clone the project from the following link:

`git@github.com:maringuyot/flight-issues.git`

### Launching the program

To launch the program, simply execute the following command from the project root:

```
python -m flightissues [-c, --chart] [path_to_scan_file]
```

The `-c/--chart` option shows the plane's seating chart.

For convenience, a scan file is located in the `./resources` folder.

### Launching tests

To launch tests, execute the following command:

```
python -m unittest
```

### Viewing the documentation

Finally, to view the documentation, launch it in your browser:

```
python -m pydoc -n localhost
```

For usage help, pass in the `-h` flag.

## Development process

### Understanding the problem

Having lost my boarding pass right before entering the plane, I forgot what my seat's ID. Luckily, thanks to an app on my phone I managed to get every other person's boarding pass information. I just need to eliminate all of the unavailable seats to find mine. Easy!

Unfortunately, the company stores the seating information behind some sort of cipher, represented by 7 'F' or 'B' letters followed by three 'L' or 'R' letters.

Each of these letters mean something, and allow the user to pinpoint his exact position in the plane, provided he follows a set of rules.

Starting with the plane's full range of rows (128), the first 7 letters tell us to consecutively divide the range of rows in half, and to keep either the lower (F) or upper (B) part each time.

Once done, the 3 final letters provide the seat's position in that row. Just follow the same rule as before, but with 8 seats!

Finally, the seat's id is determined by the following formula: row * 8 + seat

So, we need an algorithm capable of looping over each boarding pass, finding its row, seat and id number, and crossing it off the list of available seats. Once done, the available seat will be mine...

### Solving the problem

#### Loading the input data and normalizing it

The input data is a file containing a single boarding pass per line. The first step is to load it in, and extract each cipher into a list.

#### Preparing the algorithm

We need a way to store unavailable seats. We can create a seating chart, with the amount of seats the plane has: 128 rows * 8 seats per row = 1024 seats

#### Executing the algorithm

After having prepared all of the data we need, we can start executing the algorithm.

##### Deciphering & filling in the seating chart

For each of the ciphers, we need to determine what row, seat and id it corresponds to.

I decided to create a 'Cipher' class, a wrapper around the raw cipher capable of calculating the data we need. Thanks to a few functions that simplify the overall readability of the code, the algorithm is straightforward:

1. Successively divide 128 in half 7 times and keep the correct part using `split_low` and `split_high`
2. Repeat the same process 3 times with 8 instead
3. Calculate the seat's ID using the formula mentioned above

It's now time to insert the seat's ID in the correct row and column of our seating chart.

##### Finding my seat!

I decided to use a 1D list instead of a 2D list because it greatly simplifies the algorithm in this stage.

The idea here is to ignore all of the first 'None' values as the pilot told me they didn't correspond to any seats, and that I wasn't there. Then, stop at the first sign of an available seat: it's mine! Except that the seat's ID is 'None', so I have to fetch the last (or next) seat's ID, and add or remove 1.

With 2D list, we run into the risk of finding our seat on the edge of the row. For the algorithm that means it possibly can't easily fetch the last or next seat, because it's in another sub-list. A 1D list allows us to fetch the last seat using a simple `index - 1` expression.

### Improving the project

So the algorithm worked well! I'll probably use it some other time... For now I can'll stick to improving the project's lifecycle.

#### Documentation

The project's development documentation is available using the following command:

```
python -m pydoc -n localhost
```

#### Unit tests

Testing is an important part of project lifecycle management. I tested the critical part of the algorithm: the 'Cipher' class.

The tests I implemented include:

1. Invalid cipher on object creation
2. Deciphering
3. Bounds splitting

The tests live in their own module, under the `./tests` directory.

#### Github repo

To easily publish the project and keep it updated, I uploaded it to Github.

### Going further

Multiple aspects of this project can be improved.

1. **The python version**: python 3.9 is outdated. Newer versions exist with better typing and improved functionnalities. I decided to use python 3.9 because my computer came with it, and I did not want to download a new version.
2. **Python venv**: Modern python projects use virtual environments to store all of the project's dependencies, to unify development environments between team members. I didn't use any because I did not require any external python dependencies, and because python 3.9 (on my computer) came with an obsolete version of virtual environments.
4. **Development environments**: Visual Studio Code has a nice feature: development containers. They allow the IDE to connect to a Docker container, to unify development environments even more. Providing a standardized environment to teams allows them to integrate new team members faster, and to avoid the "it works on my machine" problem.
3. **Better project structure**: If I ever add more files to this project, a deeper structure will be required to better organise the source code.
4. **CI/CD pipelines**: Automated test execution on branch merging is essential for modern development. As the project grows, more tests will be required, and a system to automate them and control what is allowed to be merged on the main branch is useful.
