# rock_classifier
This is my first ML project, a VERY simple rock type classifier application.
I made it for fun and it *might* be helpful for those working in the petrology field for a quick overall analysis of a rock sample.
I will update this app for new rock types & .exe file soon. 

  # Libraries used:
 - pandas
 - scikit-learn
 - tkinter
 - joblib
 - numpy
   

  # How to Use

  - Download all the files and place them in the same folder
  - Open the folder in VSCode (or a different code interpreter) and run the rock-classifier-gui.py file (make sure you have installed all of the libraries above)
    
  - Enter chemical composition values (%) for: SiO₂, Al₂O₃, FeO, MgO, CaO
  - Click the "Classify" button

The predicted rock type will be shown below

Note: If the sample is not a perfect match, the model returns the nearest known type based on training data.





  # Model Details:

Algorithm: K-Nearest Neighbors (k=1)

Input features: SiO₂, Al₂O₃, FeO, MgO, CaO

Classes: Granite, Basalt, Rhyolite, Sandstone, Limestone, Mudstone, Marble, Gneiss, Phyllite

  # Author
  Monika (Moonrien)
  [GitHub](https://github.com/moonrien)
