# tensorflow_object_counting_api

#approach
i have used the tensorflow object detection api AND SSD_MOBILENETV2_COCO model.
The TensorFlow object detection API is the framework for creating a deep learning network that solves object detection problems.

# why chose this model
The ssd_mobilenet_v2_coco model is a Single-Shot multibox Detection (SSD) network intended to perform object detection. The model has been trained from the Common Objects in Context (COCO) image dataset.

The model input is a blob that consists of a single image of 1x3x300x300 in RGB order.

The model output is a typical vector containing the tracked object data, as previously described. Note that the "class_id" data is now significant and should be used to determine the classification for any detected object.

# what other model i would have used
pre-trained models in TF framework known as Model Zoo, which are trained with various architectures such as Resnet-50, Resnet -101 and Inception could have been used.

# why your current model is better than other models
Mobilenet model is a separable depth convolution based on a decomposable convolution operation. They decompose a standard convolution into a depth convolution and a 1 × 1 convolution called point convolution.
For mobilenets, deep convolution applies a single filter to each input channel. Then, point by point convolution applies 1 × 1 convolution to merge the output of deep convolution.

# output image
i have tried to upload the output images and file size is large.

