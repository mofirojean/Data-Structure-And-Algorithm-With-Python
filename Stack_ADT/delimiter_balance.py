# Implementation of the algorithm for validating balanced brackets
# in a C++ and Java source file
from stack_linked_list import Stack


def isValidSource(srcfile):
    s = Stack()
    for line in srcfile:
        for char in line:
            if char in "{[(":
                s.push(char)
            elif char in "}])":
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (char == "}" and left != "{") or \
                            (char == "]" and left != "[") or \
                            (char == ")" and left != "("):
                        return False
    return s.isEmpty()


# Driver method
if __name__ == "__main__":
    with open("sample.java", "r") as javaFile, open("sample.cpp", "r") as cppFile:
        print("Testing the files if delimiters are now balanced")
        print("Testing a C++ file:", isValidSource(cppFile))
        print("Testing a Java file:", isValidSource(javaFile))
