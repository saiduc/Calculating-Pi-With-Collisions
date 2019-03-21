# Calculating &pi; with Colliding Blocks

A pretty elegant but terribly inefficient method of calculating &pi;. This was inspired by 3Blue1Brown's video on the topic. This was just something I was playing around with since I was so impressed that &pi; could be calculated in this way and I wanted to see it for myself.

The general idea is that if you have two blocks, with a wall on one end of the two blocks, &pi; can be calculated by colliding one block with the other and counting the total number of collisions before the two blocks never collide again. I link the video in the Acknowledgements section and I recommend you check it out, it is very interesting.

While this method is really cool, it is a pretty slow way of calculating &pi; and quickly slows down for greater precision.

## Usage
Just run the picalc.py file in whichever way you normally run python files, with a run time argument that specifies the number of decimal places you want. For example, to get &pi; to 2 decimal places:
```
python3 picalc.py 2
``` 

## Requirements
* Python 3 (should also work in Python 2)

## Some Notes on What I Learned
All the physics behind the code is just fairly simple A-level Maths so it wasn't hard to work out. It was a pain to implement however, since Python kept having problems with float variables. Sometimes, floats would truncate and there would be problems with comparison checks. So I opted to use the Fractions data type instead, as recommended by a StackOverflow answer.

The whole thing didn't require me to learn anything new besides learning how floats work exactly in Python, but it was still a really fun little project.

## License
This project is licensed under the terms of the MIT license. Do whatever you want with it!

## Acknowledgements

* The 3Blue1Brown video that inspired this: https://www.youtube.com/watch?v=HEfHFsfGXjs
* The original paper by Gregory Galperin: https://www.maths.tcd.ie/~lebed/Galperin.%20Playing%20pool%20with%20pi.pdf
