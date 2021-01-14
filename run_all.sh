MANAGER_PATH=/home/miguel/PycharmProjects/textual-features

python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 6 -i 1000 -v 0 | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf lr -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf rf -j 6 -i 1000 -v 0 | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf lr -j 6 -i 1000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf rf -j 6 -i 1000 -v 0 | telegram-send --stdin
