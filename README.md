# minescript

### What is this?
At this point into the project (at the time of writing, 8 hours) - I have no clue. yet.

### What will it be?
Good question! My goal with this is to make programming complex commands in minecraft MUCH simpler, quicker, and hastle-free. My idea with the project is to convert a script (dubbed "Minescript") into classical minecraft commands and functions to be used inside a datapack.

### Why would I want to do this?
Another great question! Minecraft commands are tedious to make - they involve a heavy use of repetition, intermediate "variables", *no* control statements, etc. However - my end goal with Minescript is to make it a classical programming language with all these features and more, such as:
- Variables (x = 5; y = 10)
- Scoped Variables!
- Operations (x = 5 + 2; y -= 10; z = x + y)
- Control statements (IF/ELSE/ELSE IF, FUNCTIONS, FOR, WHILE)
- Importing of external scripts
- \+ more to come!

#### for example...
```
i = 12;
if ( i > 2 ) {
    execute as @e[type=minecraft:horse] run say lookie at me, I'm a horse!;
    height = 1;
    for (each player in @a) {
        execute as player run teleport @p ~ ~height ~
        tellraw player {"text":"hahaha, get pranked!"}
        height += 1;
    }
    tellraw @a {"text":"hello world!"}
}
```
At this point I'm not even fully convinced all the above is even possible, but it's worth a try anyway (and my sanity, apparently...)

### Installation
wait wait wait - you actually want to use this? Sweet! all you have to do is \<INSERT HOW TO USE IT HERE\>. It's easy!

### Contribution
and 10 other jokes fun jokes you can tell yourself!
