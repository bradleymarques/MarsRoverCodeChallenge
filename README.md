## Instructions to Run
...
### testing
`python InputParserTest.py`

## Design decisions
I've broken the problem into three main modules:
 1. Parse the input file into it's components
 2. Check the command sequence doesn't land the rover into trouble
 3. Execute the command sequence and report back on the rover position

## Testing
Each file has a corresponding test file which includes unit tests around non-trivial logic. The tests encode the expected behaviour of the functions defined in the class files and running these tests frequently during development will give you confidence that your changes have not had unintended changes.