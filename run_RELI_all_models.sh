MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### RELI
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf lr -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf rf -j 8 -i 1000 -v 0 --group 7 