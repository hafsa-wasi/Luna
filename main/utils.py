#1.add upload to in models 2.below fnc    3.Media_root&url    4.Add url in urls.py
#manage static files in django in development



def post_directory_path(instance, filename):
    return 'id_{0}/{1}'.format(instance.id, filename)