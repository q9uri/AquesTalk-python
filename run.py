import argparse
from pathlib import Path
import aquestalk

SPEAKER_LIST = ["dvd", "f1", "f2", "imd1", "jgr", "m1", "m2", "r1"]

def main(parser):


    args = parser.parse_args()

    aq = aquestalk.load(args.speaker)
    aq.synthe(args.out_file, args.kana_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='aquestalk-cli: old aquestalk-cli') 
    parser.add_argument('out_file', help='出力ファイルのパス）')    # 必須の引数を追加
    parser.add_argument('kana_text', help='aquestalk記法のテキスト')
    parser.add_argument('speaker', choices=SPEAKER_LIST,help='aquestalkの話者')
    main(parser)