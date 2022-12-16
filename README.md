# Santa Hat app

### Instructions

Allows players to get and pick someone from the `engineers` for Secret Santa
- Feed the list of players in the `engineers` file, one name per line
- Deploy the app on a shared box
- Players will have to feed their name as written in the list, which is added to the `.gifter` file
- Their randomly assigned secret santa is added to `.gifted`

To run, simply  execute the app remotely, replacing user@ip
`ssh -t user@ip "cd santa; python3 santa_hat.py"`

### Python Dependencies

- numpy
- termcolor

### Known limitations

Currently doesnt allow concurrent use. Two players going on the shared santa box at the same time may end up picking the same person
Need a queue system
