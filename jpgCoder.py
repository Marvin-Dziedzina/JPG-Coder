import os
from typing import ByteString
import PIL.Image
import io


def clear():
    return os.system('cls')


# Write sector
def writingText():
    try:
        with open("input.jpg", "ab") as f:
            a = input("Waht you want to write in: ")
            f.write(bytes(a, "utf-8"))

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def writingPicture():
    try:
        img = PIL.Image.open("append.png")

        byte_arr = io.BytesIO()
        img.save(byte_arr, format="PNG")

        with open("input.jpg", "ab") as f:
            f.write(byte_arr.getvalue())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def writingExecutable():
    try:
        a = input("File name: ")

        if (a == ""):
            a = "append.exe"

        with open("input.jpg", "ab") as f, open(a, "rb") as e:
            f.write(e.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def readMsi():
    try:
        a = input("File name: ")

        if (a == ""):
            a = "append.msi"

        with open("input.jpg", "ab") as f, open(a, "rb") as e:
            f.write(e.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def writingZip():
    try:
        a = input("File name: ")
        with open("input.jpg", "ab") as f, open(a, "rb") as e:
            f.write(e.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def writingMp4():
    try:
        with open("input.jpg", "ab") as f, open("append.mp4", "rb") as e:
            f.write(e.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def writingMp3():
    try:
        with open("input.jpg", "ab") as f, open("append.mp3", "rb") as e:
            f.write(e.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


# Read sector
def readText():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)
            clear()
            print(f.read())
            print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def readPicture():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)

            new_img = PIL.Image.open(io.BytesIO(f.read()))
            new_img.save("output.png")

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def readExecutable():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)

            with open("hiddenInstaller.exe", "wb") as e:
                e.write(f.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def writingMsi():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)

            with open("hiddenInstaller.msi", "wb") as e:
                e.write(f.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def readingZip():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)

            with open("hiddenZipFile.zip", "wb") as e:
                e.write(f.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def readMp4():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)

            with open("hiddenMp4File.mp4", "wb") as e:
                e.write(f.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def readMp3():
    try:
        with open("input.jpg", "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)

            with open("hiddenMp3File.mp4", "wb") as e:
                e.write(f.read())

        clear()
        print("Finished")
    except Exception as e:
        print()
        print(f"Error: {e}")
        input("Press enter to close")
        quit()


def main():
    print()
    print("Type first 'w' for writing or 'r' for reading.")
    print("Type space " " for argument seperation.")
    print("Now you choose waht type of stuff you want to hide / show in your image.")
    print("Type 'text' for text, 'png' for picture (just .png) and 'exe' for executable (just .exe) and 'msi' for msi (just .msi) and 'zip' for ZIP (just .zip) and 'mp4' for mp4 (just .mp4) and 'mp3' for mp3 (just .mp3).")
    print("Make shure your carrier image has the name 'input.jpg' and your appending file has the name 'append.png'.")

    print()

    answer = input("Waht you want: ")
    print()
    answer = answer.lower()
    answer = answer.split(" ")

    if (answer[0] == "w"):
        if (answer[1] == "text"):
            writingText()
        elif (answer[1] == "png"):
            writingPicture()
        elif (answer[1] == "exe"):
            writingExecutable()
        elif (answer[1] == "msi"):
            writingMsi()
        elif (answer[1] == "zip"):
            writingZip()
        elif (answer[1] == "mp4"):
            writingMp4()
        elif (answer[1] == "mp3"):
            writingMp3()
    elif (answer[0] == "r"):
        if (answer[1] == "text"):
            readText()
        elif (answer[1] == "png"):
            readPicture()
        elif (answer[1] == "exe"):
            readExecutable()
        elif (answer[1] == "msi"):
            readMsi()
        elif (answer[1] == "zip"):
            readingZip()
        elif (answer[1] == "mp4"):
            readMp4()
        elif (answer[1] == "mp3"):
            readMp3()


main()
