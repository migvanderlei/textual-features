MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### all
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 7 | telegram-send --stdin