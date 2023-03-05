# Scope
# 

# Global scope
x = 1

def f():
    # Local scope
    y = 2
    print(y) # 2
    print(x) # 1 # global scope is accessible from local scope

f()
print(x) # 1
# print(y) # NameError: name 'y' is not defined # local scope is not accessible from global scope => block scope => scope is defined by indentation (not by {}) => can look outside the scope but not inside


