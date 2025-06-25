git init
git add .
git commit -m "Load project to Github from local"

git remote add origin https://github.com/Navneet-Singh-Ghura/pysparkproject.git
git remote -v
git branch 
git branch -M main
git rebase origin main
git push --set-upstream origin main
