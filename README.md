# project-4---Xiang-Li 

# Neural Style Transfer

* The whole idea of neural style transfer is to create a new image that has the mixed features from both original image and style image.

* The orginal research paper was published in 2015.
![Screenshot of paper](powerpoint/NST_theory.png)

* In the paper, the researchers create a customized model from 5 conv layers in the original vgg 19 model. (conv 1-1, 2-1, 3-1, 4-1, 5-1).
![Screenshot of layers](powerpoint/chosen_layers.png)

* It is quite easy to implement this in the code.
![Screenshot of code](powerpoint/custom_vgg.png)

* Before the training, we need some functions to process the images.
![Screenshot of code](powerpoint/img_process.png)

* The hyperparameter settings
![Screenshot of code](powerpoint/hp_settings.png)

* The idea of the training process is to reduce the difference between the generated image and the content image and the style image.
* To minimize the total loss, the generated image will be a better mix of both original and style image.
* Math function for guidance.
![Screenshot of math](powerpoint/total_loss_f.png)
* The code implementation
![Screenshot of code](powerpoint/nst_code.png)

* Some nice results!
![Screenshot of NST results](database/test/jp+f3.png)
![Screenshot of NST results](database/test/s12+f2.png)
![Screenshot of NST results](database/test/s11+f3.png)
![Screenshot of NST results](database/test/mel1+vg.png)
![Screenshot of NST results](database/test/s14+f5.png)

# Stable Diffusion Prompt Engineering through Web Application

* Stable Diffusion prompt engineering and demo through stable diffusion api.
* The version of the Stable Diffusion used here is v1.5 from huggingface.com.
* manual_seed(42) is used to control the testing result.
* DPMSolverMultistepScheduler from diffuser library is used to reduced the decoding looping from 50 to 25.
* AutoencoderKL is a variational autoencoder to improved the quality of the generated image.
![Screenshot of Stable Diffusion API](powerpoint/sd_code1.png)

* The text prompt is explained into three parts: the initial input, details, and cues.
* The intial input is a common description of the specific thing we want the model to generate.
* The details is the part where want the thing to be as specific as possible.
* The cues is the techinical specification of the generated image.
![Screenshot of Stable Diffusion API](powerpoint/sd_code2.png)

* An example of result after fine tuned the model.
![Screenshot of Stable Diffusion API](powerpoint/sd_example.png)

# Image interpolation with Stable Diffusion

* Testing Image interpolation with Stable Diffusion using two functions through its API.
* Slerp function: it works by finding the shortest path between two rotations on the surface of a sphere and interpolating between them2. This results in a smooth and natural transition between rotations, making it ideal for animations and camera movements2.
![Screenshot of code](powerpoint/slerp.png)
* Sin/cos 0 - 2pi transition, start by moving from 0 to 2π and at each step we add the cosine of x and the sine of y to the result. Using this approach, at the end of our movement we end up with the same noise values ​​that we started with.
![Screenshot of code](powerpoint/interpolation_code.png)
* Some test results.
![.gif of interpolation](database/test/manchit_interpolation1.gif)
![.gif of interpolation](database/test/manchit_interpolation2.gif)
![.gif of interpolation](database/test/test_interpolation1.gif)

# Neural Network training with MNIST dataset

* The dataset is in .csv format, so it is read by Pyspark.
![Screenshot of code](powerpoint/mnist1.png)
* Transfer the dataframe to pandas dataframe.
![Screenshot of code](powerpoint/mnist2.png)
* Change the datatype of the dataframe from object to float32.
![Screenshot of code](powerpoint/mnist3.png)
* Assign the X training set and Y label.
![Screenshot of code](powerpoint/mnist4.png)
* Transform the data and assign labels, and assemble the model.
![Screenshot of code](powerpoint/mnist5.png)
* Transform the data and assign labels, and assemble the model.
![Screenshot of code](powerpoint/mnist5.png)
* Reaching an accuracy of 95.8% which is lower than standard CNN models.
![Screenshot of code](powerpoint/mnist6.png)