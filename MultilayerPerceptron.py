from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import sonnet as snt 
import numpy as np 
#------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------#

train_data = tf.convert_to_tensor(np.matrix[[1,2],[3,4]], dtype=np.int32)
test_data =

linear_to_hidden = snt.Linear(output_size = 50 , name ='inp_to_hidden')
hidden_to_out = snt.Linear(output_size = 25, name = 'hidden_to_out')

#Sequential is a module wich applies a number of inner ops in sequence to data 
#We can put another activation function like tf.tahn or tf.nn.relu 
mlp = snt.Sequential([linear_to_hidden, tf.sigmoid, hidden_to_out])

train_predictions = mlp(train_data)
test_predictions = mlp(test_data)
