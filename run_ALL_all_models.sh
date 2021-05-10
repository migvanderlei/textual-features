MANAGER_PATH=$(pwd)
PYTHONPATH=:$(pwd)

### HOTEL
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf lr -j 2 -i 1000 -v 0 --group 7
python3 $MANAGER_PATH/manager.py --randomsearch -d hotel --clf rf -j 8 -i 1000 -v 0 --group 7 

# ### TRIPADVISOR
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 8 -i 1000 -v 0 --group 7 

# ### RELI
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf lr -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d reli --clf rf -j 8 -i 1000 -v 0 --group 7 

# ### COMPUTERBR
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf lr -j 8 -i 1000 -v 0 --group 7 
python3 $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf rf -j 8 -i 1000 -v 0 --group 7 
