"""Contains the TS model definition."""

import tensorflow as tf
import tensorflow.contrib as tfc

import s_input


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('batch_size', 1,
                            """Number of images to process in a batch.""")

# Global constants describing the data set.
NUM_CLASSES = s_input.NUMBER_CLASSES
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = s_input.NUM_EXAMPLES_PER_EPOCH_TRAIN

# Constants describing the training process.
MOVING_AVERAGE_DECAY = 0.9999       # The decay to use for the moving average.
NUM_EPOCHS_PER_DECAY = 9.0          # Number of epochs after which learning rate decays.
LEARNING_RATE_DECAY_FACTOR = 0.6    # Learning rate decay factor.
INITIAL_LEARNING_RATE = 0.1         # Initial learning rate.


def inference(sequence, seq_len):
    """Build the TS model.
    # review Documentation

    Args:
        seq_len ():
        sequence ():

    Returns:
        logits: Softmax layer pre activation function, i.e. layer(XW + b)
    """
    num_hidden = 128
    print('inference:', sequence, seq_len)
    # LSTM cells
    with tf.variable_scope('lstm'):
        # cell = tf.nn.rnn_cell.LSTMCell(num_units=128, state_is_tuple=True)    # review: test this
        cell = tfc.rnn.LSTMCell(num_units=num_hidden, state_is_tuple=True)
        num_layers = 1
        # stack = tf.nn.rnn_cell.MultiRNNCell([cell] * num_layers, state_is_tuple=True)  # review
        stack = tfc.rnn.MultiRNNCell([cell] * num_layers, state_is_tuple=True)
        # The second output is the last hidden state, it's not required anymore.
        cell_out, _ = tf.nn.dynamic_rnn(stack, sequence, seq_len, dtype=tf.float32)

        print('cell_out:', cell_out)
        cell_out = tf.reshape(cell_out, [-1, num_hidden])
        print('cell_out.reshape:', cell_out)

    # linear layer(XW + b),
    # We don't apply softmax here because
    # tf.nn.sparse_softmax_cross_entropy_with_logits accepts the unscaled logits
    # and performs the softmax internally for efficiency.
    with tf.variable_scope('softmax_linear') as scope:
        weights = _variable_with_weight_decay('weights', [num_hidden, NUM_CLASSES], 0.04, 0.004)
        biases = _variable_on_cpu('biases', [NUM_CLASSES], tf.constant_initializer(0.0))
        softmax_linear = tf.add(tf.matmul(cell_out, weights), biases, name=scope.name)
        # _activation_summary(softmax_linear)

    return softmax_linear


def loss(logits, labels):
    """Add L2Loss to all the trainable variables.

    Args:
        logits: Logits from inference().
        labels: Labels from inputs_train or inputs().
                A 1D tensor of shape [batch_size].

    Returns:
        Loss tensor of tf.float32 type.
    """
    # Calculate the average cross entropy loss across the batch.
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
        labels=labels, logits=logits, name='cross_entropy_per_example')
    cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
    tf.add_to_collection('losses', cross_entropy_mean)

    # The total loss is defined as the cross entropy loss plus all of the weight
    # decay terms (L2 loss).
    total_loss = tf.add_n(tf.get_collection('losses'), name='total_loss')
    # total_loss = tf.Print(total_loss, [total_loss], message="total_loss_print")

    return total_loss


def train(total_loss, global_step):
    """Train the TS model.

    Create an optimizer and apply to all trainable variables. Add moving
    average for all trainable variables.

    Args:
        total_loss: Total loss from the loss() function.
        global_step: Variable counting the number of training steps processed.

    Returns:
        train_op: Operator for training.
    """
    # Variables that affect learning rate.
    num_batches_per_epoch = NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN / FLAGS.batch_size
    decay_steps = int(num_batches_per_epoch * NUM_EPOCHS_PER_DECAY)

    # Decay the learning rate exponentially based on the number of steps.
    lr = tf.train.exponential_decay(INITIAL_LEARNING_RATE,
                                    global_step,
                                    decay_steps,
                                    LEARNING_RATE_DECAY_FACTOR,
                                    staircase=True)
    tf.summary.scalar('learning_rate', lr)

    # Generate moving averages of all losses and associated summaries.
    loss_averages_op = _add_loss_summaries(total_loss)

    # Compute gradients.
    with tf.control_dependencies([loss_averages_op]):
        optimizer = tf.train.GradientDescentOptimizer(lr)
        grads = optimizer.compute_gradients(total_loss)

    # Apply gradients.
    apply_gradients_op = optimizer.apply_gradients(grads, global_step=global_step)

    # L8ER Disabled summaries.
    # Add histograms for trainable variables.
    for var in tf.trainable_variables():
        # tf.summary.histogram(var.op.name, var)
        pass

    # Add histograms for gradients.
    for grad, var in grads:
        if grad is not None:
            # tf.summary.histogram(var.op.name + '/gradients', grad)
            pass

    # Track the moving averages of all trainable variables.
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variables_averages_op = variable_averages.apply(tf.trainable_variables())

    with tf.control_dependencies([apply_gradients_op, variables_averages_op]):
        train_op = tf.no_op(name='train')

    return train_op


def inputs_train():
    """Construct modified input for the TS training.
    review Documentation

    Returns:
        samples: Image 4D tensor of [batch_size, width, height, channels] size.
        labels: Labels 1D tensor of [batch_size] size.
    """
    sequences, seq_len, labels = s_input.inputs_train(FLAGS.batch_size)
    return sequences, seq_len, labels


def inputs():
    # L8ER: Write according to `inputs_train`.
    raise NotImplementedError


def _add_loss_summaries(total_loss):
    """Add summaries for losses in the TS model.

    Generates moving average for all losses and associated summaries for
    visualizing the performance of the network.

    Args:
        total_loss: Total loss from the loss() function.

    Returns:
        loss_average_op: Op for generating moving averages of losses.
    """
    # Compute the moving average of all individual losses and the total loss.
    loss_averages = tf.train.ExponentialMovingAverage(0.9, name='avg')
    losses = tf.get_collection('losses')
    loss_averages_op = loss_averages.apply(losses + [total_loss])

    # Attach a scalar summary to all individual losses and the total loss;
    # do the same for the averaged version of the losses.
    for l in losses + [total_loss]:
        # Name each loss as '__raw_' and name the moving average version of the
        # loss as the original loss name.
        tf.summary.scalar(l.op.name + '__raw_', l)
        tf.summary.scalar(l.op.name, loss_averages.average(l))

    return loss_averages_op


def _activation_summary(x):
    """Helper to create summaries for activations.

    Creates a summary that provides a histogram of activations.
    Creates a summary that measures the sparsity of activations.

    Args:
        x: Tensor

    Returns:
        nothing
    """
    tensor_name = x.op.name
    tf.summary.histogram(tensor_name + '/activations', x)
    tf.summary.scalar(tensor_name + '/sparsity', tf.nn.zero_fraction(x))


def _variable_on_cpu(name, shape, initializer):
    """Helper to create a variable stored on CPU memory.

    Args:
        name (str): Name of the variable.
        shape (list of int): List of ints, e.g. a numpy shape.
        initializer: Initializer for the variable.

    Returns:
        Variable tensor.
    """
    with tf.device('/cpu:0'):
        return tf.get_variable(name, shape, initializer=initializer, dtype=tf.float32)


def _variable_with_weight_decay(name, shape, stddev, weight_decay):
    """Helper to create an initialized variable with weight decay.

    Note that the variable is initialized with a truncated normal distribution.
    A weight decay is added only if one is specified.

    Args:
        name (str): Name of the variable.
        shape (list of int): List of ints, e.g. a numpy shape.
        stddev (float): Standard deviation of the Gaussian.
        weight_decay: Add L2Loss weight decay multiplied by this float.
            If None, weight decay is not added for this variable.

    Returns:
        Variable tensor.
    """
    var = _variable_on_cpu(name, shape,
                           tf.truncated_normal_initializer(stddev=stddev, dtype=tf.float32))
    if weight_decay is not None:
        wd = tf.multiply(tf.nn.l2_loss(var), weight_decay, name='weight_loss')
        tf.add_to_collection('losses', wd)
    return var
