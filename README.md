## Instructions to Run

1. activate the virtualenvironment by navigating to the MarsRoverCodeChallenge directory and running `source rover-virtualenv/bin/activate`
2. Edit the `example-input-file.txt` to include the input you would like to have run.
3. Run the program by executing `python main.py`
4. To exit the virtual environment, just run `deactivate`

### testing
currently having trouble with test discovery. I would like `python -m unittest` to auto run all my tests.
To run the tests of a class, run:
- `python test/RoverTest.py`
- `python test/RoverControllerTest.py`
- `python test/ZoneTest.py`
- `python test/InputParserTest.py`

## Design decisions
I've broken the problem into three main parts:
 1. Parse the input file into it's components
 2. Use a 'Rover Controller' to handle simulating of a path, transmitting the safe path to the rover and instructing the rover to execute the path.
 3. Use a Rover class to safely execute the command sequence with a redundant safety check (cause rovers are expensive) and report back on the rover position
 
 Having the input parser in it's own class groups the logic together that is specific to that task. This can make changes to that logic easy to reason about or replace entirely with a different class if the input template changes.
 
 The Rover Controller is fundamental to the problem because it allows us to simulate movements before getting the real rover to execute the movements. This is a safety mechanism to prevent us from making the rover travel into unsafe areas. Furthermore, I would have the Rover Controller be running on a machine located on Earth as it can also saves us time by checking the safety of a path before undergoing the transmission time costs of sending the commands through space to the rover only to have the rover refuse to execute an unsafe path. In this simplified example, the "transmit commands to rover" function merely sets the command sequence as a field of the Rover object but in real life, the function would have to handle actual network transmission between the machine running the controller program and the rover hardware located on Mars.
 
 The Rover has a simple command interface and a command interpreter which can read commands of a command_queue and execute them. It also has a safety mechanism that raises an exception if a move will put it into an unsafe area.

## Testing
Each file has a corresponding test file which includes unit tests around non-trivial logic. The tests encode the expected behaviour of the functions defined in the class files and running these tests frequently during development will give you confidence that your changes have not had unintended changes.