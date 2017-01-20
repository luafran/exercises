import re
import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

pattern = re.compile("([^ ]+)@old.com")

for current_dir, directories, files in os.walk(walk_dir):
    # print('--\nroot = ' + current_dir)

    # for subdir in directories:
        # print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(current_dir, filename)
        file_path_bak = os.path.join(current_dir, filename, '.bak')

        print('-- file %s (full path: %s)' % (filename, file_path))

        with open(file_path, 'rb') as f:

            for i, line in enumerate(f.readlines()):
                line = line.rstrip('\n')

                # Find an replace
                replaced = re.sub(pattern, '\g<1>@new.com', line)
                print 'old %s: %s' % (i+1, line)
                print 'new %s: %s' % (i+1, replaced)

                # Find
                #for match in re.finditer(pattern, line):
                #    print 'Found on line %s: %s' % (i+1, match.group(0))

        print
