MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### HOTEL
# python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 7 
# python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf lr -j 8 -i 1000 -v 0 --group 7 
# python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf rf -j 8 -i 1000 -v 0 --group 7 