MANAGER_PATH=/home/miguel/textual-features

python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 1 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 2 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 3 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 4 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 5 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 6 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 4 -i 1000 -v 0 --group 7 | telegram-send --stdin
