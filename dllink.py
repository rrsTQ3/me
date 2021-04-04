import os


def main():
    path = "C:\Users\saina\Desktop\devMemes\assets\gitmeme\me"

    count = 1

    for root, dirs, files in os.walk(path):
        for i in files:
	    print(i)

            #os.rename(os.path.join(root, i), os.path.join(root, "changed" + str(count) + ".txt"))

            count += 1


if __name__ == '__main__':
    main()