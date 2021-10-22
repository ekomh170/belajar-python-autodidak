import os, compileall

def main():
	dir = "D:\\Python"
	compileall.compile_dir(dir)
	print("semua file dalam %s telah dikompalisi" % dir)
	os.system("pause");

if __name__ == "__main__":
	main()	