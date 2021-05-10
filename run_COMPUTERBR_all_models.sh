MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### COMPUTERBR
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf lr -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf rf -j 8 -i 1000 -v 0 --group 7 