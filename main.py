# This is the python main file.

# This is from feature1 branch;

# git branch -> to check branch;
# git branch feature1 -> to create branch;
# git branch -M main(to rename a brach name) 
# - means to switch to main branch)
# git checkout feature1 -> to switch to feature1
# created branch will copy the code of branch from where we are creating the branch;

# git checkout -b feature2
# it will checkout feature2 and create featue2 if it is not found.

# git checkout -b feature3 feature2
# this command will create feature3 taking all code  of feature2.
# which branch we are currently working on.

# let me create another feature4 branch based on feature3
# git checkout -b feature4 feature3
# Now I want to delete feature4
# git branch -d feature4
# so, if we want to delete branch, we need to switch antoher branch
# otherwise, it will let us delete the current branch;

# git checkout -b feature1
# this command will not work as feature1 is already created
# so, git checkout feature1 is enough to switch to the branch
# git checkout -b feature3 feature2
# Though I am on the main branch, but feature3 will not created 
# based on main, rather it will all code from feature2
# as we have explicitly mention feature2


# git pull origin main
# -> it will fetch all codes from the origin main branch to the local working directory.
