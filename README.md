# Reversible Ray Tracer
The Reversible Ray Tracer (RRT) is a program that takes a description of a 3D scene and outputs a picture of the scene. But it doesn’t end there. Say what you want to change about the output and RRT can backtrack to the inputs and update them to bring about the intended change.

The optimization works by gradient descent (or ascent). Here’s the algorithm:

1. Define a loss function on the output.

2. Move through the input parameter space in proportion to the gradient of the loss function w.r.t. each input parameter. At each iteration:

  1. Calculate the partial derivative of the loss w.r.t. each input parameter.
  2. Update each input parameter proportionally to the gradient.

3. Continue until the loss stops improving much.

Todo:
* ~~Ray intersection with a sphere~~
* ~~Lambertian shading~~
* ~~Gradient descent optimization to maximize brightness at a point in the output~~
* Support for multiple objects
* Shadows
* Color
* Phong shading
* UI for selecting/defining a loss function
* Ability to lock parameters before optimization
