MANAGER_PATH=/home/miguel/textual-features

### HOTEL
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin

### TRIPADVISOR
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin

### RELI
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin

### COMPUTERBR
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin

echo "ALL STEPS FINISHED" | telegram-send --stdin