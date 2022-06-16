class User():
    def __init__(self,name):
        self.islogged = False
        self.name = name

def authetication_decorator(function):
    def wrapper(*args):
        if args[0].islogged == True:
            function(args[0])
    return wrapper

#
@authetication_decorator
def blog_post(user):
    print(f"this is {user.name}'s first blog")

new_user = User('Deepika')
new_user.islogged = True
blog_post(new_user)
