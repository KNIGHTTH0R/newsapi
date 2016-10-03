import os, sys
import mmap



def main():
	if len(sys.argv) < 3:
		FOLDER = "/"
		TERM = "test"
	else:
		FOLDER = sys.argv[1]
		TERM = sys.argv[2]
	# for root, dirs, files in os.walk(FOLDER):
		# for file in files:
	for file in os.listdir(FOLDER):
		if file.endswith(".py"):
			with open(os.path.join(FOLDER, file), 'r') as file:
				found = False
				try:
					s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
					if s.find(TERM) != -1:
						print "FOUND IT in ", file.name
				except ValueError:
					print "oops"
			file.close()

if __name__ == "__main__":
	main()