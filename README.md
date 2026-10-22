# Machine-Learning
1) Linear Regression
this is my first attempt at ML and as so its not of the highest quality, however "the treasure is the friends we made long the way". This model uses gradient descent to find a x value (weight) that gives the smallest possible value when you plug it into the loss function's derivative, and then SUBSTRACTS the weight EXCULSIVELY (im 99.99% sure of that) because im pretty sure you cant get a negative slope somewhere without the thingy being a cubic, mines a quadratic, also, for whatever reason, at least for the one specific test case I tested it on, it likes to go to an x value that makes the y value 16 thousand more then it actually is. In doing this project, I'd gained a lot of insight into the world of ML, how not everything has to be derived from a rigorous maths proof such as `self.weight -= self.learning_rate * slope` but just by intuition and logic, I also learnt that my mastery of calculus was embarrassingly low, and what the fancy videos on the internet were actually showing, it only goes up and gets harder from here
- 21/10/2026

  23/10/2026
  Added a bias (c term in y = mx + c) and improved the code to reach about 98-99.9% accuracy after running 10 million training cases, planning for 3d version soon
