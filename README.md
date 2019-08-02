# Blob Tracker - ROS Perception

This repo contians a Python script that retrieves the needed information from the  **/blob**  topic to be able to:

-   Filter all the blobs, except the RedBall blobs.
-   Retrieve its position in 2D in the image.
-   Publish a Twist message into the topic named  _/mira/commands/velocity_, which will be used to move Mira's head to follow the red ball around in the 2D space.

