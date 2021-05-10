PYTHONPATH=:$(pwd)
MANAGER_PATH=$(pwd)
CLF=svm

## HOTEL
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 0 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 1 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 2 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 3 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 4 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 5 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf $CLF -j 8 -i 1000 -v 0 --group 6 

### TRIPADVISOR
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 0 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 1 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 2 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 3 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 4 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 5 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf $CLF -j 8 -i 1000 -v 0 --group 6 

### RELI
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 0 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 1 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 2 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 3 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 4 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 5 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf $CLF -j 8 -i 1000 -v 0 --group 6 

### COMPUTERBR
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 0 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 1 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 2 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 3 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 4 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 5 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf $CLF -j 8 -i 1000 -v 0 --group 6 

echo "ALL STEPS FINISHED" 