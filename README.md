# Image-Processing-Coursework
A record of the Image Processing assignment completed in year 2 of my undergraduate degree.

How to run document from terminal 

ImageProcessingProject.py takes two arguments:
	the video path with the -d flag and the directory which contains the images that will be converted to video format -r
	
The python program assumes this is the layout of the file:
	-d = contained within working directory and has the images that need to processed
	-r = contained within working directory and contains a directory named "vout" which will contain the video output of the processed images

	layout of results directory after the code is run:
		vout - directory
		processed images
The program will return errors if there is no vout file in the folder where the processed images are and the images cannot be in the same folder as any other type of 
files that are not images meant to be processed.

		
This assignment, given by the Department of Computer Science at Durham University, pertains to the field of Image Processing and involves several tasks, primarily focused on enhancing the quality of corrupted images, evaluating the enhancements, and observing their impact on the performance of an object detection system (specifically, YOLO).

Here's a breakdown of the assignment:

Resources Provided:

Compressed videos of corrupted validation images, ground truth validation images, and corrupted test images.
Two Python scripts: yolo.py for object detection and compare_images.py for comparing images using specific metrics.
Objective:

Enhance the quality of the provided corrupted images by removing noise, adjusting contrast and brightness, and correcting any warping.
Utilize the YOLO script to observe the impact of your image enhancements on object detection performance.
Compare your enhanced images against the ground truth using the compare_images.py script.
Hints:

The corrupted images have altered perspectives due to warping.
Multiple types of noise are present in the corrupted images.
Contrast and brightness of images are also affected.
Students are encouraged to explore beyond the techniques covered in lectures.
Code Specifications:

The program must operate with OpenCV 4.1.x.
Must contain a setting for specifying a directory of images to be processed.
Should save enhanced images in a 'results' directory without altering original filenames.
Must not use any object detection methods other than the provided YOLO implementation.
Noise removal, contrast adjustment, and dewarping should be separate functions within the code.
Submission Requirements:

Source code and required files.
“Results” directory containing enhanced test images.
Video file showing YOLO’s performance on your test results.
A report (max. 750 words) detailing your approach, successes, and evidence of performance.
Marks Distribution:

20% for noise removal.
15% for improving contrast and brightness.
15% for dewarping images.
10% for the performance of YOLO on enhanced images.
5% for clarity and presentation of source code.
25% for the report's content and evidence of performance.
Up to 15% extra credit for novel methods, advanced processing, or significant improvements in object detection performance.
Plagiarism Warning:

Students must avoid plagiarism.
Usage of code from provided examples or other sources must be acknowledged.
Automated tools will be used to detect code plagiarism, including comparisons against past submissions.
Submission Method:

Compile required files in a directory named after the student’s username, compress it into a ZIP file, and submit it via the designated platform (Ultra).
Deadline: 2pm (UK time) on 3rd February 2022.
This assignment challenges students to apply their knowledge of image processing to improve the quality of corrupted images and to understand the real-world implications of these improvements on tasks like object detection. It also emphasizes the importance of originality in coding and thorough documentation in scientific research and development.
