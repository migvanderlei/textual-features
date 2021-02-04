MANAGER_PATH=/home/miguel/PycharmProjects/textual-features

python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 2 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 2 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 2 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 2 -i 1000 -v 0 | telegram-send --stdin
