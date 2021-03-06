import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num=X.shape[0]
  for i in range(num):
    scores=X[i].dot(W)
    corr_score=np.exp(scores[y[i]])
    sum_score=np.sum(np.exp(scores))
    loss+=-np.log(corr_score/sum_score)
    dW[:,y[i]]+=-X[i]
    for j in range(W.shape[1]):
      dW[:,j]+=(np.exp(scores[j])/sum_score)*X[i]
  loss=loss/num+reg*np.sum(W*W)
  dW/=num
  dW+=reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num=X.shape[0]
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores=X.dot(W)
  temp=np.arange(num)
  loss=-np.sum(np.log(np.exp(scores[temp,y]).reshape(num,1)/np.sum(np.exp(scores),axis=1).reshape(num,1)))/num+reg*np.sum(W*W)  
  sum_score=np.sum(np.exp(scores),axis=1).reshape(num,1)
  exp_score=np.exp(scores)
  score=exp_score/sum_score
  score[np.arange(num),y]-=1
  dW=X.T.dot(score)
  dW=dW/num+reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

