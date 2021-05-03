MANAGER_PATH=/home/miguel/textual-features
PYTHONPATH=:$(pwd)
MANAGER_PATH=$(pwd)

### HOTEL
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 0 
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 1 
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 2 
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 3 
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 4 
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 5 
# python $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 6 

### TRIPADVISOR
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 0 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 1 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 2 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 3 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 4 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 5 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 6 

### RELI
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 0 
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 1 
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 2 
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 3 
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 4 
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 5 
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 6 

### COMPUTERBR
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 0 
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 1 
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 2 
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 3 
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 4 
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 5 
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 6 

echo "ALL STEPS FINISHED" 