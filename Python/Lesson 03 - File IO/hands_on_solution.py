import os
from pathlib import Path

original_dir = os.getcwd()

# exercise 1
print(os.getcwd())
my_path = Path('.')
print(my_path)
print(Path.cwd())

# exercise 2
os.chdir("projects")
print(os.getcwd())
my_path = my_path / 'projects'

# exercise 3
print(os.listdir())
# for child in my_path.glob("*"):
    # print(child)

# exercise 4
os.mkdir('data')
print(os.listdir())
(my_path / 'data').mkdir()
# for child in my_path.glob("*"):
    # print(child)

# exercise 5
os.makedirs('a/b/c')
print(os.listdir('a'))
# (my_path / 'a' / 'b' / 'c').mkdir(parents=True, exist_ok=True)

# exercise 6
os.chdir(original_dir)
os.remove('temp.txt')
print(os.listdir())
# (my_path / 'temp.txt').unlink()

# exercise 7
os.removedirs('old_data')
print(os.listdir())
# (my_path / 'old_data').rmdir()

# exercise 8
os.rename('example.txt', 'renamed_example.txt')
# (my_path / 'example.txt').rename('renamed_example.txt')

# exercise 9
print(os.path.isdir('target'))
# (my_path / 'target').is_dir()
