
# Zeno Paradoxes

Made using : 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Problematic and context

For this exercise we had to create three different algorithms to study three different paradoxes that were introduced by Zeno, a philosopher. 

The first paradox introduces a race between Achilles and a turtle. In this paradox it is said that if we give the turtle a heads up in the start Achilles will never be able to catch up to the turtle. He will always have to close the distance between him and the turtle, and while closing the distance the turtle will keep moving, creating distance in-between them again. 

The second paradox introduces the principle of Dichotomy. Meaning that if we have, in this case a tree and a rock, if we throw the rock at half the distance of the tree each time the rock will never reach the tree. For example we have a tree at 10 meters, the rock will be thrown to 5 meters, then 7.5 etc. and it will never reach the tree no matter how many times we throw it. 

The third paradox is about an arrow and a target. When aiming and shooting the arrow at the target, if we look at the position of the arrow during a time t1, t2 etc the arrow will be stopped, therefore not moving. Meaning that the movement of the arrow is impossible since at each tx time it is not moving.

These paradoxes all includes notions and information about movement, time and the correlation between 2 variables in the form of a race, a throw and a shooting. 

Each time we have a "target" meaning something that has to be reached and an "object" meaning something that has to reach the target. In each example it is, Achilles that needs to reach the turtle, the rock that needs to reach the tree and the arrow that is shot at the target. 

What we are trying to do is create algorithms using python is order to study these paradoxes and see how they perform when using different principles such as the law of motion. 

## Solutions

#### Achilles and the turtle
For this paradox we have simply introduced two variables that will have a race together. The turtle has been given a heads up in the race and the speed of both variables has been adjusted in order to, more or less, reflect a plausible reality. 

Achilles has been given a speed of 20m/s whereas the turtle has a speed of 2m/s (it is a fast turtle). 

They will both be moving at the same time using their respective speed and we will study if Achilles manages to catch up to the turtle or if the paradox introduced by Zeno is correct and the turtle will always create a gap between itself and Achilles. 

#### The tree and the rock
In this paradox we will be using a tree at a distance of 10 meters and a rock thrown at it from a starting position of 0 meters. Each time the rock is thrown we will first measure the position of the rock using the position of the tree. 

`rock.position += ( (tree.position - rock.position) *0.5)`

This way we will first measure the position of the rock, get the distance left between the rock and the tree, and measure the distance the next throw is going to achieve. 

Looking at this paradox it should be impossible for the rock to reach the tree since it never gets thrown at the full distance, always half of it. We will see, using the script if it is possible for the rock to reach the target, or not. 

#### The target and arrow
With this paradox we are studying an arrow and a target. The arrow is aimed and shot at the target at a defined distance. 

The goal here is to take a look at the position of the arrow at each tx time and see what is its position.

The paradox implies that movement is impossible since the arrow is not moving when we look at it at a specific time. 

## Results 

#### Achilles and the turtle
When we run the python script we can see that Achilles, in the case of an infinite race, will always catch up to the turtle no matter the heads up since his speed is much faster and he will always cover more distance faster than the turtle. 

The gap between both of them will always be smaller and smaller until he reaches the turtle during the race. Unless we introduce an other variable that limits the distance Achilles can achieve in each step it is not possible for a gap between both racer to exist. 

#### The tree and the rock
In this case, while running the script we can see that the rock is getting closer and closer to the tree. According to the paradox the rock should never reach the tree but, if we look at the distance of the rock compared to the tree it will reach a distance so small that it will eventually reach the tree. 

`The rock is at 99.99999999999991 meters.`
`The rock is at 99.99999999999996 meters.`
`The rock is at 99.99999999999997 meters.`
`The rock is at 99.99999999999999 meters.`
`The rock is at 100.0 meters.`
`The rock hit the tree!`

Therefore, the rock reaches the tree and the paradox implying that it will never reach the tree is false. 

#### The target and arrow
 In this paradox we will use a simple python script that show the position of the arrow within each frame. We can see that the arrow moves from position a to position b to c etc. but within each frame its position is fixed since time is "stopped". 

But the arrow still moves from point a to z in order to reach the target. 
