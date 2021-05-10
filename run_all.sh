MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### TRIPADVISOR
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 8 | telegram-send --stdin
###
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 0 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 1 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 2 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 3 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 4 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 5 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 6 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 7 --unique | telegram-send --stdin

### RELI
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 8 | telegram-send --stdin
###
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 0 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 1 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 2 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 3 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 4 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 5 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 6 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 7 --unique | telegram-send --stdin

### COMPUTERBR
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 8 | telegram-send --stdin
###
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 0 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 1 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 2 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 3 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 4 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 5 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 6 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 7 --unique | telegram-send --stdin

### HOTEL
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 6 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 8 | telegram-send --stdin
###
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 0 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 1 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 2 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 3 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 4 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 5 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 6 --unique | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 7 --unique | telegram-send --stdin

echo "ALL STEPS FINISHED" | telegram-send --stdin