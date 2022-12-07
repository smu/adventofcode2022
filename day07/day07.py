#!/usr/bin/env python3

import sys
import re


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.childs = []
        self.files = []
        self.size = 0

    def full_path(self):
        path = self.name
        if self.parent:
            path = "%s/%s" % (self.parent.full_path(), path)
        return(path)

    def add_file(self, f):
        if f.name not in [ff.name for ff in self.files]:
            self.files.append(f)

    def get_child_names(self):
        return([c.name for c in self.childs])

    def get_child(self, name):
        for c in self.childs:
            if c.name == name:
                return(c)
        child = Dir(name, self)
        self.childs.append(child)
        return(child)
        

    def add_child(self, name):
        if name not in self.get_child_names():
            child = Dir(name, self)
            self.childs.append(child)
            print("Child %s created" % name)
        else:
            print("Child %s exists" % name)

    def calc_size(self):
        self.size = 0
        for c in self.childs:
            c.calc_size()
            self.size += c.size
        for f in self.files:
            self.size += f.size

    def get_total_size(self, limit):
        total_size = 0
        if self.size <= limit:
            print("++ %s [%d]" % (self.full_path(), self.size))
            total_size += self.size
        else:
            print("-- %s [%d]" % (self.full_path(), self.size))
        for c in self.childs:
            subdir_size = c.get_total_size(limit)
            # subdir_size = c.size
            if subdir_size == 0:
                continue
            if subdir_size <= limit:
                total_size += subdir_size
        return(total_size)

    def print_directory_structure(self,):
        print("%s [%d]" % (self.full_path(), self.size))
        for f in self.files:
            print("F: %s/%s [%d]" % (self.full_path(), f.name, f.size))
        for c in self.childs:
            c.print_directory_structure()
        

cmd_re = re.compile("^\$")
cd_cmd_re = re.compile("^\$ cd (.*)")
dir_info_re = re.compile("^dir (.*)")


root = Dir("/", None)
current_dir = None

with open("input") as f:
    for line in f.readlines():
        line = line.strip()
        if re.match(cmd_re, line):
            print("cmd: %s" % line)
            if re.match(cd_cmd_re, line):
                target_dir = cd_cmd_re.findall(line)[0]
                if target_dir == "/":
                    current_dir = root
                elif not re.match("/", target_dir):
                    if target_dir == "..":
                        current_dir = current_dir.parent
                    else:
                        # not / in path. target_dir is direct subdirectory
                        current_dir = current_dir.get_child(target_dir)
                else:
                    print(line)
                    sys.exit()
        else:
            print("---: %s" % line)
            if re.match(dir_info_re, line):
                child_dir_name = dir_info_re.findall(line)[0]
                #print("child dir: %s" % child_dir_name)
                current_dir.add_child(child_dir_name)
            else :
                size, file_name = line.split(" ")
                #print("file info: %s :: %s" % (file_name, size))
                f = File(file_name, size)
                current_dir.add_file(f)
        
root.calc_size()
# root.print_directory_structure()
    
print("----------------------------------")
print()
print(root.get_total_size(100000))

# first guess 144228, wrong
# first guess 144230, wrong