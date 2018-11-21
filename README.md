# IVote_Backend

1. Install latest version of Anaconda from [Anaconda Download page](https://www.anaconda.com/download/)

1. Create a new Conda environment by following the below steps:
	+ To create an environment:<br>
		`conda create --name myenv`<br>
		NOTE: Replace `myenv` with the environment name.<br>
	+ When conda asks you to proceed, type `y`:<br>
		`proceed ([y]/n)?`<br>
	This creates the myenv environment in `/envs/`. This environment uses the same version of Python that you are currently using, because you 		did not specify a version.
	
1. Now activate the environment. To activate an environment:
	+ On Windows, in your Anaconda Prompt, run `activate myenv`
	+ On macOS and Linux, in your Terminal Window, run `source activate myenv`
	
1. Now install some packages for using opencv:

	1. `pip install numpy scipy matplotlib scikit-learn jupyter`
	1. `pip install opencv-contrib-python`
	1. `pip install dlib`
	1. `pip install pillow`
	
1. Clone the repository `git clone https://github.com/goyalritesh21/IVote_Backend.git`

1. Change directory `cd IVote_Backend`

1. Run `collect_training_data.py` on python command prompt. This will open camera to collect training data for a face. 
NOTE: Keep only face in frame while collecting data.

1. Run `classifier.py` on python command prompt. This will train the model for the faces.
 
1. Run `face_detection.py` on python command prompt. This will open camera and tells about the detected face.
