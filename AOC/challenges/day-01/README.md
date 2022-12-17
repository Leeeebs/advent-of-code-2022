# Advent Of Code 2022 - Day 1 
https://adventofcode.com/2022/day/1

**Calorie Counting**
> The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

#### --- Part 1 ---

*The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.*

For example, suppose the Elves finish writing their items' Calories and end up with the following list:
```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
This list represents the Calories of the food carried by **five Elves**:

The **first Elf** is carrying food with `1000`, `2000`, and `3000` Calories, a total of `6000` Calories.<br>
The **second Elf** is carrying one food item with `4000` Calories.<br>
The **third Elf** is carrying food with `5000` and `6000` Calories, a total of `11000` Calories.<br>
The **fourth Elf** is carrying food with `7000`, `8000`, and `9000` Calories, a total of `24000` Calories.<br>
The **fifth Elf** is carrying one food item with `10000` Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:<br>
they'd like to know how many Calories are being carried by the Elf carrying **the most Calories**.

In the example above, this is `24000` (carried by the **fourth Elf**).

**Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?**

#### --- PART 1: SOLUTION ---
<img width="903" alt="Screenshot 2022-12-17 at 18 52 16" src="https://user-images.githubusercontent.com/40168753/208257188-78a70a3d-36ca-4ce9-a79e-c4fe255a6f55.png">

#### --- Part 2 ---
> By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

*To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.*

In the example above, the top three Elves are the **fourth Elf** (with `24000` Calories), then the **third Elf** (with `11000` Calories), then the **fifth Elf** (with `10000` Calories).

The sum of the Calories carried by these three elves is `45000`.

**Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?***

#### --- Part 2: SOLUTION ---
<img width="918" alt="Screenshot 2022-12-17 at 18 52 33" src="https://user-images.githubusercontent.com/40168753/208257195-dfd64797-9d32-4094-8ec1-156693b8cc2b.png">

