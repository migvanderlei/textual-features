MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### TRIPADVISOR
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 8 -i 1000 -v 0 --group 7 