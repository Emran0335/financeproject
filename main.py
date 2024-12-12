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
# git reset <commitNumber>(git log)
# it will go back to the previous commit. but the code not changed.
# git log
# It will help us to get the commitNumber
# git reset --hard <commitNumber>
# It will go back to the previous commit and the code will also be removed from the working directory.
# git checkout -b feature1
# this command will not work as feature1 is already created
# so, git checkout feature1 is enough to switch to the branch
# git checkout -b feature3 feature2
# Though I am on the main branch, but feature3 will not created 
# based on main, rather it will all code from feature2
# as we have explicitly mention feature2
# git pull origin main
# -> it will fetch all codes from the origin main branch to the local working directory.
# git restore <filename>
# You made changes which are not even staged. so, restore them
# git restore --staged <filename>
# git reset <hashNumber>
# It will get you back
# made changes and have staged those changes. so, get them back.
# git reset --hard <commithistory>
# made changes and have committed those changes. so, get them back
# git log 
# to show the hash value
# git reset head~1
# It will also get you back to the previous commind
# fork - get a copy of the code from some other github account to your account
# fort the project so that a copy of that project is created in your github repository.