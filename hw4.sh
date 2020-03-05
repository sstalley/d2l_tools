python3 ./d2l_formatter.py HW_4.zip HW_4
python3 d2l_builder.py ./HW_4 .c "mpicc -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wconversion -lpthread -lm -lrt" "-o"
python3 d2l_timer.py ./HW_4 timerargs_4 3 "mpirun --oversubscribe -H localhost -np "
python3 d2l_cat.py ./HW3_4 .tlog .txt .c .clog .outlog .errlog
