# python /home/miguel/PycharmProjects/textual-features/manager.py --extract -d tripadvisor | telegram-send --stdin
# python /home/miguel/PycharmProjects/textual-features/manager.py --extract -d reli | telegram-send --stdin
# python /home/miguel/PycharmProjects/textual-features/manager.py --extract -d computerbr | telegram-send --stdin
python /home/miguel/PycharmProjects/textual-features/manager.py --randomsearch -d tripadvisor --clf svm -j 6 -i 200 -v 0 | telegram-send --stdin
