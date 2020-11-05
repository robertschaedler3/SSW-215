# SSW 215

Stevens Institute of Technology Individual Software Engineering

## Description

In this course students learn to practice a disciplined engineering process for developing software. Individual skills and practices, such as effort estimation and unit testing, are mastered so that students can become successful members of software engineering teams. Best practices in software engineering are followed, including the use of simple design patterns with well-known properties. Students work in small teams to construct a simple web service using the industry standard Ruby programming language, Rails framework and MySQL database technology.

## Assignments

> Code each of the following such that all of the features/rules are implemented and users can interract accordingly.

### Pig Latin

Create a piglatin translator. Given a phrase in english print the piglatin translation.


For words beginning with a consonant, all letters before the first vowel are placed at the end of the word, then `ay` is added.

```bash
> python piglatin.py pig
igpay

> python piglatin.py trash
ashtray
```

For words beginning with a vowel, just add `way` to the end.

```bash
> python piglatin.py eat
eatway
```


> **Extra credit:** Preserve punctuation and capitalization when translating.

### Shut-the-Box

**Rules:**

- There are 2 players each with 9 tiles labeled 1 through 9.
- The object of the game is to turn over all 9 tiles by rolling dice.
- If a player turns over all the tiles greater than 6, then the player rolls one die from that point, going forward.
- A player wins if they flip over all of their tiles.

**Play:**

At the beginning the first player rolls 2 die. Let’s say the player rolls a 2 and a 3. The player can either turn over tile 5 or tiles 2 and 3. Then the second player rolls and turns over tiles...this continues until one player turns over all the tiles and wins or the players go a round with each player unable to turn over a tile. If this happens the game is reset and all tiles are returned to each of the players. 

### Nim
Welcome to the game of nim. 

This nim game version starts with 21 sticks and the player selects 1, 2 or 3 sticks. If a player does not select 1, 2 or 3 sticks an error occurs and they again are asked to select 1, 2 or 3 sticks.   This continue until all the sticks are gone,  The player selecting the last stick loses.  the game then asks if the players would like to play another game.


> **Extra credit:** Give a player the option to compete against the computer.
> 
> *Hint: it is possible for the computer to learn from its mistakes.*