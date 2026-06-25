def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))
for i in range (n):
    print(fibonacci(i),end=" ")
# git config --global user.email "ajibunaji2@gmail.com"
# git config --global user.name "shaikajibun"    
# git add .                                                        
# git commit -m "add the new files "
# git push
git config --global user.email "ajibunaji2@gmail.com"
git config --global user.name "shaikajibun" 
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/shaikajibun/CRT-DSA-python.git
git push -u origin main