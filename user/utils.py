#1.add upload to in models 2.below fnc    3.Media_root&url    4.Add url in urls.py
#manage static files in django in development



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)