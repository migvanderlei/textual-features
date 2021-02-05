MANAGER_PATH=/home/miguel/PycharmProjects/textual-features

python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 6 -i 2000 -v 0 | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf lr -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf rf -j 6 -i 2000 -v 0 | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf lr -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf rf -j 6 -i 2000 -v 0 | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf svm -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf gbt -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf lr -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf rf -j 6 -i 2000 -v 0 | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf svm -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf gbt -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf lr -j 6 -i 2000 -v 0 | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf rf -j 6 -i 2000 -v 0 | telegram-send --stdin

################### preprocessed 
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf svm -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf gbt -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf lr -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d tripadvisor --clf rf -j 6 -i 2000 -v 0 -p | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf svm -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf gbt -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf lr -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli --clf rf -j 6 -i 2000 -v 0 -p | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf svm -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf gbt -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf lr -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr --clf rf -j 6 -i 2000 -v 0 -p | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf svm -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf gbt -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf lr -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d computerbr_twt --clf rf -j 6 -i 2000 -v 0 -p | telegram-send --stdin
#
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf svm -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf gbt -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf lr -j 6 -i 2000 -v 0 -p | telegram-send --stdin
python $MANAGER_PATH/manager.py --randomsearch -d reli_less --clf rf -j 6 -i 2000 -v 0 -p | telegram-send --stdin

echo "ALL STEPS FINISHED" | telegram-send --stdin