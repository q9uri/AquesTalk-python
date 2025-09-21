
from pathlib import Path
import aquestalk

def main():
    aq = aquestalk.load("f1")
    aq.synthe('output.wav', "オイオイレイムサンヤ")

if __name__ == "__main__":
    main()