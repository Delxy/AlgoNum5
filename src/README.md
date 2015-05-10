===============================================================================
Interpolation and integration methods / Cubic splines and surface interpolation 
===============================================================================

First, the sources are splitted in 3 files:
       - part1.py contains functions which load the airfoil, compute the cubic spline interpolation and draw the interpolated curves.
       - part2.py contains functions which compute the derivative of a function, "intègre" a funtion as an array, and compute the length of a curves.
       - part3.py contains the main function which compute the pressure map arround an airfoil. There is two example in the file.
       	 To use it: execute whith this syntax : compute_presure(the_name_of_file_which_contain_the_arfoil_data, the_number_of_slice_you_want, the_integration_methode_you_want_to_use)
       	 /!/ The airfoil file must contain ONLY data about extrados and intrados. Sometimes there is two line which make the parser load_foil unefficienly.


Students: Alice Milliet
	  Romain Petro
	  Henri Toussaint
	  Clara Broc
	  Pierre Meyzen