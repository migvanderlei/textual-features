MANAGER_PATH=/home/miguel/textual-features

### TRIPADVISOR
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin

### RELI
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf lr -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf rf -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin

### COMPUTERBR
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf lr -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf rf -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin

### HOTEL
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf lr -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf rf -j 6 -i 1000 -v 0 --group 8 | telegram-send --stdin

echo "ALL STEPS FINISHED" | telegram-send --stdin