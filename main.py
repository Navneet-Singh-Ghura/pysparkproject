# initialize git, letting git know to manage the folder
git init

#add all the files 
git add .
git commit -m "Load project to Github from local"

# create repo in github and run below command
git remote add origin https://github.com/Navneet-Singh-Ghura/pysparkproject.git

#check origin 
git remote -v

#check branch name 
git branch 

#change branch name 
git branch -M main

#sync files in github to local
git rebase origin main

#push local files to github
git push --set-upstream origin main
