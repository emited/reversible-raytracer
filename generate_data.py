import os
import numpy as np
from numpy.random import rand
from scene import *
from shader import *
from shape import *
import theano
from util import *

n = 100
x_dims = 32
y_dims = 32

# Generates n x_dims-by-y_dims image samples containing 2 spheres with
# randomly assigned centers. Saves the result in dataset.npz

if not os.path.exists('depth_dataset'):
    os.makedirs('depth_dataset')

material1 = Material((0.2, 0.9, 0.4), 0.3, 0.7, 0.5, 50.)
material2 = Material((0.87, 0.1, 0.507), 0.3, 0.9, 0.4, 50.)

center1 = theano.shared(np.asarray([-.5, -.5, 4], dtype=theano.config.floatX),
                        borrow=True)
center2 = theano.shared(np.asarray([.5, .5, 4], dtype=theano.config.floatX),
                        borrow=True)

shapes = [
    Sphere(translate(center1), material1)
    #, Sphere(translate(center2), material2)
]

light = Light((-1., -1., 2.), (0.961, 1., 0.87))
camera = Camera(x_dims, y_dims)
shader = DepthMapShader(6.1)
scene = Scene(shapes, [light], camera, shader)

image = scene.build()
render_fn = theano.function([], image, on_unused_input='ignore')

def random_transform(v):
    v.set_value(np.asarray([rand()*4-2, rand()*4-2, rand()*2+4], dtype=theano.config.floatX))

dataset = np.zeros((n, x_dims, y_dims), dtype=np.uint8)
for i in range(n):
    random_transform(center1)
    random_transform(center2)
    render = render_fn()[:, :, 0]
    dataset[i] = (render * 255).astype(np.uint8)
    draw('depth_dataset/%d.png' % (i,), render)

np.savez('dataset', dataset)


