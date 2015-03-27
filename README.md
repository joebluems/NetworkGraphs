# NetworkGraphs
Building network graphs from popular movie screenplays


If you have downloaded Gephi (0.8.1 beta version) you can read the finished product directly.
Download Gephi @ http://gephi.github.io.


If you'd prefer to create the edge files, use the Pyton script (which reads the screenplay), which writes the edge pairs to stdout...

./read_batman.py > batman.csv

./read_wizard.py > wizard.csv

./read_godfather.py > godfather.csv

Point Gephi (or another visualization tool) at the edge files and follow instructions for displaying the network (rotation, size, colors, modality, etc.)

If you want to try another movie, I recommend you find an HTML version (rather than PDF) with a format similar to the versions used here. It works better if there are obvious scene markers and character names appearing on a separate line. Otherwise, you will have to derive a bespoke version of the edge extraction.
