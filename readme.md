Welcome to the Documentation of our Technophobe project!

Aim of the project: create a database of zoo animals, function, and api endpoint to manipulate this database.

Files:
- model.py: here you find the different classes: specimen, species and genus. Genus is the parent of species, which is the parent of specimen. Use these classes when you want to create a new entry in the database for example. 
- import_functions.py: here we have the functions that are needed to add the data to our database. 
- data.py: in this file we have some data and we use the functions created in import_functions file to add the data to our database.  
- api.py: here we keep all the different apis. 

Definition of Done (Dod):
A Dod is a set of rules that we agree upon for optimal collaboration and making sure that we keep a high code quality. These are the following rules:
- once an issue is created, one person works on it on a separate branche. When they are done, they create a pull request to merge to master. 
- someone else reviews the code and merges it to master. 
- tests have been created if possible

