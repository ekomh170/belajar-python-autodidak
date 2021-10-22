import os, py_compile

def main():
	os.chdir("D:\\Python")
	py_compile.compile("compile-file.py")
	print("File Behasil Ke Compile Ke hello.pyc")
	os.system("pause");

if __name__ == "__main__":
	main()